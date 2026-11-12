from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Independent events A_n with P(A_n) = p_n; exact probabilities of tail unions (telescoping products).
# (a) p_n = 1/n^2: P(union_{n>=N} A_n) = 1 - prod_{n>=N}(1 - 1/n^2) = 1 - (N-1)/N = 1/N (blue),
#     union bound sum_{n>=N} 1/n^2 (purple); both -> 0.
# (b) p_n = 1/n: P(union_{n=N}^M A_n) = 1 - prod_{n=N}^M (1 - 1/n) = 1 - (N-1)/M -> 1 as M -> infinity, N = 10, 100, 1000.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.32, bottom=.3)
ax = axes[0]; style(ax)
N = np.arange(2, 1001)
tail = np.array([np.sum(1/np.arange(k, 200000)**2) + 1/200000 for k in N])
ax.loglog(N, 1/N, color=BLUE, lw=1.4)
ax.loglog(N, tail, color=PURPLE, lw=1.4, ls=DASH)
lab(ax, 30, 1/30*.62, r'$1/N$', BLUE, ha='left', va='top')
lab(ax, 9, 1/9*1.6, '并集上界', PURPLE, ha='left', va='bottom')
ax.set_xlim(2, 1000); ax.set_ylim(5e-4, 1.2); logticks(ax, [1, 2, 3], axis='x'); logticks(ax, [-3, -2, -1, 0])
axlab(ax, '$N$', '尾段并的概率')
ax = axes[1]; style(ax)
for Nn, c in ((10, BLUE), (100, YELLOW), (1000, PURPLE)):
    M = np.logspace(np.log10(Nn), 6, 300)
    ax.semilogx(M, 1 - (Nn - 1)/M, color=c, lw=1.4)
    lab(ax, 1.35*(Nn - 1), .03, r'$%d$' % Nn, c, ha='left', va='bottom')
ax.set_xlim(10, 1e6); ax.set_ylim(0, 1.05); logticks(ax, [1, 2, 3, 4, 5, 6], axis='x')
axlab(ax, '$M$', '有限段并的概率')
tags(fig, axes)
save(fig, HERE, 'figure', {'a_exact_N10': 0.1, 'a_bound_N10': float(np.sum(1/np.arange(10, 10**6)**2)), 'b_N10_M100': 1 - 9/100})
