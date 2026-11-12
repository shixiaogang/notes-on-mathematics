from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Two independent N(0,1): R ~ Rayleigh, Theta ~ Unif(0, 2pi). Seed 3, 20000 samples.
rng = np.random.default_rng(3); X = rng.standard_normal((20000, 2))
R = np.hypot(X[:, 0], X[:, 1]); T = np.mod(np.arctan2(X[:, 1], X[:, 0]), 2*pi)
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.08, right=.98, bottom=.3, top=.95, wspace=.38)
ax = axes[0]
ax.plot(X[:1500, 0], X[:1500, 1], 'o', ms=1.1, color=GREEN, mew=0)
th = np.linspace(0, 2*pi, 300)
for r in (1, 2): ax.plot(r*np.cos(th), r*np.sin(th), color=MUTED, lw=.8)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5); ax.set_aspect('equal'); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$x_1$', '$x_2$')
ax = axes[1]; hist(ax, R, 30, (0, 4)); r = np.linspace(0, 4, 300); ax.plot(r, r*np.exp(-r*r/2), color=BLUE, lw=1.4)
ax.set_xlim(0, 4); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, .3, .6]); axlab(ax, '$r$')
ax = axes[2]; hist(ax, T, 24, (0, 2*pi)); ax.plot([0, 2*pi], [1/(2*pi)]*2, color=BLUE, lw=1.4)
ax.set_xlim(0, 2*pi); ax.set_ylim(0, .25); ax.set_xticks([0, pi, 2*pi]); ax.set_xticklabels(['0', '$\\pi$', '$2\\pi$']); ax.set_yticks([0, .1, .2]); axlab(ax, '$\\theta$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 3, 'n': 20000, 'P(R<=1) sim': float(np.mean(R <= 1)), 'exact': float(1-np.exp(-.5)), 'P(R>2) sim': float(np.mean(R > 2)), 'exact2': float(np.exp(-2))})
