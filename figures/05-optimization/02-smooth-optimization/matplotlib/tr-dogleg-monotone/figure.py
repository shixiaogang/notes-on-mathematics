from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 狗腿路径上的长度与模型下降量，tau 在 [0,2]。
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
pu, pn = np.array([-1., -1.]), -np.linalg.solve(A_B, A_G)
T = np.linspace(0, 2, 300); P = np.array([t*pu if t <= 1 else pu + (t-1)*(pn-pu) for t in T])
N = np.linalg.norm(P, axis=1); M = np.array([mdec(p, A_G, A_B) for p in P])
for ax, y, c in zip(axs, (N, M), (GREEN, BLUE)):
    ax.plot(T, y, color=c, lw=1.4); ax.axvline(1, color=MUTED, lw=.85, ls=(0, (2, 2))); ax.set_xlim(0, 2); ax.set_xlabel('$\\tau$', labelpad=1); ax.set_xticks([0, 1, 2])
axs[0].set_ylabel(r'$\Vert p(\tau)\Vert_2$', labelpad=1); axs[1].set_ylabel(r'$m(p(\tau))-m(0)$', labelpad=1)
panels(fig, .095, .985, .98, .255, .3); tags(fig, axs)
save(fig, HERE, 'figure', {'g': [7, 7], 'B': 'diag(11,3)'})
