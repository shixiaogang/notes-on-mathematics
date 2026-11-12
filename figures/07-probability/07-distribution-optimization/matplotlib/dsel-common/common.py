"""Shared helpers for chapter 7.26 (selection of probability distributions) figures.

All quantities are exact finite sums or closed-form expressions; no random data.
Running example: X in {0,1,2}, reference P uniform, cost V(x)=x, statistic T(x)=x.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
X3 = np.arange(3)
U3 = np.ones(3)/3
SQ3 = math.sqrt(3)/2


def kl(q, p):
    """D(q||p) in nats for probability vectors (0 ln 0 = 0)."""
    q = np.asarray(q, float); p = np.asarray(p, float)
    m = q > 0
    if np.any(p[m] == 0):
        return math.inf
    return float(np.sum(q[m]*np.log(q[m]/p[m])))


def tilt(p, t, s):
    """Exponential tilt of p by statistic t with parameter s (scalar)."""
    w = np.asarray(p, float)*np.exp(s*np.asarray(t, float))
    return w/w.sum()


def simplex_xy(p):
    """Barycentric (p0,p1,p2) -> plane; delta0=(0,0), delta1=(1,0), delta2=(1/2, sqrt3/2)."""
    p = np.asarray(p, float)
    return p[..., 1] + 0.5*p[..., 2], SQ3*p[..., 2]


def simplex_axes(ax, labels=True, fill=True):
    V = np.array([[0, 0], [1, 0], [0.5, SQ3]])
    if fill:
        ax.fill(V[:, 0], V[:, 1], color='white', lw=0)
    ax.plot(np.r_[V[:, 0], 0], np.r_[V[:, 1], 0], color=STROKE, lw=0.95)
    if labels:
        ax.text(-0.03, -0.03, r'$\delta_0$', ha='right', va='top')
        ax.text(1.03, -0.03, r'$\delta_1$', ha='left', va='top')
        ax.text(0.5, SQ3+0.03, r'$\delta_2$', ha='center', va='bottom')
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(-0.12, 1.08); ax.set_ylim(-0.08, 0.95)


def simplex_grid(n=400):
    """Barycentric grid points of the closed simplex as (N,3) array."""
    pts = []
    for i in range(n+1):
        for j in range(n+1-i):
            pts.append((i, j, n-i-j))
    return np.array(pts, float)/n


def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha='center', va='top')
