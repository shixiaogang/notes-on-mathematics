"""Shared helpers for the chapter 7.2 (distributions of random variables) figures."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

LINE = '#4C4D4F'
HERE = lambda f: Path(f).resolve().parent


def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)


def sub(ax, letter, xlabel=None):
    """Set the x label with the panel letter underneath it (shared baseline)."""
    ax.set_xlabel((xlabel+'\n' if xlabel else '\n')+f'({letter})', linespacing=1.5)


def bars(ax, xs, ps, color=BLUE, fill=BLUE_FILL, width=.55, **kw):
    """Thin-outlined light bars for a probability mass table."""
    ax.bar(xs, ps, width=width, color=fill, edgecolor=color, linewidth=.9, **kw)


def step_cdf(ax, xs, ps, lo, hi, color=BLUE, dots=True, lw=1.4):
    """Draw a right-continuous step distribution function with filled/hollow dots."""
    xs = np.asarray(xs, float); cum = np.cumsum(ps)
    left = np.r_[lo, xs]; right = np.r_[xs, hi]; level = np.r_[0, cum]
    for a, b, v in zip(left, right, level):
        ax.plot([a, b], [v, v], color=color, lw=lw, solid_capstyle='butt')
    if dots:
        for x, v0, v1 in zip(xs, np.r_[0, cum[:-1]], cum):
            ax.plot([x], [v0], 'o', ms=3.2, mfc='white', mec=color, mew=.9, zorder=4)
            ax.plot([x], [v1], 'o', ms=3.2, color=color, zorder=4)
    return cum
