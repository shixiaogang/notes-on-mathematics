from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
a = .25; X_ = np.linspace(-1, 2, 601); G = (X_-np.clip(X_+2*a*X_, -1, 2))/a
fig, axs = figure(width_mm=108, height_mm=46, ncols=2)
ax = axs[0]; ax.plot(X_, -X_**2, color=BLUE, lw=1.4)
ax.plot([-1, 2], [-4.5, -4.5], color=EDGE, lw=2)
for p in (-1, 0): hollow(ax, (p, -p**2), RED, ms=4.8)
dot(ax, (2, -4), RED)
setup(ax, (-1.2, 2.2), (-4.7, .4), [-1, 0, 1, 2], [-4, -2, 0], xl='$x$', yl='$f(x)$')
ax = axs[1]; ax.plot(X_, G, color=GREEN, lw=1.4); ax.axhline(0, color=MUTED, lw=.85)
for p in (-1, 0): hollow(ax, (p, 0), RED, ms=4.8)
dot(ax, (2, 0), RED)
setup(ax, (-1.2, 2.2), None, [-1, 0, 1, 2], [-2, 0, 2], xl='$x$', yl='$G_\\alpha(x)$')
panels(fig, .09, .985, .98, .25, .32); tags(fig, axs)
save(fig, HERE, 'figure', {'f': '-x^2 on [-1,2]', 'alpha': a, 'stationary': [-1, 0, 2]})
