from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 原点处模型 m=p1+p2-p1^2/2+3p2^2/2，驻点 (1,-1/3)；半径 2 的精确解。
fig, ax = figure(width_mm=88, height_mm=70)
P1, P2 = np.meshgrid(np.linspace(-2.9, 2.9, 500), np.linspace(-2.6, 2.6, 500))
disk(ax, (0, 0), 2)
ax.contour(P1, P2, P1 + P2 - .5*P1**2 + 1.5*P2**2, levels=[-5, -3.5, -2, -1, 0, 1/3, 1, 2, 3.5, 6], colors=[BLUE], linewidths=.75)
pn = np.array([1, -1/3]); pe, l = exact(O_G, O_B, 2.)
arrow(ax, (0, 0), pn, YELLOW, 1.5); arrow(ax, (0, 0), pe, GREEN, 1.5)
arrow(ax, (0, 0), (-.72, -.72), INK)
ax.plot([0], [0], 'o', color=INK, ms=4, mew=0)
ax.plot(*pn, 'o', color=YELLOW, ms=4.8, mew=0, zorder=6); ax.plot(*pe, 'o', color=RED, ms=5, mew=0, zorder=6)
ax.text(1.14, -.42, '$-B^{-1}g$', va='top')
ax.text(-2.08, -.05, '$p^*$', ha='right'); ax.text(-.78, -1.05, '$-g$', ha='center')
ax.set_aspect('equal'); ax.set_xlim(-2.9, 2.9); ax.set_ylim(-2.6, 2.6); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1)
save(fig, HERE, 'figure', {'g': [1, 1], 'B': 'diag(-1,3)', 'radius': 2, 'lambda': l, 'p_exact': pe.tolist()})
