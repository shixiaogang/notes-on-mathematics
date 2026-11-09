from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Dominance quadrants around B and the six candidates.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .2, .22)
xl, yl = (0, 8), (0, 9.5)
ax = axes[0]; setup(ax, xl, yl, range(0, 9, 2), range(0, 10, 2))
b = CANDS['B']
ax.fill([0, b[0], b[0], 0], [0, 0, b[1], b[1]], color=GREEN_FILL, lw=0, zorder=1)
ax.fill([b[0], 8, 8, b[0]], [b[1], b[1], 9.5, 9.5], color=RED_FILL, lw=0, zorder=1)
ax.plot([0, 8], [b[1]]*2, color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2); ax.plot([b[0]]*2, [0, 9.5], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
dot(ax, b); ax.text(2.2, 4.3, 'B', color=INK)
ax.text(1, 2.1, '支配B', ha='center', color=INK, fontsize=7.5); ax.text(5.1, 7.2, '被B支配', ha='center', color=INK, fontsize=7.5)
ax.text(1, 7.2, '不可比', ha='center', color=MUTED, fontsize=7.5); ax.text(5.1, 2.1, '不可比', ha='center', color=MUTED, fontsize=7.5)
ax = axes[1]; setup(ax, xl, yl, range(0, 9, 2), range(0, 10, 2))
for k, c in (('B', RED_FILL), ('D', YELLOW_FILL)):
    p = CANDS[k]; ax.fill([p[0], 8, 8, p[0]], [p[1], p[1], 9.5, 9.5], color=c, lw=0, zorder=1)
p = CANDS['B']; ax.fill([p[0], 8, 8, p[0]], [p[1], p[1], 9.5, 9.5], color=RED_FILL, lw=0, zorder=1.1)
cands(ax, off={'F': (.05, .3), 'D': (-.45, .3), 'E': (.15, .25)})
tags(fig, axes)
save(fig, HERE, 'figure', {'candidates': CANDS})
