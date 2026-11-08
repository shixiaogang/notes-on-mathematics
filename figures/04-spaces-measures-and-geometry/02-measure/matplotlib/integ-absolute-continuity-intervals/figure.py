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

# F=sqrt(x) on [0,4]; intervals (0.2,0.5),(1.4,1.8),(2.6,2.9),(3.4,3.6) and their increments.
fig, ax = figure(width_mm=92, height_mm=54)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.975, top=.97, bottom=.11)
x = np.linspace(0, 4, 800); ax.plot(x, np.sqrt(x), color=BLUE, lw=1.4)
I = [(.2, .5), (1.4, 1.8), (2.6, 2.9), (3.4, 3.6)]
for l, r in I:
    for p in (l, r):
        ax.plot([p, p], [0, np.sqrt(p)], color=MUTED, lw=.65, dashes=(2.5, 2))
        ax.plot([0, p], [np.sqrt(p), np.sqrt(p)], color=MUTED, lw=.65, dashes=(2.5, 2))
    ax.plot([l, r], [0, 0], color=GREEN, lw=3, solid_capstyle='butt', clip_on=False)
    ax.plot([0, 0], [np.sqrt(l), np.sqrt(r)], color=RED, lw=3, solid_capstyle='butt', clip_on=False)
ax.text(2.2, .72, '$F(x)=\\sqrt{x}$', color=INK, ha='center')
ax.set_xlim(0, 4.1); ax.set_ylim(0, 2.15); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F=sqrt x; increments .260,.158,.090,.053; total .562; total length 1.2'})
