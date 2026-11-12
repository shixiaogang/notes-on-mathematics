"""Shared helpers for the chapter 7.25 figures (channel codes).

Every value is an exact finite sum or enumeration over all binary words; no
hand-entered data. Information in bits (log base 2). Running channel: BSC(0.1).
"""
from pathlib import Path
import sys, math, itertools
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
P = 0.1   # running flip probability


def h2(x):
    x = np.asarray(x, float)
    with np.errstate(all='ignore'):
        r = -(x*np.log2(x) + (1-x)*np.log2(1-x))
    return np.where((x <= 0) | (x >= 1), 0.0, r)


def h2inv(y):
    "inverse of h2 on [0, 1/2]"
    lo, hi = 0.0, 0.5
    for _ in range(80):
        m = (lo+hi)/2
        if h2(m) < y: lo = m
        else: hi = m
    return (lo+hi)/2


def lbinom(n, k):
    return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)


def tail(n, t, p):
    "P(Bin(n,p) > t)"
    return sum(math.comb(n, j)*p**j*(1-p)**(n-j) for j in range(t+1, n+1))


# the [5,2,3] running code and the [7,4,3] Hamming code
G5 = np.array([[1, 0, 1, 1, 0], [0, 1, 0, 1, 1]])
H5 = np.array([[1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 0, 1]])
H7 = np.array([[(j >> b) & 1 for j in range(1, 8)] for b in range(3)])
G7 = np.array([[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]])


def words(n):
    return [np.array(w) for w in itertools.product([0, 1], repeat=n)]


def ham_ber(p):
    "exact bit error rate of syndrome decoding for the [7,4,3] code; data at positions 3,5,6,7"
    data = [2, 4, 5, 6]; tot = 0.0
    for e in words(7):
        w = e.sum(); pr = p**w*(1-p)**(7-w)
        s = H7 @ e % 2; pos = s[0]+2*s[1]+4*s[2]
        r = e.copy()
        if pos: r[pos-1] ^= 1
        tot += pr*r[data].sum()/4
    return tot


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


def logticks(ax, exps, axis='y'):
    ax.minorticks_off()
    vals = [10.0**e for e in exps]
    labs = ['$1$' if e == 0 else '$10$' if e == 1 else '$10^{%d}$' % e for e in exps]
    if axis == 'y':
        ax.set_yticks(vals); ax.set_yticklabels(labs)
    else:
        ax.set_xticks(vals); ax.set_xticklabels(labs)
