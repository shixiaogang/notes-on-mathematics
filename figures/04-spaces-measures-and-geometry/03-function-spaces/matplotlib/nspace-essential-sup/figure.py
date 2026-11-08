from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f(x)=x on [0,1] with the single value f(1/2) changed to 2.
fig, ax = figure(width_mm=66, height_mm=48)
fig.set_layout_engine(None); fig.subplots_adjust(left=.11, right=.76, top=.96, bottom=.2)
ax.plot([0, 1], [0, 1], color=BLUE, lw=1.4)
ax.plot([.5], [.5], 'o', ms=4, mfc='white', mec=BLUE, mew=.9)
ax.plot([.5], [2], 'o', ms=3.8, color=GREEN, mew=0)
ax.plot([0, 1], [2, 2], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.plot([0, 1], [1, 1], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(1.02, 2, r'$\sup$', va='center'); ax.text(1.02, 1, r'$\mathrm{ess\,sup}$', va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 2.25); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=x, f(1/2)=2'})
