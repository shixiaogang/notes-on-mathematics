from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# (a) Y=min(X,1), X~Unif(0,2): atom 1/2 at 1. (b) Y=X^3, X~Unif(-1,1): density |y|^(-2/3)/6. Seed 7, 20000 samples.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.25)
ax = axes[0]
ax.plot([-.3, 0], [0, 0], color=BLUE, lw=1.4); ax.plot([0, 1], [0, .5], color=BLUE, lw=1.4); ax.plot([1, 1.6], [1, 1], color=BLUE, lw=1.4)
ax.plot([1, 1], [.5, 1], color=STROKE, lw=.7, ls=DOT)
ax.plot([1], [.5], 'o', ms=4, mfc='white', mec=BLUE, mew=.9, zorder=6); dot(ax, 1, 1, RED)
lab(ax, 1.06, .72, '跳跃1/2', RED, ha='left')
ax.set_xlim(-.3, 1.6); ax.set_ylim(-.03, 1.08); ax.set_xticks([0, .5, 1, 1.5]); ax.set_yticks([0, .5, 1]); axlab(ax, '$y$')
ax = axes[1]; rng = np.random.default_rng(7); s = rng.uniform(-1, 1, 20000)**3
hist(ax, s, 40, (-1, 1))
y = np.linspace(-1, 1, 2001); y = y[np.abs(y) > 1e-3]
yl = y[y < 0]; yr = y[y > 0]
for yy in (yl, yr): ax.plot(yy, np.abs(yy)**(-2/3)/6, color=BLUE, lw=1.4)
ax.set_xlim(-1, 1); ax.set_ylim(0, 3); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2, 3]); axlab(ax, '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 7, 'n': 20000, 'mass(|y|<.1)': float(np.mean(np.abs(s) < .1)), 'exact': .1**(1/3)})
