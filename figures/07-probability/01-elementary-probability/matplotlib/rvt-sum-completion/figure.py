from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X1,X2 iid Unif(0,1), Z = X1+X2: preimage of {Z<=0.7}, strip 0.7<Z<=0.8, triangle density.
from matplotlib.patches import Polygon
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.25, top=.96, wspace=.25)
ax = axes[0]
ax.add_patch(Polygon([[0, 0], [.7, 0], [0, .7]], fc=BLUE_FILL, ec=BLUE, lw=.8))
ax.add_patch(Polygon([[.7, 0], [.8, 0], [0, .8], [0, .7]], fc=RED_FILL, ec=RED, lw=.8))
for z in (.3, 1.2, 1.6):
    a0, a1 = max(0, z-1), min(1, z); ax.plot([a0, a1], [z-a0, z-a1], color=MUTED, lw=.6)
ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=.8)
lab(ax, .2, .2, '$Z\\leq0.7$', INK, ha='center'); lab(ax, .64, .64, '$x_1+x_2=1.2$', MUTED, ha='center', va='bottom', rotation=-45)
ax.set_xlim(-.05, 1.08); ax.set_ylim(-.05, 1.08); ax.set_aspect('equal'); ax.set_xticks([0, .7, 1]); ax.set_yticks([0, .7, 1]); axlab(ax, '$x_1$', '$x_2$')
ax = axes[1]; z = np.linspace(-.2, 2.2, 500); f = np.clip(np.minimum(z, 2-z), 0, None)
ax.plot(z, f, color=BLUE, lw=1.4); dot(ax, .7, .7, RED)
ax.set_xlim(-.2, 2.2); ax.set_ylim(0, 1.1); ax.set_xticks([0, .7, 1, 2]); ax.set_yticks([0, .7, 1]); axlab(ax, '$z$')
tags(fig, axes)
save(fig, HERE, 'figure', {'strip_area': (.8**2-.7**2)/2, 'strip_area/dz': (.8**2-.7**2)/2/.1})
