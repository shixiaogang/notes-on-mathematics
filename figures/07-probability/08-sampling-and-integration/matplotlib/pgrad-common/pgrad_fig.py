"""Shared helpers for the chapter 7.33 figures (gradient estimation of parameter-dependent expectations).

All curves come from closed-form formulas or seeded simulations; the only hand-entered numbers are
the fixed teaching normals EPS4 and uniforms U4 that the chapter text uses for hand computation.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np  # noqa: F401
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
SEED = 733
EPS4 = [0.3, -1.1, 0.8, -0.4]     # teaching standard-normal values
U4 = [0.37, 0.80, 0.15, 0.62]     # teaching uniforms


def npdf(x, m=0.0, s=1.0):
    x = np.asarray(x, float); return np.exp(-(x-m)**2/(2*s*s))/(s*math.sqrt(2*math.pi))


def ncdf(x):
    return 0.5*(1+np.vectorize(math.erf)(np.asarray(x, float)/math.sqrt(2)))


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6, **k):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False, **k)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl=None, yl=None, pad=1):
    if xl: ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)
