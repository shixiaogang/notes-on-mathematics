from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# f=xy: simultaneous and alternating GDA (alpha=1/2), distance, projected cycle (alpha=1).
fig, axes = figure(width_mm=112, height_mm=47, ncols=3)
panels(fig, .07, .985, .975, .265, .36)
g = np.linspace(-3.2, 3.2, 300); X, Y = np.meshgrid(g, g)
a = .5; T = 10; S = gda(A, a, T, (1, 0)); Alt = alt_xy(a, T, (1, 0))
ax = axes[0]; setup(ax, (-3.2, 3.2), (-3.2, 3.2), (-3, 0, 3), (-3, 0, 3), equal=True)
ax.contour(X, Y, X*Y, levels=[-4, -2, -.7, .7, 2, 4], colors=BLUE, linewidths=.7, linestyles='solid')
path(ax, S, GREEN, ms=2.6); path(ax, Alt, YELLOW, lw=1.3, ms=2.6, z=5); dot(ax, (0, 0))
ax = axes[1]; setup(ax, (0, T), (0, 3.6), (0, 5, 10), (0, 1, 2, 3), xl='$t$', yl=r'到鞍点的距离')
ax.plot(np.linalg.norm(S, axis=1), color=GREEN, lw=1.4); ax.plot(np.linalg.norm(Alt, axis=1), color=YELLOW, lw=1.6)
ax = axes[2]; setup(ax, (-1.5, 1.5), (-1.5, 1.5), (-1, 0, 1), (-1, 0, 1), equal=True)
ax.fill([-1, 1, 1, -1], [-1, -1, 1, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.85, zorder=0)
z = np.array([1., 0]); P = [z]
for _ in range(8): z = np.clip(z-A@z, -1, 1); P.append(z)
P = np.array(P); path(ax, P, GREEN, ms=3.4); dot(ax, (0, 0))
for i in range(0, 8, 2):
    p, q = P[i], P[i+1]
tags(fig, axes)
save(fig, HERE, 'figure', {'f': 'xy', 'alpha': a, 'cycle': P.tolist()})
print(S[:5], Alt[:5])
