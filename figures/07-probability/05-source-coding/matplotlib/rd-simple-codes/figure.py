"""Rate and expected Hamming distortion of four simple block codes for X~Bern(0.3).
Exact sums over source blocks; time-sharing segment between (D,R)=(0.3,0) and (0,1)."""
from pathlib import Path
import sys
import itertools
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *


def code_perf(n, book, p=P_SRC):
    """exact expected per-letter Hamming distortion with nearest-codeword encoder"""
    E = 0.
    for x in itertools.product([0, 1], repeat=n):
        px = np.prod([p if b else 1-p for b in x])
        E += px*min(sum(a != b for a, b in zip(x, c)) for c in book)/n
    return E


pts = {
    'const': (code_perf(1, [(0,)]), 0.),
    'ident': (code_perf(1, [(0,), (1,)]), 1.),
    'rep3': (code_perf(3, [(0, 0, 0), (1, 1, 1)]), 1/3),
    'four3': (code_perf(3, [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]), 2/3),
}
fig, ax = figure(width_mm=86, height_mm=52)
ax.plot([0, .3], [1, 0], color=PURPLE, lw=1.1, ls=DASH, zorder=2)
for k, (D, R) in pts.items():
    dot(ax, D, R, GREEN, ms=5)
lab(ax, .29, .06, '只发一个码字', INK, ha='right')
lab(ax, .012, 1.0, '逐位照传', INK, ha='left', va='center')
D, R = pts['rep3']; lab(ax, D+.008, R+.03, '$\\{000,111\\}$', INK, ha='left')
D, R = pts['four3']; lab(ax, D+.008, R+.03, '$\\{000,100,010,001\\}$', INK, ha='left')
lab(ax, .17, .5, '分时', PURPLE, ha='left')
ax.set_xlim(0, .34); ax.set_ylim(0, 1.1)
ax.set_xticks([0, .1, .2, .3]); ax.set_yticks([0, 1/3, 2/3, 1]); ax.set_yticklabels(['0', '1/3', '2/3', '1'])
axlab(ax, '平均失真', '码率（bit/符号）')
save(fig, HERE, 'figure', {k: list(v) for k, v in pts.items()})
