"""Shared helpers for the chapter 7.20 figures (lossless coding).

Running source of the chapter: alphabet {a,b,c,d} with probabilities
(0.4, 0.3, 0.2, 0.1). Every number is computed here (Huffman by a heap,
arithmetic-coding intervals in exact rationals, type classes enumerated
exactly, simulations with fixed seeds); no hand-entered data.
"""
from pathlib import Path
import sys, math, heapq, itertools
from fractions import Fraction
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
P = np.array([.4, .3, .2, .1]); NAMES = 'abcd'
PF = [Fraction(4, 10), Fraction(3, 10), Fraction(2, 10), Fraction(1, 10)]


def entropy(p):
    p = np.asarray(p, float); p = p[p > 0]
    return float(-(p*np.log2(p)).sum())


H = entropy(P)


def huffman_lengths(probs):
    "binary Huffman code lengths; ties broken by insertion order (original symbols first)"
    h = [(q, i, [i]) for i, q in enumerate(probs)]; heapq.heapify(h)
    L = [0]*len(probs); c = len(probs)
    if len(probs) == 1:
        return np.array([1])
    while len(h) > 1:
        a = heapq.heappop(h); b = heapq.heappop(h)
        for s in a[2]+b[2]:
            L[s] += 1
        heapq.heappush(h, (a[0]+b[0], c, a[2]+b[2])); c += 1
    return np.array(L)


def block_probs(n, p=P):
    return np.array([float(np.prod(t)) for t in itertools.product(p, repeat=n)])


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
