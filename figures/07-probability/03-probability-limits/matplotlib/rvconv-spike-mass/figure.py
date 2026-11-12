from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Distribution of Y_n = n 1{U < 1/n}: mass 1 - 1/n at 0 and 1/n at n; mean n * (1/n) = 1 for every n.
# Stems for n = 2, 5, 10 (slightly offset at 0 for readability); upper axis tick marks the mean 1.
fig, ax = figure(width_mm=86, height_mm=46)
fig.set_layout_engine(None); fig.subplots_adjust(left=.11, right=.97, top=.95, bottom=.2)
style(ax)
for n, c, off in ((2, BLUE, -.18), (5, YELLOW, 0), (10, PURPLE, .18)):
    ax.vlines([off], 0, 1 - 1/n, color=c, lw=2.2)
    ax.vlines([n], 0, 1/n, color=c, lw=2.2)
    ax.plot([off, n], [1 - 1/n, 1/n], 'o', color=c, ms=3.4, mew=0)
    lab(ax, n, 1/n + .04, r'$1/%d$' % n, c, ha='center', va='bottom')
ax.plot([1], [0], '^', color=RED, ms=5, mew=0, clip_on=False, zorder=7)
lab(ax, 1.25, .05, r'$\mathrm{E}Y_n=1$', RED, ha='left', va='bottom')
ax.set_xlim(-.8, 11); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 5, 10])
axlab(ax, '$y$', 'ℙ$(Y_n=y)$')
save(fig, HERE, 'figure', {'atoms': {n: [[0, 1 - 1/n], [n, 1/n]] for n in (2, 5, 10)}, 'mean': 1})
