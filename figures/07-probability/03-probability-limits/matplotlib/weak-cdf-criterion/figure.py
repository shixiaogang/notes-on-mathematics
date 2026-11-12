from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# (a) cdfs of delta_0, delta_{1/4}, delta_{-1/4}; (b) lattice uniform cdfs floor(nx)/n for n=5,20 vs F(x)=x.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]
step_cdf(ax, [0], [1], -1, 1, BLUE, lw=2.0, z=2)
step_cdf(ax, [.25], [1], -1, 1, GREEN, lw=1.2, z=4)
step_cdf(ax, [-.25], [1], -1, 1, YELLOW, lw=1.5, z=3)
dot(ax, 0, 1, RED); ax.plot([0], [0], 'o', ms=3.6, mfc='white', mec=GREEN, mew=1.0, zorder=7)
lab(ax, .3, .45, r'$\delta_{1/4}$', GREEN); lab(ax, -.24, .45, r'$\delta_{-1/4}$', YELLOW, ha='right')
lab(ax, .04, 1.06, r'$F(0)=1$', RED)
ax.set_xlim(-1, 1); ax.set_ylim(-.06, 1.22); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
ax = axes[1]
for n, c, lw in ((5, GREEN, 1.2), (20, YELLOW, 1.2)):
    step_cdf(ax, np.arange(1, n+1)/n, np.full(n, 1/n), -.1, 1.1, c, lw=lw)
ax.plot([-.1, 0, 1, 1.1], [0, 0, 1, 1], color=BLUE, lw=1.4)
lab(ax, .62, .36, r'$n=5$', GREEN); lab(ax, .2, .52, r'$F(x)=x$', BLUE)
ax.set_xlim(-.1, 1.1); ax.set_ylim(-.06, 1.12); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'sup_error_bound': '1/n'})
