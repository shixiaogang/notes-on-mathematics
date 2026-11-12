from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# I = P(X > 4), X ~ Exp(1).  Importance sampling from q = Exp(2.2): weights w = e^{-y}/(2.2 e^{-2.2 y}) on y > 4.
# The estimator is unbiased, but E_q[(f w)^2] = int_4^inf e^{-(2-2.2)x}/2.2 dx = infinity.
# Three independent runs of 10^6 draws (seeds 11, 12, 13): (a) running estimate, (b) share of the largest single
# term in the running sum of f w.
lam = 2.2; I = math.exp(-4); N = 1_000_000
n = np.arange(1, N+1)
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.11, right=.98, bottom=.3, top=.96, wspace=.38)
facts = {}
for seed, c in zip((11, 12, 13), (GREEN, YELLOW, PURPLE)):
    rng = np.random.default_rng(seed); y = rng.exponential(1/lam, N)
    t = np.where(y > 4, np.exp(-y)/(lam*np.exp(-lam*y)), 0.0)
    cs = np.cumsum(t); est = cs/n; mx = np.maximum.accumulate(t)
    share = np.where(cs > 0, mx/np.where(cs > 0, cs, 1), np.nan)
    a1.plot(n, est, color=c, lw=1.1); a2.plot(n, share, color=c, lw=1.1)
    facts[str(seed)] = {'hits': int((y > 4).sum()), 'final': float(est[-1]), 'final_share': float(share[-1]),
                        'first_hit': int(np.argmax(y > 4))+1 if (y > 4).any() else None}
a1.axhline(I, color=RED, lw=1.1)
a1.set_xscale('log'); a1.set_xlim(100, N); a1.set_ylim(0, .05)
logticks(a1, [2, 4, 6], 'x')
lab(a1, 150, I+.003, r'$I=\mathrm{e}^{-4}$', RED)
axlab(a1, r'$n$', '运行估计')
a2.set_xscale('log'); a2.set_xlim(100, N); a2.set_ylim(0, 1.03); logticks(a2, [2, 4, 6], 'x')
axlab(a2, r'$n$', '最大一项的占比')
tags(fig, axs)
save(fig, HERE, 'figure', facts); print(facts)
