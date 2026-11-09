from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# [-1,1]: x^2 vs constant 1/3; error^2(c)=8/45+2(c-1/3)^2; c=0 gives 2/5.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.28, wspace=.24)
x = np.linspace(-1, 1, 801)
ax = axes[0]
ax.fill_between(x, x**2, 1/3, color=RED_FILL, lw=0)
ax.plot(x, x**2, color=BLUE, lw=1.4); ax.plot(x, 0*x+1/3, color=GREEN, lw=1.4)
ax.text(.75, .77, '$x^2$', ha='right'); ax.text(0, .42, '$c=1/3$', ha='center', fontsize=7.5)
ax.axhline(0, color=MUTED, lw=.85)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-.08, 1.12); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1/3, 1]); ax.set_yticklabels(['0', '1/3', '1']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
c = np.linspace(-.3, 1, 400); e = 8/45+2*(c-1/3)**2
ax.plot(c, e, color=BLUE, lw=1.4)
ax.plot([1/3], [8/45], 'o', ms=4, color=GREEN, mew=0); ax.plot([0], [2/5], 'o', ms=3.6, color=RED, mew=0)
ax.plot([1/3, 1/3], [0, 8/45], color=MUTED, lw=.85, ls=(0, (3, 2))); ax.plot([0, 1/3], [8/45, 8/45], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(.04, .44, '$c=0$: $2/5$', fontsize=7.5); ax.text(.38, .13, '$8/45$', fontsize=7.5)
ax.set_xlim(-.3, 1); ax.set_ylim(0, 1.1); ax.set_xticks([0, 1/3, 1]); ax.set_xticklabels(['0', '1/3', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$c$', labelpad=0); ax.set_ylabel(r'$\Vert x^2-c\Vert_2^2$', labelpad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'P x^2 = 1/3 on [-1,1], ||x^2-c||^2 = 8/45 + 2(c-1/3)^2'})
