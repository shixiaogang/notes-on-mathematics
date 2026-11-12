from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# (a) P=N(0,1), Q=N(1,1): A*={p>q}={x<1/2}; d_TV = 2*Phi(1/2)-1 = 0.3829,
#     shaded areas (p-q)^+ and (q-p)^+ are equal.
# (b) P=Unif(0,1), Q=0.5*Unif(0,1)+0.5*delta_{1/2}; densities w.r.t. lambda=Leb+delta_{1/2}:
#     p=1 on (0,1)\{1/2}, p(1/2)=0; q=1/2 on (0,1)\{1/2}, q(1/2)=1/2. d_TV = 1/2.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
x = np.linspace(-3.5, 4.5, 1200)
p, q = npdf(x), npdf(x, 1.)
ax.fill_between(x, q, p, where=p > q, color=BLUE_FILL, lw=0, zorder=1)
ax.fill_between(x, p, q, where=q > p, color=YELLOW_FILL, lw=0, zorder=1)
ax.plot(x, p, color=BLUE, lw=1.4, zorder=3)
ax.plot(x, q, color=YELLOW, lw=1.6, zorder=3)
ax.axvline(.5, color=RED, lw=1.0, ymax=.93, zorder=2)
lab(ax, -1.75, .33, '$P$', BLUE, ha='center', fontsize=8)
lab(ax, 2.75, .33, '$Q$', YELLOW, ha='center', fontsize=8)
lab(ax, .62, .43, '$x=1/2$', RED, ha='left')
ax.set_xlim(-3.5, 4.5); ax.set_ylim(0, .46); ax.set_yticks([0, .2, .4])
axlab(ax, '$x$', '密度')
tv = 2*float(Phi(.5))-1
ax = axs[1]
ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4, solid_capstyle='butt')
ax.plot([0, 1], [.5, .5], color=YELLOW, lw=1.6, solid_capstyle='butt')
ax.plot([0, 0], [0, 1], color=BLUE, lw=.85, ls=DOT); ax.plot([1, 1], [0, 1], color=BLUE, lw=.85, ls=DOT)
ax.plot([.5, .5], [0, .5], color=YELLOW, lw=1.8)
dot(ax, .5, .5, YELLOW, ms=4.6)
dot(ax, .5, 0, BLUE, ms=4.0)
lab(ax, .54, .4, '原子', YELLOW, ha='left')
lab(ax, .2, 1.05, '$p=1$', BLUE, ha='center')
lab(ax, .2, .56, '$q=1/2$', YELLOW, ha='center')
ax.set_xlim(-.15, 1.15); ax.set_ylim(0, 1.2); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, '$x$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'tv_gauss': tv, 'tv_atom': .5})
