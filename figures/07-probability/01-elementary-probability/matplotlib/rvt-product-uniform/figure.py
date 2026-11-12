from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# U,V iid Unif(0,1): region uv<=0.3, density -ln z (seed 13, 20000 samples), and CDF with an atom 0.3 at zero.
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.11, right=.98, bottom=.3, top=.95, wspace=.38)
ax = axes[0]; z0 = .3; x = np.linspace(z0, 1, 300)
ax.fill_between(np.concatenate([[0, z0], x]), 0, np.concatenate([[1, 1], z0/x]), color=BLUE_FILL, lw=0)
ax.plot(x, z0/x, color=BLUE, lw=1.4); ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=.8)
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.03, 1.05); ax.set_aspect('equal'); ax.set_xticks([0, .3, 1]); ax.set_yticks([0, .3, 1]); axlab(ax, '$x$', '$y$')
ax = axes[1]; rng = np.random.default_rng(13); s = rng.uniform(size=20000)*rng.uniform(size=20000)
hist(ax, s, 30, (0, 1)); z = np.linspace(1e-3, 1, 400); ax.plot(z, -np.log(z), color=BLUE, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(0, 4.5); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 2, 4]); axlab(ax, '$z$')
ax = axes[2]; z = np.linspace(1e-6, 1, 400); F0 = z-z*np.log(z)
ax.plot([-.15, 0], [0, 0], color=BLUE, lw=1.4); ax.plot(z, .3+.7*F0, color=BLUE, lw=1.4); ax.plot(z, F0, color=YELLOW, lw=1.5, ls=DASH)
ax.plot([0, 0], [0, .3], color=STROKE, lw=.7, ls=DOT); ax.plot([0], [0], 'o', ms=4, mfc='white', mec=BLUE, mew=.9, zorder=6); dot(ax, 0, .3, RED)
ax.set_xlim(-.15, 1); ax.set_ylim(0, 1.03); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .3, 1]); axlab(ax, '$z$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 13, 'area': float(z0-z0*np.log(z0)), 'sim P(Z<=.3)': float(np.mean(s <= .3)), 'sim mean': float(s.mean())})
