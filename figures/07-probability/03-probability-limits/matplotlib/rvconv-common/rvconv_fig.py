"""Shared helpers for the chapter 7.12 (convergence of random variables) figures.

Running examples (all on one probability space carrying i.i.d. U_1, U_2, ... ~ Unif(0,1), U = U_1):
  M_n = max(U_1,...,U_n)                       running maximum, error 1 - M_n
  harmonic moving blocks: level k has k blocks [j/k,(j+1)/k), X_n = 1{U in block}
  A_n = {U_n < p_n}                            independent events
  Y_n = n 1{U < 1/n}, Z_n = sqrt(n) 1{U < 1/n}  rare large values
All curves are computed from closed forms or from seeded simulations; no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
LINE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))


def block_index(n):
    """Harmonic moving blocks: term n (1-based) -> (level k, position j), level k has k blocks."""
    k = int((1 + math.isqrt(8*n - 7)) // 2)
    while k*(k-1)//2 >= n: k -= 1
    while k*(k+1)//2 < n: k += 1
    j = n - k*(k-1)//2 - 1
    return k, j


def block_value(n, w):
    k, j = block_index(n)
    return 1.0 if j/k <= w < (j+1)/k else 0.0


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)


def dot(ax, x, y, color=RED, ms=4.0, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl=None, yl=None):
    if xl: ax.set_xlabel(xl, labelpad=1)
    if yl: ax.set_ylabel(yl, labelpad=1)


def logticks(ax, exps, axis='y'):
    ax.minorticks_off()
    vals = [10.0**e for e in exps]
    labs = ['$1$' if e == 0 else ('$10$' if e == 1 else '$10^{%d}$' % e) for e in exps]
    if axis == 'y': ax.set_yticks(vals); ax.set_yticklabels(labs)
    else: ax.set_xticks(vals); ax.set_xticklabels(labs)
