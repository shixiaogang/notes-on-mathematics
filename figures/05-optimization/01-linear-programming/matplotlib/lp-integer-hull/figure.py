from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Integer points of the workshop for raw material 6 (integral vertices) and 7 (a fractional vertex).
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .07, .985, .975, .24, .26)
xl, yl = (-.4, 4.4), (-.4, 4.6)
def points(ax, b):
    for i in range(0, 5):
        for j in range(0, 5):
            if i+j <= b[0] and 2*i+j <= b[1]:
                dot(ax, (i, j), BLUE, ms=3.6, z=5)
a, c = axes
region(a, workshop()); points(a, (4, 6))
for ax in axes: setup(ax, xl, yl, range(0, 5), range(0, 5))
V = workshop((4., 7.))
region(c, V); points(c, (4, 7))
c.fill([3, 3.5, 3], [0, 0, 1], facecolor=RED_FILL, edgecolor=RED, lw=.7, zorder=2)
dot(c, (3.5, 0), RED, ms=5.2)
c.text(3.58, .12, '$(7/2,0)$', fontsize=7.5, color=INK)
c.text(3.14, 1.08, '$(3,1)$', fontsize=7.5, color=INK)
tags(fig, axes)
save(fig, HERE, 'figure', {'a_vertices': workshop().tolist(), 'b_vertices': V.tolist()})
