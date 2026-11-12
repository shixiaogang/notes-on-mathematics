"""Hypergeometric Hyp(20,4,10) vs Bin(10,0.2); finite population correction (N-n)/(N-1)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

N, K, n = 20, 4, 10
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.34)
ax = axes[0]; style(ax)
k = np.arange(7); w = .38
h = hyper_pmf(N, K, n)[:7]; b = binom_pmf(n, K/N)[:7]
ax.bar(k-w/2, h, width=w, color=BLUE_FILL, edgecolor=BLUE, linewidth=.9)
ax.bar(k+w/2, b, width=w, color=YELLOW_FILL, edgecolor=YELLOW, linewidth=.9)
lab(ax, 2.6, .405, '不放回', BLUE, ha='left'); lab(ax, 3.2, .23, '放回', YELLOW, ha='left')
ax.set_xlim(-.7, 6.7); ax.set_ylim(0, .45); ax.set_xticks(range(7)); ax.set_yticks([0, .2, .4])
ax.set_xlabel('$k$', labelpad=1); ax.set_ylabel('$P(X=k)$', labelpad=1)
ax = axes[1]; style(ax)
for NN, c, ls in ((20, BLUE, '-'), (200, PURPLE, '--')):
    nn = np.arange(1, NN+1)
    ax.plot(nn/NN, (NN-nn)/(NN-1), color=c, lw=1.4, ls=ls)
ax.plot([0, 1], [1, 0], color=LINE, lw=.85, ls=DOT)
dot(ax, .5, 10/19); lab(ax, .53, 10/19+.03, '10/19', RED)
lab(ax, .08, .25, '$N=20$', BLUE); lab(ax, .08, .14, '$N=200$', PURPLE)
ax.set_xlim(0, 1); ax.set_ylim(0, 1.05); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$n/N$', labelpad=1); ax.set_ylabel('$(N-n)/(N-1)$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'hyper': h.round(4).tolist(), 'binom': b.round(4).tolist(), 'var_hyper': n*.2*.8*(N-n)/(N-1), 'var_binom': 1.6})
