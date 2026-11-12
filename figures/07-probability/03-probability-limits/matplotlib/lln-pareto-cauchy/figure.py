from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Sample averages, five paths each, n <= 10^5, log x-axis.
# (a) Pareto(alpha = 1.5) on [1, inf): mean 3 (blue line), infinite variance; seed 13.
# (b) standard Cauchy (no mean), generated as tan(pi (U - 1/2)); seed 14.
N, M = 10**5, 5
n = np.arange(1, N+1)
P = pareto(np.random.default_rng(13), 1.5, (M, N))
C = np.tan(np.pi*(np.random.default_rng(14).random((M, N))-.5))
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, bottom=.28, wspace=.28)
for s in np.cumsum(P, axis=1)/n: a.plot(n, s, color=GREEN, lw=.8)
a.axhline(3, color=BLUE, lw=1.2)
for s in np.cumsum(C, axis=1)/n: b.plot(n, s, color=GREEN, lw=.8)
b.axhline(0, color=STROKE, lw=.6)
for ax in (a, b): ax.set_xscale('log'); ax.set_xlim(1, N); logticks(ax, [0, 1, 2, 3, 4, 5], 'x'); axlab(ax, '$n$')
a.set_ylim(0, 8); b.set_ylim(-8, 8)
lab(a, 3e3, 3.5, r'$\mu=3$', BLUE)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'pareto_final': (np.cumsum(P, axis=1)[:, -1]/N).tolist(),
     'cauchy_final': (np.cumsum(C, axis=1)[:, -1]/N).tolist(), 'seeds': [13, 14]})
