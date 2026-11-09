from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# B=diag(-1,3)，Delta=1：g1=0.1 与 g1=0 的 ||p(lambda)||。
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
for ax, g1 in zip(axs, (.1, 0.)):
    L = np.linspace(1.005, 4, 800); N = np.hypot(g1/(L-1), 1/(L+3))
    ax.axvspan(0, 1, facecolor=RED_FILL, edgecolor='none', zorder=0)
    ax.plot(L, N, color=BLUE, lw=1.4); ax.axhline(1, color=EDGE, lw=.95, ls=(0, (4, 2)))
    ax.axvline(1, color=MUTED, lw=.85, ls=(0, (2, 2))); ax.set_xlim(0, 4); ax.set_ylim(0, 1.8); ax.set_xlabel('$\\lambda$', labelpad=1)
    ax.text(3.9, 1.04, '$\\Delta$', ha='right', va='bottom', fontsize=7.5)
axs[0].set_ylabel(r'$\Vert p(\lambda)\Vert_2$', labelpad=1)
l = exact(np.array([.1, 1.]), O_B, 1.)[1]; axs[0].plot([l], [1], 'o', color=RED, ms=4.8, mew=0, zorder=6)
axs[1].plot([1], [.25], 'o', mfc='white', mec=RED, ms=4.8, mew=1, zorder=6)
panels(fig, .1, .985, .98, .265, .2); tags(fig, axs)
save(fig, HERE, 'figure', {'B': 'diag(-1,3)', 'g': '(0.1,1) and (0,1)', 'radius': 1, 'lambda_a': l})
