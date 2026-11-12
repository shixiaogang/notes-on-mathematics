"""Four joint laws with zero covariance (500 samples each, seed 719):
(a) Y = X^2, X ~ Unif(-1,1); (b) Y = S X with independent random sign S; (c) uniform on the unit circle; (d) independent Unif(-1,1) pair.
Only (d) is independent.  Population covariances are 0 in all four panels."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 500
x = rng.uniform(-1, 1, n)
s = rng.choice([-1, 1], n)
th = rng.uniform(0, 2*np.pi, n)
data = [(x, x**2-1/3), (x, s*x), (np.cos(th), np.sin(th)), (rng.uniform(-1, 1, n), rng.uniform(-1, 1, n))]
fig, axs = figure(width_mm=112, height_mm=36, ncols=4)
corr = []
for ax, (u, v), lab in zip(axs, data, ['(a)', '(b)', '(c)', '(d)']):
    ax.scatter(u, v, s=1.2, color=GREEN, linewidths=0)
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    ax.set_box_aspect(1)
    tag(ax, lab, y=-.24)
    corr.append(float(np.corrcoef(u, v)[0, 1]))
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'sample_correlations': corr, 'note': 'panel (a) plots y = x^2 - 1/3 (centred) so all panels share axes'})
