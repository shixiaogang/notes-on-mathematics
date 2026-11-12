from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'lln-common'))
from lln_fig import *
# Five Rademacher random walks (steps +-1 with prob 1/2 each), seed 7, n = 1..1000.
# (a) raw partial sums S_n with the +-sqrt(n) standard-deviation envelope;
# (b) sample averages S_n/n with the +-1/sqrt(n) envelope.
rng = np.random.default_rng(7)
N, M = 1000, 5
S = np.cumsum(rademacher(rng, (M, N)), axis=1)
n = np.arange(1, N+1)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.96, bottom=.28, wspace=.34)
for s in S:
    a.plot(n, s, color=GREEN, lw=.8)
    b.plot(n, s/n, color=GREEN, lw=.8)
for sg in (1, -1):
    a.plot(n, sg*np.sqrt(n), color=PURPLE, lw=1.1, ls=DASH)
    b.plot(n, sg/np.sqrt(n), color=PURPLE, lw=1.1, ls=DASH)
a.axhline(0, color=STROKE, lw=.6); b.axhline(0, color=STROKE, lw=.6)
lab(a, 60, 50, r'$\pm\sqrt{n}$', PURPLE, ha='left', va='bottom')
lab(b, 30, -.75, r'$\pm1/\sqrt{n}$', PURPLE, ha='left', va='bottom')
b.set_xscale('log')
a.set_xlim(0, N); a.set_ylim(-70, 70); b.set_xlim(1, N); b.set_ylim(-1.05, 1.05)
a.set_xticks([0, 500, 1000]); logticks(b, [0, 1, 2, 3], 'x'); b.set_yticks([-1, -.5, 0, .5, 1])
axlab(a, '$n$', '$S_n$'); axlab(b, '$n$', r'$S_n/n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'seed': 7, 'paths': M, 'n_max': N,
     'final_S': [int(x) for x in S[:, -1]], 'final_mean': [float(x) for x in S[:, -1]/N]})
