from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Poisson(2) smoothed by N(0, sigma^2): f_sigma(x) = (1/pi) int_0^inf Re(e^{-isx} phi(s)) e^{-sigma^2 s^2/2} ds,
# computed by trapezoidal quadrature of the characteristic function and checked against the Gaussian mixture.
lam = 2.0; K = 40; pk = poisson_pmf(lam, K)
phi = lambda s: np.exp(lam*(np.exp(1j*s)-1))
def f_cf(x, sig):
    s = np.linspace(0, 12/sig, 6001)
    integrand = (np.exp(-1j*np.outer(x, s))*phi(s)).real*np.exp(-sig**2*s**2/2)
    return np.trapezoid(integrand, s, axis=1)/np.pi
def f_mix(x, sig):
    return (pk[None, :]*npdf(x[:, None]-np.arange(K+1)[None, :], sig)).sum(axis=1)
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.25, bottom=.27)
x = np.linspace(-1.5, 8.5, 1201); errs = {}
for ax, sig in zip(axes, (0.5, 0.2)):
    ax.bar(np.arange(8), pk[:8], width=.5, color=BLUE_FILL, edgecolor=BLUE, lw=.7, zorder=1)
    fc = f_cf(x, sig); fm = f_mix(x, sig); errs[sig] = float(np.max(np.abs(fc-fm))); assert errs[sig] < 1e-6
    ax.plot(x, fc, color=GREEN, lw=1.3, zorder=3)
    lab(ax, 7.9, .62, r'$\sigma=%.1f$' % sig, GREEN, ha='right', va='top')
    ax.set_xlim(-1.5, 8.5); ax.set_ylim(0, .7); ax.set_xticks(range(0, 9, 2)); ax.set_yticks([0, .2, .4, .6])
    axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'max_abs_diff_cf_vs_mixture': errs})
