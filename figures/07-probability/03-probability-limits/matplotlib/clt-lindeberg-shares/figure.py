from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
from lindeberg import terms
# Row n = 20, eps = 0.5. Each bar is the normalized variance sigma_{n,k}^2 / s_n^2 of one term,
# split into the part from |X| <= eps s_n (blue) and from |X| > eps s_n (red).
# The red total is the Lindeberg ratio L_n(eps). Arrays A, B, C as in lindeberg.py.
n, eps = 20, .5
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.11, right=.98, bottom=.3, wspace=.3)
facts = {}
for ax, kind, ymax in zip(axs, 'ABC', (.13, .55, .065)):
    var, tail, s = terms(kind, n, eps)
    k = np.arange(1, n+1)
    inner = (var-tail)/s**2; outer = tail/s**2
    ax.bar(k, inner, width=.72, color=BLUE_FILL, edgecolor=BLUE, lw=.6)
    ax.bar(k, outer, width=.72, bottom=inner, color=RED_FILL, edgecolor=RED, lw=.6)
    ax.set_xlim(.3, n+.7); ax.set_ylim(0, ymax); ax.set_xticks([1, 10, 20])
    axlab(ax, '$k$', None)
    facts[kind] = {'L_n': float(outer.sum()), 'max_share': float((var/s**2).max())}
axs[0].set_ylabel(r'$\sigma_{n,k}^2/s_n^2$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
