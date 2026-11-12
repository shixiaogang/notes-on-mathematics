"""Empirical grid score from samples of size n: maximum over equal-frequency k x l grids with k, l >= 2 and k*l <= n^0.6 of
(plug-in MI of the empirical table)/ln min(k,l).  200 replications per n, seed 719.
Green: independent Unif(0,1) pairs (population score 0); yellow: Y = X^2 + 0.2 Z, X ~ Unif(-1,1).  Solid: mean; thin: 5% and 95% quantiles."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

def score(x, y):
    n = len(x); B = n**0.6
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    best = 0.0
    for k in range(2, int(B//2)+1):
        for l in range(2, int(B//k)+1):
            bx = rx*k//n; by = ry*l//n
            P = np.zeros((k, l)); np.add.at(P, (bx, by), 1.0/n)
            best = max(best, mi_table(P)/math.log(min(k, l)))
    return best

rng = np.random.default_rng(SEED)
Ns = [20, 40, 80, 160, 320, 640, 1280, 2560]
R = 200
out = {}
for name in ('indep', 'parab'):
    M = []
    for n in Ns:
        v = []
        for _ in range(R):
            if name == 'indep':
                x = rng.random(n); y = rng.random(n)
            else:
                x = rng.uniform(-1, 1, n); y = x**2+.2*rng.standard_normal(n)
            v.append(score(x, y))
        v = np.array(v); M.append([v.mean(), np.quantile(v, .05), np.quantile(v, .95)])
    out[name] = np.array(M)
fig, ax = figure(width_mm=92, height_mm=50)
for name, col, lw in (('indep', GREEN, 1.4), ('parab', YELLOW, 1.6)):
    M = out[name]
    ax.plot(Ns, M[:, 0], color=col, lw=lw, marker='o', ms=2.4)
    ax.plot(Ns, M[:, 1], color=col, lw=.7); ax.plot(Ns, M[:, 2], color=col, lw=.7)
ax.axhline(0, color=RED, lw=.9, ls='--')
ax.set_xscale('log'); ax.set_xticks(Ns); ax.set_xticklabels([str(n) for n in Ns])
ax.tick_params(axis='x', labelsize=7)
ax.set_ylim(-.02, 1.0); ax.set_xlabel('$n$', labelpad=0)
ax.minorticks_off()
save(fig, HERE, 'figure', {'seed': SEED, 'reps': R, 'n': Ns, 'indep_mean_q05_q95': out['indep'].round(4).tolist(), 'parab_mean_q05_q95': out['parab'].round(4).tolist()})
