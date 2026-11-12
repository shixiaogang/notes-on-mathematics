from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: Cantor variable X = sum_k 2 D_k / 3^k with independent fair digits D_k (30 digits kept).
# Exact: E[X] = 1/2, Var(X) = 1/8, sd = 0.3536. Simulation: 20000 samples, seed 2026, 81 bins on [0,1].
rng = np.random.default_rng(2026)
D = rng.integers(0, 2, size=(20000, 30))
X = (2*D/3.0**np.arange(1, 31)).sum(axis=1)
fig, ax = figure(width_mm=100, height_mm=46)
style(ax)
ax.hist(X, bins=81, range=(0, 1), color=GREEN_FILL, edgecolor=GREEN, lw=.4)
ax.axvline(0.5, color=RED, lw=1.4)
sd = np.sqrt(1/8)
for v in (0.5-sd, 0.5+sd):
    ax.axvline(v, color=PURPLE, lw=.85, ls='--')
ax.set_xlim(0, 1); ax.set_xticks([0, 1/3, 0.5-sd, 0.5, 0.5+sd, 2/3, 1])
ax.set_xticklabels(['0', '1/3', '', '1/2', '', '2/3', '1'])
ax.set_ylabel('样本数'); ax.set_xlabel('$x$')
save(fig, HERE(__file__), 'figure', {'seed': 2026, 'n': 20000, 'sample mean': float(X.mean()), 'sample var': float(X.var()), 'exact': [0.5, 0.125]})
