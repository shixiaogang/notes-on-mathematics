"""Contributions (x-1)(y-1)p(x,y) to Cov(X,Y) around the mean (1,1).
(a) sensor table (Cov=0.4); (b) product table with the same marginals (Cov=0). Bubble area proportional to p."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

P1 = np.array([[.2, .1, 0], [.1, .2, .1], [0, .1, .2]])
p = np.array([.3, .4, .3]); P2 = np.outer(p, p)
fig, axs = figure(width_mm=100, height_mm=50, ncols=2)
for ax, P, s in zip(axs, (P1, P2), ('(a)', '(b)')):
    ax.axvline(1, color=STROKE, lw=0.85, ls='--'); ax.axhline(1, color=STROKE, lw=0.85, ls='--')
    for i in range(3):
        for j in range(3):
            c = (i-1)*(j-1)*P[i, j]
            if P[i, j] == 0:
                ax.scatter([i], [j], s=10, marker='x', color=MUTED, linewidths=0.8); continue
            col, fc = (BLUE, BLUE_FILL) if c > 0 else ((RED, RED_FILL) if c < 0 else (STROKE, 'white'))
            ax.scatter([i], [j], s=P[i, j]*1500, color=fc, edgecolors=col, linewidths=0.9, zorder=3)
            if c != 0:
                ax.text(i, j-0.36, f'{c:+.2f}', ha='center', va='top', fontsize=7.5, color=INK)
    ax.set_xlim(-0.6, 2.6); ax.set_ylim(-0.75, 2.6); ax.set_aspect('equal')
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$y$', rotation=0)
    tag(ax, s, y=-0.26)
save(fig, Path(__file__).resolve().parent, 'figure', {'cov_a': float(sum((i-1)*(j-1)*P1[i, j] for i in range(3) for j in range(3))), 'cov_b': 0.0})
