"""Multivariate t as a Gaussian scale mixture X = mu + V Z, V = sqrt(nu/U), U ~ chi^2_nu.
(a) density of the common scale V for nu = 1, 3, 10, 30 (light to dark blue); V concentrates at 1.
(b) log density of one component (Sigma_ii = 1): t_nu for nu = 1, 3, 10 against N(0,1) (yellow)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *
from matplotlib.colors import to_rgb

def shades(n):
    a = np.array(to_rgb('#BCC9D8')); b = np.array(to_rgb('#4E6784'))
    return [tuple(a+(b-a)*i/max(n-1, 1)) for i in range(n)]
def fV(v, nu):
    u = nu/v**2
    lf = (nu/2-1)*np.log(u)-u/2-(nu/2)*math.log(2)-math.lgamma(nu/2)
    return np.exp(lf)*2*nu/v**3
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.3)
ax = axes[0]; style(ax)
v = np.linspace(.02, 4, 800); nus = (1, 3, 10, 30); cc = shades(4)
for nu, c in zip(nus, cc):
    ax.plot(v, fV(v, nu), color=c, lw=1.4)
lab(ax, 1.9, .55, r'$\nu=1$', cc[0], ha='left'); lab(ax, 1.45, 1.0, '$3$', cc[1], ha='left')
lab(ax, 1.25, 1.6, '$10$', cc[2], ha='left'); lab(ax, 1.15, 2.6, '$30$', cc[3], ha='left')
ax.set_xlim(0, 4); ax.set_ylim(0, 3.2); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3])
axlab(ax, '$v$')
ax = axes[1]; style(ax)
x = np.linspace(0, 10, 500)
for nu, c in zip((1, 3, 10), cc[1:]):
    ax.plot(x, tpdf(x, nu), color=c, lw=1.4)
ax.plot(x, npdf(x), color=YELLOW, lw=1.6)
ax.set_yscale('log'); ax.set_ylim(1e-7, 1); ax.set_xlim(0, 10)
ax.set_yticks([1e-6, 1e-4, 1e-2, 1]); ax.set_xticks([0, 2, 4, 6, 8, 10])
lab(ax, 7.2, .012, r'$\nu=1$', cc[1], ha='left'); lab(ax, 7.6, 2.2e-4, '$3$', cc[2], ha='left')
lab(ax, 6.2, 1.2e-6, '$10$', cc[3], ha='left'); lab(ax, 3.3, 1e-6, r'$\mathcal{N}(0,1)$', YELLOW, ha='right')
axlab(ax, '$x$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'nu': list(nus), 'peak_density_t_vs_normal_at_6': [float(tpdf(6., nu)) for nu in (1, 3, 10)]+[float(npdf(6.))]})
