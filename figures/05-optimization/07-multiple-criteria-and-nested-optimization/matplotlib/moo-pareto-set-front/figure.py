from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Pareto set in decision space and Pareto front in objective space (isotropic pair).
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .28)
ax = axes[0]; setup(ax, (-.55, 1.6), (-.55, 1.6), [0, 1], [0, 1], '$x_1$', '$x_2$', equal=True)
X, Y = np.meshgrid(np.linspace(-.6, 1.7, 300), np.linspace(-.6, 1.7, 300)); F1, F2 = f_iso(np.stack([X, Y], -1))
ax.contour(X, Y, F1, levels=[.125, .5, 1.], colors=BLUE, linewidths=.7)
ax.contour(X, Y, F2, levels=[.125, .5, 1.], colors=BLUE, linewidths=.7, linestyles=[(0, (3, 2))])
ax.plot([1, 0], [0, 1], color=RED, lw=2, solid_capstyle='round', zorder=4)
hollow(ax, (1, 1), GREEN); arrow(ax, (1, 1), (.53, .53), GREEN); dot(ax, (.5, .5))
ax.text(1.07, 1.05, '$p$', color=INK); ax.text(.33, .3, '$q$', color=INK); ax.text(1.08, -.17, '$a$', color=INK); ax.text(-.22, 1.05, '$b$', color=INK)
ax = axes[1]; setup(ax, (0, 1.5), (0, 1.5), [0, .5, 1, 1.5], [0, .5, 1, 1.5], equal=True); iso_fill(ax, 1.5)
u, v = iso_front(); ax.plot(u, v, color=RED, lw=2, zorder=4, solid_capstyle='round')
hollow(ax, (.5, .5), GREEN); arrow(ax, (.5, .5), (.27, .27), GREEN); dot(ax, (.25, .25))
ax.text(.56, .55, '$f(p)$', color=INK); ax.text(.05, .08, '$f(q)$', color=INK)
ax.text(.03, 1.06, '$f(b)$', color=INK); ax.text(1.03, .05, '$f(a)$', color=INK)
tags(fig, axes)
save(fig, HERE, 'figure', {'front': '(s^2,(1-s)^2), s in [0,1]'})
