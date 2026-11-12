"""Unit-variance N(0,1), Laplace(0,1/sqrt2), t_3 scaled by 1/sqrt3: (a) densities; (b) log densities."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

import math
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.09, bottom=.27, wspace=.32)
b = 1/math.sqrt(2); s3 = 1/math.sqrt(3)
x = np.linspace(-4, 4, 1601)
ax = axes[0]; style(ax)
ax.plot(x, phi(x), color=BLUE, lw=1.4); ax.plot(x, laplace_pdf(x, b), color=YELLOW, lw=1.4, ls='--'); ax.plot(x, t_pdf(x, 3, s3), color=PURPLE, lw=1.4, ls='-.')
lab(ax, .3, .69, 'Laplace', YELLOW, ha='left'); lab(ax, -2.6, .3, r'$\mathcal{N}(0,1)$', BLUE, ha='center'); lab(ax, 1.15, .45, '$t_3$', PURPLE)
for c in (0.4894, 2.339):
    ax.plot([c], [phi(c)], 'o', color=RED, ms=3, zorder=6)
ax.set_xlim(-4, 4); ax.set_ylim(0, .78); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f(x)$', labelpad=1)
ax = axes[1]; style(ax)
x = np.linspace(0, 6, 601)
ax.plot(x, phi(x), color=BLUE, lw=1.4); ax.plot(x, laplace_pdf(x, b), color=YELLOW, lw=1.4, ls='--'); ax.plot(x, t_pdf(x, 3, s3), color=PURPLE, lw=1.4, ls='-.')
ax.set_yscale('log'); ax.minorticks_off(); ax.set_xlim(0, 6); ax.set_ylim(1e-8, 1.2); ax.set_yticks([1e-8, 1e-6, 1e-4, 1e-2, 1]); ax.set_xticks([0, 2, 4, 6])
ax.set_xlabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'peaks': {'normal': 1/math.sqrt(2*math.pi), 'laplace': 1/math.sqrt(2), 't3': float(t_pdf(0, 3, s3))}, 'crossings_normal_laplace': [0.4894, 2.339]})
