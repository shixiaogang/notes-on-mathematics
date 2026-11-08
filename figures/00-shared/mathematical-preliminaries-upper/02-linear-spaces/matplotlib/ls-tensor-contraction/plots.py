"""Contracting the column axis with an all-ones vector gives three row sums.

A=[[1,2],[3,4],[5,6]], w=[1,1], c=A@w=[3,7,11].
The blue row and matching output emphasize the preserved row index.
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

A = np.array([[1, 2], [3, 4], [5, 6]])
W = np.ones(2, dtype=int)
C = np.einsum("ij,j->i", A, W)
assert np.array_equal(C, [3, 7, 11])

def matrix(ax, values, x, y, cell, vector_ones=False):
    values = np.asarray(values)
    if values.ndim == 1:
        values = values[:, None]
    rows, cols = values.shape
    for i in range(rows):
        for j in range(cols):
            xx, yy = x + j * cell, y + (rows - 1 - i) * cell
            face = GREEN_FILL if vector_ones else (BLUE_FILL if i == 1 else "white")
            ax.add_patch(Rectangle((xx + .035, yy + .035), cell - .07, cell - .07,
                                   facecolor=face, edgecolor="none", linewidth=0))
            ax.text(xx + cell / 2, yy + cell / 2, str(values[i, j]), ha="center", va="center")
    for xx, inward in [(x - .18, .13), (x + cols * cell + .18, -.13)]:
        ax.plot([xx + inward, xx, xx, xx + inward],
                [y, y, y + rows * cell, y + rows * cell], color=STROKE, linewidth=1.05)

fig = plt.figure(figsize=(112 / 25.4, 51 / 25.4))
ax = fig.add_axes([0., 0., 1., 1.])
ax.set(xlim=(0., 11.2), ylim=(0., 5.1), aspect="equal")
ax.axis("off")
cell, center_y = .83, 2.6
matrix(ax, A, 1.5, center_y - 1.5 * cell, cell)
matrix(ax, W, 5.5, center_y - cell, cell, vector_ones=True)
matrix(ax, C, 8.9, center_y - 1.5 * cell, cell)
for x, label in [(2.33, r"$A$"), (5.915, r"$\mathbf{1}$"), (9.315, r"$c$")]:
    ax.text(x, 4.15, label, ha="center", va="bottom")
ax.text(4.3, center_y, r"$\cdot$", ha="center", va="center", fontsize=12)
ax.text(7.55, center_y, r"$=$", ha="center", va="center", fontsize=12)
ax.text(5.6, .48, r"$c_i=\sum_{j=1}^{2} A_{ij}\,1_j$", ha="center", va="center")
record = {
    "kind": "analytical teaching construction",
    "reader_question": "Which index disappears, and why does each original row retain one output?",
    "formula": "c_i=sum_j A_ij*1_j, j=1,2; shape (3,2) contracted with (2,) gives (3,)",
    "parameters": {"A": A.tolist(), "all_ones_vector": W.tolist()},
    "evaluated_data": {"row_sums": C.tolist(), "highlighted_row": 2, "highlighted_sum": "3+4=7"},
    "visual_encoding": "Blue input row and its output; green all-ones vector; no magnitude color scale or background grid.",
    "width_mm": 112, "height_mm": 51,
    "processing": "Exact integer data, numpy.einsum ij,j->i; no random data.",
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
