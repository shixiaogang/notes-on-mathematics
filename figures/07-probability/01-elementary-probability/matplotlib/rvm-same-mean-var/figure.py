from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Three tables with mean 2 and variance 5: reward table {0,3,6}; {1,7} w.p. 5/6,1/6; {-3,3} w.p. 1/6,5/6.
tabs = [(XV, PV), (np.array([1., 7.]), np.array([5/6, 1/6])), (np.array([-3., 3.]), np.array([1/6, 5/6]))]
fig, axes = figure(width_mm=112, height_mm=42, ncols=3, sharey=True)
panel(fig, left=.08, right=.99, bottom=.32, wspace=.12)
facts = []
for ax, (xs, ps) in zip(axes, tabs):
    m, v, g, k = moments(xs, ps); facts.append([m, v, g, k])
    bars(ax, xs, ps, width=.7)
    ax.axvline(m, color=RED, lw=1.2)
    for t in (m-np.sqrt(v), m+np.sqrt(v)):
        ax.axvline(t, color=PURPLE, lw=.9, ls=DASH)
    ax.text(.98, .97, f'偏度 {g:.2f}', transform=ax.transAxes, ha='right', va='top', fontsize=7.5, color=INK)
    ax.set_xlim(-4, 8); ax.set_ylim(0, 1.0); ax.set_xticks([-3, 0, 2, 4, 7]); ax.set_yticks([0, .5, 1])
    axlab(ax, '$x$')
axes[0].set_ylabel('$p_X(x)$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'mean var skew kurt': facts})
print(facts)
