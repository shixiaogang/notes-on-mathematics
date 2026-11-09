from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Interior point, edge point and vertex of the workshop polygon.
xl, yl = (-.4, 4.4), (-.4, 4.6)
fig, ax = figure(width_mm=84, height_mm=62)
region(ax, workshop())
P = np.array([1., 1.]); Q = np.array([2.5, 1.]); V = np.array([2., 2.])
d1 = np.array([.55, .4]); ax.plot(*zip(P-d1, P+d1), color=GREEN, lw=1.4, zorder=4)
dot(ax, P-d1, GREEN); dot(ax, P+d1, GREEN); dot(ax, P, INK, ms=4.6)
d2 = np.array([.3, -.6]); ax.plot(*zip(Q-d2, Q+d2), color=GREEN, lw=1.6, zorder=4)
dot(ax, Q-d2, GREEN); dot(ax, Q+d2, GREEN); dot(ax, Q, INK, ms=4.6)
for d in (np.array([.45, .35]), np.array([-.55, .45])):
    ax.plot(*zip(V, V+d), color=RED, lw=1.1, ls=(0, (3, 2)), zorder=4)
    ax.plot(*zip(V, V-d), color=RED, lw=1.1, ls=(0, (3, 2)), zorder=4)
    hollow(ax, V+d)
hollow(ax, V+np.array([.55, -.45]))
dot(ax, V, RED, ms=5.2)
ax.text(1.0, .55, '内部点', fontsize=7.5, ha='center', color=INK)
ax.text(2.82, 1.4, '边上的点', fontsize=7.5, color=INK)
ax.text(2.14, 2.42, '', fontsize=7.5)
ax.text(2.0, 2.72, '顶点', fontsize=7.5, ha='center', color=INK)
setup(ax, xl, yl, range(0, 5), range(0, 5))
save(fig, HERE, 'figure', {'interior': P.tolist(), 'edge': Q.tolist(), 'vertex': V.tolist()})
