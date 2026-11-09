from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# (2,2) 处模型，半径 1、2、3 时的狗腿步。
fig, axs = figure(width_mm=112, height_mm=66, ncols=3)
P1, P2 = np.meshgrid(np.linspace(-1.8, .6, 400), np.linspace(-3.3, .6, 400))
pu, pn = np.array([-1., -1.]), -np.linalg.solve(A_B, A_G)
def dog(D):
    if np.linalg.norm(pn) <= D: return pn
    if np.linalg.norm(pu) >= D: return pu/np.linalg.norm(pu)*D
    return pu + boundary(pu, pn - pu, D)*(pn - pu)
for ax, D in zip(axs, (1, 2, 3)):
    disk(ax, (0, 0), D)
    ax.contour(P1, P2, 7*P1 + 7*P2 + 5.5*P1**2 + 1.5*P2**2, levels=[-10.3, -9, -7, -4, -1, 3], colors=[BLUE], linewidths=.7)
    ax.plot([0, pu[0], pn[0]], [0, pu[1], pn[1]], color=YELLOW, lw=1.5)
    p = dog(D); s = np.array([[0, 0], pu, pn])
    pts = [[0, 0]] + ([p] if D == 1 else [pu, p] if D == 2 else [pu, pn])
    pts = np.array(pts); ax.plot(pts[:, 0], pts[:, 1], color=GREEN, lw=1.8)
    ax.plot(*p, 'o', color=GREEN, ms=5, mew=0, zorder=7); ax.plot([0], [0], 'o', color=INK, ms=3.5, mew=0)
    ax.plot(*pn, 'o', color=PURPLE, ms=4.2, mew=0, zorder=6); ax.plot(*pu, 'o', color=YELLOW, ms=4.2, mew=0, zorder=6)
    ax.set_aspect('equal'); ax.set_xlim(-1.8, .6); ax.set_ylim(-3.3, .6); ax.set_xticks([-1, 0]); ax.set_yticks([-3, -2, -1, 0]); ax.set_xlabel('$p_1$', labelpad=1)
axs[0].set_ylabel('$p_2$', labelpad=1)
axs[1].text(-1.05, -.9, '$p^{\\mathrm{U}}$', ha='right', va='bottom', fontsize=7.5)
axs[1].text(pn[0]+.08, pn[1]-.08, '$p^{\\mathrm{N}}$', va='top', fontsize=7.5)
panels(fig, .075, .985, .985, .2, .1); tags(fig, axs)
save(fig, HERE, 'figure', {'g': [7, 7], 'B': 'diag(11,3)', 'radii': [1, 2, 3]})
