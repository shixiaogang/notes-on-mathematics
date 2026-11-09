from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Reduced curvature: Q=diag(1,-1), lines through the origin along three directions.
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .065, .985, .985, .26, .24)
a, b = axes
xl, yl = (-2, 2), (-2, 2)
X, Y = grid2(xl, yl)
a.contour(X, Y, .5*(X**2-Y**2), levels=[-1.5, -1, -.5, .5, 1, 1.5], colors=BLUE, linewidths=.7, zorder=2)
a.plot([-2, 2], [0, 0], color=GREEN, lw=1.6, zorder=3)
a.plot([-2, 2], [-2, 2], color=MUTED, lw=1.4, ls=(0, (4, 2)), zorder=3)
a.plot([0, 0], [-2, 2], color=RED, lw=1.6, zorder=3)
setup(a, xl, yl, [-2, 0, 2], [-2, 0, 2])
s = np.linspace(-2, 2, 200)
b.plot(s, .5*s**2, color=GREEN, lw=1.5)
b.plot(s, 0*s, color=MUTED, lw=1.4, ls=(0, (4, 2)))
b.plot(s, -.5*s**2, color=RED, lw=1.5)
setup(b, (-2.1, 2.1), (-2.2, 2.2), [-2, 0, 2], [-2, 0, 2], xl='$s$', yl='$f$', equal=False)
b.text(1.05, 1.15, '$z=e_1$', color=GREEN, fontsize=7.5, ha='right')
b.text(1.62, .12, '$z=(1,1)$', color=MUTED, fontsize=7.5, ha='center')
b.text(1.0, -1.25, '$z=e_2$', color=RED, fontsize=7.5, ha='right')
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'Q': [[1, 0], [0, -1]], 'curvatures': [1, 0, -1]})
