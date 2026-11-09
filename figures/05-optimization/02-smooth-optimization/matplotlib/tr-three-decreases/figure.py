from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 原点处精确子问题解的预测下降、实际下降，及比值，随半径变化。
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
Ds = np.linspace(.02, 3, 300); S = [exact(O_G, O_B, d)[0] for d in Ds]
pr = np.array([-mdec(p, O_G, O_B) for p in S]); ar = np.array([f(O_X) - f(p) for p in S])
ax = axs[0]; ax.plot(Ds, pr, color=GREEN, lw=1.4); ax.plot(Ds, ar, color=BLUE, lw=1.4); ax.axhline(0, color=MUTED, lw=.85)
ax.set_xlim(0, 3); ax.set_ylim(-3, 8); ax.set_xlabel('$\\Delta$', labelpad=1)
ax.text(2.25, 5.9, '预测下降', color=INK, ha='right', fontsize=7.5); ax.text(2.0, -2.1, '实际下降', color=INK, ha='right', fontsize=7.5)
i = np.argmin(abs(Ds - 2)); ax.plot([2, 2], [pr[i], ar[i]], color=RED, lw=1.0, ls=(0, (2, 2)))
ax.plot([2], [pr[i]], 'o', color=GREEN, ms=4, mew=0); ax.plot([2], [ar[i]], 'o', color=BLUE, ms=4, mew=0)
ax = axs[1]; ax.plot(Ds, ar/pr, color=BLUE, lw=1.4); ax.axhline(1, color=MUTED, lw=.85, ls=(0, (3, 2))); ax.axhline(0, color=MUTED, lw=.85)
ax.set_xlim(0, 3); ax.set_ylim(-2, 1.3); ax.set_xlabel('$\\Delta$', labelpad=1); ax.set_ylabel('$\\rho$', labelpad=1)
panels(fig, .07, .985, .98, .25, .24); tags(fig, axs)
save(fig, HERE, 'figure', {'x': [0, 0], 'g': [1, 1], 'B': 'diag(-1,3)'})
