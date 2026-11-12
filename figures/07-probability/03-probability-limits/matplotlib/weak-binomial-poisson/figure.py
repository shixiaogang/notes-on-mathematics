from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Bin(n,2/n) -> Poisson(2). (a) cdfs for n=4,10 vs Poisson; (b) sup_x |F_n-F| vs n (log-log) with slope -1 reference.
def sup_err(n):
    pb = binom_pmf(n, 2/n); K = max(n, 60); pp = poisson_pmf(2, K)
    pb = np.concatenate([pb, np.zeros(K+1-len(pb))])
    return float(np.max(np.abs(np.cumsum(pb)-np.cumsum(pp))))
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.09, wspace=.33, bottom=.27)
ax = axes[0]; K = 8; pp = poisson_pmf(2, 40)
step_cdf(ax, np.arange(41), pp, -.5, K+.5, BLUE, lw=2.0, z=2)
step_cdf(ax, np.arange(5), binom_pmf(4, .5), -.5, K+.5, YELLOW, lw=1.5, z=3)
step_cdf(ax, np.arange(11), binom_pmf(10, .2), -.5, K+.5, GREEN, lw=1.1, z=4)
lab(ax, 3.2, .62, r'$n=4$', YELLOW); lab(ax, 5.2, .82, r'$\mathrm{Poisson}(2)$', BLUE)
ax.set_xlim(-.5, K+.5); ax.set_ylim(0, 1.08); ax.set_xticks(range(0, K+1, 2)); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
ax = axes[1]; ns = np.array([4, 6, 10, 16, 25, 40, 63, 100, 160, 250, 400, 630, 1000])
er = np.array([sup_err(int(n)) for n in ns])
ax.loglog(ns, er, 'o', ms=3, color=GREEN, mew=0)
c = er[-1]*ns[-1]; ax.loglog(ns, c/ns, color=PURPLE, lw=1.0, ls=DASH)
lab(ax, 60, c/60*1.5, r'$\propto 1/n$', PURPLE)
ax.minorticks_off(); ax.set_xticks([10, 100, 1000]); ax.set_xticklabels(['$10$', '$10^2$', '$10^3$'])
ax.set_yticks([1e-3, 1e-2, 1e-1]); ax.set_yticklabels(['$10^{-3}$', '$10^{-2}$', '$10^{-1}$'])
axlab(ax, r'$n$')
tags(fig, axes)
F2 = {int(n): float(np.cumsum(binom_pmf(n, 2/n))[2]) for n in (4, 10, 40)}
save(fig, HERE, 'figure', {'F_n(2)': F2, 'F(2)': float(5*np.exp(-2)), 'sup_err': dict(zip(map(int, ns), map(float, er)))})
