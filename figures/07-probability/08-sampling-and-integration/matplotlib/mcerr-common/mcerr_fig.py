"""Shared helpers for the chapter 7.31 figures (Monte Carlo integration error).

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

# running example: I = int_0^1 e^u du = e - 1, Var(e^U) = (e^2-1)/2 - (e-1)^2
I_EXP = math.e - 1
S2_EXP = (math.e**2 - 1)/2 - (math.e - 1)**2


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl='$N$', yl=None, pad=1):
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


def npdf(x, m=0.0, v=1.0):
    return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)


def ar1(rng, rho, n, x0=None, reps=None):
    """Gaussian AR(1) chain X(t+1)=rho X(t)+sqrt(1-rho^2) xi, invariant N(0,1).
    Returns array of shape (reps, n) of X(1..n); x0=None means start from N(0,1)."""
    shape = (1 if reps is None else reps)
    x = rng.standard_normal(shape) if x0 is None else np.full(shape, float(x0))
    out = np.empty((shape, n)); c = math.sqrt(1-rho**2)
    xi = rng.standard_normal((shape, n))
    for t in range(n):
        x = rho*x + c*xi[:, t]; out[:, t] = x
    return out if reps is not None else out[0]
