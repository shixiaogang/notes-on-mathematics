from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Local check versus global check for f(x,y)=x^2-x^4/4-y^2.
fig, ax = figure(width_mm=86, height_mm=48)
x = np.linspace(-3, 3, 500); setup(ax, (-3.2, 3.2), (-12.5, 2.5), range(-3, 4), (-12, -8, -4, 0), yl='$f(x,0)$')
ax.fill_between([-1, 1], -12.5, 2.5, color=BLUE_FILL, lw=0, zorder=0)
ax.axhline(0, color=MUTED, lw=.85, ls=':', zorder=1)
ax.plot(x, x**2-x**4/4, color=BLUE, lw=1.4, zorder=3)
hollow(ax, (0, 0), GREEN, ms=5.2); dot(ax, (-3, -11.25)); dot(ax, (3, -11.25))
ax.text(0, -9.2, '检验框B', ha='center', color=INK, fontsize=7.5)
save(fig, HERE, 'figure', {'f': 'x^2-x^4/4-y^2', 'X': '[-3,3]', 'Y': '[-1,1]'})
