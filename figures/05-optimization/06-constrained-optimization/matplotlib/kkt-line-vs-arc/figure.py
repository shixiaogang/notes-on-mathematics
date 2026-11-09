from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# (a) convex triangle: segments from xbar to feasible points. (b) unit circle: straight lines leave at once, arcs stay.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .03, .985, .985, .12, .08)
a, b = axes
off(a, (-.25, 2.3), (-.25, 2.2)); triangle(a, 2)
p = np.array([.5, .5])
for q in [(1.5, .5), (.2, 1.5), (1.3, .15), (.1, .15)]:
    arrow(a, p, q, color=GREEN); dot(a, q, BLUE, ms=3.2)
dot(a, p, INK, ms=4.5); a.text(.42, .62, '$\\bar{x}$', fontsize=8, ha='right')
t = np.linspace(0, 2*np.pi, 400)
off(b, (-1.3, 1.9), (-1.2, 1.2))
b.plot(np.cos(t), np.sin(t), color=BLUE, lw=1.4)
s = np.linspace(-.8, .8, 200); b.plot(np.cos(s), np.sin(s), color=GREEN, lw=2.4, zorder=3)
b.plot([1, 1], [-1.05, 1.05], color=RED, lw=1.0, ls=(0, (4, 2)), zorder=2)
dot(b, (1, 0), INK, ms=4.5); b.text(.9, -.02, '$\\bar{x}$', fontsize=8, ha='right', va='center')
arrow(b, (1, 0), (1, .62), color=RED)
b.text(1.08, .35, '$\\bar{x}+t\\,d$', color=RED, fontsize=8)
b.text(.62, -1.02, '弧线', color=GREEN, fontsize=7.5, ha='right')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'segments in triangle', 'b': 'circle arcs'})
