"""Render the chapter-02 TikZ figure only, using repository fonts and styles."""

from pathlib import Path
import os
import subprocess

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
NAME = "relaxation-candidates-bounds"


def main():
    preview = ROOT / "build/math-restructure-figures/ch02"
    preview.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//:" + env.get(key, "")

    source = (HERE / "preview.tex").relative_to(ROOT).as_posix()
    commands = [
        [
            "xelatex", "-no-pdf", "-no-shell-escape",
            "-interaction=nonstopmode", "-halt-on-error",
            "-output-directory=" + str(preview), "-jobname=" + NAME,
            r"\def\ChTwoFigureOnly{1}\input{" + source + "}",
        ],
        [
            "xdvipdfmx", "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
            "-E", "-o", str(HERE / (NAME + ".pdf")),
            str(preview / (NAME + ".xdv")),
        ],
    ]
    for command in commands:
        result = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, text=True
        )
        if result.returncode:
            raise RuntimeError((result.stdout + result.stderr)[-5000:])

    with fitz.open(HERE / (NAME + ".pdf")) as document:
        assert len(document) == 1
        page = document[0]
        dimensions = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
        assert all(abs(a - b) < 0.1 for a, b in zip(dimensions, (112, 72)))
        page.get_pixmap(dpi=300, alpha=False).save(
            HERE / (NAME + ".png")
        )
    print(f"{NAME}: PDF and PNG rendered at 112 x 72 mm")


if __name__ == "__main__":
    main()
