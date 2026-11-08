from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# h(x)=2x on [0,1], f(x)=x: int h=1, int f h=2/3.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
x = np.linspace(0, 1, 501)
a, b = axes
a.fill_between(x, 0, 2*x, color=BLUE_FILL, lw=0); a.plot(x, 2*x, color=BLUE, lw=1.4)
a.plot(x, x, color=GREEN, lw=1.4, ls=(0, (4, 2)))
a.text(.72, .40, r'$\int h=1$', ha='center', va='center'); a.text(.82, 1.86, r'$h=2x$', ha='right', va='center')
a.text(.20, .08, r'$f=x$', ha='left', va='center')
b.fill_between(x, 0, 2*x*x, color=BLUE_FILL, lw=0); b.plot(x, 2*x*x, color=BLUE, lw=1.4)
b.text(.76, .34, r'$\int fh=\frac{2}{3}$', ha='center', va='center'); b.text(.70, 1.45, r'$fh=2x^2$', ha='right', va='center')
for ax in axes:
    ax.set_xlim(0, 1.03); ax.set_ylim(0, 2.1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1, 2])
fig.set_layout_engine(None); fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.21, wspace=.2)
for ax, s in zip(axes, ['(a)', '(b)']):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h=2x, f=x, areas 1 and 2/3'})
