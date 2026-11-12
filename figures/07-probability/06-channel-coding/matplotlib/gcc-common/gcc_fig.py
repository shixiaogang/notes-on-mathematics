"""Shared helpers for the chapter 7.24 figures (capacity of Gaussian channels).

Running examples of the chapter (all numbers are computed by the scripts):
  scalar channel   sigma^2 = 1, P = 3, so P/sigma^2 = 3 and C = 1 bit per use;
  parallel channel sigma_j^2 = (1, 2, 5), total power P = 5, water level 4;
  correlated noise Sigma = [[2, 1], [1, 2]], eigenvalues (1, 3), P = 2.
Simulations use numpy.random.default_rng with the seed stated in each script.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
LOG2E = 1/math.log(2)


def cap(snr):
    "capacity 0.5*log2(1+snr) in bit per real channel use"
    return .5*np.log2(1+np.asarray(snr, float))


def phi(t, var=1.0):
    return np.exp(-np.asarray(t)**2/(2*var))/np.sqrt(2*np.pi*var)


def Qf(x):
    from math import erfc
    return np.vectorize(lambda t: .5*erfc(t/math.sqrt(2)))(x)


def h2(p):
    p = np.clip(np.asarray(p, float), 1e-300, 1-1e-16)
    return -(p*np.log2(p)+(1-p)*np.log2(1-p))


def diff_entropy(f, dy):
    "differential entropy in bit of a density sampled on a uniform grid"
    m = f > 0
    return float(-(f[m]*np.log2(f[m])).sum()*dy)


def binary_input_capacity(snr):
    "I(X;X+Z) in bit, X uniform on {+-sqrt(snr)}, Z ~ N(0,1); numerical integration"
    A = math.sqrt(snr); y = np.linspace(-A-12, A+12, 60001); dy = y[1]-y[0]
    f = .5*(phi(y-A)+phi(y+A))
    return diff_entropy(f, dy) - .5*math.log2(2*math.pi*math.e)


def waterfill(s, P):
    "water filling over noise levels s (any order); returns level nu and powers in the given order"
    s = np.asarray(s, float); o = np.argsort(s); ss = s[o]
    nu = ss[0]
    for k in range(len(ss), 0, -1):
        nu = (P+ss[:k].sum())/k
        if nu > ss[k-1] or (k == 1):
            break
    return nu, np.maximum(nu-s, 0)


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
