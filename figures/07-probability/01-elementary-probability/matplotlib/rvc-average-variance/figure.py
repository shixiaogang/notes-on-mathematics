"""Variance of the average of n equicorrelated readings with unit variance: 1/n+(1-1/n)rho, rho=0, 0.3, 2/3.
Green dots: sample variance over 4000 simulated replications (seed 11), X_i=sqrt(rho)Z_0+sqrt(1-rho)Z_i."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

rng = np.random.default_rng(11); R = 4000
fig, ax = figure(width_mm=92, height_mm=50)
nn = np.arange(1, 31); facts = {}
for rho, c in ((0.0, BLUE), (0.3, YELLOW), (2/3, PURPLE)):
    ax.plot(nn, 1/nn + (1-1/nn)*rho, color=c, lw=1.5)
    ax.axhline(rho, color=c, lw=0.8, ls='--')
    pts = [1, 2, 5, 10, 20, 30]
    Z0 = rng.standard_normal(R); Z = rng.standard_normal((R, 30))
    Xs = np.sqrt(rho)*Z0[:, None] + np.sqrt(1-rho)*Z
    sv = [np.var(Xs[:, :m].mean(1)) for m in pts]
    ax.scatter(pts, sv, s=10, color=GREEN, zorder=3)
    facts[f'{rho:.3f}'] = dict(zip(map(str, pts), map(float, sv)))
ax.text(30.5, 2/3, r'$\rho=2/3$', va='center', fontsize=7.5)
ax.text(30.5, 0.3, r'$\rho=0.3$', va='center', fontsize=7.5)
ax.text(30.5, 0.03, r'$\rho=0$', va='center', fontsize=7.5)
ax.set_xlim(0, 30); ax.set_ylim(0, 1.05); ax.set_xlabel('$n$', labelpad=1)
ax.set_ylabel(r'$\operatorname{Var}(\bar{X}_n)$')
save(fig, Path(__file__).resolve().parent, 'figure', {'seed': 11, 'replications': R, 'sample_var': facts})
