"""Shared helpers for chapter 7.16 (distribution families) figures.

Exact formulas only; Phi via math.erf, bivariate normal CDF by 1-D integration.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
SEED = 716


def phi(z):
    return np.exp(-np.asarray(z, float)**2/2)/math.sqrt(2*math.pi)


def Phi(z):
    z = np.asarray(z, float)
    return 0.5*(1+np.vectorize(math.erf)(z/math.sqrt(2)))


def Phi_inv(u):
    """Inverse standard normal CDF by bisection (vectorised)."""
    u = np.atleast_1d(np.asarray(u, float))
    lo = np.full_like(u, -12.0); hi = np.full_like(u, 12.0)
    for _ in range(80):
        mid = (lo+hi)/2
        m = Phi(mid) < u
        lo = np.where(m, mid, lo); hi = np.where(m, hi, mid)
    return (lo+hi)/2


def binorm_cdf(a, b, rho, n=4000):
    """P(G1<=a, G2<=b) for standard bivariate normal with correlation rho.
    Integrate phi(x) * Phi((b - rho x)/sqrt(1-rho^2)) over x <= a."""
    x = np.linspace(-9, a, n)
    y = phi(x)*Phi((b-rho*x)/math.sqrt(1-rho*rho))
    return float(np.trapezoid(y, x))


def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha='center', va='top')


def simplex_xy(p):
    """Barycentric (p0,p1,p2) -> plane; vertices delta0=(0,0), delta1=(1,0), delta2=(1/2, sqrt3/2)."""
    p = np.asarray(p, float)
    x = p[..., 1] + 0.5*p[..., 2]
    y = (math.sqrt(3)/2)*p[..., 2]
    return x, y
