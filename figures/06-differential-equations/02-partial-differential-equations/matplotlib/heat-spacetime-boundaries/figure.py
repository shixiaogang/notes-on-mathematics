from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Space-time temperature of the tent bump for Dirichlet and Neumann ends.
fig, axes = figure(width_mm=112, height_mm=58, ncols=2, sharey=True)
panel(fig, left=.085, right=.895, wspace=.1, bottom=.24, top=.97)
tt = np.linspace(0, .25, 121); xx = np.linspace(0, 1, 241)
for ax, u in zip(axes, (uD, uN)):
    Z = np.array([u(xx, t) for t in tt]); im = ax.imshow(Z, origin='lower', aspect='auto', extent=[0, 1, 0, .25], cmap=FIELD, vmin=0, vmax=.5, interpolation='bilinear')
    ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); axlab(ax); ax.set_yticks([0, .1, .2])
    for s in ax.spines.values(): s.set_visible(False)
axes[0].set_ylabel('$t$', labelpad=1)
axes[0].plot([0, 0], [0, .25], color=RED, lw=2.4, clip_on=False); axes[0].plot([1, 1], [0, .25], color=RED, lw=2.4, clip_on=False)
axes[1].plot([0, 0], [0, .25], color=STROKE, lw=1.2, ls=DASH, clip_on=False); axes[1].plot([1, 1], [0, .25], color=STROKE, lw=1.2, ls=DASH, clip_on=False)
cax = fig.add_axes([.915, .24, .02, .73]); cb = fig.colorbar(im, cax=cax); cb.set_ticks([0, .25, .5]); cb.set_ticklabels(['0', '0.25', '0.5']); cb.outline.set_visible(False); cb.ax.tick_params(length=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'color': '0 to 0.5'})
