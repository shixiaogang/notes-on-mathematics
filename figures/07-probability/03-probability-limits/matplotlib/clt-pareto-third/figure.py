from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Symmetric Pareto steps: density (3/2)|x|^{-4} on |x| >= 1, variance 3, E|X|^3 = infinity.
# Sampling |X| = U^{-1/3} with an independent random sign. Seed 11, M = 20000 replications.
# Histograms of S_n / sqrt(3n) for (a) n = 10 and (b) n = 1000, against phi.
rng = np.random.default_rng(11)
M = 20000
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.97, bottom=.28, wspace=.26)
x = np.linspace(-4, 4, 400); edges = np.linspace(-4, 4, 41)
facts = {'seed': 11, 'M': M}
for ax, n in ((a, 10), (b, 1000)):
    S = np.zeros(M)
    for _ in range(n):
        S += rng.choice((-1.0, 1.0), M)*rng.random(M)**(-1/3)
    Z = S/math.sqrt(3*n)
    ax.hist(Z, bins=edges, density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
    ax.plot(x, phi(x), color=BLUE, lw=1.4)
    ax.set_xlim(-4, 4); ax.set_ylim(0, .62); ax.set_xticks([-4, -2, 0, 2, 4])
    facts['n=%d' % n] = {'P(|Z|<=0.5) sim': float(np.mean(np.abs(Z) <= .5)), 'normal': float(Phi(.5)-Phi(-.5)),
                         'sample_var': float(Z.var())}
axlab(a, '$z$', '密度'); axlab(b, '$z$')
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
