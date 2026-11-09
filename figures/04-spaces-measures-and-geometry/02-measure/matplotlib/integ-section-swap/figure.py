from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Rectangle

def labels(fig, axes, y=.03):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

# T={0<=x<=y<=1}: x section [x0,1] and y section [0,y0].
fig, axes = figure(width_mm=92, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.975, top=.95, bottom=.2, wspace=.16)
for ax in axes:
    ax.fill([0, 0, 1], [0, 1, 1], fc=BLUE_FILL, ec=BLUE, lw=.95)
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.1); ax.set_aspect('equal'); ax.set_xlabel('$x$', labelpad=-7, loc='right'); ax.set_ylabel('$y$', labelpad=-7, loc='top', rotation=0)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
a, b = axes
x0 = .35; y0 = .6
a.plot([x0, x0], [x0, 1], color=RED, lw=2.2, solid_capstyle='butt')
a.plot([x0, x0], [0, x0], color=MUTED, lw=.85, dashes=(3, 2))
a.set_xticks([0, x0, 1]); a.set_xticklabels(['0', '$x_0$', '1'])
b.plot([0, y0], [y0, y0], color=RED, lw=2.2, solid_capstyle='butt')
b.plot([y0, 1.0], [y0, y0], color=MUTED, lw=.85, dashes=(3, 2))
b.set_yticks([0, y0, 1]); b.set_yticklabels(['0', '$y_0$', '1'])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'T={0<=x<=y<=1}; x section y in [x,1]; y section x in [0,y]'})
