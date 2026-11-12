from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Same N(0,1) marginals, different pairings: (Z,Z), (Z,-Z), (Z,Z') independent. 400 points, seed 7.
rng = np.random.default_rng(7); Z = rng.standard_normal(400); Z2 = rng.standard_normal(400)
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06, right=.98, top=.97, bottom=.24, wspace=.32)
for ax, yv in zip(axes, (Z, -Z, Z2)):
    ax.plot(Z, yv, 'o', ms=1.6, color=GREEN, mew=0)
    ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5); ax.set_aspect('equal')
    ax.set_xticks([-3, 0, 3]); ax.set_yticks([-3, 0, 3]); axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 7, 'n': 400})
