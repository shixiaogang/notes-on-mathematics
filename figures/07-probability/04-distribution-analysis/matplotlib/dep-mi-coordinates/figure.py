"""Standard bivariate Gaussian rho = 0.5 (500 samples, seed 719) in three coordinate systems:
(a) (X,Y); (b) (e^X, e^Y); (c) (Phi(X), Phi(Y)).  Mutual information is -0.5 ln(1-rho^2) = 0.144 nat in all three;
Pearson correlation 0.5, (e^rho - 1)/(e - 1) = 0.378, (6/pi) arcsin(rho/2) = 0.483."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

rng = np.random.default_rng(SEED)
n, rho = 500, .5
z1 = rng.standard_normal(n); z2 = rho*z1+math.sqrt(1-rho*rho)*rng.standard_normal(n)
corr = [rho, (math.exp(rho)-1)/(math.e-1), 6/math.pi*math.asin(rho/2)]
fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
sets = [(z1, z2), (np.exp(z1), np.exp(z2)), (Phi(z1), Phi(z2))]
lims = [((-3.2, 3.2), (-3.2, 3.2)), ((0, 8), (0, 8)), ((0, 1), (0, 1))]
ticks = [[-3, 0, 3], [0, 4, 8], [0, .5, 1]]
xl = [('$x$', '$y$'), ('$\\mathrm{e}^{x}$', '$\\mathrm{e}^{y}$'), ('$\\Phi(x)$', '$\\Phi(y)$')]
for ax, (u, v), lim, tk, lab, c, l in zip(axs, sets, lims, ticks, ['(a)', '(b)', '(c)'], corr, xl):
    ax.scatter(u, v, s=1.2, color=GREEN, linewidths=0)
    ax.set_xlim(*lim[0]); ax.set_ylim(*lim[1]); ax.set_xticks(tk); ax.set_yticks(tk)
    ax.set_xlabel(l[0], labelpad=0); ax.set_ylabel(l[1], labelpad=0)
    ax.set_box_aspect(1)
    ax.text(.5, 1.04, f'相关系数 {c:.3f}', transform=ax.transAxes, ha='center', va='bottom', fontsize=7.5, color=MUTED)
    gfmt(ax)
    tag(ax, lab, y=-.34)
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'rho': rho, 'MI_nat': float(gauss_mi(rho)), 'pearson': corr,
     'clipped_points_b': int(np.sum((np.exp(z1) > 8) | (np.exp(z2) > 8)))})
