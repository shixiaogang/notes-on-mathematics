from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Splitting a free variable x=x_plus-x_minus: every point on a diagonal gives the same x.
xl, yl = (-.25, 4.3), (-.25, 3.5)
fig, ax = figure(width_mm=72, height_mm=54)
ax.fill([0, 4.3, 4.3, 0], [0, 0, 3.5, 3.5], facecolor=BLUE_FILL, edgecolor='none', zorder=0)
for k in (-2, -1, 0, 2):
    line(ax, (1, -1), k, (0, 4.3), (0, 3.5), color=BLUE, lw=.85, zorder=2)
line(ax, (1, -1), 1, (1, 4.3), (0, 3.5), color=GREEN, lw=1.5, zorder=3)
dot(ax, (1, 0), GREEN, ms=5); dot(ax, (3, 2), GREEN, ms=5); dot(ax, (0, 0), RED, ms=5)
ax.text(1.05, -.02, '', fontsize=7.5)
ax.text(.86, .26, '$(1,0)$', fontsize=7.5, ha='right', color=INK)
ax.text(3.12, 1.82, '$(3,2)$', fontsize=7.5, color=INK)
ax.text(.1, .14, '', fontsize=7.5)
ax.text(3.72, 3.12, '$x=1$', fontsize=7.5, color=INK, ha='left')
ax.text(.8, 3.05, '$x=-2$', fontsize=7.5, color=BLUE, ha='center')
setup(ax, xl, yl, range(0, 5), range(0, 4), '$x^{+}$', '$x^{-}$')
save(fig, HERE, 'figure', {'rule': 'x=x_plus-x_minus; points (1,0),(3,2) both give x=1'})
