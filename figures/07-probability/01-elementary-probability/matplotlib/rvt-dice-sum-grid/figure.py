from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Two fair dice: 36 equally likely cells, anti-diagonals x1+x2=s, and the mass function of S.
from matplotlib.patches import Rectangle
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.98, bottom=.25, top=.95, wspace=.28)
ax = axes[0]
for a in range(1, 7):
    for b in range(1, 7):
        on = a+b == 7
        ax.add_patch(Rectangle((a-.45, b-.45), .9, .9, fc=BLUE_FILL if on else 'none', ec=BLUE if on else STROKE, lw=.8 if on else .5))
for s in range(2, 13):
    a0, a1 = max(1, s-6), min(6, s-1)
    ax.plot([a0, a1], [s-a0, s-a1], color=MUTED, lw=.55, zorder=3)
for s in (7, 12):
    lab(ax, 6.55, s-6, f'$s={s}$', MUTED, ha='left', va='center')
ax.set_xlim(.4, 7.4); ax.set_ylim(.4, 6.6); ax.set_aspect('equal')
ax.set_xticks(range(1, 7)); ax.set_yticks(range(1, 7)); axlab(ax, '$x_1$', '$x_2$')
ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False); ax.tick_params(length=0)
ax = axes[1]
s = np.arange(2, 13); p = (6-np.abs(s-7))/36
bars(ax, s, p)
ax.bar([7], [p[5]], width=.7, color=BLUE_FILL, edgecolor=BLUE, linewidth=1.4)
lab(ax, 7, p[5]+.006, '$6/36$', INK, ha='center', va='bottom')
ax.set_xticks(s); ax.set_ylim(0, .2); ax.set_yticks([0, .05, .1, .15]); axlab(ax, '$s$', '概率')
tags(fig, axes)
save(fig, HERE, 'figure', {'masses': [round(x*36) for x in p], 'total': float(p.sum())})
