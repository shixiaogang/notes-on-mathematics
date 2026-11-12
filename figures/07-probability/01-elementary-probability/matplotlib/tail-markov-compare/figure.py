from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Markov bound vs exact tails. (a) X ~ Exp(1): e^{-t} vs min(1,1/t). (b) X ~ Bin(20,1/2): P(X>=k) vs min(1,10/k).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.34, bottom=.28)
ax = axes[0]; t = np.linspace(.05, 10, 800)
ax.semilogy(t, np.exp(-t), color=BLUE, lw=1.4)
ax.semilogy(t, np.minimum(1, 1/t), color=PURPLE, lw=1.4)
lab(ax, 6.2, 1/6.2*1.35, r'$\min\{1,1/t\}$', PURPLE, ha='center', va='bottom')
lab(ax, 4.5, np.exp(-4.5)*.5, r'$\mathrm{e}^{-t}$', BLUE, ha='right', va='top')
ax.set_xlim(0, 10); ax.set_ylim(1e-4, 1.5); logticks(ax, [0, -1, -2, -3, -4]); axlab(ax, '$t$', 'ℙ$(X\\geq t)$')
ax = axes[1]; k = np.arange(10, 21)
ex = np.array([bin_tail(int(j)) for j in k])
ax.semilogy(k, ex, 'o', color=BLUE, ms=3.6, mew=0)
kk = np.linspace(10, 20, 200)
ax.semilogy(kk, 10/kk, color=PURPLE, lw=1.4)
ax.plot([15], [bin_tail(15)], 'o', ms=5, mfc='none', mec=RED, mew=1.1)
ax.plot([15], [10/15], 'o', ms=4, color=RED, mew=0)
lab(ax, 15.4, 10/15*1.2, '$2/3$', RED, va='bottom'); lab(ax, 15.5, bin_tail(15), '$0.0207$', RED, va='center')
lab(ax, 18, 10/18*1.4, r'$10/k$', PURPLE, ha='center', va='bottom')
ax.set_xlim(9.5, 20.5); ax.set_ylim(5e-7, 1.5); logticks(ax, [0, -2, -4, -6]); ax.set_xticks([10, 12, 14, 16, 18, 20]); axlab(ax, '$k$', 'ℙ$(X\\geq k)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'binomial_exact_15': bin_tail(15), 'markov_15': 10/15})
