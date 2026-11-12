from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Running maximum M_n = max(U_1..U_n) of i.i.d. Unif(0,1); error E_n = 1 - M_n, threshold eps = 0.1.
# (a) five sample paths n -> 1 - M_n(omega), n <= 40 (seed 7).
# (b) N_eps(omega) = last n with 1 - M_n > eps (N = T - 1, T = first n with U_n > 0.9 ~ Geom(0.1));
#     histogram of 4000 simulated paths (seed 11) vs exact P(N = m) = 0.9^m * 0.1.
EPS = .1
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.3)
ax = axes[0]; style(ax)
rng = np.random.default_rng(7); n = np.arange(1, 41)
cols = [GREEN]*5
last = []
for i in range(5):
    u = rng.random(40); e = 1 - np.maximum.accumulate(u)
    ax.step(n, e, where='post', color=GREEN, lw=1.0)
    idx = np.nonzero(e > EPS)[0]
    last.append(int(idx[-1]) + 1 if len(idx) else 0)
    if len(idx) and idx[-1] + 1 < 40:
        dot(ax, idx[-1] + 2, e[idx[-1] + 1], ms=3.6)
ax.axhline(EPS, color=RED, lw=1.1, ls=DASH)
lab(ax, 41, EPS + .02, r'$\varepsilon=0.1$', RED, ha='right', va='bottom')
ax.set_xlim(1, 40); ax.set_ylim(0, 1); ax.set_xticks([1, 10, 20, 30, 40])
axlab(ax, '$n$', r'$1-M_n(\omega)$')
ax = axes[1]; style(ax)
rng = np.random.default_rng(11); R = 4000
u = rng.random((R, 200)); hit = u > 1 - EPS
T = hit.argmax(axis=1) + 1; N = T - 1
m = np.arange(0, 41)
freq = np.array([(N == k).mean() for k in m])
ax.bar(m, freq, width=.8, color=GREEN_FILL, edgecolor=GREEN, linewidth=.6)
ax.plot(m, .9**m*.1, color=BLUE, lw=1.4)
ax.set_xlim(-1, 40); ax.set_ylim(0, .115); ax.set_xticks([0, 10, 20, 30, 40])
axlab(ax, r'$m$', 'ℙ$(N_{\\varepsilon}=m)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'last_exceed_indices_panel_a': last, 'mean_N_sim': float(N.mean()), 'mean_N_exact': 9.0, 'R': R})
