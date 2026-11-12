from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Blahut-Arimoto on a channel with a useless third input: W rows (1,0), (0,1), (1/2,1/2); C = 1 bit at q = (1/2,1/2,0).
# (a) from the uniform start, q^(t)(2) = 1/(2^{t+1}+1) decays geometrically but never reaches 0 (log scale).
# (b) the gap C - L_t (green) and the guarantee log2(3)/(t+1) (purple); the upper bound U_t equals C = 1 from t = 0.
W = np.array([[1., 0.], [0., 1.], [.5, .5]]); T = 14
R = ba(W, np.ones(3)/3, T); t = np.arange(T)
q2 = np.array([r[0][2] for r in R]); L = np.array([r[3] for r in R]); U = np.array([r[4] for r in R])
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, top=.95, bottom=.27, wspace=.36)
ax = axs[0]
ax.plot(t, q2, 'o-', color=GREEN, lw=1.1, ms=3, mew=0); ax.set_yscale('log'); logticks(ax, [-4, -3, -2, -1, 0]); ax.set_ylim(5e-5, 1)
ax.set_xlabel(r'$t$', labelpad=1); ax.set_ylabel(r'$q^{(t)}(2)$', labelpad=1)
ax = axs[1]
ax.plot(t, 1-L, 'o-', color=GREEN, lw=1.1, ms=3, mew=0); ax.plot(t, np.log2(3)/(t+1), color=PURPLE, lw=1.1)
ax.set_yscale('log'); logticks(ax, [-4, -3, -2, -1, 0]); ax.set_ylim(5e-5, 2)
lab(ax, 6.5, .35, r'$\log_2 3/(t+1)$', PURPLE); lab(ax, 5, 1.5e-3, r'$C-L_t$', GREEN)
ax.set_xlabel(r'$t$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'q2': [float(v) for v in q2[:5]], 'gap': [float(1-v) for v in L[:5]], 'U': [float(v) for v in U[:3]]})
