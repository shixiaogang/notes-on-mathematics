from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X ~ Unif(-1,2), Y=X^2: two branches on (0,1), one on (1,4). Seed 11, 20000 samples.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.25)
ax = axes[0]; x = np.linspace(-1, 2, 400)
ax.plot(x, x**2, color=BLUE, lw=1.4); ax.axhline(.5, color=RED, lw=1.1); ax.axhline(2, color=PURPLE, lw=1.1)
r = np.sqrt(.5)
for e in (-r, r): dot(ax, e, .5, RED, ms=3.8)
dot(ax, np.sqrt(2), 2, PURPLE, ms=3.8)
ax.set_xlim(-1.05, 2.05); ax.set_ylim(0, 4.1); ax.set_xticks([-1, 0, 1, 2]); ax.set_yticks([0, .5, 1, 2, 4]); axlab(ax, '$x$')
lab(ax, 1.05, .6, '$y=0.5$', RED, va='bottom'); lab(ax, -.95, 2.12, '$y=2$', PURPLE, va='bottom')
ax = axes[1]; rng = np.random.default_rng(11); s = rng.uniform(-1, 2, 20000)**2
hist(ax, s, 40, (0, 4))
y1 = np.linspace(.02, 1, 200); y2 = np.linspace(1, 4, 200)
ax.plot(y1, 1/(3*np.sqrt(y1)), color=BLUE, lw=1.4); ax.plot(y2, 1/(6*np.sqrt(y2)), color=BLUE, lw=1.4)
ax.plot([1, 1], [1/6, 1/3], color=STROKE, lw=.7, ls=DOT)
ax.set_xlim(0, 4); ax.set_ylim(0, 1.6); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1/6, 1/3, 1]); ax.set_yticklabels(['0', '1/6', '1/3', '1']); axlab(ax, '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 11, 'P(Y<1) sim': float(np.mean(s < 1)), 'exact': 2/3})
