from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# (a) (y-x)/(1+x+y) on the quadrant: values differ; (b) y exp(-x): equal values, x not attained.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .075, .985, .975, .235, .28)
s = np.linspace(0, 40, 500); ax = axes[0]; setup(ax, (0, 40), (-1.25, 1.25), range(0, 41, 10), (-1, 0, 1), xl='$s$', yl='函数值')
ax.axhline(1, color=BLUE, lw=.85, ls=(0, (3, 2))); ax.axhline(-1, color=PURPLE, lw=.85, ls=(0, (3, 2)))
ax.plot(s, (s-1)/(2+s), color=BLUE, lw=1.4); ax.plot(s, (1-s)/(2+s), color=PURPLE, lw=1.4)
ax.text(39, .62, '$f(1,s)$', color=BLUE, ha='right'); ax.text(39, -.68, '$f(s,1)$', color=PURPLE, ha='right')
ax = axes[1]; x = np.linspace(0, 6, 300); setup(ax, (0, 6), (-.08, 1.1), range(0, 7, 2), (0, .5, 1), yl='$f(x,y)$')
ax.axhline(0, color=PURPLE, lw=.85, ls=(0, (3, 2)))
ax.plot(x, np.exp(-x), color=BLUE, lw=1.4); ax.plot(x, .5*np.exp(-x), color=YELLOW, lw=1.6)
ax.text(.75, .55, '$y=1$', color=BLUE); ax.text(.1, .2, r'$y=\frac{1}{2}$', color=INK, fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': '(y-x)/(1+x+y) on [0,inf)^2', 'b': 'y exp(-x) on [0,inf) x [0,1]'})
