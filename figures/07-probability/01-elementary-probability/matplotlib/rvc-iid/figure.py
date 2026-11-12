"""Joint pmfs as bubbles (area proportional to probability).
(a) two independent fair dice (iid); (b) X2=X1 (same marginal, dependent); (c) fair die X1 and independent fair coin X2 in {0,1} (independent, different marginals)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
k = np.arange(1, 7)
def bub(ax, xs, ys, ps):
    ax.scatter(xs, ys, s=np.array(ps)*900, color=BLUE_FILL, edgecolors=BLUE, linewidths=0.8)
X, Y = np.meshgrid(k, k)
bub(axs[0], X.ravel(), Y.ravel(), [1/36]*36)
bub(axs[1], k, k, [1/6]*6)
X2, Y2 = np.meshgrid(k, [0, 1])
bub(axs[2], X2.ravel(), Y2.ravel(), [1/12]*12)
for ax, s in zip(axs, ('(a)', '(b)', '(c)')):
    ax.set_xlim(0.3, 6.7); ax.set_xticks(k); ax.set_xlabel('$x_1$', labelpad=1)
    ax.set_ylabel('$x_2$', rotation=0, labelpad=9)
    tag(ax, s, y=-0.34)
for ax in axs[:2]:
    ax.set_ylim(0.3, 6.7); ax.set_yticks(k); ax.set_aspect('equal')
axs[2].set_ylim(-0.7, 1.7); axs[2].set_yticks([0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'a': '1/36 each', 'b': '1/6 on diagonal', 'c': '1/12 each'})
