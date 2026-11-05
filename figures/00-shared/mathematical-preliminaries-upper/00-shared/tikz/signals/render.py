"""Render the two chapter 12 TikZ figures at their final publication sizes."""

from pathlib import Path
import os
import subprocess

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
FIGURES = {"basic-operations": (169, 121), "channel-mixing": (169, 78)}


def render():
    temporary = ROOT / "build/math-restructure-figures/ch12"
    temporary.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//:" + env.get(key, "")
    driver = (HERE / "preview.tex").relative_to(ROOT).as_posix()
    for name, size in FIGURES.items():
        # Figure-only runs have no cross-references or bibliography state to reuse.
        for suffix in (".aux", ".out"):
            (temporary / (name + suffix)).unlink(missing_ok=True)
        commands = [
            [
                "xelatex", "-no-pdf", "-no-shell-escape",
                "-interaction=nonstopmode", "-halt-on-error",
                "-output-directory=" + str(temporary), "-jobname=" + name,
                r"\def\ChTwelveFigure{" + name + r"}\input{" + driver + "}",
            ],
            [
                "xdvipdfmx", "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
                "-E", "-o", str(HERE / (name + ".pdf")),
                str(temporary / (name + ".xdv")),
            ],
        ]
        for command in commands:
            result = subprocess.run(
                command, cwd=ROOT, env=env, capture_output=True, text=True
            )
            if result.returncode:
                raise RuntimeError((result.stdout + result.stderr)[-7000:])
        with fitz.open(HERE / (name + ".pdf")) as document:
            assert len(document) == 1
            page = document[0]
            actual = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
            assert all(abs(a - b) < 0.1 for a, b in zip(actual, size)), actual
            page.get_pixmap(dpi=180, alpha=False).save(HERE / (name + ".png"))
        print(f"{name}: rendered PDF and PNG at {size[0]} x {size[1]} mm")


if __name__ == "__main__":
    render()
