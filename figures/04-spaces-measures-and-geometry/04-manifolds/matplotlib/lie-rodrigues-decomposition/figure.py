"""Rodrigues: e1 split along the axis (1,1,1)/sqrt3, rotated by 120 degrees to e2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 80, 62
fig, ax = canvas(W, H)
view = View(-28, 26)
pl = Placed(view, 30, 22, 32)
u = np.array([1, 1, 1.0])/np.sqrt(3)
x = np.array([1.0, 0, 0])
xpar = (x@u)*u
xper = x-xpar
w = np.cross(u, xper)
th = 2*np.pi/3
xrot = xpar+np.cos(th)*xper+np.sin(th)*w
for e, name in zip(np.eye(3), ('$e_1$', '$e_2$', '$e_3$')):
    arrow(ax, pl(0*e), pl(1.05*e), color=MUTED, lw=.7, scale=5, zorder=3)
ts = np.linspace(0, 2*np.pi, 241)
circ = xpar+np.cos(ts)[:, None]*xper+np.sin(ts)[:, None]*w
ax.plot(*pl(circ).T, color=GRID, lw=.7, zorder=2)
arc = xpar+np.cos(np.linspace(0, th, 80))[:, None]*xper+np.sin(np.linspace(0, th, 80))[:, None]*w
ax.plot(*pl(arc).T, color=YELLOW, lw=1.4, zorder=4)
arrow(ax, pl(arc[-8]), pl(arc[-1]), color=YELLOW, lw=1.2, scale=7, zorder=5)
ax.plot(*pl(np.array([-.25*u, 1.5*u])).T, color=STROKE, lw=.85, ls=(0, (3, 2)), zorder=2)
arrow(ax, pl(1.42*u), pl(1.5*u), color=STROKE, lw=.85, scale=6)
arrow(ax, pl(0*u), pl(x), color=BLUE, lw=1.3, scale=7, zorder=6)
arrow(ax, pl(0*u), pl(xrot), color=BLUE, lw=1.3, scale=7, zorder=6)
arrow(ax, pl(xpar), pl(x), color=GREEN, lw=1.15, scale=6.5, zorder=6)
arrow(ax, pl(xpar), pl(xrot), color=GREEN, lw=1.15, scale=6.5, zorder=6)
arrow(ax, pl(xpar), pl(xpar+.5*w), color=RED, lw=1.15, scale=6.5, zorder=6)
arrow(ax, pl(0*u), pl(xpar), color=PURPLE, lw=1.3, scale=7, zorder=7)
dot(ax, pl(xpar), INK, size=1.2, zorder=8)
L = lambda P, d, t, c=INK, **k: label(ax, pl(P)+np.array(d), t, color=c, halo=True, **k)
L(x, (-6.8, -1.0), r'$x=e_1$', BLUE)
L(xrot, (4.6, 2.0), r'$Rx=e_2$', BLUE)
L(np.array([0, 0, 1.0]), (3.5, 2.6), '$e_3$', MUTED, size=7.5)
L(.55*xpar, (-4.0, 2.4), r'$x_\parallel$', PURPLE)
L(xpar+.6*xper, (-.3, -3.4), r'$x_\perp$', GREEN)
L(xpar+.5*w, (4.2, -2.4), r'$u\times x_\perp$', RED)
L(1.48*u, (3.2, 2.0), '$u$', STROKE)
dot(ax, pl(0*u), INK, size=1.1, zorder=8)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'u=(1,1,1)/sqrt3, x=e1, x_par=(1,1,1)/3, x_perp=(2,-1,-1)/3, theta=2pi/3, Rx=x_par+cos x_perp+sin u x x_perp=e2'})
