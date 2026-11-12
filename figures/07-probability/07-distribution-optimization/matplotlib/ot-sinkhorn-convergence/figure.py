from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Sinkhorn on the running example (log domain, f-update then g-update per round).
# After each round the column sums are exact; plotted: (a) row residual ||pi 1 - a||_1,
# (b) regularized gap P_eps(rounded plan) - D_eps(f,g), for eps = 1 (blue), 0.25 (yellow), 0.1 (purple).
a, b, C = A_EX, B_EX, C_EX
T = 60
runs = {}
for eps in (1., .25, .1):
    _, _, h = sinkhorn_log(a, b, C, eps, T, record=True)
    runs[eps] = h
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.98, top=.95, bottom=.28, wspace=.32)
cols = {1.: BLUE, .25: YELLOW, .1: PURPLE}
facts = {}
for eps, h in runs.items():
    t = np.arange(1, T+1)
    r = np.array([d['row_res'] for d in h]); g = np.array([max(d['gap'], 1e-17) for d in h])
    axs[0].semilogy(t, r, color=cols[eps], lw=1.4)
    axs[1].semilogy(t, g, color=cols[eps], lw=1.4)
    facts[str(eps)] = {'row_res_first7': r[:7].tolist(), 'gap_first7': g[:7].tolist(),
                       'rounds_gap_below_1e-4': int(np.argmax(g < 1e-4))+1 if np.any(g < 1e-4) else None}
for ax in axs:
    ax.set_xlabel('轮次', labelpad=1); ax.set_xlim(0, T)
axs[0].set_ylim(1e-12, 1); axs[1].set_ylim(1e-12, 1)
axs[1].axhline(1e-4, color=STROKE, lw=.6, ls=DOT)
axs[0].text(8, 1e-10, '$\\varepsilon=1$', color=BLUE, fontsize=7.5)
axs[0].text(28, 3e-6, '$0.25$', color=YELLOW, fontsize=7.5)
axs[0].text(44, 3e-2, '$0.1$', color=PURPLE, fontsize=7.5)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
