from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Young area picture for p=3, q=3/2, a=1, b=0.6: curve s=t^2.
fig, ax = figure(width_mm=62, height_mm=52)
fig.set_layout_engine(None); fig.subplots_adjust(left=.13, right=.97, top=.97, bottom=.16)
t = np.linspace(0, 1, 400); a, b = 1, .6
ax.fill_between(t, 0, t**2, color=BLUE_FILL, lw=0)
tb = np.linspace(0, b**.5, 300); 
ax.fill_between(tb, tb**2, b, color=GREEN_FILL, lw=0)
ax.plot(t, t**2, color=INK, lw=1.4)
ax.plot([0, a, a, 0], [b, b, 0, 0], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.plot([a, a], [0, 1], color=BLUE, lw=1.0)
ax.plot([0, b**.5], [b, b], color=GREEN, lw=1.0)
ax.text(.69, .2, '$a^p/p$', ha='center', va='center')
ax.text(.2, .37, '$b^q/q$', ha='center', va='center')
ax.text(.74, .68, '$s=t^{p-1}$', ha='right', va='bottom')
ax.set_xlim(0, 1.12); ax.set_ylim(0, 1.1); ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$a$']); ax.set_yticks([0, b]); ax.set_yticklabels(['0', '$b$'])
ax.text(1.1, .03, '$t$', ha='right', va='bottom'); ax.text(.03, 1.07, '$s$', ha='left', va='top')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=3,q=3/2,a=1,b=.6; a^p/p=1/3, b^q/q=.3098'})
