from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Truncation at level k in the strong law: Pareto(alpha = 1.5) sample X_1..X_2000 (seed 17), log-log axes.
# Points with X_k > k (red) are the only ones changed by Y_k = X_k 1{X_k <= k}; expected count sum_k k^{-1.5} ~ 2.6.
rng = np.random.default_rng(17)
N = 2000
k = np.arange(1, N+1)
X = pareto(rng, 1.5, N)
big = X > k
fig, ax = figure(width_mm=96, height_mm=54)
panel(fig, left=.12, right=.97, bottom=.2, top=.95)
ax.plot(k[~big], X[~big], 'o', ms=1.6, color=GREEN, mew=0)
ax.plot(k[big], X[big], 'o', ms=4, color=RED, mew=0)
ax.plot(k, k, color=STROKE, lw=.9)
lab(ax, 400, 160, '$x=k$', STROKE)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(1, N); ax.set_ylim(.8, 3000)
logticks(ax, [0, 1, 2, 3], 'x'); logticks(ax, [0, 1, 2, 3])
axlab(ax, '$k$', '$X_k$')
save(fig, HERE, 'figure', {'seed': 17, 'big_indices': [int(i) for i in k[big]], 'big_values': [float(v) for v in X[big]],
     'expected': float(np.sum(k**-1.5))})
