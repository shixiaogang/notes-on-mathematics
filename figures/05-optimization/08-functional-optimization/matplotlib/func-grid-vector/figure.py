from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 函数 u(x)=x^2 在 n 个小区间网格上的结点值，n=4 与 n=20。
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
panel(fig, left=.07, wspace=.08, bottom=.27)
for ax, n in zip(axes, (4, 20)):
    ax.plot(X, X**2, color=BLUE, lw=1.4)
    xs = np.arange(n+1)/n
    ax.vlines(xs[1:-1], 0, xs[1:-1]**2, color=GREEN, lw=1.1)
    ax.plot(xs[1:-1], xs[1:-1]**2, 'o', ms=3.4, color=GREEN, mew=0)
    ax.plot([0, 1], [0, 1], 'o', ms=4.2, color=STROKE, mew=0)
    ax.set_xlim(-.03, 1.06); ax.set_ylim(-.03, 1.1); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4)
axes[0].set_ylabel('$u$', labelpad=-2)
for i in (1, 2, 3):
    axes[0].text(i/4+.015, (i/4)**2+.08, f'$u_{i}$', color=INK, ha='center', fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'u': 'x^2', 'n': [4, 20]})
