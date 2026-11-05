"""Export local XeLaTeX figure proofs and chapter contact sheets with PyMuPDF."""

from pathlib import Path

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
RENDER = ROOT / "build/math-restructure-figures/ch01"
NAMES = ("preimage-inverse", "quantifier-dependence")


with fitz.open(RENDER / "figures-preview.pdf") as source:
    assert len(source) == len(NAMES), "Expected one PDF page per TikZ picture"
    for number, name in enumerate(NAMES):
        with fitz.open() as figure:
            figure.insert_pdf(source, from_page=number, to_page=number)
            figure.save(HERE / f"{name}.pdf", garbage=4, deflate=True)
            page = figure[0]
            assert abs(page.rect.width * 25.4 / 72 - 112) < 0.1
            assert not page.get_images(), "New TikZ output must remain vector"
            page.get_pixmap(dpi=300).save(HERE / f"{name}.png")
            page.get_pixmap(dpi=140, colorspace=fitz.csGRAY).save(
                RENDER / f"{name}-gray.png"
            )
            print(
                f"{name}: {page.rect.width * 25.4 / 72:.2f} x "
                f"{page.rect.height * 25.4 / 72:.2f} mm; vector PDF"
            )


chapter = RENDER / "chapter-preview.pdf"
if chapter.exists():
    with fitz.open(chapter) as source:
        for start in range(0, len(source), 6):
            with fitz.open() as contact:
                sheet = contact.new_page(width=918, height=812)
                for slot, number in enumerate(range(start, min(start + 6, len(source)))):
                    column, row = slot % 3, slot // 3
                    target = fitz.Rect(
                        column * 306, row * 406 + 10, (column + 1) * 306, (row + 1) * 406
                    )
                    sheet.show_pdf_page(target, source, number)
                    sheet.insert_text(
                        (column * 306 + 8, row * 406 + 10),
                        f"p. {number + 1}",
                        fontsize=8,
                    )
                sheet.get_pixmap(dpi=110).save(RENDER / f"chapter-pages-{start + 1:02d}.png")
        for number, page in enumerate(source):
            text = page.get_text()
            if "原像与逆映射回答不同问题" in text or "固定S = W" in text:
                page.get_pixmap(dpi=130).save(RENDER / f"figure-page-{number + 1:02d}.png")
        print(f"Chapter proof: {len(source)} pages; contact sheets exported")
