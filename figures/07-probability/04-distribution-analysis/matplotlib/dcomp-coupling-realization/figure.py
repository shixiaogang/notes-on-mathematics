from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Two couplings of N(0,1) with itself; 300 simulated pairs, seed 717.
# (a) independent copies (X, X'): E|X-X'|^2 = 2 (empirical value recorded).
# (b) identity coupling (X, X): cost 0 = W_2^2. Diagonal y=x drawn in grey.
rng = np.random.default_rng(SEED)
n = 300
X = rng.standard_normal(n); Xp = rng.standard_normal(n)
fig, axs = figure(width_mm=100, height_mm=52, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.27, wspace=.35)
for ax, Y in zip(axs, (Xp, X)):
    ax.plot([-3.2, 3.2], [-3.2, 3.2], color=STROKE, lw=.85, ls=DOT)
    ax.plot(X, Y, 'o', ms=1.6, color=GREEN, mew=0)
    ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3.2, 3.2); ax.set_aspect('equal')
    ax.set_xticks([-3, 0, 3]); ax.set_yticks([-3, 0, 3])
axlab(axs[0], '$X$', "$X'$"); axlab(axs[1], '$X$', '$X$')
tags(fig, axs)
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'empirical_mean_sq_diff_indep': float(np.mean((X-Xp)**2))})
