from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Heat multiplier and its action on the box spectrum, and the resulting field.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.07, wspace=.36, bottom=.27)
xi = np.linspace(0, 6, 800); cc = shades(3)
ax = axes[0]
for t, c in zip((.001, .01, .1), cc): ax.plot(xi, np.exp(-4*pi**2*xi**2*t), color=c, lw=1.4)
lab(ax, 3.9, .6, '$t=0.001$', cc[0], ha='left', fontsize=7.5); lab(ax, 1.75, .45, '$0.01$', cc[1], ha='left'); lab(ax, .75, .12, '$0.1$', cc[2], ha='left')
ax.set_xlim(0, 6); ax.set_ylim(0, 1.05); ax.set_xticks([0, 3, 6]); ax.set_yticks([0, 1]); axlab(ax, r'$|\xi|$', r'$\mathrm{e}^{-4\pi^2\xi^2 t}$')
ax = axes[1]
B = np.sinc(xi)
ax.plot(xi, B, color=RED, lw=1.3); ax.plot(xi, B*np.exp(-4*pi**2*xi**2*.01), color=BLUE, lw=1.4)
ax.axhline(0, color=STROKE, lw=.6)
lab(ax, 2.6, .28, r'$\widehat{u}_0$', RED, ha='left'); lab(ax, 1.15, .55, r'$\widehat{u}(\cdot,0.01)$', BLUE, ha='left')
ax.set_xlim(0, 6); ax.set_ylim(-.3, 1.05); ax.set_xticks([0, 3, 6]); ax.set_yticks([0, 1]); axlab(ax, r'$\xi$')
ax = axes[2]; xx = np.linspace(-1.5, 1.5, 700)
ax.plot(xx, (np.abs(xx) < .5)*1., color=RED, lw=1.3); ax.plot(xx, box(xx, .01), color=BLUE, lw=1.4)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-.04, 1.15); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); axlab(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'factor xi=5 t=.01': float(np.exp(-4*pi**2*25*.01))})
