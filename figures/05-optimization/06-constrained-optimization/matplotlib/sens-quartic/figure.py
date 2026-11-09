from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min x^4/4-theta*x: x=cbrt(theta), V=-(3/4)|theta|^(4/3).
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
ax = axs[0]
X = np.linspace(-1.4, 1.4, 301)
ax.plot(X, X**4/4, color=BLUE, lw=1.4); ax.plot(X, X**4/4-.3*X, color=BLUE, lw=1.0, ls='--')
opt_point(ax, (0, 0)); x = .3**(1/3); opt_point(ax, (x, x**4/4-.3*x))
clean(ax, (-1.4, 1.4), (-.4, 1.0), xlabel='$x$', sub='(a)'); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, .5, 1])
T = np.linspace(-1, 1, 2001); C = np.cbrt(T)
ax = axs[1]; ax.plot(T, C, color=GREEN, lw=1.5); opt_point(ax, (0, 0))
clean(ax, (-1, 1), (-1.1, 1.1), xlabel=r'$\theta$', sub='(b)'); ax.set_ylabel(r'$x^{*}(\theta)$', labelpad=1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
ax = axs[2]; ax.plot(T, -.75*np.abs(T)**(4/3), color=BLUE, lw=1.5); opt_point(ax, (0, 0))
clean(ax, (-1, 1), (-.85, .1), xlabel=r'$\theta$', sub='(c)'); ax.set_ylabel(r'$V(\theta)$', labelpad=1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-.75, -.25])
save(fig, Path(__file__).resolve().parent, 'figure', {'x': 'cbrt(theta)', 'V': '-(3/4)|theta|^(4/3)'})
