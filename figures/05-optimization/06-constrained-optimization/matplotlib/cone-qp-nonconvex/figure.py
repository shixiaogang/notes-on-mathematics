from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Nonconvex QP: f=1/2 x1^2-1/2 x2^2+1/4 x2 on -1<=x2<=1.
f = lambda a, b: .5*a*a-.5*b*b+.25*b
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .07, .985, .985, .25, .24)
a, b = axes
xl, yl = (-1.6, 1.6), (-1.5, 1.5)
a.fill([xl[0], xl[1], xl[1], xl[0]], [-1, -1, 1, 1], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
X, Y = grid2(xl, yl)
a.contour(X, Y, f(X, Y), levels=[-1, -.75, -.25, 0, .03125, .3, .7, 1.1], colors=BLUE, linewidths=.7, zorder=2)
active(a, (xl[0], 1), (xl[1], 1)); active(a, (xl[0], -1), (xl[1], -1))
dot(a, (0, -1)); dot(a, (0, 1), YELLOW); hollow(a, (0, .25), RED)
setup(a, xl, yl, [-1, 0, 1], [-1, 0, 1])
a.text(.1, -.9, 'A', fontsize=8); a.text(.1, .78, 'B', fontsize=8); a.text(.1, .34, 'S', fontsize=8)
s = np.linspace(-1, 1, 200); o = np.linspace(-1.5, 1.5, 300)
b.plot(o, f(0, o), color=BLUE, lw=.9, ls=(0, (3, 2)))
b.plot(s, f(0, s), color=BLUE, lw=1.5)
for v in (-1, 1): b.axvline(v, color=EDGE, lw=1.2)
dot(b, (-1, -.75)); dot(b, (1, -.25), YELLOW); hollow(b, (.25, 1/32), RED)
setup(b, (-1.55, 1.55), (-1.5, .35), [-1, 0, 1], [-1, -.5, 0], xl='$x_2$', yl='$f(0,x_2)$', equal=False)
b.text(-.9, -.85, 'A', fontsize=8); b.text(.86, -.42, 'B', fontsize=8, ha='right'); b.text(.25, .09, 'S', fontsize=8, ha='center')
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'A': [0, -1, -.75], 'B': [0, 1, -.25], 'S': [0, .25, 1/32]})
