from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Bern(1/2) marginals with three couplings: independent, Y=X, Y=1-X; joint tables and law of X+Y.
from matplotlib.colors import LinearSegmentedColormap
CM = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE])
tabs = [np.array([[.25, .25], [.25, .25]]), np.array([[.5, 0], [0, .5]]), np.array([[0, .5], [.5, 0]])]
names = ['1/4', '1/2', '0']
fig = None
fig, axs = figure(width_mm=112, height_mm=70, nrows=2, ncols=3)
panel(fig, left=.1, right=.98, bottom=.16, top=.97, wspace=.45, hspace=.42)
out = []
for j, T in enumerate(tabs):
    ax = axs[0, j]
    ax.imshow(T, cmap=CM, vmin=0, vmax=.6, origin='lower', extent=(-.5, 1.5, -.5, 1.5))
    for x in (0, 1):
        for y in (0, 1):
            v = T[y, x]; s = {0: '0', .25: '1/4', .5: '1/2'}[v]
            ax.text(x, y, s, ha='center', va='center', fontsize=7.5, color=INK)
    for k in (-.5, .5, 1.5):
        ax.plot([-.5, 1.5], [k, k], color=STROKE, lw=.5); ax.plot([k, k], [-.5, 1.5], color=STROKE, lw=.5)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.tick_params(length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=0)
    ax = axs[1, j]
    p = np.array([T[0, 0], T[0, 1]+T[1, 0], T[1, 1]]); out.append(p.tolist())
    bars(ax, [0, 1, 2], p, w=.6)
    ax.set_xticks([0, 1, 2]); ax.set_ylim(0, 1.05); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x+y$', labelpad=0)
tags(fig, axs[1], y=.01)
save(fig, HERE, 'figure', {'sum_laws': out})
