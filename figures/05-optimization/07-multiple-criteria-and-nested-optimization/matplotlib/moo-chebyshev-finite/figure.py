from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Weighted Chebyshev on the finite candidates with z=(0,0): (a) w=(1/2,1/2) picks C. (b) w=(0.1,0.9) ties D and F.
def score(w): return {k: max(w[0]*v[0], w[1]*v[1]) for k, v in CANDS.items()}
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .2, .22)
for ax, w, lev in zip(axes, ((.5, .5), (.1, .9)), (2., .9)):
    setup(ax, (0, 10), (0, 9.5), range(0, 11, 2), range(0, 10, 2))
    c = (lev/w[0], lev/w[1]); ax.fill([0, c[0], c[0], 0], [0, 0, c[1], c[1]], color=GREEN_FILL, lw=0, zorder=1)
    ax.plot([0, c[0], c[0]], [c[1], c[1], 0], color=PURPLE, lw=1.2, zorder=3)
    ax.plot([0, c[0]], [0, c[1]], color=GREEN, lw=.85, zorder=2)
    cands(ax, 'ABCDEF', off={'A': (.25, .2), 'B': (.25, .2), 'C': (.25, .3), 'D': (-.3, .4), 'E': (.25, .2), 'F': (.1, .4)})
hollow(axes[0], (0, 0), INK); hollow(axes[1], (0, 0), INK)
tags(fig, axes)
s1, s2 = score((.5, .5)), score((.1, .9))
save(fig, HERE, 'figure', {'score_a': s1, 'score_b': s2}); print(s1, s2)
