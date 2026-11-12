"""Without replacement vs with replacement, class share q1=0.5, n=4 draws.
(a) pmf of N1: hypergeometric with M=10 (K1=5) and M=40 (K1=20), binomial Bin(4,0.5).
(b) variance ratio (M-n)/(M-1) of hypergeometric to multinomial counts for
M=10 and M=40, against the sampling fraction n/M; reference line 1-n/M."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

n = 4
def hyp1(k, M):
    K1 = M//2
    return math.comb(K1, k)*math.comb(M-K1, n-k)/math.comb(M, n)
ks = np.arange(n+1)
h10 = np.array([hyp1(k, 10) for k in ks]); h40 = np.array([hyp1(k, 40) for k in ks])
b = np.array([math.comb(n, k)*.5**n for k in ks])
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, top=.95, bottom=.3, wspace=.32)
ax = axes[0]; style(ax)
ax.bar(ks-.22, h10, width=.4, color=BLUE_FILL, edgecolor=BLUE, lw=.9)
ax.plot(ks+.05, h40, 'o', ms=3.6, color=PURPLE, zorder=5)
ax.plot(ks+.22, b, 's', ms=3.4, color=YELLOW, zorder=5)
lab(ax, 2.5, .47, '$M=10$', BLUE, ha='left')
lab(ax, 2.5, .41, '$M=40$', PURPLE, ha='left')
lab(ax, 2.5, .35, r'$\mathrm{Bin}(4,0.5)$', YELLOW, ha='left')
ax.set_xticks(ks); ax.set_ylim(0, .52); ax.set_yticks([0, .2, .4])
axlab(ax, '$k$', r'$\mathrm{P}(N_1=k)$')
ax = axes[1]; style(ax)
f = np.linspace(0, 1, 200)
ax.plot(f, 1-f, color=PURPLE, lw=1.0, ls=DASH)
for M, c, mk in ((10, BLUE, 'o'), (40, PURPLE, '.')):
    nn = np.arange(1, M+1)
    ax.plot(nn/M, (M-nn)/(M-1), mk, ms=3.4 if mk == 'o' else 3.0, color=c, zorder=5)
dot(ax, .4, 6/9)
lab(ax, .43, .7, '$n=4,\\ M=10$', RED, ha='left')
lab(ax, .42, .3, '$1-n/M$', PURPLE, ha='left'); lab(ax, .16, 1.0, '$M=10$', BLUE, ha='left'); lab(ax, .03, .66, '$M=40$', PURPLE, ha='left')
ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.05); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, '$n/M$', r'$(M-n)/(M-1)$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'hyp10': h10.round(4).tolist(), 'hyp40': h40.round(4).tolist(), 'binom': b.tolist()})
