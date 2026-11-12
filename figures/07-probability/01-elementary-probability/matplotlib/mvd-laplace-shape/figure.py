"""Multivariate Laplace X = sqrt(W) Z, W ~ Exp(1), Z ~ N(0, I_d).
(a) one component: Laplace with b = 1/sqrt2 (blue) against N(0,1) (yellow), same variance 1, log scale.
(b) density along a ray, g_d(r) = int_0^inf (2 pi w)^{-d/2} exp(-r^2/(2w)) exp(-w) dw, for d = 1, 2, 3
(light to dark blue), log scale; closed forms for d=1: exp(-sqrt2 r)/sqrt2, d=3: exp(-sqrt2 r)/(2 pi r)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *
from matplotlib.colors import to_rgb

def shades(n):
    a = np.array(to_rgb('#BCC9D8')); b = np.array(to_rgb('#4E6784'))
    return [tuple(a+(b-a)*i/max(n-1, 1)) for i in range(n)]
def g(r, d):
    # substitute w = e^s to integrate over s in R
    s = np.linspace(-30, 6, 20001); w = np.exp(s)
    vals = (2*pi*w)**(-d/2)*np.exp(-r*r/(2*w)-w)*w
    return float(np.trapezoid(vals, s))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.3)
ax = axes[0]; style(ax)
x = np.linspace(-6, 6, 801)
ax.plot(x, lappdf(x, 1/np.sqrt(2)), color=BLUE, lw=1.4); ax.plot(x, npdf(x), color=YELLOW, lw=1.6)
ax.set_yscale('log'); ax.set_ylim(1e-7, 1.5); ax.set_xlim(-6, 6); ax.set_xticks([-6, -3, 0, 3, 6])
ax.set_yticks([1e-6, 1e-4, 1e-2, 1])
lab(ax, 3.5, 5e-2, 'Laplace', BLUE, ha='left'); lab(ax, 2.0, 2e-6, r'$\mathcal{N}(0,1)$', YELLOW, ha='right')
axlab(ax, '$x$')
ax = axes[1]; style(ax)
r = np.linspace(.02, 4, 200); cc = shades(3)
G = {d: np.array([g(ri, d) for ri in r]) for d in (1, 2, 3)}
for d, c in zip((1, 2, 3), cc):
    ax.plot(r, G[d], color=c, lw=1.4)
ax.set_yscale('log'); ax.set_xlim(0, 4); ax.set_ylim(1e-4, 20); ax.set_xticks([0, 1, 2, 3, 4])
ax.set_yticks([1e-4, 1e-2, 1, 10])
lab(ax, 2.6, .05, '$d=1$', cc[0], ha='left'); lab(ax, 1.6, 4e-3, '$2$', cc[1], ha='left'); lab(ax, .25, 2.5, '$3$', cc[2], ha='left')
axlab(ax, r'$r=\sqrt{Q}$')
tags(fig, axes)
chk = {'d1_at_1': [g(1., 1), math.exp(-math.sqrt(2))/math.sqrt(2)], 'd3_at_1': [g(1., 3), math.exp(-math.sqrt(2))/(2*pi)]}
save(fig, HERE(__file__), 'figure', chk)
