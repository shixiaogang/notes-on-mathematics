"""Plot helpers for the quadratic and conic programming chapter."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'
# Running least-squares QP: min 1/2||Dx-r||^2 s.t. x>=0, x1+x2<=2.
D = np.array([[1., 1.], [1., 0.], [0., 1.]]); R = np.array([4., 1., 0.])
Q = D.T@D; q = -D.T@R
XSTAR = np.array([1.5, .5]); XLS = np.array([2., 1.])
def fls(X, Y): return .5*((X+Y-4)**2+(X-1)**2+Y**2)
def active(ax, a, b, z=4): ax.plot([a[0], b[0]], [a[1], b[1]], color=EDGE, lw=2.0, solid_capstyle='round', zorder=z)
def arrow(ax, a, b, color=GREEN, lw=1.3, ms=8, z=5):
    ax.annotate('', xy=tuple(b), xytext=tuple(a), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=ms), zorder=z)
def dot(ax, p, color=RED, ms=5, z=7): ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)
def hollow(ax, p, color=RED, ms=4.8, z=7): ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)
def grid2(xl, yl, n=500):
    return np.meshgrid(np.linspace(*xl, n), np.linspace(*yl, n))
def setup(ax, xlim, ylim, xt=None, yt=None, xl='$x_1$', yl='$x_2$', equal=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal: ax.set_aspect('equal')
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_xlabel(xl, labelpad=1); ax.set_ylabel(yl, labelpad=1)
def off(ax, xlim, ylim):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect('equal'); ax.axis('off')
def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None); fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
