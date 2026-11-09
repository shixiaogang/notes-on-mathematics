from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Relaxed cost table f(p,q)=4(p-1/2)(q-1/4)+3/2.
fig, axes = figure(width_mm=112, height_mm=45, ncols=3)
panels(fig, .075, .985, .975, .27, .4)
g = np.linspace(0, 1, 300); P, Q = np.meshgrid(g, g); Z = 4*(P-.5)*(Q-.25)+1.5
ax = axes[0]; setup(ax, (0, 1), (0, 1), (0, .5, 1), (0, .5, 1), xl='$p$', yl='$q$', equal=True)
ax.fill([0, 1, 1, 0], [0, 0, 1, 1], color=BLUE_FILL, lw=0, zorder=0)
ax.contour(P, Q, Z, levels=[.5, 1, 1.25, 1.75, 2, 2.5], colors=BLUE, linewidths=.8, linestyles='solid')
ax.plot([.5, .5], [0, 1], color=BLUE, lw=.8); ax.plot([0, 1], [.25, .25], color=BLUE, lw=.8)
dot(ax, (.5, .25)); dot(ax, (.8, .5), GREEN)
ax = axes[1]; p = np.linspace(0, 1, 200); setup(ax, (0, 1), (0, 3.2), (0, .5, 1), (0, 1, 2, 3), xl='$p$', yl=r'$\phi(p)$')
ax.plot(p, np.maximum(2-p, 3*p), color=BLUE, lw=1.5); ax.axhline(1.5, color=MUTED, lw=.85, ls=':'); dot(ax, (.5, 1.5)); dot(ax, (.8, 2.4), GREEN)
ax = axes[2]; q = np.linspace(0, 1, 200); setup(ax, (0, 1), (0, 3.2), (0, .5, 1), (0, 1, 2, 3), xl='$q$', yl=r'$\psi(q)$')
ax.plot(q, np.minimum(2-2*q, 1+2*q), color=PURPLE, lw=1.5); ax.axhline(1.5, color=MUTED, lw=.85, ls=':'); dot(ax, (.25, 1.5)); dot(ax, (.5, 1), GREEN)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '4(p-1/2)(q-1/4)+3/2'})
