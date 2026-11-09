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

# f(x)=x on [0,1], dyadic layer approximations phi_n=floor(2^n x)/2^n, n=1,2,3.
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.045, right=.985, top=.95, bottom=.23, wspace=.16)
x = np.linspace(0, 1, 200)
for ax, n in zip(axes, (1, 2, 3)):
    m = 2**n
    for k in range(m):
        ax.add_patch(Rectangle((k/m, 0), 1/m, k/m, fc=GREEN_FILL, ec=GREEN, lw=.75))
    ax.plot(x, x, color=BLUE, lw=1.4)
    ax.set_xlim(0, 1.04); ax.set_ylim(0, 1.08); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x)=x, phi_n=floor(2^n x)/2^n, n=1,2,3; integrals 1/4,3/8,7/16'})
