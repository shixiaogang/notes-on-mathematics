from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Three local pictures around the origin.
fig, axes = figure(width_mm=112, height_mm=45, ncols=3)
panels(fig, .06, .985, .975, .27, .32)
g = np.linspace(-1.5, 1.5, 300); X, Y = np.meshgrid(g, g)
funs = [X**2-Y**2, Y**2-X**2, -.5*X**2+2*X*Y-.5*Y**2]
marks = [[(1.15, 0, '高'), (-1.15, 0, '高'), (0, 1.15, '低'), (0, -1.15, '低')],
         [(1.15, 0, '低'), (-1.15, 0, '低'), (0, 1.15, '高'), (0, -1.15, '高')],
         [(1.05, 1.05, '高'), (-1.05, -1.05, '高'), (1.05, -1.05, '低'), (-1.05, 1.05, '低')]]
for i, (ax, Z) in enumerate(zip(axes, funs)):
    setup(ax, (-1.5, 1.5), (-1.5, 1.5), (-1, 0, 1), (-1, 0, 1), equal=True)
    ax.contour(X, Y, Z, levels=[-1.5, -1, -.5, -.15, .15, .5, 1, 1.5], colors=BLUE, linewidths=.8, linestyles='solid')
    for a, b, s in marks[i]: ax.text(a, b, s, ha='center', va='center', color=INK, fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.8), zorder=6)
dot(axes[0], (0, 0)); hollow(axes[1], (0, 0)); dot(axes[2], (0, 0))
s = np.array([-.75, .75]); axes[2].plot(s, 2*s, color=PURPLE, lw=1.2, zorder=5)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': ['x^2-y^2', 'y^2-x^2', '-x^2/2+2xy-y^2/2']})
