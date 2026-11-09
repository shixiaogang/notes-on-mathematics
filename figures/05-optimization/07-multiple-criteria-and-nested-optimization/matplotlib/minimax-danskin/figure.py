from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# phi(x)=(|x|+1)^2 from f=(x-y)^2, Y=[-1,1]: active tangents and subdifferential graph.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panels(fig, .075, .985, .975, .225, .28)
x = np.linspace(-1.5, 1.5, 400); ax = axes[0]; setup(ax, (-1.5, 1.5), (0, 6), (-1, 0, 1), range(0, 7, 2), yl=r'$\phi(x)$')
ax.plot(x, (x+1)**2, color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2); ax.plot(x, (x-1)**2, color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
ax.plot(x, (abs(x)+1)**2, color=BLUE, lw=1.6, zorder=3)
xs = np.array([-.3, 1.3]); ax.plot(xs, 2.25+3*(xs-.5), color=GREEN, lw=1.2, zorder=4); dot(ax, (.5, 2.25), GREEN)
s = np.array([0, 1.]); ax.plot(s, 1+2*s, color=GREEN, lw=1.0, zorder=4); ax.plot(-s, 1+2*s, color=GREEN, lw=1.0, zorder=4); dot(ax, (0, 1))
ax.text(1.05, 2.05, '$y=-1$', fontsize=7.5, color=MUTED); ax.text(-1.45, 2.05, '$y=1$', fontsize=7.5, color=MUTED)
ax = axes[1]; setup(ax, (-1.5, 1.5), (-5.4, 5.4), (-1, 0, 1), (-4, -2, 0, 2, 4), yl=r'$\partial\phi(x)$')
ax.axhline(0, color=MUTED, lw=.85, ls=':', zorder=1)
ax.plot([-1.5, 0], [2*(-1.5-1), -2], color=BLUE, lw=1.6); ax.plot([0, 1.5], [2, 2*(1.5+1)], color=BLUE, lw=1.6); ax.plot([0, 0], [-2, 2], color=BLUE, lw=1.6)
dot(ax, (0, 0))
tags(fig, axes)
save(fig, HERE, 'figure', {'phi': '(|x|+1)^2'})
