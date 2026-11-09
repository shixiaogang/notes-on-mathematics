from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min -x^2, x<=1+u, x>=-1. V(u)=-1 on [-2,0], -(1+u)^2 for u>0. KKT multiplier 2 at x=1 gives a line violated for u>0.
fig, ax = figure(width_mm=86, height_mm=52)
U = np.linspace(-2, 1.25, 500); V = np.where(U <= 0, -1, -(1+U)**2); L = -1-2*U
Up = U[U >= 0]
ax.fill_between(Up, -(1+Up)**2, -1-2*Up, facecolor=RED_FILL, edgecolor='none', zorder=0)
ax.plot(U, V, color=BLUE, lw=1.4, zorder=3)
ax.plot(U, L, color=PURPLE, lw=1.1, ls='--', zorder=2)
opt_point(ax, (0, -1))
ax.text(-1.7, -.72, '$V(u)$', fontsize=8, color=BLUE)
ax.text(-1.5, 2.25, r'$-1-2u$', fontsize=7.5, color=PURPLE)
clean(ax, (-2.1, 1.3), (-5.5, 3.2), xlabel='$u$', ylabel='最优值')
ax.set_xticks([-2, -1, 0, 1]); ax.set_yticks([-4, -2, 0, 2])
save(fig, Path(__file__).resolve().parent, 'figure', {'V': 'piecewise'})
