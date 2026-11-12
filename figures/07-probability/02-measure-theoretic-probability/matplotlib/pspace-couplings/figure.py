from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: three couplings of two Unif(0,1) marginals and the law of the difference D = X - Y.
# (U,U): D = 0; (U,1-U): D = 2U-1 ~ Unif(-1,1), density 1/2; (U,V) independent: triangular density 1-|z|.
# Scatter: 300 simulated pairs, seed 9; histograms: 20000 pairs, same seed stream.
rng = np.random.default_rng(9)
fig, axs = figure(width_mm=112, height_mm=78, nrows=2, ncols=3)
U = rng.random(300); V = rng.random(300)
pairs = [(U, U), (U, 1-U), (U, V)]
Ub = rng.random(20000); Vb = rng.random(20000)
diffs = [Ub-Ub, Ub-(1-Ub), Ub-Vb]
z = np.linspace(-1, 1, 201)
dens = [None, np.full_like(z, 0.5), 1-np.abs(z)]
for j in range(3):
    ax = axs[0, j]; style(ax)
    ax.plot(pairs[j][0], pairs[j][1], 'o', ms=1.3, color=GREEN, mew=0)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal')
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=0)
    ax = axs[1, j]; style(ax)
    if j == 0:
        ax.plot([0, 0], [0, 1], color=BLUE, lw=1.4)
        ax.plot([0], [1], '^', ms=4, color=BLUE)
        ax.set_ylim(0, 1.15); ax.set_yticks([0, 1]); ax.set_yticklabels(['0', ''])
    else:
        ax.hist(diffs[j], bins=40, range=(-1, 1), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
        ax.plot(z, dens[j], color=BLUE, lw=1.4)
        ax.set_ylim(0, 1.15); ax.set_yticks([0, 0.5, 1])
    ax.set_xlim(-1.05, 1.05); ax.set_xticks([-1, 0, 1])
    sub(ax, 'abc'[j], '$z=x-y$')
stats = {name: [float(d.mean()), float(d.var())] for name, d in zip(['UU', 'U1-U', 'UV'], diffs)}
save(fig, HERE(__file__), 'figure', {'seed': 9, 'mean,var of D (sim)': stats, 'exact var': [0, 1/3, 1/6]})
