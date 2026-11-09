from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min -x1*x2 s.t. x1+x2=2. Lagrangian with nu=1 curves up along the constraint and down across it.
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax = axs[0]
X, Y = np.meshgrid(np.linspace(.02, 2.6, 300), np.linspace(.02, 2.6, 300))
Z = X*Y
ax.contour(X, Y, Z, levels=[.25, .5, 1, 1.6, 2.4, 3.3], colors=BLUE, linewidths=.7)
ax.plot([0, 2.3], [2, -.3], color=ACTIVE, lw=1.6, zorder=3)
opt_point(ax, (1, 1))
kw = dict(arrowstyle='-|>', lw=1.0, mutation_scale=7, shrinkA=0, shrinkB=0)
ax.annotate('', xy=(1.5, .5), xytext=(1, 1), arrowprops=dict(color=GREEN, **kw), zorder=9)
ax.annotate('', xy=(1.5, 1.5), xytext=(1, 1), arrowprops=dict(color=RED, **kw), zorder=9)
ax.text(1.56, .48, '切向', fontsize=7.5, color=GREEN, va='center'); ax.text(1.55, 1.56, '法向', fontsize=7.5, color=RED, va='center')
ax.set_aspect('equal'); clean(ax, (0, 2.6), (0, 2.6), xlabel='$x_1$', ylabel='$x_2$', sub='(a)')
ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
ax = axs[1]
S = np.linspace(-1, 1, 201)
ax.plot(S, S**2-1, color=GREEN, lw=1.4); ax.plot(S, -1-S**2, color=RED, lw=1.4)
opt_point(ax, (0, -1))
ax.text(.55, -.45, '切向', fontsize=7.5, color=GREEN); ax.text(.5, -1.72, '法向', fontsize=7.5, color=RED)
clean(ax, (-1, 1), (-2.2, .2), xlabel='$s$', sub='(b)', ylabel=r'$\mathcal{L}$')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([-2, -1, 0])
save(fig, Path(__file__).resolve().parent, 'figure', {'along_tangent': 's^2-1', 'along_normal': '-1-s^2'})
