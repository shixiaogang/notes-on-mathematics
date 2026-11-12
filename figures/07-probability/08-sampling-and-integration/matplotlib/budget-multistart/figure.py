from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Random-walk Metropolis on pi = 0.3 N(-2, 0.5^2) + 0.7 N(2, 1) with step s = 0.5, f(x) = x, I = 0.8.
# Four chains started at -4, -1, 1, 4 (seed 0..3), 500 iterations each; (a) traces, (b) running means.
p = lambda x: 0.3*phi(x, -2, .5)+0.7*phi(x, 2, 1)
def mh(x0, s, N, seed):
    rng = np.random.default_rng(seed); x = x0; px = p(x); out = np.empty(N)
    z = rng.standard_normal(N)*s; u = rng.random(N)
    for t in range(N):
        y = x+z[t]; py = p(y)
        if u[t]*px < py: x, px = y, py
        out[t] = x
    return out
N = 500; starts = [-4.0, -1.0, 1.0, 4.0]; cols = [YELLOW, GREEN, BLUE, PURPLE]
runs = [mh(x0, .5, N, k) for k, x0 in enumerate(starts)]
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.09, right=.98, bottom=.3, top=.96, wspace=.3)
t = np.arange(1, N+1)
for r, c in zip(runs, cols):
    a1.plot(t, r, color=c, lw=.8)
    a2.plot(t, np.cumsum(r)/t, color=c, lw=1.3)
a2.axhline(.8, color=RED, lw=1.1)
a1.set_xlim(0, N); a1.set_ylim(-5, 6); a2.set_xlim(0, N); a2.set_ylim(-4.2, 4.5)
axlab(a1, '迭代步数', '状态'); axlab(a2, '迭代步数', '运行均值')
lab(a2, 300, 1.05, r'$I=0.8$', RED)
tags(fig, axs)
pooled = np.concatenate(runs)
facts = {'final_means': [float(r.mean()) for r in runs], 'frac_left': [float((r < 0).mean()) for r in runs],
         'pooled_mean': float(pooled.mean()), 'between_sd': float(np.std([r.mean() for r in runs], ddof=1))}
save(fig, HERE, 'figure', facts); print(facts)
