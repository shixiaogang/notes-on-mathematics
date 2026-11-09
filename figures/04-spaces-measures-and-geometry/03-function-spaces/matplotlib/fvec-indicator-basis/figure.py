from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# X={0,1,2} 上的指示函数与 f=1 delta_0+0 delta_1+4 delta_2。
fig, axes = figure(width_mm=112, height_mm=36, ncols=4)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.045, right=.985, top=.93, bottom=.27, wspace=.3)
X = np.array([0, 1, 2])
vals = [(1,0,0), (0,1,0), (0,0,1), (1,0,4)]; names = [r'$\delta_0$', r'$\delta_1$', r'$\delta_2$', '$f$']
for i, (ax, v, n) in enumerate(zip(axes, vals, names)):
    v = np.array(v); c = BLUE if i == 3 else GREEN
    ax.vlines(X, 0, v, color=c, lw=1.3); ax.plot(X, v, 'o', ms=3.6, color=c, mew=0)
    ax.set_xlim(-.45, 2.45); ax.set_xticks(X)
    top = 4.6 if i == 3 else 1.25
    ax.set_ylim(0, top); ax.set_yticks([0, 1, 4] if i == 3 else [0, 1])
    ax.text(.97, .98, n, transform=ax.transAxes, ha='right', va='top')
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .035, '(%s)' % 'abcd'[i], ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'delta_i on {0,1,2}, f=delta_0+4 delta_2 with values (1,0,4)'})
