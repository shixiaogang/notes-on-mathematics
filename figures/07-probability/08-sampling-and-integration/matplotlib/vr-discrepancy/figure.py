from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
import matplotlib.patches as mp
# Star discrepancy D* = sup_b | #{i: a_i in [0,b)}/n - b1 b2 | for n = 13 points in [0,1)^2.
# (a) 13 independent uniform points (seed 4).  (b) Fibonacci lattice a_i = ((i-1)/13, frac(8(i-1)/13)).
# D* is computed exactly by checking all boxes with corners at point coordinates or 1 (closed and open limits);
# the box attaining the supremum is shaded.
n = 13
rng = np.random.default_rng(4); P1 = rng.random((n, 2))
i = np.arange(n); P2 = np.stack([i/n, (8*i % n)/n], 1)
def star(P):
    xs = np.unique(np.r_[P[:, 0], 1.0]); ys = np.unique(np.r_[P[:, 1], 1.0]); best = (0, None, None)
    for bx in xs:
        for by in ys:
            vol = bx*by
            op = np.sum((P[:, 0] < bx) & (P[:, 1] < by))/n     # open box count
            cl = np.sum((P[:, 0] <= bx) & (P[:, 1] <= by))/n   # closed box (limit from above)
            for val in (abs(op-vol), abs(cl-vol)):
                if val > best[0]: best = (val, bx, by)
    return best
d1 = star(P1); d2 = star(P2)
fig, axs = figure(width_mm=100, height_mm=56, ncols=2)
panel(fig, left=.11, right=.97, bottom=.22, top=.97, wspace=.34)
for ax, P, d in zip(axs, (P1, P2), (d1, d2)):
    ax.add_patch(mp.Rectangle((0, 0), d[1], d[2], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.8))
    ax.plot(P[:, 0], P[:, 1], 'o', ms=3.4, color=GREEN, mew=0, zorder=5, clip_on=False)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal'); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    axlab(ax, '$u_1$', '$u_2$')
tags(fig, axs)
cnt = lambda P, d: int(np.sum((P[:, 0] < d[1]) & (P[:, 1] < d[2])))
save(fig, HERE, 'figure', {'Dstar_iid': d1[0], 'box_iid': [d1[1], d1[2]], 'count_iid_open': cnt(P1, d1),
     'Dstar_lattice': d2[0], 'box_lattice': [d2[1], d2[2]], 'count_lattice_open': cnt(P2, d2)})
