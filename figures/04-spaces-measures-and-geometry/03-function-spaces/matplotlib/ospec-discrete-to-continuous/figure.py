from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Diagonal matrices D_n = diag((k-1/2)/n) sample the multiplication operator (Mf)(x)=x f(x) on L2(0,1).
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.965, top=.96, bottom=.25, wspace=.34)
for ax, n in zip(axes[:2], (5, 20)):
    xk = (np.arange(1, n+1)-.5)/n
    ax.vlines(xk, 0, xk, color=BLUE, lw=1.0 if n == 5 else .8)
    ax.plot(xk, xk, 'o', color=BLUE, ms=3.2 if n == 5 else 2.0, mew=0)
    ax.hlines(xk, 1.07, 1.13, color=BLUE, lw=.95, clip_on=False)
ax = axes[2]
x = np.linspace(0, 1, 201)
ax.plot(x, x, color=BLUE, lw=1.4)
ax.plot([1.1, 1.1], [0, 1], color=BLUE, lw=2.2, solid_capstyle='butt', clip_on=False)
for ax, n in zip(axes, (r'$k/n,\ n=5$', r'$k/n,\ n=20$', r'$x$')):
    ax.set_xlim(0, 1.15); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.spines['bottom'].set_bounds(0, 1)
    ax.set_xlabel(n, labelpad=0)
axes[0].set_ylabel('对角元', labelpad=-4)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'D_n=diag((k-1/2)/n), n=5,20; limit (Mf)(x)=x f(x); ticks at right mark the eigenvalues / spectrum'})
