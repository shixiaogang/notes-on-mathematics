from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 原点处 B 不定：把狗腿路径照搬过来，第二段上模型上升。
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]; P1, P2 = np.meshgrid(np.linspace(-2.2, 2.0, 400), np.linspace(-2.2, 1.2, 400))
disk(ax, (0, 0), 2)
ax.contour(P1, P2, P1 + P2 - .5*P1**2 + 1.5*P2**2, levels=[-4, -3, -2, -1, 0, 1/3, 1, 2, 3], colors=[BLUE], linewidths=.7)
pu, pn = np.array([-1., -1.]), np.array([1., -1/3])
ax.plot([0, pu[0]], [0, pu[1]], color=GREEN, lw=1.6); ax.plot([pu[0], pn[0]], [pu[1], pn[1]], color=RED, lw=1.6)
ax.plot([0], [0], 'o', color=INK, ms=3.8, mew=0); ax.plot(*pu, 'o', color=YELLOW, ms=4.5, mew=0, zorder=6); ax.plot(*pn, 'o', color=PURPLE, ms=4.5, mew=0, zorder=6)
ax.set_aspect('equal'); ax.set_xlim(-2.2, 2.0); ax.set_ylim(-2.2, 1.2); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1)
ax = axs[1]; T = np.linspace(0, 2, 300); P = np.array([t*pu if t <= 1 else pu + (t-1)*(pn-pu) for t in T]); M = np.array([mdec(p, O_G, O_B) for p in P])
ax.plot(T[T <= 1], M[T <= 1], color=GREEN, lw=1.4); ax.plot(T[T >= 1], M[T >= 1], color=RED, lw=1.4)
ax.axvline(1, color=MUTED, lw=.85, ls=(0, (2, 2))); ax.set_xlim(0, 2); ax.set_xticks([0, 1, 2]); ax.set_xlabel('$\\tau$', labelpad=1); ax.set_ylabel(r'$m(p(\tau))-m(0)$', labelpad=1)
panels(fig, .085, .985, .985, .22, .3); tags(fig, axs)
save(fig, HERE, 'figure', {'g': [1, 1], 'B': 'diag(-1,3)'})
