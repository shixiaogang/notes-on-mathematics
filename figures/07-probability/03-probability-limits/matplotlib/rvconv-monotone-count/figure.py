from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Counting variable N_n = sum_{k<=n} 1{U < 1/k} = min(n, ceil(1/U) - 1), increasing in n to N = ceil(1/U) - 1 (finite for U > 0).
# (a) N_n as a function of U for n = 2, 5, 20 and the limit N (blue).  (b) E N_n = H_n = sum_{k<=n} 1/k (blue) -> infinity.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.3)
ax = axes[0]; style(ax)
u = np.linspace(1e-4, 1, 20000, endpoint=False)
lim = np.ceil(1/u) - 1
ax.plot(u, lim, color=BLUE, lw=1.4, drawstyle='steps-post')
for n, c in ((20, GREEN), (5, PURPLE), (2, YELLOW)):
    ax.plot(u, np.minimum(n, lim), color=c, lw=1.2, drawstyle='steps-post')
lab(ax, .1, 21, r'$n=20$', GREEN, ha='left', va='bottom')
lab(ax, .93, 5.5, r'$n=5$', PURPLE, ha='right', va='bottom')
lab(ax, .93, 2.5, r'$n=2$', YELLOW, ha='right', va='bottom')
lab(ax, .06, 31, r'$N$', BLUE, ha='left', va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 34); ax.set_xticks([0, .5, 1])
axlab(ax, '$U$', r'$N_n$')
ax = axes[1]; style(ax)
n = np.arange(1, 201); H = np.cumsum(1/n)
ax.semilogx(n, H, color=BLUE, lw=1.4)
lab(ax, 60, H[59] - .9, r'$H_n$', BLUE, ha='left', va='top')
ax.set_xlim(1, 200); ax.set_ylim(0, 6.5)
logticks(ax, [0, 1, 2], axis='x')
axlab(ax, '$n$', r'$\mathrm{E}N_n$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E_N_n': 'H_n', 'H_5': float(H[4]), 'H_20': float(H[19]), 'H_200': float(H[199])})
