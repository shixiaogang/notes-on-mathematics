"""Shared helpers for the tail-probability figures (chapter 7.5).

All curves are computed from closed-form formulas or exact finite sums;
no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
erfc = np.vectorize(math.erfc)

# Running example: X ~ Bin(20, 1/2)
N_BIN = 20
CB = np.array([math.comb(N_BIN, k) for k in range(N_BIN+1)], dtype=float)
PB = CB/2**N_BIN
KB = np.arange(N_BIN+1)

def bin_tail(k):
    "P(X >= k) for X ~ Bin(20,1/2)"
    return PB[k:].sum()

def bin_central_moment(p):
    return float((PB*np.abs(KB-10.0)**p).sum())

def bin_mgf(lam):
    return ((1+np.exp(lam))/2)**N_BIN

def Q(t):
    "standard normal right tail"
    return 0.5*erfc(np.asarray(t)/math.sqrt(2))

def normal_abs_moment(p):
    return 2**(p/2)*math.gamma((p+1)/2)/math.sqrt(math.pi)

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

def axlab(ax, xl='$t$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)

def logticks(ax, exps):
    ax.minorticks_off()
    ax.set_yticks([10.0**e for e in exps])
    ax.set_yticklabels(['$1$' if e == 0 else '$10^{%d}$' % e for e in exps])
