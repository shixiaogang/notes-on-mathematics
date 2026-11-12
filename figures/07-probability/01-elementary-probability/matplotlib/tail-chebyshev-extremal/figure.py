from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Extremal three-point law for Chebyshev with mean 0, variance 1, t=2: masses 1/8, 3/4, 1/8 at -2,0,2,
# against the N(0,1) density (same mean and variance).
fig, ax = figure(width_mm=86, height_mm=46)
x = np.linspace(-3.5, 3.5, 701)
ax.plot(x, np.exp(-x**2/2)/np.sqrt(2*np.pi), color=YELLOW, lw=1.5)
for v, m in ((-2, 1/8), (0, 3/4), (2, 1/8)):
    tail = v != 0
    ax.plot([v, v], [0, m], color=BLUE, lw=2.2, solid_capstyle='butt')
    ax.plot([v], [m], 'o', ms=4, color=BLUE, mew=0)
    lab(ax, v+.12, m, {-2: '$1/8$', 0: '$3/4$', 2: '$1/8$'}[v], BLUE, va='bottom')
lab(ax, -3.3, .06, r'$\mathcal{N}(0,1)$', YELLOW, ha='left')
ax.set_xlim(-3.5, 3.5); ax.set_ylim(0, .82); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, .25, .5, .75])
axlab(ax, '$x$')
save(fig, HERE, 'figure', {'three_point_tail': 0.25, 'normal_tail': float(2*Q(2))})
