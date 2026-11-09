from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# f(x)=x1^2+x1 x2+x2^2, x0=(3,4): coordinate staircase versus one joint solve.
fig, ax = figure(width_mm=88, height_mm=66)
panel(fig, .1, .98, .98, .13)
contour_c(ax, (-4, 5), (-3, 5.2), [.75, 3, 12, 22, 37])
P = cyclic((3, 4), updates=6); path(ax, P, GREEN)
ax.plot([3, 0], [4, 0], color=YELLOW, lw=1.6, zorder=3)
ax.annotate('', xy=(.18, .24), xytext=(1.5, 2), arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=1.6, shrinkA=0, shrinkB=0))
opt(ax)
ax.text(3.15, 4.2, r'$x^{(0)}$', fontsize=8, color=INK); ax.text(-3.0, 4.15, '$(-2,4)$', fontsize=7.5, color=INK); ax.text(-1.9, 1.15, '$(-2,1)$', fontsize=7.5, color=INK, ha='left')
ax.text(1.9, 1.5, '联合求解', fontsize=7.5, color=INK)
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1); ax.set_xlim(-4, 5); ax.set_ylim(-3, 5.2); ax.set_aspect('equal')
save(fig, HERE, 'figure', {'formula': 'x1^2+x1x2+x2^2', 'path': P.tolist()})
