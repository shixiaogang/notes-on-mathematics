from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J=int (u'^2-1)^2+u^2，锯齿列 z_k，G(p)=(p^2-1)^2。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.09, wspace=.26, bottom=.26)
ax = axes[0]
ax.axhline(0, color=RED, lw=1.4)
for k, c, lw in ((2, YELLOW, 1.4), (6, GREEN, 1.1)):
    ax.plot(X, zigzag(X, k), color=c, lw=lw)
ax.text(.26, .275, '$k=2$', color=YELLOW, fontsize=7.5, ha='center'); ax.text(.5, .115, '$k=6$', color=GREEN, fontsize=7.5, ha='center'); ax.text(.97, -.035, '$u=0$', color=RED, fontsize=7.5, ha='right', va='top')
ax.set_xlim(0, 1); ax.set_ylim(-.11, .33); ax.set_xticks([0, 1]); ax.set_yticks([0, .25]); ax.set_yticklabels(['0', '0.25']); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$u$', labelpad=1)
ax = axes[1]
p = np.linspace(-1.5, 1.5, 400)
ax.plot(p, (p**2-1)**2, color=BLUE, lw=1.4)
ax.plot([-1, 1], [0, 0], color=GREEN, lw=1.4)
ax.plot([-1, 1], [0, 0], 'o', ms=4.2, color=GREEN, mew=0)
ax.plot([0], [1], 'o', ms=4.6, color=RED, mew=0, zorder=6)
ax.vlines(0, 0, 1, color=RED, lw=.85, ls=(0, (2, 2)))
ax.text(.1, 1.04, '$G(0)=1$', color=RED, fontsize=7.5)
ax.text(0, -.16, r'$\frac{1}{2}G(-1)+\frac{1}{2}G(1)=0$', color=GREEN, fontsize=7.5, ha='center', va='top')
ax.set_xlim(-1.55, 1.55); ax.set_ylim(-.5, 1.6); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$p$', labelpad=1); ax.set_ylabel('$G(p)$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'z_k': 'k teeth, slope +-1', 'J(z_k)': '1/(12 k^2)', 'G': '(p^2-1)^2'})
