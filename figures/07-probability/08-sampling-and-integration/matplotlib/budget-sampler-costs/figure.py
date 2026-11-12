from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Target pi = 0.3 N(-2, 0.5^2) + 0.7 N(2, 1), f(x) = x, I = 0.8, Var_pi(f) = 4.135.
# Teaching cost model (units): uniform 1, Gaussian 2, mixture density 4, Gaussian envelope density 2, f 1.
#  direct (component then Gaussian): 1 + 2 + 1 = 4 per iid sample.
#  rejection from envelope N(m, s^2), (m, s) minimising M = sup p/q on a grid: per candidate 2 + 2 + 4 + 1 = 9,
#     expected M candidates per accepted sample, plus f.
#  random-walk Metropolis step s: per iteration 2 + 4 + 1 + 1 = 8; integrated autocorrelation time tau of f
#     from batch means (10^6 iterations after 10^4 discarded, 200 batches, seed 1).
p = lambda x: 0.3*phi(x, -2, .5)+0.7*phi(x, 2, 1)
xs = np.linspace(-14, 14, 280001)
best = min(((p(xs)/phi(xs, m, s)).max(), m, s) for m in np.arange(0, 1.51, .05) for s in np.arange(2.0, 3.51, .05))
M, me, se = best
def mh(s, N, seed):
    rng = np.random.default_rng(seed); x = 0.0; px = p(x); out = np.empty(N)
    z = rng.standard_normal(N)*s; u = rng.random(N)
    for t in range(N):
        y = x+z[t]; py = p(y)
        if u[t]*px < py: x, px = y, py
        out[t] = x
    return out
def tau(x, nb=200):
    L = len(x)//nb; bm = x[:L*nb].reshape(nb, L).mean(1); return L*bm.var(ddof=1)/x.var()
def acf(x, K):
    x = x-x.mean(); v = x.var(); return np.array([1.0]+[np.mean(x[:-k]*x[k:])/v for k in range(1, K+1)])
steps = [1.0, 2.5, 4.0]; chains = {s: mh(s, 1_010_000, 1)[10_000:] for s in steps}
taus = {s: tau(chains[s]) for s in steps}
cost = {'直接生成': 4.0, '拒绝采样': 9*M+1}
for s in steps: cost['MH, s=%g' % s] = 8*taus[s]
fig, axs = figure(width_mm=108, height_mm=54, ncols=2)
a1, a2 = axs
panel(fig, left=.09, right=.97, bottom=.29, top=.96, wspace=.62)
K = 60; ks = np.arange(K+1)
for s, c in zip(steps, [YELLOW, GREEN, BLUE]):
    a1.plot(ks, acf(chains[s], K), color=c, lw=1.4)
a1.axhline(0, color=STROKE, lw=.85)
a1.set_xlim(0, K); a1.set_ylim(-.1, 1.02)
lab(a1, 28, .62, r'$s=1$', YELLOW); lab(a1, 7, .2, r'$s=2.5$', GREEN)
lab(a1, 40, .08, r'$s=4$', BLUE)
axlab(a1, '滞后步数', '自相关')
names = list(cost)[::-1]; vals = [cost[n] for n in names]
a2.barh(range(len(names)), vals, color=[BLUE_FILL if 'MH' not in n else GREEN_FILL for n in names],
        edgecolor=[BLUE if 'MH' not in n else GREEN for n in names], lw=.8, height=.6)
a2.set_xscale('log'); a2.set_xlim(1, 1000); logticks(a2, [0, 1, 2, 3], 'x')
a2.set_yticks(range(len(names))); a2.set_yticklabels(names)
for i, v in enumerate(vals): lab(a2, v*1.15, i-.15, '%.0f' % v, INK)
axlab(a2, '每个有效样本的成本')
tags(fig, axs)
facts = {'M': M, 'env_mean': me, 'env_sd': se, 'accept_rate': 1/M, 'tau': taus, 'cost_per_eff': cost,
         'chain_means': {s: float(chains[s].mean()) for s in steps}}
save(fig, HERE, 'figure', {k: (v if not isinstance(v, dict) else {str(a): float(b) for a, b in v.items()}) for k, v in facts.items()})
print(facts)
