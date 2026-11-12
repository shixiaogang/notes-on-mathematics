from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# (a) N(0,n) cdfs Phi(x/sqrt n), n=1,9,81 -> 1/2; (b) 1/2 delta_0 + 1/2 delta_n cdfs, n=3,6 -> defective 1/2 1{x>=0}.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; x = np.linspace(-10, 10, 600)
for n, c in ((1, BLUE), (9, GREEN), (81, YELLOW)): ax.plot(x, Phi(x/np.sqrt(n)), color=c, lw=1.4)
ax.axhline(.5, color=PURPLE, lw=1.0, ls=DASH)
lab(ax, -1.9, .1, r'$n=1$', BLUE, ha='right'); lab(ax, 7.5, .62, r'$n=81$', YELLOW, ha='center')
ax.set_xlim(-10, 10); ax.set_ylim(0, 1.05); ax.set_xticks([-10, -5, 0, 5, 10]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
ax = axes[1]
step_cdf(ax, [0, 3], [.5, .5], -1.5, 8, GREEN, lw=1.2, z=4)
step_cdf(ax, [0, 6], [.5, .5], -1.5, 8, YELLOW, lw=1.5, z=3)
ax.plot([-1.5, 0], [0, 0], color=PURPLE, lw=1.0, ls=DASH); ax.plot([0, 8], [.5, .5], color=PURPLE, lw=1.0, ls=DASH)
lab(ax, 3.1, .78, r'$n=3$', GREEN); lab(ax, 6.1, .9, r'$n=6$', YELLOW)
ax.set_xlim(-1.5, 8); ax.set_ylim(0, 1.08); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'limit_a': 0.5, 'limit_b_mass': 0.5})
