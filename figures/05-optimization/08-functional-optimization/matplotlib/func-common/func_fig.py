from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
X = np.linspace(0, 1, 801)
def panel(fig, left=.09, right=.985, top=.96, bottom=.26, wspace=.26):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def zigzag(x, k, slope=1.0):
    """k identical teeth on [0,1]: slope +-slope, zero at the tooth boundaries."""
    y = np.mod(x*k, 1.0)/k
    return slope*np.minimum(y, 1.0/k-y)
def hats(n):
    """P1 stiffness K, consistent mass M on n cells of [0,1], all n+1 nodes."""
    d = 1.0/n
    K = np.zeros((n+1, n+1)); M = np.zeros((n+1, n+1))
    for i in range(n):
        K[np.ix_([i,i+1],[i,i+1])] += np.array([[1,-1],[-1,1]])/d
        M[np.ix_([i,i+1],[i,i+1])] += np.array([[2,1],[1,2]])*d/6
    return K, M
def dot(ax, x, y, color=RED, ms=4.6, z=6):
    ax.plot([x],[y],'o',ms=ms,color=color,mew=0,zorder=z)
