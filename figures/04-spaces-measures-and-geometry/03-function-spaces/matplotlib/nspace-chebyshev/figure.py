from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Tent h=1-|2x-1| with eps=1/2: exceedance set (1/4,3/4); rectangle eps*mu(A)=1/4 inside total area 1/2.
fig, ax = figure(width_mm=78, height_mm=46)
fig.set_layout_engine(None); fig.subplots_adjust(left=.09, right=.97, top=.97, bottom=.18)
x = np.linspace(0, 1, 800); h = 1-abs(2*x-1)
ax.fill_between(x, 0, h, color=BLUE_FILL, lw=0)
ax.fill_between([.25, .75], 0, .5, color=YELLOW_FILL, lw=0)
ax.plot(x, h, color=BLUE, lw=1.4)
ax.plot([0, 1], [.5, .5], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.plot([.25, .75], [0, 0], color=RED, lw=2.4, solid_capstyle='butt')
ax.text(.5, .3, r'$\varepsilon\,\mu(A)$', ha='center', va='center')
ax.text(.98, .53, r'$\varepsilon=1/2$', ha='right', va='bottom', fontsize=7.5)
ax.text(.5, .05, '$A$', ha='center', va='bottom', color=INK)
ax.text(.2, .72, '$h$', ha='center', va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 1.1); ax.set_xticks([0, .25, .75, 1]); ax.set_xticklabels(['0', '1/4', '3/4', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h=1-|2x-1|, eps=.5, A=(1/4,3/4), eps mu(A)=1/4, int h=1/2'})
