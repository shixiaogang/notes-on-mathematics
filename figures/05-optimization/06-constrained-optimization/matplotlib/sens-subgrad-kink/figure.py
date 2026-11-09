from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min -x, x-1<=u, x-1<=0. V(u)=max(-1-u,-1). Multiplier set lam1+lam2=1, lam>=0 with slopes -lam1.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax = axs[0]
U = np.linspace(-1.2, 1.2, 201); V = np.maximum(-1-U, -1)
for s in (0, -.5, -1):
    ax.plot(U, -1+s*U, color=PURPLE, lw=1.0, ls='--', zorder=2)
ax.plot(U, V, color=BLUE, lw=1.4, zorder=3); opt_point(ax, (0, -1))
ax.text(-.55, .08, '$V(u)$', fontsize=8, color=BLUE, va='bottom')
ax.text(1.17, -2.28, '-1', fontsize=7.5, color=PURPLE, ha='right', va='top')
ax.text(1.17, -1.4, '-1/2', fontsize=7.5, color=PURPLE, ha='right', va='bottom')
ax.text(1.17, -.92, '0', fontsize=7.5, color=PURPLE, ha='right', va='bottom')
clean(ax, (-1.25, 1.25), (-2.5, .6), xlabel='$u$', sub='(a)', ylabel='最优值')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([-2, -1, 0])
ax = axs[1]
ax.plot([0, 1], [1, 0], color=RED, lw=1.8, zorder=3)
for a in (0, .5, 1): ax.plot([a], [1-a], 'o', color=PURPLE, ms=4.2, zorder=4)
ax.text(1.04, .06, '斜率 -1', fontsize=7.5, ha='left', va='bottom')
ax.text(.55, .54, '斜率 -1/2', fontsize=7.5, ha='left', va='bottom')
ax.text(.06, 1.04, '斜率 0', fontsize=7.5, ha='left', va='bottom')
ax.set_aspect('equal'); clean(ax, (-.08, 1.55), (-.08, 1.3), xlabel=r'$\lambda_1$', sub='(b)', ylabel=r'$\lambda_2$')
ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'V': 'max(-1-u,-1)'})
