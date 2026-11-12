from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Random-sign series with the same signs eps_k (+-1, prob 1/2), six paths, seed 5, k <= 10^4:
# (a) partial sums of sum eps_k/k (variances 1/k^2 summable: converges);
# (b) partial sums of sum eps_k/sqrt(k) (variances 1/k not summable) with envelope +-2 sqrt(H_n), H_n = sum_{k<=n} 1/k.
rng = np.random.default_rng(5)
N, M = 10**4, 6
E = rademacher(rng, (M, N)); k = np.arange(1, N+1)
A1 = np.cumsum(E/k, axis=1); A2 = np.cumsum(E/np.sqrt(k), axis=1)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, bottom=.28, wspace=.3)
for s in A1: a.plot(k, s, color=GREEN, lw=.8)
for s in A2: b.plot(k, s, color=GREEN, lw=.8)
H = np.cumsum(1/k)
b.plot(k, 2*np.sqrt(H), color=PURPLE, lw=1.1, ls=DASH); b.plot(k, -2*np.sqrt(H), color=PURPLE, lw=1.1, ls=DASH)
lab(b, 1.5, 5.6, r'$\pm2\sqrt{H_n}$', PURPLE, ha='left')
for ax in (a, b):
    ax.set_xscale('log'); ax.set_xlim(1, N); logticks(ax, [0, 1, 2, 3, 4], 'x'); ax.axhline(0, color=STROKE, lw=.6)
a.set_ylim(-3, 3); b.set_ylim(-7, 7)
axlab(a, '$n$'); axlab(b, '$n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'seed': 5, 'final_a': [float(x) for x in A1[:, -1]], 'change_a_1000_to_10000': [float(x) for x in A1[:, -1]-A1[:, 999]],
     'final_b': [float(x) for x in A2[:, -1]]})
