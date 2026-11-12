"""Shared helpers for the weak-convergence figures (chapter 7.14).

All curves come from closed-form formulas, exact finite sums, numerical
quadrature or seeded simulation; no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
erf = np.vectorize(math.erf)

def Phi(x):
    return 0.5*(1+erf(np.asarray(x, dtype=float)/math.sqrt(2)))

def npdf(x, s=1.0):
    return np.exp(-np.asarray(x)**2/(2*s*s))/(s*math.sqrt(2*math.pi))

def binom_pmf(n, p):
    k = np.arange(n+1)
    return np.array([math.exp(math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)+j*math.log(p)+(n-j)*math.log1p(-p)) if 0<p<1 else float(j==(n if p==1 else 0)) for j in k])

def poisson_pmf(lam, kmax):
    return np.array([math.exp(-lam+k*math.log(lam)-math.lgamma(k+1)) for k in range(kmax+1)])

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

def axlab(ax, xl=None, yl=None, pad=1):
    if xl: ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)

def step_cdf(ax, atoms, masses, x0, x1, color, lw=1.4, z=3):
    """Draw a right-continuous step distribution function on [x0, x1]."""
    order = np.argsort(atoms); a = np.asarray(atoms, float)[order]; m = np.asarray(masses, float)[order]
    xs = [x0]; ys = [0.0]; c = 0.0
    for ai, mi in zip(a, m):
        if ai < x0: c += mi; ys[-1] = c; continue
        if ai > x1: break
        xs.append(ai); ys.append(c); c += mi; xs.append(ai); ys.append(c)
    xs.append(x1); ys.append(c)
    ax.plot(xs, ys, color=color, lw=lw, zorder=z, solid_joinstyle='miter')
