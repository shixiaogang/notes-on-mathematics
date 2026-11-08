from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# Haar tiles of f=1_[0,1/3): a=1/3, level j has one nonzero coefficient 2^{-j/2}/3 at k=floor(2^j/3). Budget 8 terms.
from matplotlib.patches import Rectangle
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.23, wspace=.08)
L = 6
def cell(ax, x, y, w, fc):
    ax.add_patch(Rectangle((x, y), w, 1, facecolor=fc, edgecolor=GRID, lw=.3))
for pi_, ax in enumerate(axes):
    # coarse row at y=L+1 (top), levels j=0..L at y=L-j
    ynz = lambda j: L-j
    cell(ax, 0, L+1, 1, BLUE)
    for j in range(L+1):
        n = 2**j; w = 1/n; k0 = int(np.floor(n/3))
        for k in range(n):
            if pi_ == 0:
                fc = (BLUE if k == k0 else BLUE_FILL) if j < 3 else (RED if k == k0 else 'white')
            else:
                fc = BLUE if k == k0 else 'white'
            cell(ax, k*w, ynz(j), w, fc)
    ax.set_xlim(0, 1); ax.set_ylim(0, L+2)
    ax.set_xticks([0, 1/3, 1]); ax.set_xticklabels(['0', '1/3', '1']); ax.set_xlabel('$x$', labelpad=0)
    ax.axvline(1/3, color=MUTED, lw=.75, ls=(0, (2, 2)))
    for sp in ('left', 'bottom'): ax.spines[sp].set_visible(False)
    ax.tick_params(length=2)
axes[0].set_yticks([L-j+.5 for j in range(L+1)]+[L+1.5]); axes[0].set_yticklabels([f'$j={j}$' for j in range(L+1)]+['$a$'])
axes[1].set_yticks([])
for a, t in zip(axes, '(a) (b)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, t, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'tiles j<=6, f=1_[0,1/3), budget 8'})
