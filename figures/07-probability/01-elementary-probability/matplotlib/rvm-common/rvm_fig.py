"""Shared helpers for the figures of chapter 7.3 (numerical characteristics).

All numbers are computed here from the chapter's running examples:
  * reward table X: values 0, 3, 6 with probabilities 1/2, 1/3, 1/6 (a die
    with faces 1-3 paying 0, faces 4-5 paying 3, face 6 paying 6);
  * density f(x) = 2x on (0, 1).
"""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
XV = np.array([0., 3., 6.]); PV = np.array([1/2, 1/3, 1/6])


def moments(xs, ps):
    xs = np.asarray(xs, float); ps = np.asarray(ps, float)
    m = (xs*ps).sum(); v = ((xs-m)**2*ps).sum()
    c3 = ((xs-m)**3*ps).sum(); c4 = ((xs-m)**4*ps).sum()
    return m, v, c3/v**1.5, c4/v**2


def panel(fig, left=.09, right=.98, top=.96, bottom=.26, wspace=.3, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.4, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def bars(ax, xs, ps, width=.55, color=BLUE, fill=BLUE_FILL, z=2):
    ax.bar(xs, ps, width=width, color=fill, edgecolor=color, linewidth=.9, zorder=z)


def fulcrum(ax, x, y0, h, w, color=RED):
    ax.fill([x-w/2, x+w/2, x], [y0-h, y0-h, y0], color=color, lw=0, zorder=5, clip_on=False)


def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)
