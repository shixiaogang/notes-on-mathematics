from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Exact derivative growth for a jump and a kink on the line.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.28, bottom=.27)
ax = axes[0]; xx = np.linspace(-.6, .6, 800); cc = shades(3)
for t, c in zip((.0025, .01, .04), cc): ax.plot(xx, 2*gauss(xx, t), color=c, lw=1.4)
lab(ax, .05, 10.6, '$t=0.0025$', cc[0], ha='left'); lab(ax, .29, 2.0, '$t=0.04$', cc[2], ha='left')
ax.set_xlim(-.6, .6); ax.set_ylim(0, 12.5); ax.set_xticks([-.5, 0, .5]); ax.set_yticks([0, 5, 10]); axlab(ax, yl=r'$\partial_x u$')
ax = axes[1]; T = np.logspace(-4, 0, 80)
ax.loglog(T, 1/np.sqrt(pi*T), color=BLUE, lw=1.5); ax.loglog(T, 0*T+1, color=YELLOW, lw=1.5); ax.loglog(T, 2/(np.sqrt(8*pi)*T)*np.exp(-.5), color=RED, lw=1.5)
lab(ax, 2e-4, .75, '折线，一阶导数', YELLOW, ha='left', va='top'); lab(ax, 1.2e-4, 6, '跳跃，一阶导数', BLUE, ha='left', va='top')
lab(ax, 8e-3, 60, '跳跃，二阶导数', RED, ha='left', va='bottom')
ax.set_xlim(1e-4, 1); ax.set_ylim(.3, 3000); ax.minorticks_off(); ax.set_xticks([1e-4, 1e-2, 1]); ax.set_xticklabels(['$10^{-4}$', '$10^{-2}$', '1']); ax.set_yticks([1, 10, 100, 1000]); ax.set_yticklabels(['1', '10', '100', '1000']); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'1/sqrt(pi t) .01': float(1/np.sqrt(pi*.01))})
