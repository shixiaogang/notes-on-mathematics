from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J=int u'^2-u'^4；锯齿斜率 ±2。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.27, bottom=.28)
ax = axes[0]
ax.axhline(0, color=RED, lw=1.4)
for k, c, lw in ((3, YELLOW, 1.4), (10, GREEN, 1.1)):
    ax.plot(X, zigzag(X, k, 2), color=c, lw=lw)
ax.text(.17, .37, '$k=3$', color=YELLOW, fontsize=7.5, ha='center'); ax.text(.335, .115, '$k=10$', color=GREEN, fontsize=7.5, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(-.05, .43); ax.set_xticks([0, 1]); ax.set_yticks([0, .33]); ax.set_yticklabels(['0', '1/3']); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$u$', labelpad=-2)
ax = axes[1]
p = np.linspace(-2.25, 2.25, 400)
ax.plot(p, p**2-p**4, color=BLUE, lw=1.4)
dot(ax, 0, 0, RED); dot(ax, 2, -12, GREEN); dot(ax, -2, -12, GREEN)
ax.axhline(0, color=MUTED, lw=.85, zorder=0)
ax.text(1.75, -12, '$-12$', color=GREEN, fontsize=7.5, ha='right', va='center')
ax.set_xlim(-2.3, 2.3); ax.set_ylim(-16, 2.5); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-12, 0]); ax.set_xlabel('$p$', labelpad=1); ax.set_ylabel('$p^2-p^4$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'slope': 2, 'sup_norm': '1/k', 'J': -12})
