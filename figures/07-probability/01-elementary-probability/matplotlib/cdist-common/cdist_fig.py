"""Shared helpers for the chapter 7.4 (common distributions) figures.

All values are computed from the closed-form mass functions and densities;
no hand-entered data.  Only math, numpy and matplotlib are used.
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

LINE = '#4C4D4F'
DASH = (0, (4, 2))
DOT = (0, (1.4, 1.6))


def here(f):
    return Path(f).resolve().parent


def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)


def panel(fig, left=.09, right=.98, top=.96, bottom=.27, wspace=.32):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom', fontsize=8, color=INK)


def bars(ax, xs, ps, color=BLUE, fill=BLUE_FILL, width=.55, **kw):
    ax.bar(xs, ps, width=width, color=fill, edgecolor=color, linewidth=.9, **kw)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5)
    ax.text(x, y, s, color=color, **k)


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


# ---------- closed forms ----------
def binom_pmf(n, p):
    return np.array([math.comb(n, k)*p**k*(1-p)**(n-k) for k in range(n+1)])


def hyper_pmf(N, K, n):
    return np.array([math.comb(K, k)*math.comb(N-K, n-k)/math.comb(N, n) for k in range(n+1)])


def poisson_pmf(lam, kmax):
    return np.array([math.exp(-lam + k*math.log(lam) - math.lgamma(k+1)) for k in range(kmax+1)])


def phi(z):
    return np.exp(-z**2/2)/math.sqrt(2*math.pi)


Phi = np.vectorize(lambda z: .5*(1+math.erf(z/math.sqrt(2))))


def gamma_pdf(x, a, b):
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(a*math.log(b) - math.lgamma(a) + (a-1)*np.log(x[m]) - b*x[m])
    return out


def beta_pdf(x, a, b):
    x = np.asarray(x, float)
    lb = math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b)
    return np.exp((a-1)*np.log(x)+(b-1)*np.log1p(-x)-lb)


def t_pdf(x, nu, s=1.0):
    c = math.exp(math.lgamma((nu+1)/2)-math.lgamma(nu/2))/math.sqrt(nu*math.pi)/s
    return c*(1+(np.asarray(x)/s)**2/nu)**(-(nu+1)/2)


def laplace_pdf(x, b):
    return np.exp(-np.abs(x)/b)/(2*b)
