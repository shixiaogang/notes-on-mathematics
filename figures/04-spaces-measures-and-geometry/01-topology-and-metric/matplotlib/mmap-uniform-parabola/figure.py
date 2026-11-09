from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# y=x^2; at x0 in {1,2,4} with eps=1 the admissible radius is delta=sqrt(x0^2+1)-x0.
fig, ax = figure(width_mm=104, height_mm=62)
x = np.linspace(0, 4.6, 600)
lx, ly = {1: 1, 2: 2, 4: 3.25}, {1: 2.9, 2: 6.2, 4: 18.4}
for x0 in (1, 2, 4):
    d = np.sqrt(x0**2+1)-x0
    ax.fill_between([0, x0+d], x0**2-1, x0**2+1, color=GREEN_FILL, lw=0, zorder=1)
    ax.fill_betweenx([0, x0**2+1], x0-d, x0+d, color=BLUE_FILL, lw=0, zorder=1)
    ax.plot([x0], [x0**2], 'o', ms=3.4, color=INK, mew=0, zorder=4)
    ax.text(lx[x0], ly[x0], rf'$\delta\approx{d:.3f}$', ha='center', va='center', color=INK)
ax.plot(x, x**2, color=BLUE, lw=1.4, zorder=3)
ax.set_xlim(0, 4.75); ax.set_ylim(0, 21.5)
ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([1, 4, 16])
ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
ax.set_xlabel('$x$'); ax.set_ylabel('$x^2$', rotation=0, labelpad=8)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'y=x^2; delta(x0)=sqrt(x0^2+1)-x0 for eps=1, x0=1,2,4'})
