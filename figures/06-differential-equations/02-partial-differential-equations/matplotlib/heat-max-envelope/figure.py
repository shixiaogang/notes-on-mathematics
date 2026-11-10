from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Max and min of u0=sin(pi x)+sin(5 pi x) under zero ends: never leave initial/boundary range.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.28, bottom=.27)
xx = np.linspace(0, 1, 2001)
U = lambda t: np.exp(-pi**2*t)*np.sin(pi*xx)+np.exp(-25*pi**2*t)*np.sin(5*pi*xx)
ax = axes[0]; cc = shades(3)
ax.plot(xx, U(0), color=RED, lw=1.4)
for t, c in zip((.001, .005, .03), cc): ax.plot(xx, U(t), color=c, lw=1.4)
ax.axhline(0, color=STROKE, lw=.6); ax.axhline(U(0).max(), color=STROKE, lw=.8, ls=DOT); ax.axhline(U(0).min(), color=STROKE, lw=.8, ls=DOT)
ax.set_xlim(0, 1); ax.set_ylim(-.9, 2.1); ax.set_xticks([0, .5, 1]); ax.set_yticks([-.5, 0, 1, 2]); axlab(ax, yl='$u$')
ax = axes[1]; T = np.linspace(0, .06, 300)
ax.plot(T, [U(t).max() for t in T], color=BLUE, lw=1.4); ax.plot(T, [U(t).min() for t in T], color=YELLOW, lw=1.4)
ax.axhline(0, color=STROKE, lw=.6)
lab(ax, .035, 1.0, r'$\max_x u$', BLUE, ha='left'); lab(ax, .018, -.17, r'$\min_x u$', YELLOW, ha='left', va='top')
ax.set_xlim(0, .06); ax.set_ylim(-.9, 2.1); ax.set_xticks([0, .03, .06]); ax.set_xticklabels(['0', '0.03', '0.06']); ax.set_yticks([-.5, 0, 1, 2]); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'max0': float(U(0).max()), 'min0': float(U(0).min())}); print(U(0).max(), U(0).min())
