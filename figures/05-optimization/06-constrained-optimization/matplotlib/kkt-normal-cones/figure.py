from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Normal cone at the optimum for tau=4 (interior), 2 (edge), .5 (corner). -grad f arrows are drawn at scale.
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
panels(fig, .02, .99, .985, .13, .06)
a, b, c = axes
off(a, (-.3, 4.3), (-.75, 4.15)); triangle(a, 4); dot(a, budget_x(4))
a.text(2.12, 1.15, '$\\nabla f=0$', fontsize=7.5); a.text(2.12, .62, '$N=\\{0\\}$', color=PURPLE, fontsize=7.5)
off(b, (-.2, 2.7), (-.4, 2.0)); triangle(b, 2); active(b, (2, 0), (0, 2)); p = budget_x(2)
b.plot([p[0], p[0]+.9], [p[1], p[1]+.9], color=PURPLE, lw=2.2, zorder=3)
arrow(b, p, p-grad_f(p), color=BLUE, lw=1.6, z=6); dot(b, p)
b.text(1.95, 1.42, '$N$', color=PURPLE, fontsize=8); b.text(2.1, .7, '$-\\nabla f$', color=BLUE, fontsize=8)
off(c, (-.25, 1.95), (-1.1, 1.05)); triangle(c, .5); active(c, (.5, 0), (0, .5)); active(c, (0, 0), (.5, 0)); p = budget_x(.5)
th = np.radians(np.linspace(-90, 45, 40)); R = .95
c.fill(np.r_[p[0], p[0]+R*np.cos(th)], np.r_[p[1], p[1]+R*np.sin(th)], facecolor=PURPLE_FILL, edgecolor='none', zorder=2)
for ang in (-90, 45): c.plot([p[0], p[0]+R*np.cos(np.radians(ang))], [p[1], p[1]+R*np.sin(np.radians(ang))], color=PURPLE, lw=1.1, zorder=3)
arrow(c, p, p-grad_f(p)*.5, color=BLUE, lw=1.6, z=6); dot(c, p)
c.text(1.2, -.3, '$N$', color=PURPLE, fontsize=8); c.text(1.32, .58, '$-\\nabla f$', color=BLUE, fontsize=8)
tags(fig, axes)
save(fig, HERE, 'figure', {'tau': [4, 2, .5], 'scale_panel_c': .5, 'grad_c': grad_f(p).tolist()})
