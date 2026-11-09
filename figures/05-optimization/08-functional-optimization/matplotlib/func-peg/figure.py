from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# min int u'^2/2, u in H_0^1, u(1/2)>=a：解 2a min(x,1-x)，J*(a)=2a^2。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.26, bottom=.27)
ax = axes[0]
ax.plot(X, np.sin(np.pi*X), color=YELLOW, lw=1.4)
ax.plot(X, 2*np.minimum(X, 1-X), color=GREEN, lw=1.4)
ax.vlines(.5, -.1, 1, color=STROKE, lw=2.0, zorder=3)
dot(ax, .5, 1, RED)
ax.annotate('', xy=(.5, .62), xytext=(.5, .98), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=1.4, shrinkA=0, shrinkB=0), zorder=7)
ax.text(.54, .22, r'$\lambda^*=4$', color=PURPLE, fontsize=8)
ax.text(.2, .82, r'$\sin\pi x$', color=YELLOW, fontsize=7.5, ha='right')
ax.text(.2, .24, '$u^*$', color=GREEN, fontsize=8, ha='left')
ax.set_xlim(-.03, 1.03); ax.set_ylim(-.1, 1.15); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=-2)
ax = axes[1]
a = np.linspace(0, 1.6, 200)
ax.plot(a, 2*a**2, color=BLUE, lw=1.4)
ax.plot(a, 2+4*(a-1), color=PURPLE, lw=1.1, ls=(0, (4, 2)))
dot(ax, 1, 2, RED)
ax.text(.92, 2.3, '$(1,2)$', fontsize=7.5, ha='right')
ax.text(1.6, 2.5, '斜率 4', color=PURPLE, fontsize=7.5, ha='right', va='top')
ax.set_xlim(0, 1.65); ax.set_ylim(-.3, 5.4); ax.set_xticks([0, 1]); ax.set_yticks([0, 2, 4]); ax.set_xlabel('$a$', labelpad=1); ax.set_ylabel(r'$J^*(a)$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'sol': '2a min(x,1-x)', 'J*(a)': '2a^2', 'J(sin pi x)': float(np.pi**2/4)})
