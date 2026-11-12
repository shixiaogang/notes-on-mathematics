"""Random coin, n=10: (a) 400 simulated (U,N) (seed 3, vertical jitter U(-0.15,0.15)), conditional mean 10u (red),
mean +- conditional sd (blue dashed); (b) total variance 10 = within 5/3 + between 25/3."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
n = 10
rng = np.random.default_rng(3)
U = rng.random(400); N = rng.binomial(n, U)
fig, (a, b) = figure(width_mm=104, height_mm=48, ncols=2, gridspec_kw={'width_ratios': [2.2, 1]})
a.scatter(U, N + rng.uniform(-0.15, 0.15, U.size), s=2.5, color=GREEN, lw=0)
u = np.linspace(0, 1, 300); sd = np.sqrt(n*u*(1 - u))
a.plot(u, n*u, color=RED, lw=1.4)
a.plot(u, n*u + sd, color=BLUE, lw=1.0, ls=DASH); a.plot(u, n*u - sd, color=BLUE, lw=1.0, ls=DASH)
a.set_xlim(0, 1); a.set_ylim(-0.6, 10.6); a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 5, 10])
a.set_xlabel('$u$', labelpad=1); a.set_ylabel('$N$', rotation=0)
w, bt = n/6, n**2/12
b.bar([0], [w], width=0.5, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
b.bar([0], [bt], bottom=[w], width=0.5, color=YELLOW_FILL, edgecolor=YELLOW, lw=0.8)
b.text(0.32, w/2, '组内 5/3', va='center', fontsize=7.5)
b.text(0.32, w + bt/2, '组间 25/3', va='center', fontsize=7.5)
b.set_xlim(-0.4, 1.3); b.set_ylim(0, 10.6); b.set_xticks([]); b.set_yticks([0, 5, 10])
b.spines['bottom'].set_visible(False)
b.set_ylabel('方差')

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'n': n, 'seed': 3, 'samples': 400, 'within': w, 'between': bt, 'sample_var_N': float(N.var())})
