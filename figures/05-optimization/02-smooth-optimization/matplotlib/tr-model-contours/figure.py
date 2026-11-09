from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# (2,2) 处真实目标与二次模型的等高线，半径 2。
fig, axs = figure(width_mm=112, height_mm=60, ncols=2)
P1, P2 = np.meshgrid(np.linspace(-4.2, 2.2, 500), np.linspace(-4.2, 2.2, 500))
Z = [f(np.array([2+P1, 2+P2])), 12 + 7*P1 + 7*P2 + 5.5*P1**2 + 1.5*P2**2]
lv = [-1, 0, 2, 5, 9, 12, 18, 26, 36]
for ax, z in zip(axs, Z):
    disk(ax, (0, 0), 2)
    ax.contour(P1, P2, z, levels=lv, colors=[BLUE], linewidths=.75)
    ax.plot([0], [0], 'o', color=INK, ms=4, mew=0)
    ax.set_aspect('equal'); ax.set_xlim(-4.2, 2.2); ax.set_ylim(-4.2, 2.2)
    ax.set_xlabel('$p_1$', labelpad=1); ax.set_xticks([-4, -2, 0, 2]); ax.set_yticks([-4, -2, 0, 2])
axs[0].set_ylabel('$p_2$', labelpad=1)
axs[0].plot([XSTAR[0]-2], [XSTAR[1]-2], 'o', color=RED, ms=4.6, mew=0)
pn = -np.linalg.solve(A_B, A_G); axs[1].plot([pn[0]], [pn[1]], 'o', color=PURPLE, ms=4.6, mew=0)
panels(fig, .085, .985, .985, .205, .16); tags(fig, axs)
save(fig, HERE, 'figure', {'x': [2, 2], 'g': [7, 7], 'B': 'diag(11,3)', 'radius': 2})
