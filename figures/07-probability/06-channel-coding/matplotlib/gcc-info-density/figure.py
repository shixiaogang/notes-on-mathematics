from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Normalised information density (1/n) i_n(x^n; y^n) for the Gaussian channel with sigma^2 = 1 and Gaussian
# codebook input N(0, P'), P' = 3, so i(x;y) = 0.5 log2(1+P') + (log2 e)/2 (y^2/(P'+1) - (y-x)^2).
# Blue: sent codeword and its output (mean C' = 1 bit, variance (log2 e)^2 P'/(P'+1) = 1.561 per letter);
# yellow: an independent codeword of the same codebook law (mean 1 - 3 log2 e = -3.33).
# Seed 7, 20000 pairs per histogram. Red line: decoding threshold gamma = 0.6.
rng = np.random.default_rng(7); Pp = 3.0; T = 20000; gam = .6
def dens(x, y):
    return .5*math.log2(1+Pp) + LOG2E/2*(y*y/(Pp+1) - (y-x)**2)
fig, axs = figure(width_mm=110, height_mm=46, ncols=2)
panel(fig, left=.03, right=.98, top=.95, bottom=.3, wspace=.1)
facts = {}
for ax, n in zip(axs, (20, 200)):
    x = rng.normal(0, math.sqrt(Pp), (T, n)); z = rng.normal(0, 1, (T, n)); y = x+z
    xb = rng.normal(0, math.sqrt(Pp), (T, n))
    it = dens(x, y).mean(1); ib = dens(xb, y).mean(1)
    bins = np.linspace(-6, 3, 91)
    ax.hist(ib, bins=bins, density=True, color=YELLOW_FILL, edgecolor=YELLOW, lw=.5)
    ax.hist(it, bins=bins, density=True, color=BLUE_FILL, edgecolor=BLUE, lw=.5)
    ax.axvline(gam, color=RED, lw=1.1)
    ax.set_xlim(-6, 3); ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.set_xticks([-5, -3.33, 0, 1]); ax.set_xticklabels(['$-5$', '$-3.33$', '0', '1'])
    ax.set_xlabel(r'$i_n/n$ (bit)', labelpad=1)
    facts['n=%d' % n] = {'P(true <= gamma)': float((it <= gam).mean()), 'P(indep > gamma)': float((ib > gam).mean()),
                         'mean_true': float(it.mean()), 'var_true*n': float(it.var()*n), 'mean_indep': float(ib.mean())}
tags(fig, axs)
save(fig, HERE, 'figure', facts)
