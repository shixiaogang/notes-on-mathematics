from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
from lindeberg import lindeberg_ratio, max_share
# (a) Lindeberg ratio L_n(0.5) and (b) largest normalized variance max_k sigma_{n,k}^2/s_n^2
# against n = 2..200 for arrays A (green), B (yellow), C (red); exact formulas in lindeberg.py.
ns = np.arange(2, 201)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, bottom=.28, wspace=.3)
facts = {}
for kind, c, lw in (('A', GREEN, 1.4), ('B', YELLOW, 1.7), ('C', RED, 1.4)):
    L = [lindeberg_ratio(kind, n, .5) for n in ns]; M = [max_share(kind, n) for n in ns]
    a.plot(ns, L, color=c, lw=lw); b.plot(ns, M, color=c, lw=lw)
    facts[kind] = {'L_20': L[18], 'L_200': L[-1], 'max_200': M[-1]}
for ax in (a, b):
    ax.set_xscale('log'); logticks(ax, [0, 1, 2], 'x'); ax.set_xlim(2, 200); ax.set_ylim(-.02, 1.04)
lab(a, 6, .93, 'C', RED); lab(a, 40, .8, 'B', YELLOW); lab(a, 22, .3, 'A', GREEN)
lab(b, 3, .4, 'C', RED); lab(b, 40, .55, 'B', YELLOW); lab(b, 40, .07, 'A', GREEN)
axlab(a, '$n$', r'$L_n(0.5)$'); axlab(b, '$n$', r'$\max_k\sigma_{n,k}^2/s_n^2$')
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
