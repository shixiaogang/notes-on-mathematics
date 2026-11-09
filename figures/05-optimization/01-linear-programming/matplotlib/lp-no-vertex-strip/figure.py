from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# A strip contains a line and has no vertex; adding x1>=0 creates vertices.
fig, axes = figure(width_mm=112, height_mm=42, ncols=2)
panels(fig, .07, .985, .955, .3, .26)
a, b = axes
xl, yl = (-3.2, 3.2), (-.5, 1.7)
a.fill([-3.2, 3.2, 3.2, -3.2], [0, 0, 1, 1], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
a.plot(xl, [1, 1], color=EDGE, lw=1.0, zorder=2)
a.plot(xl, [0, 0], color=RED, lw=2.0, zorder=3)
dot(a, (0, .5), INK, ms=4.2)
a.annotate('', xy=(1.5, .5), xytext=(-1.5, .5), arrowprops=dict(arrowstyle='<|-|>', color=GREEN, lw=1.2, shrinkA=0, shrinkB=0, mutation_scale=8), zorder=5)
setup(a, xl, yl, range(-3, 4), [0, 1])
b.fill([0, 3.2, 3.2, 0], [0, 0, 1, 1], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
b.plot([0, 0], [0, 1], color=EDGE, lw=1.0, zorder=2); b.plot([0, 3.2], [1, 1], color=EDGE, lw=1.0, zorder=2)
b.plot([0, 3.2], [0, 0], color=RED, lw=2.0, zorder=3)
dot(b, (0, 0), RED, ms=5.2); dot(b, (0, 1), BLUE, ms=4.4)
b.text(.16, .1, '$(0,0)$', fontsize=7.5, color=INK); b.text(.16, 1.12, '$(0,1)$', fontsize=7.5, color=INK)
setup(b, (-.7, 3.2), yl, range(0, 4), [0, 1])
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'strip 0<=x2<=1, min x2 attained on a line, no extreme points', 'b': 'strip with x1>=0, vertices (0,0),(0,1)'})
