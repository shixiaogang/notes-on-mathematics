"""Cauchy: (a) truncated means int_{-R}^{cR} x f(x)dx for c=1/2,1,2; (b) x f(x) for Cauchy vs normal."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

import math
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.09, bottom=.27, wspace=.32)
ax = axes[0]; style(ax)
R = np.logspace(-1, 3, 400)
for c, col, ls in ((2, YELLOW, '--'), (1, BLUE, '-'), (.5, PURPLE, '-.')):
    ax.plot(R, np.log((1+c**2*R**2)/(1+R**2))/(2*np.pi), color=col, lw=1.4, ls=ls)
    ax.plot([R[-1]], [math.log(c)/np.pi], 'o', color=RED, ms=3.6, clip_on=False, zorder=6)
ax.set_xscale('log'); ax.minorticks_off()
lab(ax, 2, .25, '$c=2$', YELLOW); lab(ax, 2, .03, '$c=1$', BLUE); lab(ax, 2, -.28, '$c=1/2$', PURPLE)
lab(ax, 400, .262, r'$\ln 2/\pi$', RED, ha='center')
ax.set_xlim(.1, 1000); ax.set_ylim(-.3, .3); ax.set_xticks([.1, 1, 10, 100, 1000]); ax.set_xticklabels(['0.1', '1', '10', '100', '1000']); ax.set_yticks([-.2, 0, .2])
ax.set_xlabel('$R$', labelpad=1)
ax = axes[1]; style(ax)
x = np.linspace(0, 10, 800)
ax.plot(x, x/(np.pi*(1+x**2)), color=PURPLE, lw=1.4, ls='-.')
ax.plot(x, x*phi(x), color=BLUE, lw=1.4)
ax.plot(x[80:], 1/(np.pi*x[80:]), color=PURPLE, lw=.85, ls=DOT)
lab(ax, 3.2, .135, 'Cauchy', PURPLE); lab(ax, 1.7, .26, r'$\mathcal{N}(0,1)$', BLUE); lab(ax, 6.4, .065, r'$1/(\pi x)$', PURPLE)
ax.set_xlim(0, 10); ax.set_ylim(0, .3); ax.set_xticks([0, 2, 4, 6, 8, 10]); ax.set_yticks([0, .1, .2, .3])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$x f(x)$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'limits': {'c=2': math.log(2)/math.pi, 'c=1': 0, 'c=1/2': -math.log(2)/math.pi}})
