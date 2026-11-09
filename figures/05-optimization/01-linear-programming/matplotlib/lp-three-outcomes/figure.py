from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Three outcomes of a linear program.
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panels(fig, .06, .985, .97, .26, .34)
a, b, c = axes
xl, yl = (-.3, 3.2), (-.3, 3.2)
# (a) x>=0, x1+x2<=1 and x1+x2>=2 do not meet
a.fill([0, 1, 0], [0, 0, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
a.fill([2, 3.2, 3.2, 0, 0], [0, 0, 3.2, 3.2, 2], facecolor=RED_FILL, edgecolor=RED, lw=.95, zorder=1)
a.text(1.9, 2.05, '$x_1+x_2\\geq2$', fontsize=7.5, color=INK, ha='center')
a.text(1.05, .42, '$x_1+x_2\\leq1$', fontsize=7.5, color=INK, ha='left')
# (b),(c) the same unbounded region x>=0, x1-x2<=1
R = np.array([[0, 0], [1, 0], [3.2, 2.2], [3.2, 3.2], [0, 3.2]], float)
region(b, R); levels(b, (1, 1), [1, 2, 3], xl, yl); dot(b, (0, 0), RED, ms=5.4)
b.text(.14, .06, '$(0,0)$', fontsize=7.5, color=INK)
region(c, R); levels(c, (1, -1), [-1, -2], xl, yl, color=BLUE)
arrow(c, (.0, .3), (.0, 3.1), RED, lw=1.6)
dot(c, (0, .3), GREEN, ms=4.6)
for ax in axes:
    setup(ax, xl, yl, range(0, 4), range(0, 4))
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'empty', 'b': 'min x1+x2 over x>=0, x1-x2<=1: optimum (0,0)', 'c': 'min x1-x2: unbounded along (0,1)'})
