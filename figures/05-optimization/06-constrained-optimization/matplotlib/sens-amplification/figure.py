from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# (a) near-parallel equalities x1+x2=tau, x1+1.25*x2=2.25: tau 2 -> 1.9 moves the intersection (5,-4)*(-0.1).
# (b) flat bowl H=diag(1,.1), b2 .1 -> .2 moves the minimum from (1,1) to (1,2).
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]; xs = np.linspace(0, 2.4, 3); eps = .25
ax.plot(xs, (2.25-xs)/1.25, color=ACTIVE, lw=1.6, zorder=3)
ax.plot(xs, 2-xs, color=ACTIVE, lw=1.6, zorder=3); ax.plot(xs, 1.9-xs, color=ACTIVE, lw=1.0, ls='--', zorder=3)
J = np.array([[1, 1], [1, 1+eps]])
p0 = np.linalg.solve(J, [2, 2.25]); p1 = np.linalg.solve(J, [1.9, 2.25])
ax.plot(*zip(p0, p1), color=GREEN, lw=1.7, zorder=5); opt_point(ax, p0); ax.plot(*p1, 'o', color=GREEN, ms=3.8, zorder=7)
ax.text(2.3, .1, r'$h_2=0$', fontsize=7.5); ax.text(.08, 2.02, r'$\tau=2$', fontsize=7.5, va='bottom'); ax.text(.14, 1.0, r'$\tau=1.9$', fontsize=7.5, color=MUTED, va='center')
clean(ax, (0, 2.95), (0, 2.3), xlabel='$x_1$', ylabel='$x_2$', sub='(a)'); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2]); ax.set_aspect('equal')
ax = axs[1]
X, Y = np.meshgrid(np.linspace(-.2, 2.2, 240), np.linspace(-.6, 3.6, 300))
for b2, col, ls in [(.1, BLUE, '-')]:
    Z = .5*(X-1)**2+.05*(Y-1)**2
    ax.contour(X, Y, Z, levels=[.02, .08, .18, .34, .55], colors=col, linewidths=.7)
Z = .5*(X-1)**2+.05*(Y-2)**2
ax.contour(X, Y, Z, levels=[.02, .08, .18, .34, .55], colors=YELLOW, linewidths=.9, linestyles='--')
opt_point(ax, (1, 1)); ax.plot([1], [2], 'o', color=YELLOW, ms=4, zorder=7)
ax.plot([1, 1], [1, 2], color=GREEN, lw=1.6, zorder=6)
clean(ax, (-.2, 2.2), (-.6, 3.6), xlabel='$x_1$', ylabel='$x_2$', sub='(b)'); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2, 3]); ax.set_aspect('equal')
save(fig, Path(__file__).resolve().parent, 'figure', {'p0': list(p0), 'p1': list(p1)})
print(p0, p1)
