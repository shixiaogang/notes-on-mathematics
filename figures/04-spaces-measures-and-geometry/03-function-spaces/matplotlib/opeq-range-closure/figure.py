from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f_n = n 1_[0,1/n] and V f_n = min(nx,1). ||Vf_n-1||^2=1/(3n), ||f_n||^2=n.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.28, wspace=.18)
ns = (2, 4, 8); cs = (BLUE, GREEN, YELLOW)
ax = axes[0]
for n, c in zip(ns, cs):
    ax.plot([0, 0, 1/n, 1/n, 1], [0, n, n, 0, 0], color=c, lw=1.4)
ax.text(.52, 2.0, '$f_2$', ha='left', va='center'); ax.text(.27, 4.0, '$f_4$', ha='left', va='center'); ax.text(.145, 8.0, '$f_8$', ha='left', va='center')
ax.set_xlim(-.02, 1); ax.set_ylim(-.3, 9); ax.set_xticks([0, .125, .25, .5, 1]); ax.set_xticklabels(['0', '1/8', '1/4', '1/2', '1']); ax.set_yticks([0, 2, 4, 8]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
x = np.linspace(0, 1, 2001)
ax.plot([0, 1], [1, 1], color=RED, lw=1.0, ls=(0, (3, 2)))
for n, c in zip(ns, cs):
    ax.plot(x, np.minimum(n*x, 1), color=c, lw=1.4)
ax.plot([0], [0], 'o', ms=3.4, color=INK, mew=0)
ax.text(.36, .5, '$Vf_2$', ha='left', va='center'); ax.text(.235, .8, '$Vf_4$', ha='left', va='center'); ax.text(.025, 1.13, '$Vf_8$', ha='left', va='center')
ax.text(.62, 1.08, '$g=1$', ha='left')
ax.set_xlim(-.02, 1); ax.set_ylim(-.06, 1.25); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f_n=n 1_[0,1/n]; Vf_n=min(nx,1)'})
