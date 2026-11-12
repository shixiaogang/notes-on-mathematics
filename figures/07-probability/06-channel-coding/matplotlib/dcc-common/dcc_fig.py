"""Shared helpers for the chapter 7.23 figures (capacity of discrete channels).

Every curve is computed from a closed-form formula, an exact finite sum, or a
seeded simulation; no hand-entered data. Information in bits (log base 2).
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))

# channels used throughout the chapter
BSC_P = 0.1
BEC_E = 0.25
Z = np.array([[1.0, 0.0], [0.5, 0.5]])          # Z-channel: 1 -> 0 with prob 1/2


def bsc(p):
    return np.array([[1-p, p], [p, 1-p]])


def bec(e):
    return np.array([[1-e, e, 0.0], [0.0, e, 1-e]])   # outputs 0, e, 1


def h2(p):
    p = np.asarray(p, float)
    with np.errstate(all='ignore'):
        r = -(p*np.log2(p) + (1-p)*np.log2(1-p))
    return np.where((p <= 0) | (p >= 1), 0.0, r)


def kl(a, b):
    m = a > 0
    return float(np.sum(a[m]*np.log2(a[m]/b[m])))


def mi(q, W):
    p = q @ W
    return sum(q[x]*kl(W[x], p) for x in range(len(q)) if q[x] > 0)


def ba(W, q, T, c=None, s=0.0):
    "Blahut-Arimoto rounds: list of (q, pY, D_x - s c(x), lower, upper)"
    out = []
    for _ in range(T):
        pY = q @ W
        Dx = np.array([kl(W[x], pY) for x in range(len(q))])
        if c is not None:
            Dx = Dx - s*np.asarray(c)
        L = math.log2(np.sum(q*2**Dx)); U = Dx.max()
        out.append((q.copy(), pY, Dx, L, U))
        q = q*2**Dx; q = q/q.sum()
    return out


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


def binpmf(n, p=.5):
    "exact Bin(n,p) masses via log-gamma"
    k = np.arange(n+1)
    lg = np.array([math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1) for i in k])
    with np.errstate(divide='ignore'):
        return np.exp(lg + k*np.log(p) + (n-k)*np.log(1-p))
