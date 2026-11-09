from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Farkas: b in the cone of the columns, or a separating hyperplane through the projection.
a1, a2 = np.array([1., 2.]), np.array([1., 1.])
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .07, .985, .975, .2, .24)
a, b = axes
def cone(ax, s):
    ax.fill([0, a1[0]*s, a2[0]*s], [0, a1[1]*s, a2[1]*s], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
    ax.plot([0, a1[0]*s], [0, a1[1]*s], color=BLUE, lw=.95, zorder=2); ax.plot([0, a2[0]*s], [0, a2[1]*s], color=BLUE, lw=.95, zorder=2)
cone(a, 4.4)
A = np.column_stack([a1, a2]); bb = np.array([4., 6.]); x = np.linalg.solve(A, bb)
arrow(a, (0, 0), a1, BLUE); arrow(a, (0, 0), a2, BLUE); 
arrow(a, (0, 0), bb, GREEN, lw=1.5)
a.plot([x[0]*a1[0], bb[0], x[1]*a2[0]], [x[0]*a1[1], bb[1], x[1]*a2[1]], color=MUTED, lw=.85, ls=(0, (2, 2)), zorder=3)
a.text(.4, 1.5, '$\\bm{a}_1$'.replace('\\bm{a}', 'a'), fontsize=8, color=BLUE, ha='right'); a.text(1.15, .75, '$a_2$', fontsize=8, color=BLUE)
a.text(4.1, 6.05, '$b$', fontsize=8, color=GREEN)
setup(a, (-.5, 5.2), (-.5, 7), range(0, 6), range(0, 8), '$v_1$', '$v_2$')
xl, yl = (-.7, 2.4), (-.7, 2.6)
b2 = np.array([1., 0.]); pr = (b2@a2)/(a2@a2)*a2; z = pr-b2
b.fill([xl[0], xl[1], xl[1]], [xl[0], xl[0], xl[1]], facecolor=RED_FILL, edgecolor='none', zorder=0)
cone(b, 1.8)
b.plot([xl[0], xl[1]], [xl[0], xl[1]], color=EDGE, lw=1.3, zorder=2)
arrow(b, (0, 0), a1, BLUE); arrow(b, (0, 0), a2, BLUE); arrow(b, (0, 0), b2, RED, lw=1.5)
arrow(b, b2, pr, GREEN, lw=1.3)
arrow(b, pr, pr+z, PURPLE, lw=1.5)
b.plot(*pr, 'o', color=GREEN, ms=4.6, mew=0, zorder=6)
b.text(.42, 1.55, '$a_1$', fontsize=8, color=BLUE, ha='right'); b.text(1.1, .75, '$a_2$', fontsize=8, color=BLUE)
b.text(1.06, -.17, "$b'$", fontsize=8, color=RED); b.text(.56, .2, '$\\hat{v}$', fontsize=8, color=GREEN)
b.text(-.08, 1.2, '$z$', fontsize=8, color=PURPLE, ha='right')
setup(b, xl, yl, range(0, 3), range(0, 3), '$v_1$', '$v_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': x.tolist(), 'projection': pr.tolist(), 'z': z.tolist(), 'bz': float(b2@z)})
