from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Two-sided tails P(|X|>=k) of laws with mean 0 and variance 1, against Chebyshev min(1,1/k^2).
k = np.linspace(0, 4, 801)
fig, ax = figure(width_mm=96, height_mm=54)
ax.plot(k, np.minimum(1, 1/np.maximum(k, 1e-9)**2), color=PURPLE, lw=1.4)
ax.plot(k, np.maximum(0, 1-k/np.sqrt(3)), color=GREEN, lw=1.4)
ax.plot(k, 2*Q(k), color=BLUE, lw=1.4)
ax.plot(k, np.exp(-np.sqrt(2)*k), color=YELLOW, lw=1.6)
ax.plot([0, 1], [1, 1], color=RED, lw=1.4); ax.plot([1, 4], [0, 0], color=RED, lw=1.4)
ax.plot([1], [1], 'o', ms=3.4, color=RED, mew=0); ax.plot([1], [0], 'o', ms=3.4, mfc='white', mec=RED, mew=.8)
lab(ax, 2.05, .3, r'$1/k^2$', PURPLE, ha='left')
lab(ax, .9, .56, '均匀', GREEN, ha='right'); lab(ax, 1.15, .44, '高斯', BLUE, ha='left'); lab(ax, .5, .35, 'Laplace', YELLOW, ha='right')
lab(ax, .5, .95, r'$\pm1$', RED, ha='center', va='top')
ax.set_xlim(0, 4); ax.set_ylim(-.02, 1.05); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, .25, .5, .75, 1])
axlab(ax, '$k$', 'ℙ$(|X|\\geq k)$')
save(fig, HERE, 'figure', {'k=2': {'chebyshev': .25, 'uniform': float(max(0, 1-2/np.sqrt(3))), 'normal': float(2*Q(2)), 'laplace': float(np.exp(-2*np.sqrt(2))), 'two_point': 0.0}})
