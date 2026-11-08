from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# h(x)=x-x^2 on [0,1]: max 1/4 at x=1/2, integral 1/6; four midpoint samples give the vector v.
fig, axes = figure(width_mm=112, height_mm=44, ncols=3, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.3, wspace=.12)
x = np.linspace(0, 1, 400); h = x-x**2
ax = axes[0]
ax.plot(x, h, color=BLUE, lw=1.4)
ax.plot([0, 1], [.25, .25], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.plot([.5], [.25], 'o', ms=3.6, color=BLUE, mew=0)
ax.text(.5, .265, r'$\max\,\vert h\vert=1/4$', ha='center', va='bottom')
ax = axes[1]
ax.fill_between(x, 0, h, color=BLUE_FILL, lw=0)
ax.plot(x, h, color=BLUE, lw=1.4)
ax.text(.5, .075, '面积 1/6', ha='center', va='center')
ax = axes[2]
xi = np.array([1, 3, 5, 7])/8; v = xi-xi**2
ax.bar(xi, v, width=.25, color=BLUE_FILL, edgecolor=BLUE, lw=.85)
ax.plot(x, h, color=BLUE, lw=1.4)
ax.plot(xi, v, 'o', ms=3.4, color=BLUE, mew=0)
ax.text(.115, .178, '7/64', ha='center', va='bottom', fontsize=7.5)
ax.text(.36, .262, '15/64', ha='center', va='bottom', fontsize=7.5)
for ax in axes:
    ax.set_xlim(0, 1); ax.set_ylim(0, .33); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .25]); ax.set_yticklabels(['0', '1/4']); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h=x-x^2; midpoints (2i-1)/8, h values 7/64,15/64,15/64,7/64'})
