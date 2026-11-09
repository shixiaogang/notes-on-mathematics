from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=108, height_mm=48, ncols=2)
ax = axs[0]; fn = lambda t: .5*t**2+.1; X_ = np.linspace(-.8, 1.9, 300); x = 1.2; g = x; s = -.8
ax.plot(X_, fn(X_), color=BLUE, lw=1.4); ax.plot([-.8, 1.9], [fn(x)+g*(-.8-x), fn(x)+g*(1.9-x)], color=YELLOW, lw=1.3)
ax.plot([x, x], [-1.75, fn(x)], color=MUTED, lw=.75, ls=(0, (1, 1.5))); dot(ax, (x, fn(x)), GREEN, ms=4.8); dot(ax, (0, fn(0)), RED)
ly = fn(x)+g*(s-x); hollow(ax, (s, ly), PURPLE, ms=4.8); ax.plot([1.45, 1.45], [ly, fn(x)], color=PURPLE, lw=1.3); ax.plot([s, 1.45], [ly, ly], color=PURPLE, lw=.75, ls=(0, (2, 2))); ax.plot([x, 1.45], [fn(x), fn(x)], color=PURPLE, lw=.75, ls=(0, (2, 2)))
ax.text(1.5, (ly+fn(x))/2, '$\\Gamma(x)$', color=PURPLE, fontsize=8, va='center')
ax.plot([-.8, 1.9], [-2.0, -2.0], color=EDGE, lw=2)
setup(ax, (-.95, 2.45), (-2.2, 2.2), [-.8, 0, 1.2, 1.9], [-2, 0, 2], xl='$x$'); ax.set_xticklabels(['$s$', '$x^*$', '$x$', ''])
ax = axs[1]; X_ = np.linspace(-1, 2, 300); ax.plot(X_, -X_**2, color=BLUE, lw=1.4); ax.plot([-1, 2], [0, 0], color=YELLOW, lw=1.3); hollow(ax, (0, 0), RED); dot(ax, (2, -4), RED)
ax.plot([-1, 2], [-4.5, -4.5], color=EDGE, lw=2)
setup(ax, (-1.2, 2.2), (-4.7, .6), [-1, 0, 1, 2], [-4, -2, 0], xl='$x$')
panels(fig, .08, .985, .98, .23, .24); tags(fig, axs)
save(fig, HERE, 'figure', {'left': 'f=x^2/2+0.1 on [-0.8,1.9], x=1.2', 'right': 'f=-x^2 on [-1,2]'})
