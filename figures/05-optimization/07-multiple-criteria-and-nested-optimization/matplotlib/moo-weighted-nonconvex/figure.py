from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# (a) concave front (x,1-x^2): weighted sums only reach the two ends. (b) front with a dent and its convex hull.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
ax = axes[0]; setup(ax, (0, 1.2), (0, 1.2), [0, .5, 1], [0, .5, 1], equal=True)
x = np.linspace(0, 1, 300); ax.fill(np.r_[x, 1, 1.2, 1.2, 0], np.r_[1-x**2, 0, 0, 1.2, 1.2], color=BLUE_FILL, lw=0, zorder=1)
ax.plot(x, 1-x**2, color=YELLOW, lw=2.4, zorder=3)
for w, c in ((.5, .5), (.3, .3), (.7, .3)):
    t = np.array([0, 1.2]); ax.plot(t, (c-w*t)/(1-w), color=PURPLE, lw=1.1, zorder=4)
dot(ax, (0, 1)); dot(ax, (1, 0))
ax.text(.04, 1.05, '$(0,1)$', color=INK, fontsize=7.5); ax.text(1.0, .06, '$(1,0)$', color=INK, fontsize=7.5)
ax = axes[1]; setup(ax, (0, 1.2), (0, 1.2), [0, .5, 1], [0, .5, 1], equal=True)
u = np.linspace(0, 1, 4001); v = bump(u); H = lower_hull(u, v)
ax.fill(np.r_[u, 1, 1.2, 1.2, 0], np.r_[v, 0, 0, 1.2, 1.2], color=BLUE_FILL, lw=0, zorder=1)
ax.plot(u, v, color=RED, lw=2, zorder=3)
Hv = np.interp(u, H[:, 0], H[:, 1]); miss = v > Hv+1e-5
ax.plot(u[miss], v[miss], color=YELLOW, lw=2.6, zorder=4, solid_capstyle='round')
ax.plot(H[:, 0], H[:, 1], color=PURPLE, lw=1.0, ls=(0, (3, 2)), zorder=5)
save_range = (float(u[miss].min()), float(u[miss].max()))
ax.annotate('', xy=(0, 0)) if 0 else None
tags(fig, axes)
save(fig, HERE, 'figure', {'dent': save_range}); print(save_range)
