from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 原点：半径 2 的候选点被拒绝，半径 1 的候选点被接受（真实目标等高线）。
fig, ax = figure(width_mm=90, height_mm=66)
X1, X2 = np.meshgrid(np.linspace(-2.4, 1.5, 500), np.linspace(-2.1, 1.3, 500))
disk(ax, (0, 0), 2, facecolor='white', edgecolor=RED, lw=.9, ls=(0, (3, 2))); disk(ax, (0, 0), 1, facecolor=BLUE_FILL, edgecolor=BLUE)
ax.contour(X1, X2, f(np.array([X1, X2])), levels=[-1.5, -1.2, -.85, -.4, 0, .5, 1.2, 2.2, 3.5], colors=[BLUE], linewidths=.75)
p1 = np.array([-1.6, -1.2]); p2 = -np.ones(2)/np.sqrt(2)
arrow(ax, (0, 0), p1, RED, 1.3); arrow(ax, (0, 0), p2, GREEN, 1.5)
ax.plot(*p1, 'o', mfc='white', mec=RED, mew=1, ms=5, zorder=7); ax.plot(*p2, 'o', color=GREEN, ms=5, mew=0, zorder=7); ax.plot([0], [0], 'o', color=INK, ms=4, mew=0, zorder=7); ax.plot(*XSTAR, 'o', color=RED, ms=4.6, mew=0, zorder=7)
ax.text(-1.68, -1.33, '$\\rho\\approx 0.15$', ha='right', va='top', fontsize=7.5); ax.text(-.56, -.82, '$\\rho\\approx 0.93$', ha='left', va='top', fontsize=7.5)
ax.set_aspect('equal'); ax.set_xlim(-2.4, 1.5); ax.set_ylim(-2.1, 1.3); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, HERE, 'figure', {'x0': [0, 0], 'radii': [2, 1]})
