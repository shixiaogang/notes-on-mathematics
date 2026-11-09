from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Budget tau=2. (a) xbar=(1,1) not optimal: tangent d=(1,-1) has <grad f,d>=-1. (b) x*=(1.5,.5): -grad f is normal to the edge.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .21, .2)
xl, yl = (-.2, 2.6), (-.2, 2.2)
for ax, p in zip(axes, [np.array([1., 1.]), budget_x(2)]):
    triangle(ax, 2); circles(ax, xl, yl); setup(ax, xl, yl, range(0, 3), range(0, 3)); active(ax, (2, 0), (0, 2))
a, b = axes
p = np.array([1., 1.]); arrow(a, p, p-grad_f(p)*.85, color=BLUE); arrow(a, p, p+.5*np.array([1, -1]), color=GREEN)
dot(a, p, GREEN); hollow(a, C, BLUE)
a.text(1.32, 1.14, '$-\\nabla f$', color=BLUE, fontsize=8); a.text(1.55, .62, '$d$', color=GREEN, fontsize=8)
a.text(.88, .87, '$\\bar{x}$', fontsize=8, ha='right')
p = budget_x(2); arrow(b, p, p-grad_f(p)*.95, color=BLUE)
arrow(b, p, p+.45*np.array([1, -1]), color=GREEN); arrow(b, p, p-.45*np.array([1, -1]), color=GREEN)
dot(b, p); hollow(b, C, BLUE)
b.text(1.98, .64, '$-\\nabla f$', color=BLUE, fontsize=8, ha='left'); b.text(1.42, .36, '$x^{*}$', color=RED, fontsize=8, ha='right')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': {'xbar': [1, 1], 'grad': [-1, 0], 'd': [1, -1]}, 'b': {'x*': [1.5, .5], 'grad': [-.5, -.5]}})
