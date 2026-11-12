"""(a) Poisson(lambda) mass functions; (b) Bin(n,2/n) for n=10,100 against Poisson(2)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
for lam, c, mk in ((.5, YELLOW, 's'), (2, BLUE, 'o'), (6, PURPLE, 'D')):
    k = np.arange(0, 15); pm = poisson_pmf(lam, 14)
    ax.vlines(k, 0, pm, color=c, lw=.9); ax.plot(k, pm, mk, color=c, ms=2.8)
lab(ax, 1.0, .58, r'$\lambda=0.5$', YELLOW); lab(ax, 2.6, .29, r'$\lambda=2$', BLUE); lab(ax, 7.3, .18, r'$\lambda=6$', PURPLE)
ax.set_xlim(-.5, 14.5); ax.set_ylim(0, .65); ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14]); ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel('$k$', labelpad=1); ax.set_ylabel('$P(N=k)$', labelpad=1)
ax = axes[1]; style(ax)
k = np.arange(0, 9)
po = poisson_pmf(2, 8)
bars(ax, k, po, width=.62)
for n, c, mk in ((10, YELLOW, 's'), (100, GREEN, 'o')):
    ax.plot(k, binom_pmf(n, 2/n)[:9], mk, color=c, ms=3.6, mec=c, mfc='white' if n == 10 else c, mew=1)
lab(ax, 3.1, .29, '$n=10$', YELLOW); lab(ax, 3.1, .25, '$n=100$', GREEN)
ax.set_xlim(-.6, 8.6); ax.set_ylim(0, .33); ax.set_xticks(range(9)); ax.set_yticks([0, .1, .2, .3])
ax.set_xlabel('$k$', labelpad=1)
tags(fig, axes)
d = {n: float(np.max(np.abs(binom_pmf(n, 2/n)[:9]-po))) for n in (10, 100, 1000)}
save(fig, here(__file__), 'figure', {'poisson2': po.round(4).tolist(), 'max_abs_diff_first9': d})
