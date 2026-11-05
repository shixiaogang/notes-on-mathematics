"""Reproduce the deterministic chapter 14 example and its figure only."""

from pathlib import Path
import csv
import math
import os
import subprocess

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
NAME = "temperature-regulation-tracking"


def reference(t, moving):
    return 2.0 + (0.4 * math.sin(math.pi * t / 8) if moving else 0.0)


def simulate(moving, constrained=False):
    state = 0.0
    rows = []
    for t in range(25):
        target = reference(t, moving)
        feedforward = reference(t + 1, moving) - 0.8 * target
        nominal = feedforward - 0.3 * (state - target)
        action = nominal
        if constrained:
            lower = max(0.0, -0.8 * state)
            upper = min(1.0, 3.0 - 0.8 * state)
            assert lower <= upper
            action = min(upper, max(lower, nominal))
            assert 0 <= state <= 3 and 0 <= action <= 1
        else:
            assert abs(state - target + 2 * 0.5**t) < 1e-12
        rows.append([target, state, feedforward, action])
        state = 0.8 * state + action
    return rows


def build_data():
    fixed = simulate(False)
    moving = simulate(True)
    constrained = simulate(True, constrained=True)
    assert abs(moving[0][3] - 1.1530733729460358) < 1e-12
    assert constrained[0][3] == 1.0
    assert constrained[1][1] == 1.0
    assert max(abs(row[1] - row[0]) for row in constrained[1:]) < 1.154
    with (HERE / "temperature.tsv").open("w", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow(
            ["t", "r_fixed", "x_fixed", "ur_fixed", "u_fixed",
             "r_moving", "x_moving", "ur_moving", "u_moving"]
        )
        for t, (left, right) in enumerate(zip(fixed, moving)):
            writer.writerow([t, *left, *right])
    print("25 discrete samples; both unconstrained errors equal -2*(0.5**t).")
    print(f"Moving-reference first input: {moving[0][3]:.12f}; safe projection: 1.")
    print("Constrained comparison checked numerically; not used in figure.")


def render():
    temporary = ROOT / "build/math-restructure-figures/ch14"
    temporary.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//:" + env.get(key, "")
    commands = [
        ["xelatex", "-no-pdf", "-no-shell-escape", "-interaction=nonstopmode",
         "-halt-on-error", "-output-directory=" + str(temporary),
         "-jobname=" + NAME, str((HERE / "preview.tex").relative_to(ROOT))],
        ["xdvipdfmx", "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
         "-E", "-o", str(HERE / (NAME + ".pdf")),
         str(temporary / (NAME + ".xdv"))],
    ]
    for command in commands:
        result = subprocess.run(
            command, cwd=ROOT, env=env, capture_output=True, text=True
        )
        if result.returncode:
            raise RuntimeError((result.stdout + result.stderr)[-7000:])
    with fitz.open(HERE / (NAME + ".pdf")) as document:
        assert len(document) == 1
        page = document[0]
        size = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
        assert all(abs(a - b) < 0.1 for a, b in zip(size, (169, 110))), size
        assert not page.get_images(), "Expected a vector-only figure."
        page.get_pixmap(dpi=300, alpha=False).save(HERE / (NAME + ".png"))
        page.get_pixmap(dpi=150, colorspace=fitz.csGRAY, alpha=False).save(
            temporary / (NAME + "-gray.png")
        )
    print("Figure PDF and preview: 169 x 110 mm, vector paths and embedded fonts.")


if __name__ == "__main__":
    build_data()
    render()
