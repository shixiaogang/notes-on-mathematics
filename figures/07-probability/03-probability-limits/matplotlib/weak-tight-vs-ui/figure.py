from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# X_n = n w.p. 1/n else 0. (a) pmf for n=4,10; (b) sup_n P(X_n>r) = 1/(floor(r)+1) <= 1/r and sup_n E[X_n 1{X_n>r}] = 1.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]
for n, c, off in ((4, YELLOW, -.18), (10, GREEN, .18)):
    for xv, pv in ((0, 1-1/n), (n, 1/n)):
        ax.plot([xv+off, xv+off], [0, pv], color=c, lw=1.6); dot(ax, xv+off, pv, c, ms=3.4)
lab(ax, 4, .3, r'$1/4$', YELLOW, ha='center'); lab(ax, 10, .16, r'$1/10$', GREEN, ha='center')
lab(ax, .5, .95, r'$n=10$', GREEN); lab(ax, .5, .7, r'$n=4$', YELLOW)
ax.set_xlim(-1, 11.5); ax.set_ylim(0, 1.05); ax.set_xticks([0, 4, 10]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
ax = axes[1]; r = np.linspace(1, 20, 800)
ax.plot(r, 1/(np.floor(r)+1), color=GREEN, lw=1.4, drawstyle='steps-post')
ax.plot(r, 1/r, color=PURPLE, lw=1.0, ls=DASH)
ax.plot(r, np.ones_like(r), color=RED, lw=1.4)
lab(ax, 19.5, 1.04, '尾部积分', RED, ha='right', va='bottom')
lab(ax, 7, .2, '尾概率', GREEN); lab(ax, 2.6, .52, r'$1/r$', PURPLE)
ax.set_xlim(1, 20); ax.set_ylim(0, 1.25); ax.set_xticks([1, 5, 10, 15, 20]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$r$')
tags(fig, axes)
save(fig, HERE, 'figure', {'tail_integral': 1.0})
