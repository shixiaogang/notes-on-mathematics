from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# f(x,y)=-x^2/2+2xy-y^2/2 at x=1: inner gap, response distance, and outer gradient error.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .975, .235, .3)
y = np.linspace(-.5, 3.5, 300); ax = axes[0]; setup(ax, (-.5, 3.5), (-1.5, 2), (0, 1, 2, 3), (-1, 0, 1), xl='$y$', yl='$f(1,y)$')
fv = -.5+2*y-.5*y**2; ax.plot(y, fv, color=BLUE, lw=1.4)
ax.axhline(1.5, color=MUTED, lw=.85, ls=':'); dot(ax, (2, 1.5)); dot(ax, (1, 1), GREEN)
ax.plot([1, 1], [1, 1.5], color=RED, lw=1.6); ax.text(.88, 1.2, r'$\varepsilon$', color=RED, ha='right')
ax.annotate('', xy=(2, .55), xytext=(1, .55), arrowprops=dict(arrowstyle='<|-|>', color=INK, lw=.85, shrinkA=0, shrinkB=0, mutation_scale=7)); ax.text(1.5, .28, r'$|\tilde y-y^*|$', ha='center', fontsize=7.5)
ax = axes[1]; setup(ax, (-.5, 3.5), (-2.5, 6.5), (0, 1, 2, 3), (-2, 0, 2, 4, 6), xl='$y$', yl=r'$\partial_x f(1,y)$')
ax.plot(y, -1+2*y, color=BLUE, lw=1.4); ax.axhline(3, color=MUTED, lw=.85, ls=':'); dot(ax, (2, 3)); dot(ax, (1, 1), GREEN)
ax.plot([1, 1], [1, 3], color=RED, lw=1.6); ax.text(.88, 1.85, '误差', color=RED, ha='right', fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '-x^2/2+2xy-y^2/2', 'x': 1, 'y_tilde': 1})
