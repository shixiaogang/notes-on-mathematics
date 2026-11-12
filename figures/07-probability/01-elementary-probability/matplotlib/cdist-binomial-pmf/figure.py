"""Bin(n,p) mass functions: (a) n=10, p=0.2 with mean and +-1 sd; (b) n=10, p=0.5 and 0.8."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

n = 10
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, sharey=True)
panel(fig, left=.08, bottom=.27, wspace=.12)
k = np.arange(n+1)
ax = axes[0]; style(ax)
pm = binom_pmf(n, .2); m, sd = n*.2, (n*.2*.8)**.5
bars(ax, k, pm, width=.6)
ax.plot([m], [-.012], marker='^', ms=6, color=RED, mew=0, clip_on=False, zorder=6)
ax.plot([m-sd, m+sd], [.36, .36], color=RED, lw=1.2); ax.plot([m-sd]*2, [.35, .37], color=RED, lw=1.2); ax.plot([m+sd]*2, [.35, .37], color=RED, lw=1.2)
lab(ax, m+sd+.25, .355, r'$np\pm\sqrt{np(1-p)}$', RED, va='center')
lab(ax, 2, pm[2]+.008, '0.302', ha='center'); lab(ax, 0, pm[0]+.008, '0.107', ha='center')
ax.set_xlim(-.7, 10.7); ax.set_ylim(0, .4); ax.set_xticks(range(0, 11, 2)); ax.set_yticks([0, .1, .2, .3, .4])
ax.set_xlabel('$k$', labelpad=1); ax.set_ylabel(r'$\mathbb{P}(X=k)$'.replace(r'\mathbb{P}', 'P'), labelpad=1)
ax = axes[1]; style(ax)
w = .38
p5 = binom_pmf(n, .5); p8 = binom_pmf(n, .8)
ax.bar(k-w/2, p5, width=w, color=BLUE_FILL, edgecolor=BLUE, linewidth=.9)
ax.bar(k+w/2, p8, width=w, color=YELLOW_FILL, edgecolor=YELLOW, linewidth=.9)
lab(ax, 5, p5[5]+.01, '$p=0.5$', BLUE, ha='center'); lab(ax, 8.6, p8[8]+.01, '$p=0.8$', YELLOW, ha='center')
ax.set_xlim(-.7, 10.7); ax.set_xticks(range(0, 11, 2)); ax.set_xlabel('$k$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'pmf_p0.2': pm.round(4).tolist(), 'mean': m, 'sd': sd, 'mode': int(np.argmax(pm))})
