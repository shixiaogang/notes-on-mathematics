from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# (2,2) 处：线搜索沿 Newton 方向的射线；信赖域精确解随半径变化的曲线。
fig, ax = figure(width_mm=86, height_mm=68)
P1, P2 = np.meshgrid(np.linspace(-1.5, .6, 500), np.linspace(-3.2, .5, 500))
disk(ax, (0, 0), 2, facecolor='white', edgecolor=MUTED, lw=.7, ls=(0, (3, 2)))
disk(ax, (0, 0), 1, facecolor='white', edgecolor=MUTED, lw=.7, ls=(0, (3, 2)))
ax.contour(P1, P2, 7*P1 + 7*P2 + 5.5*P1**2 + 1.5*P2**2, levels=[-10.3, -9.5, -8, -6, -4, -2, 1, 4], colors=[BLUE], linewidths=.75)
pn = -np.linalg.solve(A_B, A_G)
ax.plot([0, pn[0]*1.3], [0, pn[1]*1.3], color=YELLOW, lw=1.6)
Ds = np.linspace(1e-3, np.linalg.norm(pn), 200); C = np.array([exact(A_G, A_B, d)[0] for d in Ds])
ax.plot(C[:, 0], C[:, 1], color=GREEN, lw=1.6)
for d in (1, 2):
    p = exact(A_G, A_B, d)[0]; ax.plot(*p, 'o', color=GREEN, ms=4.8, mew=0, zorder=6)
    ax.text(p[0]-.08, p[1]-.03, f'$\\Delta={d}$', ha='right', va='center', fontsize=7.5)
ax.plot([0], [0], 'o', color=INK, ms=4, mew=0); ax.plot(*pn, 'o', color=PURPLE, ms=5, mew=0, zorder=7)
ax.text(pn[0]+.08, pn[1]-.02, 'Newton', va='top', fontsize=7.5)
ax.set_aspect('equal'); ax.set_xlim(-1.5, .6); ax.set_ylim(-3.2, .5); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1)
save(fig, HERE, 'figure', {'g': [7, 7], 'B': 'diag(11,3)'})
