from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Cost-constrained Blahut-Arimoto on the Z-channel with c(0)=0, c(1)=1. For each multiplier s the iteration
# q <- q 2^{D(W_x||p) - s c(x)} (400 rounds from (1/2,1/2)) gives a point (Gamma(s), I) on the capacity-cost curve.
# Blue: exact curve h2(G/2) - G (flat at log2(5/4) for G >= 0.4); green dots: s = 0, 0.1, ..., 1.5;
# red: multiplier found by bisection (40 halvings on [0,3]) so that Gamma(s) = 0.25.
def run(s, T=400):
    q = np.array([.5, .5])
    for _ in range(T):
        pY = q @ Z; Dx = np.array([kl(Z[x], pY) for x in range(2)]) - s*np.array([0, 1.]); q = q*2**Dx; q /= q.sum()
    return q
g = np.linspace(0, 1, 801); Cg = np.where(g <= .4, h2(np.minimum(g, .4)/2) - np.minimum(g, .4), np.log2(1.25))
fig, ax = figure(width_mm=90, height_mm=50)
panel(fig, left=.14, right=.97, top=.95, bottom=.2)
ax.plot(g, Cg, color=BLUE, lw=1.4)
pts = []
for s in np.arange(0, 1.51, .1):
    q = run(s); pts.append((q[1], mi(q, Z))); ax.plot([q[1]], [mi(q, Z)], 'o', ms=3.2, color=GREEN, mew=0, zorder=5)
lo, hi = 0., 3.
for _ in range(40):
    mid = (lo+hi)/2
    if run(mid)[1] > .25: lo = mid
    else: hi = mid
qs = run(hi); dot(ax, qs[1], mi(qs, Z))
lab(ax, .27, .25, r'$s=%.3f$' % hi, RED); lab(ax, .41, .335, r'$s=0$', GREEN); lab(ax, .035, .03, r'$s=1.5$', GREEN)
ax.set_xlim(0, .7); ax.set_ylim(0, .36); ax.set_xlabel(r'$\Gamma(s)$', labelpad=1); ax.set_ylabel(r'$I$ / bit', labelpad=1)
save(fig, HERE, 'figure', {'s_bisect': hi, 'q_at_s': float(qs[1]), 'points': [[float(a), float(b)] for a, b in pts]})
