from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# 截断 N=5：x=(1,1,...) 与 y=(1,1/2,1/3,...) 的保留项与误差项。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.95, bottom=.3, wspace=.13)
N = 5; k = np.arange(1, 15)
for ax, v, sup, lab in ((axes[0], np.ones_like(k, float), 1.0, '$1$'), (axes[1], 1/k, 1/(N+1), r'$\frac{1}{N+1}$')):
    kept = k <= N
    ax.vlines(k[kept], 0, v[kept], color=BLUE, lw=1.2); ax.plot(k[kept], v[kept], 'o', ms=3.4, color=BLUE, mew=0)
    ax.vlines(k[~kept], 0, v[~kept], color=RED, lw=1.2); ax.plot(k[~kept], v[~kept], 'o', ms=3.4, color=RED, mew=0)
    ax.plot([N+.5, 15.3], [sup, sup], color=MUTED, lw=.85, ls=(0, (3, 2)))
    ax.axvline(N+.5, color=MUTED, lw=.85, ymax=.9)
    ax.set_xlim(.2, 16.6); ax.set_ylim(0, 1.3); ax.set_xticks([1, N, 10, 14]); ax.set_xticklabels(['1', '$N$', '10', '14']); ax.set_yticks([0, .5, 1])
    ax.set_xlabel('$k$', labelpad=0)
    ax.text(15.9, .06, r'$\cdots$', ha='center', va='center', color=MUTED)
axes[1].text(10.3, 1/(N+1)+.06, r'$1/(N+1)$', ha='left', va='bottom')
axes[0].text(10.3, 1.05, r'$\sup=1$', ha='left', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'N=5, x_k=1, y_k=1/k, k<=14; kept k<=N, error k>N'})
