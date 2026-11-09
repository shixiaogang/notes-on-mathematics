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

# f(x)=sin(x)/x on [1,7pi]; lobes alternate in sign.
fig, ax = figure(width_mm=104, height_mm=44)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.98, top=.95, bottom=.15)
x = np.linspace(1, 7*np.pi, 1600); y = np.sin(x)/x
ax.fill_between(x, 0, y, where=y >= 0, fc=BLUE_FILL, lw=0); ax.fill_between(x, 0, y, where=y <= 0, fc=RED_FILL, lw=0)
ax.plot(x, y, color=INK, lw=1.3); ax.axhline(0, color=MUTED, lw=.75)
ax.set_xlim(0, 7*np.pi+.5); ax.set_ylim(-.26, .9); ax.set_yticks([0, .5])
ax.set_xticks([1]+[k*np.pi for k in range(1, 8)]); ax.set_xticklabels(['1', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$', '$5\\pi$', '$6\\pi$', '$7\\pi$'])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x)=sin(x)/x on [1,7pi]'})
