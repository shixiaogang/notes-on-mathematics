"""Shared helpers for chapter 7.28 (information geometry) figures.

All curves come from closed-form Gaussian / exponential-family formulas;
Monte Carlo figures fix SEED and state the sample sizes in their own scripts.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
SEED = 728


def npdf(x, mu=0.0, var=1.0):
    x = np.asarray(x, float)
    return np.exp(-(x-mu)**2/(2*var))/math.sqrt(2*math.pi*var)


def kl_gauss(m1, v1, m2, v2):
    """D_KL(N(m1,v1) || N(m2,v2)), natural log."""
    return 0.5*np.log(v2/v1)+(v1+(m1-m2)**2)/(2*v2)-0.5


def tag(ax, s, y=-0.28):
    ax.text(0.5, y, s, transform=ax.transAxes, ha='center', va='top')


# running example: target Pi = N(0,1), objective L = D_KL(N(mu,v) || Pi)
def L_mv(mu, v):
    return kl_gauss(mu, v, 0.0, 1.0)


def nat_from_mv(mu, v):
    return np.array([mu/v, -1/(2*v)])


def mv_from_nat(t):
    v = -1/(2*t[1])
    return t[0]*v, v


def fisher_nat(mu, v):
    """Cov of T=(X,X^2) under N(mu,v)."""
    return np.array([[v, 2*mu*v], [2*mu*v, 2*v*v+4*mu*mu*v]])


THETA_PI = np.array([0.0, -0.5])
