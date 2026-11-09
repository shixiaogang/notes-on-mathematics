from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Running QP: min 1/2||Dx-r||^2, D=[[1,1],[1,0],[0,1]], r=(4,1,0), x>=0, x1+x2<=2.
fig, ax = figure(width_mm=84, height_mm=62)
xl, yl = (-.25, 3.2), (-.25, 2.35)
ax.fill([0, 2, 0], [0, 0, 2], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
X, Y = grid2(xl, yl)
ax.contour(X, Y, fls(X, Y), levels=[1.6, 1.8, 2.25, 3, 4, 5.5, 7.5], colors=BLUE, linewidths=.75, zorder=2)
active(ax, (2, 0), (0, 2))
g = Q@XSTAR+q
arrow(ax, XSTAR, XSTAR-.22*g, color=BLUE, lw=1.4)
hollow(ax, XLS, BLUE); dot(ax, XSTAR)
setup(ax, xl, yl, range(0, 4), range(0, 3))
ax.text(XLS[0]+.1, XLS[1]+.05, '$(2,1)$', fontsize=7.5)
ax.text(XSTAR[0]-.09, XSTAR[1]-.13, '$x^*$', color=RED, ha='right', fontsize=8)
ax.text(1.62, .98, '$-\\nabla f$', color=BLUE, fontsize=8, ha='right')
ax.text(.42, 1.8, '$x_1+x_2=2$', fontsize=7.5)
ax.text(.42, .42, '$C$', color=INK, fontsize=8)
save(fig, HERE, 'figure', {'Q': Q.tolist(), 'q': q.tolist(), 'x*': XSTAR.tolist(), 'grad': g.tolist(), 'f*': float(fls(*XSTAR))})
