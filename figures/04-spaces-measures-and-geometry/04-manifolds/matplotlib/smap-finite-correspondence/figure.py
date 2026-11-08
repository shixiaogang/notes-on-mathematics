from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
def axes_box(ax, x0, y0, w, h, xlim, ylim):
    """Plain axes at mm position on the canvas (data coordinates in the returned callable)."""
    sx, sy = w/(xlim[1]-xlim[0]), h/(ylim[1]-ylim[0])
    return (lambda x, y: (x0+(np.asarray(x)-xlim[0])*sx, y0+(np.asarray(y)-ylim[0])*sy))
def axis(ax, a, b, **kw):
    arrow(ax, a, b, color=MUTED, lw=.75, scale=5.5, zorder=2)

"""Curves through the same four data points: f and f+c*prod (x-x_i)^2."""
W, H = 100, 44
fig, ax = canvas(W, H)
xi = np.array([.5, 1.5, 2.5, 3.5]); f = lambda x: .55*x+.3
yi = f(xi)
xlim, ylim = (0, 4), (-.4, 3.3)
T = axes_box(ax, 8, 6, 86, 34, xlim, ylim)
axis(ax, T(0, 0), T(4, 0)); axis(ax, T(0, ylim[0]), T(0, ylim[1]))
x = np.linspace(.1, 3.9, 500); phi = np.prod([(x-a)**2 for a in xi], axis=0)
ax.plot(*T(x, f(x)), color=BLUE, lw=1.4, zorder=3)
u, l = f(x)+.5*phi, f(x)-.5*phi
ku, kl = (u >= ylim[0]) & (u <= ylim[1]), (l >= ylim[0]) & (l <= ylim[1])
ax.plot(*T(x[ku], u[ku]), color=GREEN, lw=1.2, zorder=3); ax.plot(*T(x[kl], l[kl]), color=YELLOW, lw=1.2, zorder=3)
for a, b in zip(xi, yi): dot(ax, T(a, b), INK)
label(ax, T(4, 0)+np.array([-.5, 2.2]), '$x$', 7.5, MUTED, ha='right'); label(ax, T(0, 3.3)+np.array([1.8, -.4]), '$y$', 7.5, MUTED, ha='left')
label(ax, T(3.9, 2.45)+np.array([1, -1.6]), '$f$', 7.5, BLUE, ha='left')
label(ax, T(2.0, 1.55)+np.array([0, 3.1]), r'$f+\frac{1}{2}\varphi$', 7.5, GREEN, halo=True)
label(ax, T(2.0, 1.07)+np.array([1.3, -3.2]), r'$f-\frac{1}{2}\varphi$', 7.5, YELLOW, halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=.55x+.3, phi=prod (x-xi)^2, xi=.5,1.5,2.5,3.5'})
