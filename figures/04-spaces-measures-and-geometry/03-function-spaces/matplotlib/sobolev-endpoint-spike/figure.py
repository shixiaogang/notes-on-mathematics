from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# v_n=max(1-nx,0): v_n(0)=1, ||v_n||_2=(3n)^(-1/2), ||v_n'||_2=sqrt(n).
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.07, right=.98, top=.97, bottom=.27, wspace=.25)
ax = axes[0]; x = np.linspace(0, 1, 800)
for n, c in zip((2, 4, 8), (BLUE, GREEN, YELLOW)):
    ax.plot(x, np.maximum(1-n*x, 0), color=c, lw=1.4)
ax.text(.34, .42, '$v_2$', ha='left'); ax.text(.24, .2, '$v_4$', ha='left'); ax.text(.135, .09, '$v_8$', ha='left')
ax.plot([0], [1], 'o', color=INK, ms=3.4)
ax.set_xlim(0, 1); ax.set_ylim(-.04, 1.12); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; n = np.arange(1, 17)
ax.plot(n, np.sqrt(n), color=GREEN, lw=1.4, marker='o', ms=2.6)
ax.plot(n, (3*n)**-.5, color=BLUE, lw=1.4, marker='o', ms=2.6)
ax.axhline(1, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(9.2, 3.45, r"$\Vert v_n'\Vert_2$", ha='right'); ax.text(14, .32, r'$\Vert v_n\Vert_2$', ha='center'); ax.text(15.5, 1.1, '$v_n(0)=1$', ha='right')
ax.set_xlim(.5, 16.5); ax.set_ylim(0, 4.3); ax.set_xticks([1, 4, 8, 12, 16]); ax.set_yticks([0, 1, 2, 3, 4]); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'v_n=max(1-nx,0); norms (3n)^-1/2 and n^1/2'})
