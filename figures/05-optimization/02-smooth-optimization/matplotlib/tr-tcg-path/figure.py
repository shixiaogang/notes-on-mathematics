from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 截断共轭梯度的两次运行：(a) (2,2) 处边界停止；(b) 原点处负曲率停止。
fig, axs = figure(width_mm=112, height_mm=64, ncols=2)
ax = axs[0]; P1, P2 = np.meshgrid(np.linspace(-1.8, .4, 400), np.linspace(-2.9, .4, 400)); disk(ax, (0, 0), 2)
ax.contour(P1, P2, 7*P1 + 7*P2 + 5.5*P1**2 + 1.5*P2**2, levels=[-10.3, -9, -7, -4, -1, 2], colors=[BLUE], linewidths=.7)
p, why, pth, _ = tcg(A_G, A_B, 2.); pth = np.array(pth); pe = exact(A_G, A_B, 2.)[0]; pn = -np.linalg.solve(A_B, A_G)
ax.plot(pth[:, 0], pth[:, 1], color=GREEN, lw=1.7); ax.plot([pth[-1, 0], pn[0]], [pth[-1, 1], pn[1]], color=GREEN, lw=1, ls=(0, (2, 2)))
ax.plot(pth[:-1, 0], pth[:-1, 1], 'o', color=GREEN, ms=4, mew=0); ax.plot(*p, 'o', color=GREEN, ms=5.2, mew=0, zorder=7); ax.plot(*pe, 'o', color=RED, ms=4.6, mew=0, zorder=8); ax.plot(*pn, 'o', color=PURPLE, ms=4.2, mew=0)
ax.set_aspect('equal'); ax.set_xlim(-1.8, .4); ax.set_ylim(-2.9, .4); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1)
ax.text(-1.05, -.85, '$p^{(1)}$', ha='right', va='bottom', fontsize=7.5)
ax = axs[1]; P1, P2 = np.meshgrid(np.linspace(-2.3, 1.2, 400), np.linspace(-2.3, 1.2, 400)); disk(ax, (0, 0), 2)
ax.contour(P1, P2, P1 + P2 - .5*P1**2 + 1.5*P2**2, levels=[-4, -3, -2, -1, 0, 1, 2, 3.5], colors=[BLUE], linewidths=.7)
p, why, pth, _ = tcg(O_G, O_B, 2.); pth = np.array(pth); pe = exact(O_G, O_B, 2.)[0]
ax.plot(pth[:, 0], pth[:, 1], color=GREEN, lw=1.7); ax.plot(pth[:-1, 0], pth[:-1, 1], 'o', color=GREEN, ms=4, mew=0); ax.plot(*p, 'o', color=GREEN, ms=5.2, mew=0, zorder=7); ax.plot(*pe, 'o', color=RED, ms=4.6, mew=0, zorder=8)
ax.set_aspect('equal'); ax.set_xlim(-2.3, 1.2); ax.set_ylim(-2.3, 1.2); ax.set_xlabel('$p_1$', labelpad=1)
ax.text(-.9, -1.08, '$p^{(1)}$', ha='left', va='top', fontsize=7.5)
panels(fig, .08, .985, .985, .2, .18); tags(fig, axs)
save(fig, HERE, 'figure', {'A': 'g=(7,7),B=diag(11,3),radius 2', 'O': 'g=(1,1),B=diag(-1,3),radius 2'})
