"""Sensor table: conditional pmfs p(y|x) for x=0,1,2 (rows divided by 0.3,0.4,0.3) with conditional means
1/3, 1, 5/3 (red) and overall mean 1 (dashed)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

P = np.array([[.2, .1, 0], [.1, .2, .1], [0, .1, .2]])
fig, axs = figure(width_mm=108, height_mm=44, ncols=3, sharey=True)
for i, ax in enumerate(axs):
    c = P[i]/P[i].sum(); m = (np.arange(3)*c).sum()
    ax.bar(np.arange(3), c, width=0.55, color=BLUE_FILL, edgecolor=BLUE, linewidth=0.8)
    for j in range(3):
        ax.text(j, c[j] + 0.03, ['0', '1/3', '1/2', '2/3', '1/4'][[0, 1/3, 1/2, 2/3, 1/4].index(min([0, 1/3, 1/2, 2/3, 1/4], key=lambda v: abs(v-c[j])))], ha='center', fontsize=7.5)
    ax.plot([1, 1], [0, 0.78], color=STROKE, lw=0.85, ls='--')
    ax.plot([m, m], [0, 0.78], color=RED, lw=1.6)
    ax.set_title(f'$x={i}$', pad=2); ax.set_xticks([0, 1, 2]); ax.set_xlabel('$y$', labelpad=1)
    ax.set_ylim(0, 0.9); ax.set_xlim(-0.6, 2.6)
    tag(ax, f'({"abc"[i]})', y=-0.36)
axs[0].set_ylabel(r'$p_{Y\mid X}(y\mid x)$')
save(fig, Path(__file__).resolve().parent, 'figure', {'cond_means': [1/3, 1, 5/3], 'cond_vars': [2/9, 1/2, 2/9]})
