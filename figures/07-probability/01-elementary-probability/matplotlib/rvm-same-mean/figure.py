from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Three games with the same mean 2: constant 2 (Var 0), {1,3} each 1/2 (Var 1),
# reward table {0,3,6} (Var 5). Red bar: mean; dashed purple: mean +/- standard deviation.
games = [([2.], [1.]), ([1., 3.], [.5, .5]), (list(XV), list(PV))]
fig, axes = figure(width_mm=112, height_mm=42, ncols=3, sharey=True)
panel(fig, left=.08, right=.99, bottom=.32, wspace=.12)
facts = {}
for ax, (xs, ps), name in zip(axes, games, 'ABC'):
    m, v, _, _ = moments(xs, ps) if len(xs) > 1 else (2., 0., 0, 0)
    bars(ax, xs, ps, width=.6)
    ax.axvline(m, color=RED, lw=1.2, zorder=4)
    if v > 0:
        s = np.sqrt(v)
        for t in (m-s, m+s):
            ax.axvline(t, color=PURPLE, lw=.9, ls=DASH, zorder=3)
    lab(ax, 6.6, 1.0, f'方差 {v:g}', INK, ha='right', va='top')
    ax.set_xlim(-1, 7); ax.set_ylim(0, 1.05); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, .5, 1])
    axlab(ax, '$x$')
    facts[name] = [m, v]
axes[0].set_ylabel('$p_X(x)$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', facts)
