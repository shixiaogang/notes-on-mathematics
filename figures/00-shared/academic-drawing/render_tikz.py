"""Render editable book TikZ sources using the exact book fonts and math map.

Compilation is sequential and uses a worktree-local proof directory. Scientific
and visual approval are separate from this export and are never inferred here.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import pymupdf as fitz

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
PREAMBLE = (ROOT / "figures/00-shared/academic-drawing/preamble.tex").read_text() + "\n\\begin{document}\n"

def render(source, output_dir=None):
    source = source.resolve()
    relative = source.relative_to(ROOT)
    work = ROOT / "build/figure-proofs" / relative.parent / source.stem
    work.mkdir(parents=True, exist_ok=True)
    driver = work / "figure.tex"
    theme = ""
    if str(relative).startswith(("figures/07-classic-models/",
                                 "figures/08-neural-network-models/",
                                 "figures/09-probabilistic-graphical-models/")):
        theme = "\\input{figures/00-shared/model-generators/muted-theme.tex}\n"
    driver.write_text(PREAMBLE + theme + r"\input{" + str(relative) + "}\n\\end{document}\n")
    with (work / "compile.log").open("w") as log:
        subprocess.run(["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory="+str(work.relative_to(ROOT)), str(driver.relative_to(ROOT))], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
        subprocess.run(["xdvipdfmx", "-o", str(work/"figure.pdf"),
                        str(work/"figure.xdv")], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    logtext=(work/"compile.log").read_text()
    if "Missing character:" in logtext:
        raise ValueError("Missing character in TikZ output: " + str(relative))
    dest = Path(output_dir).resolve() if output_dir else source.parent
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / source.stem
    with fitz.open(work/"figure.pdf") as doc:
        if len(doc)!=1:
            raise ValueError(f"Expected one TikZ picture page: {relative}; got {len(doc)}")
        doc.save(out.with_suffix(".pdf"))
        page = doc[0]
        out.with_suffix(".svg").write_text(page.get_svg_image(text_as_path=True))
        page.get_pixmap(dpi=300).save(out.with_suffix(".png"))
        report = {"source":str(relative),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
                  "physical_size_mm":[round(x*25.4/72,3) for x in [page.rect.width,page.rect.height]],
                  "raster_images_embedded":len(page.get_images()),"math":"Actual FiraMath-Regular.otf via unicode-math",
                  "exports":["PDF","SVG paths","PNG 300 dpi"],"status":"rendered; scientific and visual review required"}
        if theme:
            theme_path = ROOT / "figures/00-shared/model-generators/muted-theme.tex"
            report.update(volume_theme=str(theme_path.relative_to(ROOT)),theme_sha256=hashlib.sha256(theme_path.read_bytes()).hexdigest())
    out.with_suffix(".render.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    for source in args.sources:
        result = render(source,args.output_dir)
        print(result["source"],result["physical_size_mm"],"raster images:",result["raster_images_embedded"],flush=True)
