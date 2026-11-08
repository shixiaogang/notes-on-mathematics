from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# g(x)=|x-1/2| periodic, h=1/16: g, Delta_h g, Delta_h^2 g.
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.08, right=.985, top=.96, bottom=.27, wspace=.42)
g = lambda x: np.abs(np.mod(x, 1)-.5)
x = np.linspace(0, 1, 2001); h = 1/16
d1 = g(x+h)-g(x); d2 = g(x+2*h)-2*g(x+h)+g(x)
for ax, y, c, yl, ticks, labs in ((axes[0], g(x), BLUE, (0, .62), [0, .5], ['0', '1/2']),
                                  (axes[1], d1, GREEN, (-.09, .09), [-h, 0, h], ['$-h$', '0', '$h$']),
                                  (axes[2], d2, RED, (-.16, .16), [-2*h, 0, 2*h], ['$-2h$', '0', '$2h$'])):
    ax.plot(x, y, color=c, lw=1.4); ax.set_xlim(0, 1); ax.set_ylim(*yl); ax.set_yticks(ticks); ax.set_yticklabels(labs)
    ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=0)
for a, t in zip(axes, '(a) (b) (c)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, t, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'g=|x-1/2| periodic; h=1/16; first and second differences'})
