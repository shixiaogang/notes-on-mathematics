"""Shared helpers for the chapter 7.18 figures (information measures).

All curves come from closed-form formulas, exact finite sums or seeded
simulations; nothing is hand-entered. Logarithms are natural (nat) unless a
panel states bits.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
LN2 = math.log(2)


def H(p):
    "entropy in nat of a probability vector, 0 ln 0 = 0"
    p = np.asarray(p, dtype=float).ravel(); p = p[p > 0]
    return float(-(p*np.log(p)).sum())


def hb(e):
    "binary entropy in nat, vectorised"
    e = np.asarray(e, dtype=float); out = np.zeros_like(e)
    m = (e > 0) & (e < 1)
    out[m] = -e[m]*np.log(e[m]) - (1-e[m])*np.log(1-e[m])
    return out


_erf = np.vectorize(math.erf)


def Phi(x):
    return 0.5*(1+_erf(np.asarray(x, dtype=float)/math.sqrt(2)))


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)
