"""Densities f(x,y)=1+theta(1-2x)(1-2y) on the unit square for theta=-1,0,1.
All three have Unif(0,1) marginals; Cov=theta/36. Analytic heat maps (white to BLUE)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
g = np.linspace(0, 1, 201); X, Y = np.meshgrid(g, g)
for ax, th, s in zip(axs, (-1, 0, 1), ('(a)', '(b)', '(c)')):
    F = 1 + th*(1-2*X)*(1-2*Y)
    im = ax.imshow(F, origin='lower', extent=(0, 1, 0, 1), cmap=cmap, vmin=0, vmax=2, interpolation='bilinear')
    ax.set_aspect('equal'); ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$y$', rotation=0, labelpad=-2)
    ax.set_title(rf'$\theta={th}$', pad=3)
    tag(ax, s, y=-0.28)
cb = fig.colorbar(im, ax=axs, shrink=0.8, ticks=[0, 1, 2])
cb.outline.set_linewidth(0.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'density': '1+theta(1-2x)(1-2y)', 'theta': [-1, 0, 1], 'cov': 'theta/36'})
