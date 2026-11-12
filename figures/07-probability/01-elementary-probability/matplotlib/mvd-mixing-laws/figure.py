"""Variance factors of the two scale mixtures X = mu + sqrt(V) Z.
Laplace: V = W ~ Exp(1) (blue); t with nu=5: V = 5/U, U ~ chi^2_5 (yellow).
(a) densities of V on [0,5]; (b) tail P(V>v) on log-log axes for v in [1,1000], with reference slope
v^{-5/2} (purple dashed). Tails computed by numerical integration of the exact densities."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

nu = 5
def chi2pdf(u):
    return np.exp((nu/2-1)*np.log(u)-u/2-(nu/2)*math.log(2)-math.lgamma(nu/2))
def finv(v):  # density of V = nu/U
    return chi2pdf(nu/v)*nu/v**2
def tail_inv(v):  # P(nu/U > v) = P(U < nu/v)
    a = nu/v; u = np.linspace(0, a, 4001)[1:]
    return float(np.trapezoid(chi2pdf(u), u))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.32)
ax = axes[0]; style(ax)
v = np.linspace(.005, 5, 800)
ax.plot(v, np.exp(-v), color=BLUE, lw=1.4); ax.plot(v, finv(v), color=YELLOW, lw=1.8)
lab(ax, .3, .9, r'$W$', BLUE, ha='left'); lab(ax, 1.9, .55, r'$5/U$', YELLOW, ha='left')
ax.set_xlim(0, 5); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, .5, 1])
axlab(ax, '$v$')
ax = axes[1]; style(ax)
vv = np.logspace(0, 3, 120)
ax.plot(vv, np.exp(-vv), color=BLUE, lw=1.4)
ti = np.array([tail_inv(x) for x in vv]); ax.plot(vv, ti, color=YELLOW, lw=1.8)
ax.plot(vv, ti[0]*vv**(-2.5), color=PURPLE, lw=1.0, ls=DASH)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(1, 1000); ax.set_ylim(1e-8, 1.5)
ax.set_yticks([1e-8, 1e-6, 1e-4, 1e-2, 1]); ax.set_xticks([1, 10, 100, 1000])
lab(ax, 4.5, 2e-5, r'$\mathrm{e}^{-v}$', BLUE, ha='left'); lab(ax, 60, 6e-4, r'$5/U$', YELLOW, ha='left')
lab(ax, 25, 3e-6, r'$v^{-5/2}$', PURPLE, ha='left')
axlab(ax, '$v$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'tail_inv_at_10_100': [tail_inv(10.), tail_inv(100.)], 'tail_W_at_10': math.exp(-10)})
