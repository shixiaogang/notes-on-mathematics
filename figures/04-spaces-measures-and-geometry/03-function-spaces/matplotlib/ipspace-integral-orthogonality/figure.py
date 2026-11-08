from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# 1*x has signed areas -1/2, +1/2; 1*x^2 has area 2/3 on [-1,1].
fig, axes = figure(width_mm=100, height_mm=44, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.3, wspace=.2)
x = np.linspace(-1, 1, 801)
ax = axes[0]
ax.fill_between(x, x, 0, where=x<=0, color=RED_FILL, lw=0); ax.fill_between(x, x, 0, where=x>=0, color=BLUE_FILL, lw=0)
ax.axhline(0, color=MUTED, lw=.85); ax.plot(x, x, color=BLUE, lw=1.4)
ax.text(.68, .22, '$+1/2$', ha='center'); ax.text(-.68, -.3, '$-1/2$', ha='center')
ax.text(-.15, .62, '$1\\cdot x$', ha='right')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.15, 1.15); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.fill_between(x, x**2, 0, color=BLUE_FILL, lw=0)
ax.axhline(0, color=MUTED, lw=.85); ax.plot(x, x**2, color=BLUE, lw=1.4)
ax.text(.0, .28, '面积 2/3', ha='center', fontsize=7.5); ax.text(.42, .62, '$1\\cdot x^2$', ha='right')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-.1, 1.15); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'int_{-1}^1 x dx = 0; int_{-1}^1 x^2 dx = 2/3'})
