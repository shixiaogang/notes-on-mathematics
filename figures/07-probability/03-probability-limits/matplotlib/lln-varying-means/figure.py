from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Independent Bernoulli X_k ~ Bern(p_k) with block-varying means: p_k = 0.2 for k in [2^j, 2^(j+1)) with j even,
# p_k = 0.8 for j odd, k = 1..2^14. One path, seed 3.
# (a) running mean of the means m_n = (1/n) sum p_k (blue) and sample average S_n/n (green);
# (b) centred average (S_n - sum p_k)/n (green) with the two-standard-deviation envelope 2*sqrt(sum p_k(1-p_k))/n (purple).
rng = np.random.default_rng(3)
N = 2**14
k = np.arange(1, N+1)
j = np.floor(np.log2(k)).astype(int)
p = np.where(j % 2 == 0, .2, .8)
X = (rng.random(N) < p).astype(float)
S = np.cumsum(X); m = np.cumsum(p)/k
env = 2*np.sqrt(np.cumsum(p*(1-p)))/k
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, bottom=.28, wspace=.36)
a.plot(k, S/k, color=GREEN, lw=.9)
a.plot(k, m, color=BLUE, lw=1.4)
a.set_xscale('log'); a.set_xlim(1, N); a.set_ylim(0, 1)
lab(a, 3000, .72, r'$S_n/n$', GREEN); lab(a, 2000, .2, r'$m_n$', BLUE)
b.plot(k, (S-np.cumsum(p))/k, color=GREEN, lw=.9)
b.plot(k, env, color=PURPLE, lw=1.1, ls=DASH); b.plot(k, -env, color=PURPLE, lw=1.1, ls=DASH)
b.axhline(0, color=STROKE, lw=.6)
b.set_xscale('log'); b.set_xlim(1, N); b.set_ylim(-.5, .5)
for ax in (a, b): logticks(ax, [0, 2, 4], 'x')
axlab(a, '$n$'); axlab(b, '$n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'seed': 3, 'N': N, 'm_at_2^13-1': float(m[2**13-2]), 'm_at_2^14': float(m[-1]),
     'min_m_late': float(m[1000:].min()), 'max_m_late': float(m[1000:].max())})
