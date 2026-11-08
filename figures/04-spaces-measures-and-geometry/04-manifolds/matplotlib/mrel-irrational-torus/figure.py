"""Injective immersion of R into the torus with irrational slope sqrt 2: square picture, torus picture."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 58
fig, ax = canvas(W, H)
sq = 40.; x0 = 6.; y0 = 11.
ax.plot([x0, x0+sq, x0+sq, x0, x0], [y0, y0, y0+sq, y0+sq, y0], color=STROKE, lw=.95, zorder=2)
T = 2*np.pi*12
n = 40000
t = np.linspace(0, T, n)
a = (t % (2*np.pi))/(2*np.pi); b = (np.sqrt(2)*t % (2*np.pi))/(2*np.pi)
jumps = np.r_[False, (np.abs(np.diff(a)) > .5) | (np.abs(np.diff(b)) > .5)]
idx = np.flatnonzero(jumps)
for i0, i1 in zip(np.r_[0, idx], np.r_[idx, n]):
    ax.plot(x0+sq*a[i0:i1], y0+sq*b[i0:i1], color=BLUE, lw=.8, zorder=3)
dot(ax, (x0, y0), INK, size=1.5)
for k, col in ((5, RED), (12, GREEN)):
    f = (np.sqrt(2)*k) % 1
    dot(ax, (x0, y0+sq*f), col, size=1.4, zorder=8)
label(ax, (x0-3, y0-.5), '$0$', 7.5, MUTED); label(ax, (x0+sq+1.5, y0-3.2), r'$2\pi$', 7.5, MUTED)
label(ax, (x0+sq/2, y0-3.5), r'$\theta_1$', 7.5, MUTED); label(ax, (x0-3.2, y0+sq/2), r'$\theta_2$', 7.5, MUTED)
label(ax, (x0-3, y0+sq*(np.sqrt(2)*5 % 1)), '$5$', 7.5, RED)
label(ax, (x0-3.6, y0+sq*(np.sqrt(2)*12 % 1)-1), '$12$', 7.5, GREEN)
panel_tag(ax, x0+sq/2, 1.6, '(a)')
view = View(30, 38)
pl = Placed(view, 84, 27, 8.0)
tor = Torus(pl, R=2.0, r=.82)
tor.fill(ax, lambda th, ph: BLUE_FILL)
tor.silhouette(ax)
tt = np.linspace(0, T, 18000)
tor.curve(ax, tt, np.sqrt(2)*tt, BLUE, lw=.7, hidden=False, zorder=3)
def mark(th, ph, col):
    P = tor.point(np.array([th]), np.array([ph]))
    dot(ax, pl(P)[0], col, size=1.3, zorder=9)
mark(0, 0, INK)
mark(0, 2*np.pi*((np.sqrt(2)*5) % 1), RED)
mark(0, 2*np.pi*((np.sqrt(2)*12) % 1), GREEN)
panel_tag(ax, 84, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'gamma(t)=(t, sqrt2 t) mod 2pi for t in [0,24pi]; red, green: t=10pi, 24pi at theta1=0'})
