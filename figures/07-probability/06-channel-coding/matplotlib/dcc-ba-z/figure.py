from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Blahut-Arimoto on the Z-channel from q^(0) = (1/2, 1/2).
# (a) iterate q^(t)(1) (green) approaching the optimum 0.4 (blue dashed);
# (b) upper bound U_t = max_x D(W_x || p_t) (purple), lower bound L_t = log2 sum_x q_t(x) 2^{D_x} (green) and the
#     capacity log2(5/4) (blue dashed); red line = first round with U_t - L_t <= 0.01.
T = 16; R = ba(Z, np.array([.5, .5]), T); C = np.log2(1.25)
t = np.arange(T); q1 = np.array([r[0][1] for r in R]); L = np.array([r[3] for r in R]); U = np.array([r[4] for r in R])
stop = int(np.argmax(U-L <= .01))
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.13, right=.97, top=.95, bottom=.27, wspace=.4)
ax = axs[0]
ax.plot(t, q1, 'o-', color=GREEN, lw=1.1, ms=3, mew=0); ax.axhline(.4, color=BLUE, lw=1.0, ls=DASH)
lab(ax, 11, .392, r'$0.4$', BLUE, va='top'); ax.set_xlabel(r'$t$', labelpad=1); ax.set_ylabel(r'$q^{(t)}(1)$', labelpad=1); ax.set_ylim(.38, .51)
ax = axs[1]
ax.plot(t, U, 'o-', color=PURPLE, lw=1.1, ms=3, mew=0); ax.plot(t, L, 'o-', color=GREEN, lw=1.1, ms=3, mew=0)
ax.axhline(C, color=BLUE, lw=1.0, ls=DASH); ax.axvline(stop, color=RED, lw=1.0)
lab(ax, 1.2, .385, r'$U_t$', PURPLE); lab(ax, 1.2, .305, r'$L_t$', GREEN); lab(ax, stop+.4, .4, '停止', RED)
ax.set_xlabel(r'$t$', labelpad=1); ax.set_ylim(.30, .42)
tags(fig, axs)
save(fig, HERE, 'figure', {'C': float(C), 'stop_round': stop, 'rounds': [{'t': int(i), 'q1': float(q1[i]), 'L': float(L[i]), 'U': float(U[i])} for i in range(8)]})
