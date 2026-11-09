from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# (a) f(x,y)=(x-y)^2 on Y=[-1,1]; (b) worst-value functions for three response sets.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .075, .985, .975, .22, .28)
x = np.linspace(-2, 2, 500); ax = axes[0]; setup(ax, (-2, 2), (0, 6), range(-2, 3), range(0, 7, 2), yl='$f(x,y)$')
for y in (-1, -.5, 0, .5, 1): ax.plot(x, (x-y)**2, color=MUTED, lw=.85, zorder=2)
ax.plot(x, (abs(x)+1)**2, color=BLUE, lw=1.6, zorder=3); dot(ax, (0, 1))
ax.text(.95, 5.25, r'$\phi$', color=BLUE, ha='right')
ax = axes[1]; setup(ax, (-2, 3), (0, 12), range(-2, 4), range(0, 13, 4), yl=r'$\phi(x)$')
x = np.linspace(-2, 3, 700)
sets = [(-.5, .5, YELLOW), (-1, 1, BLUE), (-1, 3, PURPLE)]
for lo, hi, c in sets: ax.plot(x, np.maximum((x-lo)**2, (x-hi)**2), color=c, lw=1.4, zorder=3)
for p in ((0, .25), (0, 1), (1, 4)): dot(ax, p)
ax.text(2.0, 2.2, r'$[-\frac{1}{2},\frac{1}{2}]$', color=INK, fontsize=7.5, ha='left'); ax.text(-1.1, 5.4, '$[-1,1]$', color=INK, fontsize=7.5, ha='center')
ax.text(-.02, 10.5, '$[-1,3]$', color=INK, fontsize=7.5, ha='left')
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '(x-y)^2', 'Y': ['[-1,1]', '[-1/2,1/2]', '[-1,3]']})
