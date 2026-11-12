from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Expectation as balance point: (a) reward table, E X = 2; (b) density 2x on (0,1), E X = 2/3.
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.1, right=.98, bottom=.3, wspace=.28)
ax = axes[0]
bars(ax, XV, PV, width=.7)
ax.plot([-1, 7], [0, 0], color=STROKE, lw=1.1, zorder=3)
m = (XV*PV).sum()
fulcrum(ax, m, 0, .07, .7)
for x, p, s in zip(XV, PV, ['1/2', '1/3', '1/6']):
    lab(ax, x, p+.015, s, ha='center', va='bottom')
lab(ax, m+.45, -.05, r"$\mu=2$", RED, ha='left', va='center')
ax.set_xlim(-1, 7); ax.set_ylim(-.1, .62); ax.set_xticks([0, 3, 6]); ax.set_yticks([0, .25, .5])
ax.spines['bottom'].set_visible(False); ax.set_xticks([0,3,6]); ax.tick_params(axis='x', length=0); axlab(ax, '', '$p_X(x)$')
ax = axes[1]
x = np.linspace(0, 1, 400)
ax.fill_between(x, 0, 2*x, color=BLUE_FILL, lw=0)
ax.plot(x, 2*x, color=BLUE, lw=1.4)
ax.plot([-.1, 1.1], [0, 0], color=STROKE, lw=1.1, zorder=3)
fulcrum(ax, 2/3, 0, .2, .1)
lab(ax, 2/3+.07, -.13, r"$\mu=2/3$", RED, ha='left', va='center')
lab(ax, .3, 1.15, r'$f_X(x)=2x$', BLUE, ha='center')
ax.set_xlim(-.1, 1.1); ax.set_ylim(-.3, 2.15); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, 1, 2])
ax.spines['bottom'].set_visible(False); ax.tick_params(axis='x', length=0); axlab(ax, '', '$f_X(x)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E reward': float(m), 'E density': float(np.trapezoid(x*2*x, x))})
