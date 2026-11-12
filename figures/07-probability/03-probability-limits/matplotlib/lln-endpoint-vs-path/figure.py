from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Centred fair-die walk S_k = sum_{i<=k} (D_i - 3.5), D_i uniform on {1,...,6}, k <= 100, threshold a = 30.
# 30 displayed paths (seed 11): red = path whose running maximum |S_k| reaches 30 at some k <= 100,
# green = path that stays inside. Probabilities estimated from 200000 paths (seed 12).
# Chebyshev endpoint bound: Var(S_100)/a^2 = 100*(35/12)/900.
rng = np.random.default_rng(11)
n, a0, M = 100, 30, 30
S = np.cumsum(rng.integers(1, 7, size=(M, n))-3.5, axis=1)
S = np.hstack([np.zeros((M, 1)), S]); k = np.arange(n+1)
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, left=.11, right=.86, bottom=.2, top=.95)
ax.axhspan(a0, 60, color=RED_FILL, lw=0); ax.axhspan(-60, -a0, color=RED_FILL, lw=0)
crossed = np.max(np.abs(S), axis=1) >= a0
for s, c in zip(S, crossed):
    if not c: ax.plot(k, s, color=GREEN, lw=.7)
for s, c in zip(S, crossed):
    if c: ax.plot(k, s, color=RED, lw=1.1)
sd = np.sqrt(35/12*k)
ax.plot(k, 2*sd, color=PURPLE, lw=1.1, ls=DASH); ax.plot(k, -2*sd, color=PURPLE, lw=1.1, ls=DASH)
ax.axhline(a0, color=RED, lw=.8); ax.axhline(-a0, color=RED, lw=.8)
lab(ax, 101.5, 30, '$a=30$', RED, va='center'); lab(ax, 101.5, -30, '$-a$', RED, va='center')
lab(ax, 3, 41, r'$\pm2\sqrt{\operatorname{Var}(S_k)}$', PURPLE, va='center')
ax.set_xlim(0, 100); ax.set_ylim(-50, 50); ax.set_xticks([0, 25, 50, 75, 100])
axlab(ax, '$k$', '$S_k$')
rng2 = np.random.default_rng(12)
B = np.cumsum(rng2.integers(1, 7, size=(200000, n))-3.5, axis=1)
p_end = float(np.mean(np.abs(B[:, -1]) >= a0)); p_max = float(np.mean(np.max(np.abs(B), axis=1) >= a0))
save(fig, HERE, 'figure', {'seed_display': 11, 'crossed_display': int(crossed.sum()),
     'end_inside_but_crossed_display': int(np.sum(crossed & (np.abs(S[:, -1]) < a0))),
     'P_end': p_end, 'P_max': p_max, 'chebyshev': 100*35/12/900, 'MC_paths': 200000, 'seed_MC': 12})
