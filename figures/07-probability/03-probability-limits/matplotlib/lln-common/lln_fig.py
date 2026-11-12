"""Shared helpers for the chapter 7.13 figures (independent sums, laws of large numbers).

Every curve is computed from a closed-form formula, an exact finite sum, or a
seeded simulation; no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))


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


def axlab(ax, xl='$n$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)


def logticks(ax, exps, axis='y'):
    ax.minorticks_off()
    vals = [10.0**e for e in exps]
    labs = ['$1$' if e == 0 else '$10$' if e == 1 else '$10^{%d}$' % e for e in exps]
    if axis == 'y':
        ax.set_yticks(vals); ax.set_yticklabels(labs)
    else:
        ax.set_xticks(vals); ax.set_xticklabels(labs)


def binpmf(n, p=.5):
    "exact Bin(n,p) masses via log-gamma"
    k = np.arange(n+1)
    lg = np.array([math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1) for i in k])
    return np.exp(lg + k*np.log(p) + (n-k)*np.log(1-p))


def rademacher(rng, size):
    return rng.integers(0, 2, size=size)*2 - 1


def pareto(rng, alpha, size):
    "Pareto(alpha) on [1, inf): P(X>t)=t^{-alpha}, by inverse transform"
    return rng.random(size)**(-1/alpha)
