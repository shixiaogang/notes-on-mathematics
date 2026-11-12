from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X = 0 w.p. 0.3, ~N(0,1) w.p. 0.7; Y=|X|. CDFs with the atom.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.07, right=.98, bottom=.28, top=.95, wspace=.25)
ax = axes[0]; xl = np.linspace(-3, 0, 200); xr = np.linspace(0, 3, 200)
ax.plot(xl, .7*Phi(xl), color=BLUE, lw=1.4); ax.plot(xr, .3+.7*Phi(xr), color=BLUE, lw=1.4)
ax.plot([0, 0], [.35, .65], color=STROKE, lw=.7, ls=DOT)
ax.plot([0], [.35], 'o', ms=4, mfc='white', mec=BLUE, mew=.9, zorder=6); dot(ax, 0, .65, RED)
lab(ax, .15, .45, '跳跃0.3', RED, ha='left')
ax.set_xlim(-3, 3); ax.set_ylim(0, 1.03); ax.set_yticks([0, .35, .65, 1]); axlab(ax, '$x$')
ax = axes[1]; y = np.linspace(0, 3, 300)
ax.plot([-.4, 0], [0, 0], color=BLUE, lw=1.4)
ax.plot(y, .3+.7*(2*Phi(y)-1), color=BLUE, lw=1.4); ax.plot(y, .7*(2*Phi(y)-1), color=YELLOW, lw=1.5, ls=DASH)
ax.plot([0, 0], [0, .3], color=STROKE, lw=.7, ls=DOT)
ax.plot([0], [0], 'o', ms=4, mfc='white', mec=BLUE, mew=.9, zorder=6); dot(ax, 0, .3, RED)
lab(ax, 1.3, .4, '只保留连续部分', YELLOW, ha='left')
ax.set_xlim(-.4, 3); ax.set_ylim(0, 1.03); ax.set_yticks([0, .3, .7, 1]); axlab(ax, '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'atom': .3, 'continuous_total': .7})
