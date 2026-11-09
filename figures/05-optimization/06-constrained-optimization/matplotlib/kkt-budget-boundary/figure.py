from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# min 1/2[(x1-2)^2+(x2-1)^2], x>=0, x1+x2<=2: optimum on the budget edge, gradient nonzero.
fig, ax = figure(width_mm=82, height_mm=66)
xl, yl = (-.25, 3.25), (-.25, 2.45)
triangle(ax, 2); circles(ax, xl, yl); setup(ax, xl, yl, range(0, 4), range(0, 3))
xs = budget_x(2); active(ax, (2, 0), (0, 2))
arrow(ax, xs, C-.04, color=BLUE)
hollow(ax, C, BLUE); dot(ax, xs)
ax.text(C[0]+.1, C[1]+.06, '$c=(2,1)$', color=INK, fontsize=7.5)
ax.text(xs[0]-.1, xs[1]-.17, '$x^*$', color=RED, ha='right', fontsize=8)
ax.text(1.62, .92, '$-\\nabla f$', color=BLUE, fontsize=8, ha='right')
ax.text(.42, 1.78, '$x_1+x_2=2$', color=INK, fontsize=7.5)
save(fig, HERE, 'figure', {'problem': 'budget tau=2', 'x*': xs.tolist(), 'grad': grad_f(xs).tolist()})
