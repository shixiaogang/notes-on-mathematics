"""Kronecker product using exactly the adjacent worked example.

A=[[1,2],[3,4]], B=[[0,1],[1,0]]; four 2x2 blocks form numpy.kron(A,B).
Color denotes block correspondence, never numerical magnitude.
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

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
K = np.kron(A, B)
assert np.array_equal(K, [[0, 1, 0, 2], [1, 0, 2, 0],
                          [0, 3, 0, 4], [3, 0, 4, 0]])

def bracket(ax, x, y, width, height):
    d = .13
    for xx, inward in [(x - .18, d), (x + width + .18, -d)]:
        ax.plot([xx + inward, xx, xx, xx + inward],
                [y, y, y + height, y + height], color=STROKE, linewidth=1.05)

def matrix(ax, values, x, y, cell, fills, block_gap=0.):
    rows, cols = values.shape
    width = cols * cell + ((cols - 1) // 2) * block_gap
    height = rows * cell + ((rows - 1) // 2) * block_gap
    for i in range(rows):
        for j in range(cols):
            xx = x + j * cell + (j // 2) * block_gap
            yy = y + (rows - 1 - i) * cell + ((rows - 1 - i) // 2) * block_gap
            ax.add_patch(Rectangle((xx + .025, yy + .025), cell - .05, cell - .05,
                                   facecolor=fills[i][j], edgecolor="none", linewidth=0))
            ax.text(xx + cell / 2, yy + cell / 2, str(values[i, j]), ha="center", va="center")
    bracket(ax, x, y, width, height)

fig = plt.figure(figsize=(112 / 25.4, 85 / 25.4))
ax = fig.add_axes([0., 0., 1., 1.])
ax.set(xlim=(0., 11.2), ylim=(0., 8.5), aspect="equal")
ax.axis("off")
cell = .63
matrix(ax, A, 2.45, 6.6, cell, [[GREEN_FILL, BLUE_FILL], [BLUE_FILL, BLUE_FILL]])
matrix(ax, B, 7.5, 6.6, cell, [[GREEN_FILL] * 2] * 2)
ax.text(3.08, 8.05, r"$A$", ha="center", va="bottom")
ax.text(8.13, 8.05, r"$B$", ha="center", va="bottom")
ax.text(5.6, 7.23, r"$\otimes$", ha="center", va="center", fontsize=12)
ax.add_patch(FancyArrowPatch((5.6, 6.25), (5.6, 5.65), arrowstyle="-|>",
                            mutation_scale=8, color=STROKE, linewidth=1.1))
cell, gap = .94, .14
width = 4 * cell + gap
x, y = (11.2 - width) / 2, .62
fills = [[GREEN_FILL if i < 2 and j < 2 else BLUE_FILL for j in range(4)] for i in range(4)]
matrix(ax, K, x, y, cell, fills, block_gap=gap)
# These boundaries express the mathematical blocks; there is no background grid.
for i in range(2):
    for j in range(2):
        ax.add_patch(Rectangle((x + j * (2 * cell + gap), y + i * (2 * cell + gap)),
                               2 * cell, 2 * cell, facecolor="none",
                               edgecolor=GREEN if i == 1 and j == 0 else BLUE, linewidth=1.05))
ax.text(5.6, 4.96, r"$A\otimes B$", ha="center", va="bottom")
record = {
    "kind": "analytical teaching construction",
    "reader_question": "How does each entry of A select and scale one block B?",
    "formula": "(A kron B)[2*i+k,2*j+l]=A[i,j]*B[k,l]",
    "parameters": {"A": A.tolist(), "B": B.tolist()},
    "evaluated_data": {"kronecker_product": K.tolist()},
    "visual_encoding": "Top inputs, bottom product; green links A[0,0], B, and first block; outlined 2x2 blocks, no background grid.",
    "width_mm": 112, "height_mm": 85,
    "processing": "Exact integer data, calculated by numpy.kron; no random data.",
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
