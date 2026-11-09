from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) sin(x+c), c=0,0.8,1.6,2.4,3.2 (1-Lipschitz); (b) sin(nx), n=1,3,9,27, with first peak pi/(2n).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.21, wspace=.16)
x = np.linspace(0, 1.6, 2000); d = .2
a = axes[0]
a.axvspan(0, d, color=YELLOW_FILL, lw=0, zorder=1)
for c in (0, .8, 1.6, 2.4, 3.2):
    a.plot(x, np.sin(x+c), color=BLUE, lw=1.2, zorder=3)
b = axes[1]
b.axvspan(0, d, color=YELLOW_FILL, lw=0, zorder=1)
for n in (1, 3, 9, 27):
    b.plot(x, np.sin(n*x), color=BLUE, lw=1.1 if n < 27 else .9, zorder=3)
    b.plot([np.pi/(2*n)], [1], 'o', ms=3, color=RED, mew=0, zorder=5, clip_on=False)
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.set_xlim(0, 1.6); ax.set_ylim(-1.25, 1.25); ax.set_xticks([0, d, 1, 1.5]); ax.set_xticklabels(['0', r'$\delta$', '1', '1.5']); ax.set_yticks([-1, 0, 1])
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sin(x+c); sin(n x), peak at pi/(2n); delta=0.2'})
