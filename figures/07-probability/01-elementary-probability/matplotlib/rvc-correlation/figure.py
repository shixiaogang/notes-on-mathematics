"""Scatter plots, 400 simulated points each (seed 7). (a)-(c): standard normal pairs with rho=0.9,-0.6,0
(Y=rho X+sqrt(1-rho^2) Z). (d): X~Unif(-sqrt3,sqrt3), Y=X^2-1+0.1 Z, rho=0 although Y is nearly a function of X."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

rng = np.random.default_rng(7); n = 400
fig, axs = figure(width_mm=112, height_mm=36, ncols=4)
facts = {}
for ax, rho, s in zip(axs[:3], (0.9, -0.6, 0.0), ('(a)', '(b)', '(c)')):
    x = rng.standard_normal(n); y = rho*x + np.sqrt(1-rho**2)*rng.standard_normal(n)
    ax.scatter(x, y, s=1.6, color=GREEN, linewidths=0)
    ax.set_title(rf'$\rho={rho:g}$', pad=2); facts[s] = float(np.corrcoef(x, y)[0, 1])
    ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.3, 3.3)
x = rng.uniform(-np.sqrt(3), np.sqrt(3), n); y = x**2 - 1 + 0.1*rng.standard_normal(n)
axs[3].scatter(x, y, s=1.6, color=GREEN, linewidths=0); axs[3].set_title(r'$\rho=0$', pad=2)
axs[3].set_xlim(-2, 2); axs[3].set_ylim(-1.5, 2.5); facts['(d)'] = float(np.corrcoef(x, y)[0, 1])
for ax, s in zip(axs, ('(a)', '(b)', '(c)', '(d)')):
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    tag(ax, s, y=-0.10)
save(fig, Path(__file__).resolve().parent, 'figure', {'seed': 7, 'n': n, 'sample_corr': facts})
