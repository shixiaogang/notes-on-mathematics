from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -u''+cu=1, Dirichlet, c>=0; and c=-pi^2 kernel.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.27)
ax = axes[0]
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
for c, co in ((10, YELLOW), (100, PURPLE)):
    s = np.sqrt(c); ax.plot(X, (1-np.cosh(s*(X-.5))/np.cosh(s/2))/c, color=co, lw=1.4)
    ax.axhline(1/c, color=co, lw=.85, ls=DOT)
lab(ax, .5, .127, '$c=0$', BLUE, ha='center', va='bottom'); lab(ax, .5, .05, '$c=10$', YELLOW, ha='center', va='top'); lab(ax, .5, .016, '$c=100$', PURPLE, ha='center', va='bottom', fontsize=7.5)
dot(ax, 0, 0, RED, 4); dot(ax, 1, 0, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.002, .155); ax.set_xticks([0, 1]); ax.set_yticks([0, .1]); hat01(ax, yl='$u$')
ax = axes[1]
ax.axhline(0, color=STROKE, lw=.6)
for a, co in ((1, RED), (.5, RED), (-.7, RED)):
    ax.plot(X, a*np.sin(np.pi*X), color=co, lw=1.3)
dot(ax, 0, 0, RED, 4); dot(ax, 1, 0, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.9, 1.15); ax.set_xticks([0, 1]); ax.set_yticks([-.5, 0, 1]); hat01(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'c>=0': 'u=(1-cosh(sqrt c (x-1/2))/cosh(sqrt c/2))/c', 'c=-pi^2': 'A sin(pi x)'})
