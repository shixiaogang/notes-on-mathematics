from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Spikes n*1_(0,1/n) and sqrt(n)*1_(0,1/n), threshold M=3.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.3, wspace=.12)
def draw(ax, data):
    for a, w, c, lab in data:
        if a > 3: ax.fill_between([0, w], 3, a, color=RED_FILL, lw=0)
    for a, w, c, lab in data:
        ax.plot([0, 0, w, w, 1], [0, a, a, 0, 0], color=c, lw=1.4)
        ax.text(w+.02, a-.1, lab, ha='left', va='top', fontsize=7.5)
    ax.plot([0, 1], [3, 3], color=MUTED, lw=.85, ls=(0, (3, 2)))
    ax.text(.98, 3.1, '$M=3$', ha='right', va='bottom', fontsize=7.5)
    ax.set_xlim(0, 1); ax.set_ylim(0, 9); ax.set_xticks([0, 1]); ax.set_yticks([0, 2, 4, 8]); ax.set_xlabel('$x$', labelpad=-4)
draw(axes[0], [(2, .5, BLUE, '$n=2$'), (4, .25, GREEN, '$n=4$'), (8, .125, YELLOW, '$n=8$')])
draw(axes[1], [(2, .25, BLUE, '$n=4$'), (4, .0625, GREEN, '$n=16$'), (8, 1/64, YELLOW, '$n=64$')])
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'n 1_(0,1/n) n=2,4,8; sqrt(n) 1_(0,1/n) n=4,16,64; M=3'})
