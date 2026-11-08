from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# e^x = cosh + sinh on [-1,1]; ||sinh||^2 = sinh(2)/2 - 1 ~ 0.813
fig, ax = figure(width_mm=72, height_mm=46)
x = np.linspace(-1, 1, 801)
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(x, np.exp(x), color=BLUE, lw=1.4); ax.plot(x, np.cosh(x), color=GREEN, lw=1.4); ax.plot(x, np.sinh(x), color=RED, lw=1.4)
ax.text(.58, 2.2, '$e^x$'); ax.text(-.78, 1.55, r'$\cosh x$'); ax.text(.58, .16, r'$\sinh x$')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.3, 2.9); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
print('sinh2', np.sinh(2)/2-1)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'P_E e^x = cosh x, error sinh x, ||sinh||_2^2 = sinh(2)/2-1'})
