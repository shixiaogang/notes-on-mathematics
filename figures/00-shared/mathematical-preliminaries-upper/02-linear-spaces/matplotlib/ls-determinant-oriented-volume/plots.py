"""Unit square and two determinant scalings using the current book example.

A=[[2,.5],[0,1.5]], A_minus=A@diag(-1,1). All panels use the same scale.
The arc follows the first column to the second column.
"""
from pathlib import Path
import argparse
import json
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
from plot_style import configure, prepare_figure, style_record
from plot_style import BLUE, GREEN, BLUE_FILL, GREEN_FILL, STROKE, INK
configure()
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME])
parser.parse_args()

A = np.array([[2., .5], [0., 1.5]])
A_MINUS = A @ np.diag([-1., 1.])
MATRICES = [np.eye(2), A, A_MINUS]
assert np.allclose([np.linalg.det(m) for m in MATRICES], [1., 3., -3.])

def arrow(ax, start, end, color, width=1.4, size=8):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=size,
                               color=color, linewidth=width, shrinkA=0, shrinkB=0))

def panel(ax, matrix, labels, title):
    u, v = matrix[:, 0], matrix[:, 1]
    vertices = np.array([[0., 0.], u, u + v, v])
    ax.add_patch(Polygon(vertices, closed=True, facecolor=BLUE_FILL,
                         edgecolor=BLUE, linewidth=1.05))
    arrow(ax, (0., 0.), u, BLUE)
    arrow(ax, (0., 0.), v, GREEN)
    ax.text(u[0], u[1] - .15, labels[0], ha="center", va="top", color=BLUE)
    ax.text(v[0], v[1] + .12, labels[1], ha="center", va="bottom", color=GREEN)
    # Signed shortest angle from column 1 to column 2.
    t0 = np.arctan2(u[1], u[0])
    delta = np.arctan2(np.linalg.det(matrix), np.dot(u, v))
    theta = np.linspace(t0 + .14 * delta, t0 + .86 * delta, 60)
    points = .38 * np.column_stack([np.cos(theta), np.sin(theta)])
    ax.plot(points[:, 0], points[:, 1], color=STROKE, linewidth=.85)
    arrow(ax, points[-5], points[-1], STROKE, width=.85, size=6)
    ax.plot(0., 0., marker="o", markersize=2, color=INK, linewidth=0)
    center_x = (vertices[:, 0].min() + vertices[:, 0].max()) / 2
    ax.set(xlim=(center_x - 1.8, center_x + 1.8), ylim=(-.45, 2.05))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(.5, -.07, title, transform=ax.transAxes, ha="center", va="top")

fig, axes = plt.subplots(1, 3, figsize=(169 / 25.4, 59 / 25.4))
fig.subplots_adjust(left=.025, right=.975, bottom=.19, top=.98, wspace=.13)
panel(axes[0], MATRICES[0], [r"$e_1$", r"$e_2$"], r"$\det I=1$")
panel(axes[1], MATRICES[1], [r"$a_1$", r"$a_2$"], r"$\det A=3$")
panel(axes[2], MATRICES[2], [r"$-a_1$", r"$a_2$"], r"$\det A_{-}=-3$")
record = {
    "kind": "analytical teaching construction",
    "reader_question": "How do determinant magnitude and sign describe area and orientation?",
    "formula": "A=[[2,0.5],[0,1.5]], A_minus=A@diag(-1,1); determinants 1,3,-3",
    "parameters": {"matrices": [m.tolist() for m in MATRICES], "common_panel_span": [3.6, 2.5]},
    "evaluated_data": {"determinants": [float(np.linalg.det(m)) for m in MATRICES]},
    "visual_encoding": "Common scale; blue first column, green second column; dark arc follows first to second; no background axes/grid.",
    "width_mm": 169, "height_mm": 59,
    "processing": "Exact analytic matrices, determinants checked with numpy; no random data.",
}
prepare_figure(fig)
for ext in ("pdf", "svg", "png"):
    fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)
record.update({
    "source": str(Path(__file__).relative_to(ROOT)),
    "reference_width_mm": record["width_mm"], "reference_scale": 1,
    "label_size_pt_at_reference": 8, "png_dpi": 300,
    "outputs": [f"{NAME}.{ext}" for ext in ("pdf", "svg", "png")],
})
(HERE / "sources.json").write_text(json.dumps(
    {"style": style_record(), "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
