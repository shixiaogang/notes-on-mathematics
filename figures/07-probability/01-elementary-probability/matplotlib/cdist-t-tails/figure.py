"""Student t densities nu=1,3,30 vs N(0,1): (a) densities; (b) two-sided tails P(|T|>x), log scale."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

import math
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.09, bottom=.27, wspace=.32)
ax = axes[0]; style(ax)
x = np.linspace(-5, 5, 1001)
ax.plot(x, phi(x), color=BLUE, lw=1.4)
for nu, c, ls in ((1, PURPLE, '-.'), (3, YELLOW, '--'), (30, GREEN, (0, (1.2, 1.2)))):
    ax.plot(x, t_pdf(x, nu), color=c, lw=1.4, ls=ls)
lab(ax, 1.35, .33, r'$\mathcal{N}(0,1)$', BLUE); lab(ax, -4.8, .1, r'$\nu=1$', PURPLE); lab(ax, 2.2, .1, r'$\nu=3$', YELLOW)
ax.set_xlim(-5, 5); ax.set_ylim(0, .43); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, .2, .4])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f(x)$', labelpad=1)
ax = axes[1]; style(ax)
xs = np.linspace(0, 8, 401)
def tail_t(nu, x0):
    z = np.linspace(x0, x0+4000, 400001)
    return 2*np.trapezoid(t_pdf(z, nu), z)
ax.plot(xs, 2*(1-Phi(xs)), color=BLUE, lw=1.4)
for nu, c, ls in ((1, PURPLE, '-.'), (3, YELLOW, '--'), (30, GREEN, (0, (1.2, 1.2)))):
    if nu == 1:
        ys = 1-2/np.pi*np.arctan(xs)
    elif nu == 3:
        F = .5+(1/np.pi)*(xs/(np.sqrt(3)*(1+xs**2/3))+np.arctan(xs/np.sqrt(3))); ys = 2*(1-F)
    else:
        ys = np.array([tail_t(nu, v) for v in xs])
    ax.plot(xs, ys, color=c, lw=1.4, ls=ls)
ax.set_yscale('log'); ax.set_xlim(0, 8); ax.set_ylim(1e-8, 1.5); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([1e-8, 1e-6, 1e-4, 1e-2, 1])
ax.minorticks_off()
dot(ax, 3, 1-2/np.pi*np.arctan(3), color=PURPLE, ms=3.6); dot(ax, 3, .0576689, color=YELLOW, ms=3.6); dot(ax, 3, 2*(1-float(Phi(3))), color=BLUE, ms=3.6)
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel(r'$P(|T|>x)$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'P(|T|>3)': {'cauchy': float(1-2/np.pi*np.arctan(3)), 't3': .0576689, 'normal': 2*(1-float(Phi(3)))}})
