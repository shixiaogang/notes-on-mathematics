from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Same simulation as clt-bivariate-scatter (seed 3, n = 100, M = 1500, X = (xi, xi+eta)).
# Histograms of the projections a^T sqrt(n) Xbar_n for a = (1,0), (0,1), (1,-1)/sqrt2,
# against N(0, a^T Sigma a) densities, a^T Sigma a = 1, 2, 1/2.
rng = np.random.default_rng(3)
n, M = 100, 1500
A = (2*rng.binomial(n, .5, M)-n)/math.sqrt(n)
B = (2*rng.binomial(n, .5, M)-n)/math.sqrt(n)
P = [(A, 1.0), (A+B, 2.0), ((A-(A+B))/math.sqrt(2), .5)]
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, left=.06, right=.98, bottom=.32, wspace=.22)
x = np.linspace(-5, 5, 400); facts = {}
for ax, (y, v), nm in zip(axs, P, ('e1', 'e2', 'diag')):
    step = 0.2/math.sqrt(2) if nm == 'diag' else 0.2  # lattice spacing of the projection
    edges = np.arange(-6-step/2, 6+step, step)
    ax.hist(y, bins=edges, density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
    ax.plot(x, phi(x/math.sqrt(v))/math.sqrt(v), color=BLUE, lw=1.4)
    ax.set_xlim(-4.5, 4.5); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_ylim(0, .66)
    facts[nm] = {'theory_var': v, 'sample_var': float(np.var(y))}
axs[0].set_xlabel(r'$\mathbf{a}=(1,0)$', labelpad=1); axs[1].set_xlabel(r'$\mathbf{a}=(0,1)$', labelpad=1)
axs[2].set_xlabel(r'$\mathbf{a}=(1,-1)/\sqrt{2}$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
