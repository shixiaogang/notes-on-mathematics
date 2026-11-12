"""Shared helpers for the chapter 7.9 (probability spaces) figures."""
from pathlib import Path
import sys
import math
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


# Running example of the chapter: the waiting time W with an atom 0.3 at 0
# and the remaining mass 0.7 spread with density 0.7 e^{-t} on (0, inf).
def F_W(t):
    t = np.asarray(t, float)
    return np.where(t < 0, 0.0, 0.3+0.7*(1-np.exp(-np.clip(t, 0, None))))


def Q_W(u):
    u = np.asarray(u, float)
    out = np.zeros_like(u)
    m = u > 0.3
    out[m] = np.log(0.7/(1-u[m]))
    return out
