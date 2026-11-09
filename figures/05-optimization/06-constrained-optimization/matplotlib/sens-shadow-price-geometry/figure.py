from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Near x*=(1.5,.5): budget line moved from tau=2 to 2.4; -grad f = lambda*(1,1).
fig, ax = figure(width_mm=84, height_mm=66)
circles(ax, radii=(np.sqrt(.5), .3))
xs = np.linspace(0, 3.2, 3)
ax.plot(xs, 2-xs, color=ACTIVE, lw=1.6, zorder=4)
ax.plot(xs, 2.4-xs, color=ACTIVE, lw=.95, ls='--', zorder=4)
p0 = np.array([1.5, .5]); p1 = budget(2.4)[0]
ax.annotate('', xy=(2, 1), xytext=p0, arrowprops=dict(arrowstyle='-|>', color=INK, lw=1.0, mutation_scale=7, shrinkA=0, shrinkB=2), zorder=9)
ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=GREEN, lw=1.6, zorder=6)
opt_point(ax, p0); ax.plot([p1[0]], [p1[1]], 'o', color=GREEN, ms=4, zorder=8)
ax.plot([2], [1], marker='x', color=BLUE, ms=4.2, mew=1.1, ls='none', zorder=9)
ax.text(1.42, .38, r'$x^{*}(2)$', fontsize=8, ha='right', va='top')
ax.annotate(r'$x^{*}(2.4)$', xy=p1, xytext=(2.2, .38), fontsize=8, va='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.7, shrinkA=1, shrinkB=3))
ax.text(2.06, 1.0, '$c$', fontsize=8, va='center')
ax.text(.9, 1.6, r'$\tau=2.4$', fontsize=7.5, color=MUTED, ha='left')
ax.text(.72, 1.42, r'$\tau=2$', fontsize=7.5, color=INK, ha='left')
ax.text(1.96, .78, r'$-\nabla f$', fontsize=7.5, ha='left')
ax.set_aspect('equal'); clean(ax, (.5, 2.9), (0, 1.9), xlabel='$x_1$', ylabel='$x_2$')
ax.set_xticks([1, 2]); ax.set_yticks([0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'x(2)': list(p0), 'x(2.4)': list(p1)})
