from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Limit of the random harmonic series S = sum eps_k/k.
# (a) histogram of S_N, N = 1000 (remaining variance sum_{k>1000} 1/k^2 ~ 1e-3), 200000 samples (seed 2),
#     against N(0, pi^2/6) density (yellow) with the same variance.
# (b) P(max_{m<k<=K}|S_k - S_m| >= eps), eps = 0.25, K = 20000, estimated from 4000 paths (seed 8), against the
#     Kolmogorov bound (1/eps^2) sum_{m<k<=K} 1/k^2 (purple).
rng = np.random.default_rng(2)
N, R = 1000, 200000
k = 1/np.arange(1, N+1)
SN = np.zeros(R)
for c in range(20):
    SN[c*10000:(c+1)*10000] = rademacher(rng, (10000, N)) @ k
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, bottom=.28, wspace=.32)
bins = np.linspace(-4, 4, 81)
a.hist(SN, bins=bins, density=True, color=GREEN_FILL, ec=GREEN, lw=.4)
v = np.pi**2/6; x = np.linspace(-4, 4, 401)
a.plot(x, np.exp(-x**2/(2*v))/np.sqrt(2*np.pi*v), color=YELLOW, lw=1.5)
a.set_xlim(-4, 4); a.set_ylim(0, .36); a.set_yticks([0, .1, .2, .3]); axlab(a, '$s$')
eps, K = .25, 20000
ms = np.array([10, 20, 50, 100, 200, 500, 1000])
rng2 = np.random.default_rng(8)
cnt = np.zeros(len(ms)); P = 4000
w = 1/np.arange(1, K+1)
for c in range(8):
    S = np.cumsum(rademacher(rng2, (P//8, K))*w, axis=1)
    for i, m in enumerate(ms):
        cnt[i] += np.sum(np.max(np.abs(S[:, m:]-S[:, [m-1]]), axis=1) >= eps)
prob = cnt/P
bound = np.array([np.sum(w[m:]**2) for m in ms])/eps**2
b.plot(ms, np.minimum(bound, 1), color=PURPLE, lw=1.4, marker='o', ms=3)
b.plot(ms, prob, color=GREEN, lw=1.4, marker='o', ms=3)
b.set_xscale('log'); logticks(b, [1, 2, 3], 'x'); b.set_yticks([0, .25, .5, .75, 1])
b.set_xlim(8, 1200); b.set_ylim(0, 1.02)
lab(b, 60, .5, 'Kolmogorov界', PURPLE); lab(b, 11, .06, '模拟频率', GREEN)
axlab(b, '$m$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'samples': R, 'seed_hist': 2, 'sample_var': float(SN.var()), 'pi2_over_6': v,
     'sample_excess_kurtosis': float(np.mean(SN**4)/SN.var()**2-3),
     'm': ms.tolist(), 'prob': prob.tolist(), 'bound': bound.tolist(), 'paths': P, 'seed_b': 8})
