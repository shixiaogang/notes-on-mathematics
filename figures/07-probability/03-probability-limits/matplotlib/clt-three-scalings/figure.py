from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Fair coin. Exact central 90% band (5% and 95% quantiles) of n^a (Xbar_n - 1/2)
# for a = 0.3, 0.5, 0.7 and n = 10..10^4, computed from the exact Bin(n,1/2) law.
AS = (0.3, 0.5, 0.7)
ns = np.unique(np.round(np.logspace(1, 4, 60)).astype(int))
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.1, right=.98, bottom=.3, wspace=.62)
facts = {}
def q(n, a, u):
    pm = binpmf(n); F = np.cumsum(pm); k = int(np.searchsorted(F, u))
    return n**a*(k/n-.5)
for ax, a in zip(axs, AS):
    lo = np.array([q(n, a, .05) for n in ns]); hi = np.array([q(n, a, .95) for n in ns])
    ax.fill_between(ns, lo, hi, color=GREEN_FILL, lw=0, step='mid')
    ax.plot(ns, lo, color=GREEN, lw=1.0, drawstyle='steps-mid'); ax.plot(ns, hi, color=GREEN, lw=1.0, drawstyle='steps-mid')
    ref = 1.6449*.5*ns**(a-.5)
    ax.plot(ns, ref, color=PURPLE, lw=1.0, ls=DASH); ax.plot(ns, -ref, color=PURPLE, lw=1.0, ls=DASH)
    ax.axhline(0, color=STROKE, lw=.6)
    ax.set_xscale('log'); logticks(ax, [1, 2, 3, 4], 'x'); ax.set_xlim(10, 1e4)
    facts['a=%.1f' % a] = {'q95_n10': float(hi[0]), 'q95_n10000': float(hi[-1])}
axs[0].set_ylim(-.45, .45); axs[1].set_ylim(-1.2, 1.2); axs[2].set_ylim(-5.5, 5.5)
for ax, a in zip(axs, AS):
    axlab(ax, '$n$', r'$n^{%.1f}(\bar{X}_n-\frac{1}{2})$' % a)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
