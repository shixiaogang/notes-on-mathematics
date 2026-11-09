from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Slice a=b of the sign relaxation: X=[[1,a,a],[a,1,c],[a,c,1]]; objective x^T W x -> 2(2a+c).
fig, ax = figure(width_mm=88, height_mm=70)
xl, yl = (-1.25, 1.25), (-1.2, 1.35)
A = np.linspace(-1/1, 1/1, 400)
ax.fill_between(A, 2*A**2-1, 1, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
ax.plot(A, 2*A**2-1, color=BLUE, lw=1.2, zorder=2); ax.plot([-1, 1], [1, 1], color=BLUE, lw=1.2, zorder=2)
ax.fill([1, -1, 0], [1, 1, -1], facecolor=GREEN_FILL, edgecolor=GREEN, lw=1.2, zorder=3)
Aa = np.array(xl)
for lev in (-3, -2, 0):
    ax.plot(Aa, (lev-4*Aa)/2, color=BLUE, lw=.75, ls=(0, (4, 2)), zorder=2.5)
dot(ax, (-.5, -.5), PURPLE); dot(ax, (-1, 1)); dot(ax, (0, -1)); dot(ax, (1, 1), GREEN)
setup(ax, xl, yl, [-1, -.5, 0, .5, 1], [-1, -.5, 0, .5, 1], xl='$a$', yl='$c$')
ax.text(-.6, -.6, '$-3$', color=PURPLE, fontsize=7.5, ha='right'); ax.text(-1.07, 1.03, '$-2$', color=RED, fontsize=7.5, ha='right')
ax.text(.1, -1.05, '$-2$', color=RED, fontsize=7.5); ax.text(1.05, 1.03, '$6$', color=GREEN, fontsize=7.5)
save(fig, HERE, 'figure', {'relaxation boundary': 'c>=2a^2-1, c<=1', 'hull': 'triangle (1,1),(-1,1),(0,-1)', 'min': -3})
