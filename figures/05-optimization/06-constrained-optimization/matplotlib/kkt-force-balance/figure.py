from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Force balance. (a) tau=2: -grad f=.5*(1,1). (b) tau=.5: -grad f=1.5*(1,1)+.5*(0,-1).
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .02, .99, .985, .12, .08)
a, b = axes
off(a, (-.2, 2.5), (-.25, 2.1)); triangle(a, 2); active(a, (2, 0), (0, 2)); p = budget_x(2)
off_ = .05*np.array([-1, 1])/np.sqrt(2); arrow(a, p+off_, p+off_+np.array([.5, .5]), color=PURPLE, lw=1.6); arrow(a, p, p-.9*np.array([.5, .5]), color=BLUE, lw=1.4, z=6) if 0 else None
arrow(a, p-off_, p-off_-grad_f(p), color=BLUE, lw=1.6, z=6); dot(a, p)
a.text(2.08, .8, '$-\\nabla f$', color=BLUE, fontsize=8); a.text(1.72, 1.1, '$\\lambda_1\\nabla g_1$', color=PURPLE, fontsize=8, ha='right')
off(b, (-.25, 2.4), (-.75, 1.7)); triangle(b, .5); active(b, (.5, 0), (0, .5)); active(b, (0, 0), (.5, 0)); p = budget_x(.5)
v1, v3 = 1.5*np.array([1., 1.]), .5*np.array([0., -1.]); g = v1+v3
b.plot([p[0]+v1[0], p[0]+g[0]], [p[1]+v1[1], p[1]+g[1]], color=PURPLE, lw=.85, ls=(0, (2, 2)), zorder=3)
b.plot([p[0]+v3[0], p[0]+g[0]], [p[1]+v3[1], p[1]+g[1]], color=PURPLE, lw=.85, ls=(0, (2, 2)), zorder=3)
arrow(b, p, p+v1, color=PURPLE, lw=1.6); arrow(b, p, p+v3, color=PURPLE, lw=1.6); arrow(b, p, p+g, color=BLUE, lw=1.6, z=6); dot(b, p)
b.text(1.1, 1.42, '$\\lambda_1\\nabla g_1$', color=PURPLE, fontsize=8, ha='right'); b.text(.58, -.55, '$\\lambda_3\\nabla g_3$', color=PURPLE, fontsize=8)
b.text(2.06, .86, '$-\\nabla f$', color=BLUE, fontsize=8)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': {'lam1': .5}, 'b': {'lam1': 1.5, 'lam3': .5}})
