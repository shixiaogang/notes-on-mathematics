from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Slack variables of the workshop at the point (1,1): x3=4-x1-x2, x4=6-2x1-x2.
xl, yl = (-.4, 5.1), (-.4, 6.5)
fig, ax = figure(width_mm=88, height_mm=62)
region(ax, workshop())
line(ax, WS_A[0], 4, xl, yl, lw=1.3); line(ax, WS_A[1], 6, xl, yl, lw=1.3)
line(ax, WS_A[0], 2, xl, yl, color=MUTED, ls=(0, (1.5, 1.5)), lw=.85)
line(ax, WS_A[1], 3, xl, yl, color=MUTED, ls=(0, (1.5, 1.5)), lw=.85)
x = np.array([1., 1.])
dot(ax, x, GREEN, ms=5)
ax.text(1.12, 1.1, '$(1,1)$', color=INK, fontsize=7.5, zorder=7)
ax.text(4.0, .62, '工时', color=INK, fontsize=7.5); ax.text(4.0, .17, '$x_3=0$', color=INK, fontsize=7.5)
ax.text(1.62, 3.72, '原料', color=INK, fontsize=7.5); ax.text(1.62, 3.25, '$x_4=0$', color=INK, fontsize=7.5)
ax.text(.14, 2.9, '$x_4=3$', color=MUTED, fontsize=7.5, ha='left')
ax.text(1.74, .36, '$x_3=2$', color=MUTED, fontsize=7.5, ha='left')
setup(ax, xl, yl, range(0, 6), range(0, 7))
save(fig, HERE, 'figure', {'point': '(1,1)', 'x3': 4-x.sum(), 'x4': 6-2*x[0]-x[1]})
