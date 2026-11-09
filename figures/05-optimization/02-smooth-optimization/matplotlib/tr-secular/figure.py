from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# ||p(lambda)|| 随 lambda 的变化：(a) (2,2) 处 B 正定；(b) 原点处 B 不定。
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
ax = axs[0]; L = np.linspace(0, 6, 400); N = np.hypot(7/(11+L), 7/(3+L))
ax.plot(L, N, color=BLUE, lw=1.4); ax.axhline(2, color=EDGE, lw=.95, ls=(0, (4, 2)))
l = exact(A_G, A_B, 2.)[1]; ax.plot([l], [2], 'o', color=RED, ms=4.8, mew=0, zorder=6)
ax.text(l+.25, 2.08, '$\\lambda\\approx 0.669$', fontsize=7.5); ax.text(5.6, 2.05, '$\\Delta$', ha='right', va='bottom', fontsize=7.5)
ax.set_xlim(0, 6); ax.set_ylim(0, 3); ax.set_xlabel('$\\lambda$', labelpad=1); ax.set_ylabel(r'$\Vert p(\lambda)\Vert_2$', labelpad=1)
ax = axs[1]; L = np.linspace(1.04, 6, 500); N = np.hypot(1/(L-1), 1/(L+3))
ax.axvspan(0, 1, facecolor=RED_FILL, edgecolor='none', zorder=0)
ax.plot(L, N, color=BLUE, lw=1.4); ax.axhline(2, color=EDGE, lw=.95, ls=(0, (4, 2)))
l = exact(O_G, O_B, 2.)[1]; ax.plot([l], [2], 'o', color=RED, ms=4.8, mew=0, zorder=6)
ax.text(l+.25, 2.08, '$\\lambda\\approx 1.503$', fontsize=7.5); ax.text(5.9, 2.05, '$\\Delta$', ha='right', va='bottom', fontsize=7.5)
ax.axvline(1, color=MUTED, lw=.85, ls=(0, (2, 2))); ax.set_xlim(0, 6); ax.set_ylim(0, 4.5); ax.set_xlabel('$\\lambda$', labelpad=1)
panels(fig, .1, .985, .98, .25, .2); tags(fig, axs)
save(fig, HERE, 'figure', {'A': 'g=(7,7),B=diag(11,3)', 'O': 'g=(1,1),B=diag(-1,3)', 'radius': 2})
