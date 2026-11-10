from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# Neumann: f=1-2x compatible, u=x^3/3-x^2/2+c; f=1 incompatible.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.27)
ax = axes[0]
base = X**3/3-X**2/2
ax.plot(X, base+.2, color=YELLOW, lw=1.4); ax.plot(X, base-.05, color=YELLOW, lw=1.4)
ax.plot(X, base+1/12, color=BLUE, lw=1.4)
lab(ax, .03, .012, r'$c=\frac{1}{12}$', BLUE, va='top'); lab(ax, .03, .225, r'$c=0.2$', YELLOW); lab(ax, .52, -.19, r'$c=-0.05$', YELLOW, va='top')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.28, .3); ax.set_xticks([0, 1]); ax.set_yticks([-.2, 0, .2]); hat01(ax, yl='$u$')
ax = axes[1]
ax.plot(X, X**2-X, color=BLUE, lw=1.4); ax.plot(X, -X, color=RED, lw=1.4)
ax.axhline(0, color=STROKE, lw=.85); dot(ax, 0, 0); hollow(ax, 1, 0); dot(ax, 1, -1, RED)
lab(ax, .5, -.13, r'$f=1-2x$', BLUE, ha='center', va='top'); lab(ax, .3, -.52, r'$f=1$', RED, ha='left')
lab(ax, .97, .06, r"$u'(1)=0$", MUTED, ha='right', fontsize=7.5)
ax.set_xlim(-.02, 1.05); ax.set_ylim(-1.1, .25); ax.set_xticks([0, 1]); ax.set_yticks([-1, 0]); hat01(ax, yl=r"$u'$")
tags(fig, axes)
save(fig, HERE, 'figure', {'u': 'x^3/3-x^2/2+c', 'zero_mean_c': 1/12})
