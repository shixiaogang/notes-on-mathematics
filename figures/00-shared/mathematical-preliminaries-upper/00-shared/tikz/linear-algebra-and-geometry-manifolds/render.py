"""Render and check the two chapter-07 analytic TikZ figures."""

from pathlib import Path
import math
import os
import subprocess

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
FIGURES = (
    ("sphere-parallel-transport", 88),
    ("sphere-retraction", 82),
)


def verify_geometry():
    for index in range(101):
        t = index * math.pi / 200
        s, c = math.sin(t), math.cos(t)
        segments = (
            ((s, 0, c), (c, 0, -s), (-s, 0, -c)),
            ((c, s, 0), (0, 0, -1), (0, 0, 0)),
            ((0, c, s), (0, s, -c), (0, c, s)),
        )
        for point, vector, derivative in segments:
            dot = sum(a * b for a, b in zip(point, vector))
            norm = sum(a * a for a in vector)
            normal = sum(a * b for a, b in zip(point, derivative))
            projected = [a - normal * b for a, b in zip(derivative, point)]
            assert abs(dot) < 1e-12 and abs(norm - 1) < 1e-12
            assert max(abs(a) for a in projected) < 1e-12
    step = 1.1
    retraction = (1 / math.sqrt(1 + step**2), step / math.sqrt(1 + step**2))
    assert abs(sum(a * a for a in retraction) - 1) < 1e-12
    assert abs(math.atan2(retraction[1], retraction[0]) - math.atan(step)) < 1e-12
    print("Geometry: 303 tangent/unit/parallel checks; retraction angle verified")


def main():
    verify_geometry()
    output = ROOT / "build/math-restructure-figures/ch07"
    output.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//:" + env.get(key, "")
    source = (HERE / "preview.tex").relative_to(ROOT).as_posix()
    commands = (
        [
            "xelatex", "-no-pdf", "-no-shell-escape",
            "-interaction=nonstopmode", "-halt-on-error",
            "-output-directory=" + str(output), "-jobname=figures",
            source,
        ],
        [
            "xdvipdfmx", "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
            "-E", "-o", str(output / "figures.pdf"), str(output / "figures.xdv"),
        ],
    )
    for command in commands:
        result = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, text=True
        )
        if result.returncode:
            raise RuntimeError((result.stdout + result.stderr)[-6000:])
    with fitz.open(output / "figures.pdf") as document:
        assert len(document) == len(FIGURES)
        for page, (name, height) in zip(document, FIGURES):
            dimensions = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
            assert all(abs(a - b) < 0.1 for a, b in zip(dimensions, (112, height)))
            with fitz.open() as single:
                single.insert_pdf(document, from_page=page.number, to_page=page.number)
                single.save(HERE / (name + ".pdf"))
            page.get_pixmap(dpi=240, alpha=False).save(HERE / (name + ".png"))
            print(f"{name}: {dimensions[0]:.2f} x {dimensions[1]:.2f} mm")


if __name__ == "__main__":
    main()
