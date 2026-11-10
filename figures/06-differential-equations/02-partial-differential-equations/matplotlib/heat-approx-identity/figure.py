from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Kernel mass concentrates: tail outside |y|>delta tends to zero.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
yy = np.linspace(-1, 1, 1000); d = .15
ax = axes[0]; t = .01
g = gauss(yy, t)
ax.fill_between(yy, 0, g, where=np.abs(yy) >= d, color=RED_FILL, lw=0)
ax.plot(yy, g, color=BLUE, lw=1.4); ax.plot(yy, gauss(yy, .04), color=YELLOW, lw=1.3)
ax.axvline(d, color=STROKE, lw=.8, ls=DOT); ax.axvline(-d, color=STROKE, lw=.8, ls=DOT)
lab(ax, .2, 2.65, '$t=0.01$', BLUE, ha='left'); lab(ax, .55, .62, '$t=0.04$', YELLOW, ha='left')
ax.set_xlim(-1, 1); ax.set_ylim(0, 3.05); ax.set_xticks([-d, 0, d]); ax.set_xticklabels([r'$-\delta$', '0', r'$\delta$']); ax.set_yticks([0, 1, 2, 3]); axlab(ax, '$y$', '$G(y,t)$')
ax = axes[1]; T = np.logspace(-3.2, 0, 300)
ax.semilogx(T, erfc(d/(2*np.sqrt(T))), color=RED, lw=1.4)
ax.set_xlim(6e-4, 1); ax.set_ylim(0, 1.03); ax.minorticks_off(); ax.set_xticks([1e-3, 1e-2, 1e-1, 1]); ax.set_xticklabels(['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '1']); ax.set_yticks([0, .5, 1]); axlab(ax, '$t$', '尾部质量')
tags(fig, axes)
save(fig, HERE, 'figure', {'tail d=.15,t=.01': float(math.erfc(.15/(2*.1)))})
