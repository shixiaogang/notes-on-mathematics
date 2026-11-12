"""Shared helpers for chapter 7.17 (comparison of probability distributions).

All values come from closed forms, exact finite sums or numerical quadrature on
fine grids; simulations (if any) use the fixed seed SEED. No hand-entered data.
Running example of the chapter: P=(0.6,0.3,0.1), Q=(0.3,0.3,0.4) on {0,1,2}.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
DASH = (0, (4, 2))
DOT = (0, (1.5, 1.8))
SEED = 717
P_EX = np.array([.6, .3, .1])
Q_EX = np.array([.3, .3, .4])
X_EX = np.array([0., 1., 2.])
_erf = np.vectorize(math.erf)


def Phi(x):
    return 0.5*(1+_erf(np.asarray(x, dtype=float)/math.sqrt(2)))


def npdf(x, m=0., s=1.):
    x = np.asarray(x, dtype=float)
    return np.exp(-(x-m)**2/(2*s*s))/(s*math.sqrt(2*math.pi))


def kl(p, q):
    p = np.asarray(p, float); q = np.asarray(q, float); m = p > 0
    if np.any(q[m] == 0):
        return math.inf
    return float(np.sum(p[m]*np.log(p[m]/q[m])))


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5)
    ax.text(x, y, s, color=color, **k)


def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl:
        ax.set_ylabel(yl, labelpad=1)


def bars(ax, x, h, color=BLUE, fill=BLUE_FILL, width=.34, offset=0., lw=.8, z=2):
    ax.bar(np.asarray(x)+offset, h, width=width, color=fill, edgecolor=color, linewidth=lw, zorder=z)


def gauss_kernel(x, y, s=1.):
    x = np.asarray(x, float); y = np.asarray(y, float)
    return np.exp(-(x[:, None]-y[None, :])**2/(2*s*s))
