from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Cusp: g1=x2-(1-x1)^3<=0, g2=-x2<=0 at xbar=(1,0).
fig, ax = figure(width_mm=88, height_mm=60)
xs = np.linspace(.15, 1, 200)
ax.fill_between(xs, 0, (1-xs)**3, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
ax.plot(xs, (1-xs)**3, color=EDGE, lw=1.8, zorder=3); ax.plot(xs, 0*xs, color=EDGE, lw=1.8, zorder=3)
ax.plot([1, 1.5], [0, 0], color=RED, lw=1.1, ls=(0, (3, 2)), zorder=2)
setup(ax, (.15, 1.6), (-.45, .62), [.4, .8, 1.2, 1.6], [0, .5])
p = np.array([1., 0.]); arrow(ax, p, p+[0, .42], color=PURPLE); arrow(ax, p, p-[0, .42], color=PURPLE)
arrow(ax, p, p+[.45, 0], color=RED); arrow(ax, p, p-[.45, 0], color=GREEN, lw=1.8, z=6)
dot(ax, p, INK, ms=4.5)
ax.text(1.03, .3, '$\\nabla g_1$', color=PURPLE, fontsize=8); ax.text(1.03, -.36, '$\\nabla g_2$', color=PURPLE, fontsize=8)
ax.text(1.25, .05, '虚假方向', color=RED, fontsize=7.5); ax.text(.42, -.1, '真实方向', color=INK, fontsize=7.5)
save(fig, HERE, 'figure', {'xbar': [1, 0], 'grads': [[0, 1], [0, -1]]})
