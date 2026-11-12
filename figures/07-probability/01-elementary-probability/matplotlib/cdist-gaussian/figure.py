"""Gaussian densities: (a) location and scale; (b) N(10,0.2^2) with tolerance interval [9.8,10.4]."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
x = np.linspace(-3.5, 5.5, 900)
ax.plot(x, phi(x), color=BLUE, lw=1.4)
ax.plot(x, phi(x-2), color=YELLOW, lw=1.4, ls='--')
ax.plot(x, phi(x/.5)/.5, color=PURPLE, lw=1.4, ls='-.')
lab(ax, -3.3, .3, r'$\mathcal{N}(0,1)$', BLUE); lab(ax, 3.3, .3, r'$\mathcal{N}(2,1)$', YELLOW); lab(ax, .55, .72, r'$\mathcal{N}(0,0.5^2)$', PURPLE)
ax.set_xlim(-3.5, 5.5); ax.set_ylim(0, .85); ax.set_xticks([-2, 0, 2, 4]); ax.set_yticks([0, .4, .8])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f_X(x)$', labelpad=1)
ax = axes[1]; style(ax)
mu, s = 10, .2
x = np.linspace(9.3, 10.7, 700); f = phi((x-mu)/s)/s
xs = np.linspace(9.8, 10.4, 300)
ax.fill_between(xs, 0, phi((xs-mu)/s)/s, color=BLUE_FILL, lw=0)
ax.plot(x, f, color=BLUE, lw=1.4)
for v in (9.8, 10.4):
    ax.plot([v, v], [0, phi((v-mu)/s)/s], color=RED, lw=1.2)
P = float(Phi(2)-Phi(-1)); lab(ax, 10.06, .7, f'{P:.3f}', ha='center')
ax.set_xlim(9.3, 10.7); ax.set_ylim(0, 2.15); ax.set_xticks([9.4, 9.8, 10, 10.4]); ax.set_yticks([0, 1, 2])
ax.set_xlabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'P(9.8<X<10.4)': P, 'mu': mu, 'sigma': s})
