from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Unit vectors from factorizing the relaxed X: triangle (120deg) and pentagon (144deg between neighbours).
def draw(ax, angs, cut):
    n = np.array([np.cos(cut), np.sin(cut)])
    th = np.linspace(0, 2*np.pi, 200); ax.plot(np.cos(th), np.sin(th), color=GRID, lw=.8, zorder=1)
    ax.plot([-1.3*n[1], 1.3*n[1]], [1.3*n[0], -1.3*n[0]], color=EDGE, lw=1.2, zorder=2)
    for i, an in enumerate(angs):
        v = np.array([np.cos(an), np.sin(an)]); c = GREEN if v@n > 0 else YELLOW
        arrow(ax, (0, 0), v, color=c, lw=1.5)
        ax.text(1.2*v[0], 1.2*v[1], f'{i+1}', ha='center', va='center', fontsize=8)
    arrow(ax, (0, 0), .55*n, color=INK, lw=1.0, ms=6)
    ax.text(.72*n[0], .72*n[1]+.02, '$g$', fontsize=8, ha='center', va='center')
fig, axes = figure(width_mm=100, height_mm=56, ncols=2)
panels(fig, .01, .99, .99, .11, .06)
a, b = axes
for ax in axes: off(ax, (-1.45, 1.45), (-1.45, 1.45))
draw(a, np.radians([90, 210, 330]), np.radians(30))
draw(b, np.radians([90+144*i for i in range(5)]), np.radians(50))
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'triangle': '120deg', 'pentagon': '144deg'})
