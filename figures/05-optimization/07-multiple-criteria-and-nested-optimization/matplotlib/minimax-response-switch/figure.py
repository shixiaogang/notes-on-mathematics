from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# f(x,y)=xy on Y=[-1,1]: lines, envelope |x|, response set.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .075, .985, .975, .235, .28)
x = np.linspace(-1.5, 1.5, 300); ax = axes[0]; setup(ax, (-1.5, 1.5), (-1.6, 1.6), (-1, 0, 1), (-1, 0, 1), yl='$f(x,y)$')
for y in (-1, -.5, 0, .5, 1): ax.plot(x, x*y, color=MUTED, lw=.85, zorder=2)
ax.plot(x, abs(x), color=BLUE, lw=1.7, zorder=3); dot(ax, (0, 0))
ax.text(1.0, 1.32, r'$\phi=|x|$', color=BLUE, ha='right')
ax.text(.85, -1.38, '$y=-1$', color=MUTED, fontsize=7.5, ha='right')
ax.text(1.49, 1.05, '', color=MUTED)
ax = axes[1]; setup(ax, (-1.5, 1.5), (-1.4, 1.4), (-1, 0, 1), (-1, 0, 1), yl=r"$Y^*(x)$")
ax.plot([-1.5, 0], [-1, -1], color=PURPLE, lw=1.8, solid_capstyle='butt'); ax.plot([0, 1.5], [1, 1], color=PURPLE, lw=1.8, solid_capstyle='butt'); ax.plot([0, 0], [-1, 1], color=PURPLE, lw=1.8)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': 'xy', 'Y': '[-1,1]', 'phi': '|x|'})
