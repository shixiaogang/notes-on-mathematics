from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# (a) region U/V<=0.5 in the unit square; (b) density of U/V; (c) iid N(0,1): double wedge {Y/X<=1}, seed 17, 1500 points.
from matplotlib.patches import Polygon, Wedge
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.11, right=.98, bottom=.3, top=.95, wspace=.38)
ax = axes[0]
ax.add_patch(Polygon([[0, 0], [0, 1], [.5, 1]], fc=BLUE_FILL, ec=BLUE, lw=.8))
ax.plot([0, 1], [0, .5], color=MUTED, lw=.7); ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=.8)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.03, 1.05); ax.set_aspect('equal'); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1]); axlab(ax, '$u$', '$v$')
ax = axes[1]; r = np.linspace(0, 6, 600); f = .5*np.minimum(1, 1/np.maximum(r, 1e-9)**2)
ax.plot(r, f, color=BLUE, lw=1.4); ax.set_xlim(0, 6); ax.set_ylim(0, .6); ax.set_xticks([0, 1, 3, 6]); ax.set_yticks([0, .25, .5]); axlab(ax, '$r$')
ax = axes[2]; R = 3.4
ax.add_patch(Wedge((0, 0), R, -90, 45, fc=BLUE_FILL, ec=BLUE, lw=.8)); ax.add_patch(Wedge((0, 0), R, 90, 225, fc=BLUE_FILL, ec=BLUE, lw=.8))
rng = np.random.default_rng(17); X = rng.standard_normal((1500, 2)); ax.plot(X[:, 0], X[:, 1], 'o', ms=1.0, color=GREEN, mew=0)
ax.plot([-R/np.sqrt(2), R/np.sqrt(2)], [-R/np.sqrt(2), R/np.sqrt(2)], color=STROKE, lw=.7)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5); ax.set_aspect('equal'); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$x$', '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 17, 'sim P(Y/X<=1)': float(np.mean(X[:, 1]/X[:, 0] <= 1)), 'exact': .75})
