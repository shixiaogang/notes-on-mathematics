from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Continuous ramps g_n rising from 0 to 1 on (1/2,1/2+1/n); L1 distance between g_4 and g_8 equals 1/16.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.3, wspace=.18)
x = np.linspace(0, 1, 2001)
def g(n): return np.clip(n*(x-.5), 0, 1)
ax = axes[0]
for n, c in ((2, BLUE), (4, GREEN), (16, YELLOW)):
    ax.plot(x, g(n), color=c, lw=1.4)
ax.plot([0, .5], [0, 0], color=RED, lw=1.4)
ax.plot([.5, 1], [1, 1], color=RED, lw=1.0, ls=(0, (3, 2)))
ax.plot([.5], [1], 'o', ms=3.6, mfc='white', mec=RED, mew=.85)
ax.plot([.5], [0], 'o', ms=3.4, color=RED, mew=0)
ax.text(.88, .68, '$g_2$', ha='left'); ax.text(.73, .7, '$g_4$', ha='left'); ax.text(.57, 1.08, '$g_{16}$', ha='left')
ax.set_xlim(0, 1); ax.set_ylim(-.06, 1.2); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.fill_between(x, g(4), g(8), color=RED_FILL, lw=0)
ax.plot(x, g(4), color=GREEN, lw=1.4); ax.plot(x, g(8), color=YELLOW, lw=1.4)
ax.text(.72, .63, '$g_4$', ha='left'); ax.text(.57, 1.08, '$g_{8}$', ha='left')
ax.annotate('面积 1/16', xy=(.625, .62), xytext=(.1, .78), ha='left', fontsize=7.5, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.85))
ax.set_xlim(0, 1); ax.set_ylim(-.06, 1.2); ax.set_xticks([0, .5, .75, 1]); ax.set_xticklabels(['0', '1/2', '3/4', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'g_n=clip(n(x-1/2),0,1); ||g_4-g_8||_1=1/8-1/16=1/16'})
