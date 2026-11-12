from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Latin hypercube, n = 4, d = 2: U_{i,j} = (pi_j(i) - 1 + V_{i,j})/4.
# (a) pi_1 = (2,4,1,3), pi_2 = (1,3,2,4); V_{:,1} = (0.37,0.81,0.06,0.52), V_{:,2} = (0.23,0.68,0.45,0.91).
# (b) same V with pi_1 = pi_2 = (1,2,3,4): also a valid Latin hypercube, but all points in diagonal cells.
V1 = [.37, .81, .06, .52]; V2 = [.23, .68, .45, .91]
def lhs(p1, p2):
    return [((p1[i]-1+V1[i])/4, (p2[i]-1+V2[i])/4) for i in range(4)]
A = lhs([2, 4, 1, 3], [1, 3, 2, 4]); Bp = lhs([1, 2, 3, 4], [1, 2, 3, 4])
fig, axs = figure(width_mm=100, height_mm=56, ncols=2)
panel(fig, left=.11, right=.97, bottom=.22, top=.97, wspace=.34)
for ax, P in zip(axs, (A, Bp)):
    for x, y in P:
        cx, cy = math.floor(4*x)/4, math.floor(4*y)/4
        ax.add_patch(__import__('matplotlib').patches.Rectangle((cx, cy), .25, .25, color=BLUE_FILL, lw=0))
    for t in np.arange(0, 1.01, .25):
        ax.plot([t, t], [0, 1], color=STROKE, lw=.5); ax.plot([0, 1], [t, t], color=STROKE, lw=.5)
    for x, y in P:
        dot(ax, x, y, color=GREEN, ms=4)
        ax.plot([x, x], [-.05, 0], color=GREEN, lw=1.2, clip_on=False); ax.plot([-.05, 0], [y, y], color=GREEN, lw=1.2, clip_on=False)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal')
    ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); ax.tick_params(pad=6)
    ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False)
    axlab(ax, '$u_1$', '$u_2$', pad=4)
tags(fig, axs)
save(fig, HERE, 'figure', {'points_a': A, 'points_b': Bp})
