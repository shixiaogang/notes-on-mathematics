"""Shared helpers for the chapter 7.30 (sample generation) figures."""
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


def npdf(x, m=0.0, s=1.0):
    x = np.asarray(x, float)
    return np.exp(-0.5*((x-m)/s)**2)/(s*math.sqrt(2*math.pi))


# Running mixture target of the chapter: 0.3 N(-2, 0.5^2) + 0.7 N(2, 1).
W_MIX = (0.3, 0.7)
M_MIX = (-2.0, 2.0)
S_MIX = (0.5, 1.0)


def mix_pdf(x):
    return sum(w*npdf(x, m, s) for w, m, s in zip(W_MIX, M_MIX, S_MIX))


def rwmh(logp, x0, step, n, rng):
    """Random-walk Metropolis with N(0, step^2) proposals; returns chain and acceptance rate."""
    x = float(x0); lp = logp(x); out = np.empty(n); acc = 0
    for t in range(n):
        y = x + step*rng.standard_normal()
        ly = logp(y)
        if math.log(rng.random()) <= ly-lp:
            x, lp = y, ly; acc += 1
        out[t] = x
    return out, acc/n


def acf(x, maxlag):
    x = np.asarray(x, float)-np.mean(x)
    v = np.dot(x, x)/len(x)
    return np.array([np.dot(x[:len(x)-k], x[k:])/len(x)/v for k in range(maxlag+1)])
