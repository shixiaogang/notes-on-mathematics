from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Minimize the largest distance to p1=(0,0), p2=(6,0), p3=(3,9): optimum (3,4), t=5.
P = np.array([[0., 0.], [6., 0.], [3., 9.]]); c = np.array([3., 4.])
fig, axes = figure(width_mm=112, height_mm=66, ncols=2)
panels(fig, .06, .985, .985, .22, .2)
a, b = axes
xl, yl = (-2.8, 8.8), (-1.8, 10.2)
th = np.linspace(0, 2*np.pi, 300)
a.fill(c[0]+5*np.cos(th), c[1]+5*np.sin(th), facecolor=BLUE_FILL, edgecolor=EDGE, lw=1.5, zorder=1)
for p in P:
    a.plot([c[0], p[0]], [c[1], p[1]], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2); dot(a, p, INK, ms=4)
dot(a, c); setup(a, xl, yl, [0, 3, 6], [0, 4, 8])
a.text(1.1, 2.55, '$t^*=5$', fontsize=7.5, ha='right'); a.text(3.25, 4.25, '$x^*$', color=RED, fontsize=8)
for p, s, off_ in zip(P, ('$p_1$', '$p_2$', '$p_3$'), ((-.2, -.75), (.3, -.75), (.45, .1))):
    a.text(p[0]+off_[0], p[1]+off_[1], s, fontsize=8)
X, Y = grid2(xl, yl, 600)
G = np.max([np.hypot(X-p[0], Y-p[1]) for p in P], axis=0)
b.contour(X, Y, G, levels=[5.3, 6, 7, 8, 9.5], colors=BLUE, linewidths=.75, zorder=2)
for p in P: dot(b, p, INK, ms=4)
dot(b, c); setup(b, xl, yl, [0, 3, 6], [0, 4, 8])
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'x*': c.tolist(), 't*': 5, 'dist': [float(np.hypot(*(c-p))) for p in P]})
