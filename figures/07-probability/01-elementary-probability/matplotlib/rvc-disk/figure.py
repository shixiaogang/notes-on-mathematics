"""Uniform distribution on the unit disk: uncorrelated but dependent. 600 simulated points (seed 3);
red segments: possible y-range sqrt(1-x^2) above x=0.2 and x=0.9."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

rng = np.random.default_rng(3); n = 600
r = np.sqrt(rng.random(n)); t = 2*np.pi*rng.random(n); x = r*np.cos(t); y = r*np.sin(t)
fig, a = figure(width_mm=58, height_mm=52)
th = np.linspace(0, 2*np.pi, 300)
a.plot(np.cos(th), np.sin(th), color=BLUE, lw=1.1)
a.scatter(x, y, s=1.6, color=GREEN, linewidths=0)
for xv in (0.2, 0.9):
    h = np.sqrt(1-xv**2); a.plot([xv, xv], [-h, h], color=RED, lw=1.5)
a.set_aspect('equal'); a.set_xlim(-1.1, 1.1); a.set_ylim(-1.1, 1.1); a.set_xticks([-1, 0, 0.2, 0.9]); a.set_xticklabels(['-1', '0', '0.2', '0.9'], fontsize=7)
a.set_yticks([-1, 0, 1])
a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$y$', rotation=0)
save(fig, Path(__file__).resolve().parent, 'figure', {'seed': 3, 'n': n, 'sample_corr': float(np.corrcoef(x, y)[0, 1])})
