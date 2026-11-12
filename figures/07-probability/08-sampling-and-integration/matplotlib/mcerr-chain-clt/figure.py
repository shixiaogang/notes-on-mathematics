from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# (a) Two-state chain, P(0->1) = 0.1, P(1->0) = 0.2, started at state 0, f = indicator of state 1, I = 1/3.
#     Histogram of sqrt(N)(hat I_N - 1/3), N = 2000, 20000 independent chains (seed 3124, green);
#     N(0, 34/27) long-run variance (blue); N(0, 2/9) variance of a single value (yellow).
# (b) Reducible chain with state (W, X): W in {1, 3} chosen once with probability 1/2 each and never changed,
#     X(t) = W * eps_t with eps_t iid N(0,1).  gamma_k = 0 for k >= 1, long-run variance E W^2 = 5.
#     sqrt(N) * mean = W * Z exactly; histogram of 20000 draws (seed 3125, green) vs N(0,5) (blue).
N, R = 2000, 20000
rng = np.random.default_rng(3124)
s = np.zeros(R, dtype=np.int8); tot = np.zeros(R)
for t in range(N):
    u = rng.random(R)
    s = np.where(s == 0, (u < .1).astype(np.int8), (u >= .2).astype(np.int8))
    tot += s
z = np.sqrt(N)*(tot/N - 1/3)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.31, top=.95, wspace=.28)
bins = np.linspace(-4, 4, 41); h, e = np.histogram(z, bins=bins, density=True)
a.bar(e[:-1], h, width=e[1]-e[0], align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.5)
g = np.linspace(-4, 4, 300); a.plot(g, npdf(g, 0, 34/27), color=BLUE, lw=1.3); a.plot(g, npdf(g, 0, 2/9), color=YELLOW, lw=1.4)
a.set_xlim(-4, 4); a.set_ylim(0, .9); a.set_xticks([-4, 0, 4]); a.set_yticks([0, .4, .8]); axlab(a, r'$\sqrt{N}(\hat I_N-I)$')
rng2 = np.random.default_rng(3125); w = np.where(rng2.random(R) < .5, 1.0, 3.0); y = w*rng2.standard_normal(R)
bins = np.linspace(-9, 9, 46); h2, e2 = np.histogram(y, bins=bins, density=True)
b.bar(e2[:-1], h2, width=e2[1]-e2[0], align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.5)
g = np.linspace(-9, 9, 400); b.plot(g, npdf(g, 0, 5), color=BLUE, lw=1.3)
b.set_xlim(-9, 9); b.set_ylim(0, .3); b.set_xticks([-8, 0, 8]); b.set_yticks([0, .1, .2]); axlab(b, r'$\sqrt{N}\,\bar X_N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'var_z': float(z.var()), 'theory': 34/27, 'mean_z': float(z.mean()), 'var_y': float(y.var())})
