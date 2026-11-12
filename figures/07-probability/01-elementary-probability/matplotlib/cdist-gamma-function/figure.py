"""Gamma function on (0,5]: integer points (n-1)! and Gamma(1/2)=sqrt(pi)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

import math
fig, ax = figure(width_mm=80, height_mm=48)
style(ax)
x = np.linspace(.12, 5, 800); g = np.array([math.gamma(v) for v in x])
ax.plot(x, g, color=BLUE, lw=1.4)
for n in range(1, 6):
    dot(ax, n, math.factorial(n-1))
lab(ax, 1, 2.3, '$0!$', RED, ha='center'); lab(ax, 2, 2.3, '$1!$', RED, ha='center')
lab(ax, 3, 3.3, '$2!$', RED, ha='center'); lab(ax, 3.82, 6.3, '$3!$', RED, ha='center'); lab(ax, 4.62, 21.5, '$4!$', RED, ha='left')
dot(ax, .5, math.sqrt(math.pi), color=GREEN); lab(ax, .12, .55, r'$\sqrt{\pi}$', GREEN)
ax.set_xlim(0, 5.2); ax.set_ylim(0, 25); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, 6, 12, 18, 24])
ax.set_xlabel(r'$\alpha$', labelpad=1); ax.set_ylabel(r'$\Gamma(\alpha)$', labelpad=1)
xm = .5+0*x
save(fig, here(__file__), 'figure', {'Gamma(1/2)': math.gamma(.5), 'min_on_grid': float(x[np.argmin(g)])})
