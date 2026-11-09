"""Two smooth extensions of sin x from [0,inf) agree in value and slope at the boundary point 0."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 84, 44
fig, ax = canvas(W, H)
ox, oy, sx, sy = 40, 16.5, 12.5, 12.5
X = lambda x: ox+sx*np.asarray(x); Y = lambda y: oy+sy*np.asarray(y)
arrow(ax, (X(-2.9), oy), (X(3.1), oy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (ox, Y(-1.1)), (ox, Y(1.9)), color=MUTED, lw=.75, scale=5.5)
label(ax, (X(3.05), oy+2.3), '$x$', 7.5, MUTED)
f = lambda x: np.sin(x)
bump = lambda x: 1.6*np.exp(-1/np.maximum(x**2, 1e-9))
xp = np.linspace(0, 2.72, 200); xn = np.linspace(-2.65, 0, 300)
ax.plot(X(xn), Y(f(xn)), color=BLUE, lw=1.0, ls=(0, (3, 2)), zorder=3)
ax.plot(X(xn), Y(f(xn)+bump(xn)), color=GREEN, lw=1.0, ls=(0, (3, 2)), zorder=3)
ax.plot(X(xp), Y(f(xp)), color=INK, lw=1.4, zorder=5)
t = np.array([-.95, 1.0])
ax.plot(X(t), Y(t), color=RED, lw=.95, zorder=4)
dot(ax, (ox, oy), INK, zorder=8)
label(ax, (X(1.75), Y(1.12)), r'$\sin x$', 7.5, INK, halo=True)
label(ax, (X(-2.2), Y(-.95)), r'$E_1$', 7.5, BLUE, halo=True)
label(ax, (X(-2.2), Y(.92)), r'$E_2$', 7.5, GREEN, halo=True)
label(ax, (X(.62), Y(.97)), '$y=x$', 7.5, RED, halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sin x on x>=0; E1=sin x; E2=sin x+1.6 exp(-1/x^2) for x<0; common slope 1 at 0'})
