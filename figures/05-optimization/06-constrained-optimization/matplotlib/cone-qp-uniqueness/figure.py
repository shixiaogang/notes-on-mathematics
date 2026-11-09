from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Uniqueness: (a) running QP (Q pd). (b) 1/2(x1+x2-2)^2 on x1=x2. (c) 1/2(x1+x2-2)^2 on box [0,1.5]^2.
fig, axes = figure(width_mm=112, height_mm=47, ncols=3)
panels(fig, .055, .995, .985, .235, .22)
a, b, c = axes
xl, yl = (-.15, 2.6), (-.15, 2.2)
a.fill([0, 2, 0], [0, 0, 2], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
X, Y = grid2(xl, yl)
a.contour(X, Y, fls(X, Y), levels=[2.25, 3, 4, 5.5, 7.5], colors=BLUE, linewidths=.7, zorder=2)
dot(a, XSTAR); setup(a, xl, yl, [0, 1, 2], [0, 1, 2])
F = .5*(X+Y-2)**2
b.contour(X, Y, F, levels=[.02, .32, .72, 1.28], colors=BLUE, linewidths=.7, zorder=2)
b.plot([0, 2.2], [0, 2.2], color=BLUE, lw=1.6, zorder=3)
dot(b, (1, 1)); setup(b, xl, yl, [0, 1, 2], [0, 1, 2])
b.text(1.72, 1.34, '$x_1=x_2$', fontsize=7.5, ha='left')
c.fill([0, 1.5, 1.5, 0], [0, 0, 1.5, 1.5], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
c.contour(X, Y, F, levels=[.32, .72, 1.28], colors=BLUE, linewidths=.7, zorder=2)
c.plot([.5, 1.5], [1.5, .5], color=RED, lw=2.4, solid_capstyle='round', zorder=4)
setup(c, xl, yl, [0, 1, 2], [0, 1, 2])
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'a': 'unique (1.5,.5)', 'b': 'unique (1,1); d=(1,1): d^TQd=4', 'c': 'solution set segment (.5,1.5)-(1.5,.5)'})
