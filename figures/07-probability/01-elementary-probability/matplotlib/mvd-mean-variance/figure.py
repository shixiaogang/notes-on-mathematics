"""Sample mean vs sum of squared residuals for n=5 i.i.d. observations, 1500 replications each.
(a) N(1,1) samples (seed 21): no visible relation between mean and residual sum of squares;
(b) Exp(1) samples (same mean and variance, seed 22): residual spread grows with the mean.
Correlations of (mean, SS) are recorded in figure.json."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

n, R = 5, 1500
A = np.random.default_rng(21).normal(1, 1, (R, n))
B = np.random.default_rng(22).exponential(1, (R, n))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.12)
facts = {'n': n, 'replications': R, 'seeds': [21, 22]}
for ax, D, name in zip(axes, (A, B), ('gauss', 'exp')):
    style(ax)
    m = D.mean(1); ss = ((D-m[:, None])**2).sum(1)
    ax.plot(m, ss, '.', ms=1.6, color=GREEN)
    facts['corr_'+name] = float(np.corrcoef(m, ss)[0, 1])
    ax.set_xlim(-.6, 3.2); ax.set_ylim(0, 16); ax.set_xticks([0, 1, 2, 3])
    axlab(ax, r'$\bar{x}$')
axes[0].set_yticks([0, 5, 10, 15]); axes[0].set_ylabel('残差平方和', labelpad=1)
tags(fig, axes)
save(fig, HERE(__file__), 'figure', facts)
