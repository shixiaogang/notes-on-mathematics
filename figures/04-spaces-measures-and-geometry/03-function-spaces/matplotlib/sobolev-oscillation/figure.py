from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f_n(x)=sin(2 pi n x): ||f_n||_2 = 1/sqrt2 and ||f_n'||_2 = sqrt2*pi*n.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.07, right=.98, top=.97, bottom=.27, wspace=.27)
ax = axes[0]; x = np.linspace(0, 1, 1200)
ax.plot(x, np.sin(2*np.pi*x), color=BLUE, lw=1.4)
ax.plot(x, np.sin(8*np.pi*x), color=YELLOW, lw=1.1)
ax.axhline(0, color=MUTED, lw=.85)
ax.text(.09, 1.08, '$f_1$', ha='center', color=INK); ax.text(.41, 1.08, '$f_4$', ha='center', color=INK)
ax.set_xlim(0, 1); ax.set_ylim(-1.2, 1.35); ax.set_xticks([0, .5, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; n = np.arange(1, 7)
ax.plot(n, np.sqrt(2)*np.pi*n, color=GREEN, lw=1.4, marker='o', ms=3)
ax.plot(n, np.full(n.shape, 2**-.5), color=BLUE, lw=1.4, marker='o', ms=3)
ax.text(4.0, 25.2, r"$\Vert f_n'\Vert_2=\sqrt{2}\,\pi n$", ha='right', va='center')
ax.text(6, 3.5, r'$\Vert f_n\Vert_2=1/\sqrt{2}$', ha='right', va='center')
ax.set_xlim(.7, 6.3); ax.set_ylim(0, 30); ax.set_xticks(n); ax.set_yticks([0, 10, 20, 30]); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sin(2 pi n x); norms 1/sqrt2 and sqrt2 pi n'})
