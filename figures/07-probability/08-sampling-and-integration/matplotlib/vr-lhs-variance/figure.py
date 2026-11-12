from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Ratio n Var(LHS estimate)/sigma^2 (1 = independent sampling) for even n.
# Additive F(u) = e^{u1} + e^{u2}: exact, Var = 2 n^{-2} sum_k s_k^2 with s_k^2 the variance of e^V, V ~ Unif(stratum k).
# Interaction F(u) = s(u1) s(u2), s = sign(u - 1/2): exact, Var = 1/(n-1) (hypergeometric count), sigma^2 = 1.
# Check: seeded simulation of the interaction case (seed 8, 20000 designs) at n = 2, 4, 8, 16.
s2 = (E*E-1)/2-(E-1)**2
def add_ratio(n):
    a = np.arange(n)/n; h = 1/n
    m = (np.exp(a+h)-np.exp(a))/h; m2 = (np.exp(2*(a+h))-np.exp(2*a))/(2*h)
    return n*(2*(m2-m*m).sum()/n**2)/(2*s2)
ns = np.array([2, 4, 8, 16, 32, 64, 128, 256])
ra = np.array([add_ratio(n) for n in ns]); ri = ns/(ns-1)
rng = np.random.default_rng(8); sim = {}
for n in (2, 4, 8, 16):
    R = 20000; est = np.empty(R)
    for r in range(R):
        U = (np.stack([rng.permutation(n), rng.permutation(n)], 1) + rng.random((n, 2)))/n
        est[r] = np.mean(np.sign(U[:, 0]-.5)*np.sign(U[:, 1]-.5))
    sim[n] = float(n*est.var())
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
ax.axhline(1, color=PURPLE, lw=.9, ls=DASH)
ax.plot(ns, ra, 'o-', color=GREEN, lw=1.2, ms=3)
ax.plot(ns, ri, 'o-', color=RED, lw=1.2, ms=3)
ax.plot(list(sim), list(sim.values()), 'o', ms=5, mfc='none', mec=RED, mew=.8)
ax.set_xscale('log', base=2); ax.set_yscale('log'); ax.set_xlim(1.7, 300); ax.set_ylim(5e-6, 5)
ax.set_xticks(ns); ax.set_xticklabels([str(n) for n in ns]); ax.minorticks_off()
logticks(ax, [-5, -4, -3, -2, -1, 0])
lab(ax, 20, 1.6, '交互项', RED); lab(ax, 20, 2e-3, '可加函数', GREEN); lab(ax, 130, .3, '独立抽样', PURPLE)
axlab(ax, '$n$', r'$n\operatorname{Var}/\sigma^{2}$')
save(fig, HERE, 'figure', {'ns': ns.tolist(), 'additive_ratio': ra.tolist(), 'interaction_ratio': ri.tolist(), 'sim_interaction': sim})
