from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
G = lambda x, y: np.where(x <= y, x*(1-y), y*(1-x))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.115, wspace=.28, bottom=.27)
ax = axes[0]
for y in (.2, .5, .8):
    ax.plot(X, G(X, y), color=BLUE, lw=1.4); dot(ax, y, y*(1-y))
    lab(ax, y, y*(1-y)+.02, '$y=%g$' % y, BLUE, ha='center')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.01, .31); ax.set_xticks([0, 1]); ax.set_yticks([0, .25]); hat01(ax, yl=r'$G(x,y)$')
ax = axes[1]
for N, c, ls in ((2, PURPLE, '-'), (4, GREEN, '-')):
    ys = (np.arange(N)+.5)/N
    u = sum(G(X, y)/N for y in ys); ax.plot(X, u, color=c, lw=1.2, ls=ls)
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
lab(ax, .08, .118, '$N=2$', PURPLE); lab(ax, .755, .118, '$N=4$', GREEN); lab(ax, .5, .098, r'$\frac{x(1-x)}{2}$', BLUE, ha='center', va='top')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.005, .15); ax.set_xticks([0, 1]); ax.set_yticks([0, .125]); ax.set_yticklabels(['0', '1/8']); hat01(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'G': 'x(1-y), x<=y; y(1-x), x>=y', 'sum': 'midpoint sums of G(x,y_j)/N'})
