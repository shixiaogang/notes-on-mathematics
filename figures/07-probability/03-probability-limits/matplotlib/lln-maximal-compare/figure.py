from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Rademacher walk, n = 100 steps. Exact probabilities (no simulation):
# endpoint P(|S_100| >= a) from Bin(100,1/2); running maximum P(max_{k<=100}|S_k| >= a) by dynamic programming
# with absorption at |s| >= a. Kolmogorov bound n/a^2 and union bound sum_k Var(S_k)/a^2 = 5050/a^2.
n = 100
pm = binpmf(n); K = np.arange(n+1); Send = 2*K-n
A = np.arange(4, 41)
p_end = np.array([pm[np.abs(Send) >= a].sum() for a in A])
def p_max(a):
    w = {0: 1.0}; hit = 0.0
    for _ in range(n):
        nw = {}
        for s, q in w.items():
            for d in (-1, 1):
                t = s+d
                if abs(t) >= a: hit += q/2
                else: nw[t] = nw.get(t, 0)+q/2
        w = nw
    return hit
pmx = np.array([p_max(a) for a in A])
fig, ax = figure(width_mm=100, height_mm=54)
panel(fig, left=.12, right=.97, bottom=.2, top=.95)
ax.plot(A, 5050/A**2, color=YELLOW, lw=1.6, ls=DASH)
ax.plot(A, n/A**2, color=PURPLE, lw=1.4)
ax.plot(A, pmx, color=GREEN, lw=1.4)
ax.plot(A, p_end, color=BLUE, lw=1.4)
ax.set_yscale('log'); ax.set_ylim(1e-4, 400); ax.set_xlim(4, 40)
logticks(ax, [-4, -3, -2, -1, 0, 1, 2]); ax.axhline(1, color=STROKE, lw=.6, ls=DOT)
lab(ax, 30, 12, r'$5050/a^2$', YELLOW, va='center')
lab(ax, 33, .2, r'$n/a^2$', PURPLE, va='center')
lab(ax, 26, 3e-2, '全程最大值越过', GREEN, ha='left', va='center')
lab(ax, 13, 6e-4, '终点越过', BLUE, ha='left', va='center')
axlab(ax, '$a$')
i20 = list(A).index(20)
save(fig, HERE, 'figure', {'n': n, 'a=20': {'end': float(p_end[i20]), 'max': float(pmx[i20]), 'kolmogorov': n/400, 'union': 5050/400},
     'a=30': {'end': float(p_end[list(A).index(30)]), 'max': float(pmx[list(A).index(30)])},
     'ratio_max_over_end_a20': float(pmx[i20]/p_end[i20])})
