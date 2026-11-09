"""Shared helpers for the block-optimization figures (chapter 5.12)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def fc(X, Y, c=1.0): return X**2 + c*X*Y + Y**2
def contour_c(ax, xr, yr, levels, c=1.0):
    X, Y = np.meshgrid(np.linspace(*xr, 600), np.linspace(*yr, 600))
    ax.contour(X, Y, fc(X, Y, c), levels=sorted(levels), colors=[BLUE], linewidths=.65)
def path(ax, P, col, ms=3.2, lw=1.3, **k):
    P = np.asarray(P); ax.plot(P[:, 0], P[:, 1], '-o', color=col, lw=lw, ms=ms, mew=0, zorder=4, **k)
def opt(ax, x=0, y=0): ax.plot([x], [y], 'o', ms=4.8, color=RED, mew=0, zorder=6)
def cyclic(x0, c=1.0, order=(0, 1), updates=8):
    """Exact coordinate minimisation of f=x1^2+c x1 x2+x2^2."""
    x = np.array(x0, float); P = [x.copy()]
    for k in range(updates):
        i = order[k % 2]; x[i] = -c*x[1-i]/2; P.append(x.copy())
    return np.array(P)
HEAD = 'from pathlib import Path\n'
