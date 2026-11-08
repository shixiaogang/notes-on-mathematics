"""Longitude-latitude chart: the pole is blown up to a whole edge and the seam meridian is cut."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common'))
from mfd3d import *

W, H = 104, 50
fig, ax = canvas(W, H)
LAT = np.radians(62)
pl = Placed(View(-30, 24), 25, 26, 19.5)
sphere_disc(ax, pl)
for d in (-60, -30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(d)), MUTED, lw=.5, hidden=False)
for lon in np.radians(np.arange(-150, 180, 30)):
    sphere_curve(ax, pl, meridian(lon), MUTED, lw=.5, hidden=False)
sphere_curve(ax, pl, meridian(np.pi), RED, lw=1.4, hidden_lw=.7)
sphere_curve(ax, pl, parallel(LAT), BLUE, lw=1.4)
N = pl([0, 0, 1])
dot(ax, N, INK)
label(ax, N+[0, 3.1], '$N$')
A = pl(spherical(LAT, np.pi))
dot(ax, A, RED, size=1.3)
# Chart rectangle: lambda horizontal, phi vertical.
x0, x1, y0, y1 = 58, 100, 9, 43
xlon = lambda v: x0+(v+np.pi)/(2*np.pi)*(x1-x0)
ylat = lambda v: y0+(v+np.pi/2)/np.pi*(y1-y0)
ax.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fc=BLUE_FILL, ec='none', zorder=1))
for d in (-60, -30, 0, 30, 60):
    ax.plot([x0, x1], [ylat(np.radians(d))]*2, color=MUTED, lw=.5, zorder=2)
for d in range(-150, 180, 30):
    ax.plot([xlon(np.radians(d))]*2, [y0, y1], color=MUTED, lw=.5, zorder=2)
ax.plot([x0, x0], [y0, y1], color=RED, lw=1.4, zorder=3)
ax.plot([x1, x1], [y0, y1], color=RED, lw=1.4, zorder=3)
ax.plot([x0, x1], [y1, y1], color=INK, lw=1.4, zorder=3)
ax.plot([x0, x1], [y0, y0], color=STROKE, lw=.95, zorder=3)
ax.plot([x0, x1], [ylat(LAT)]*2, color=BLUE, lw=1.4, zorder=4)
dot(ax, (x0, ylat(LAT)), RED, size=1.3); dot(ax, (x1, ylat(LAT)), RED, size=1.3)
mixed(ax, ((x0+x1)/2, y1+1.8), ['整条上边都对应', '$N$'])
label(ax, (x0, y0-2.8), r'$-\pi$', 7.5, MUTED); label(ax, (x1, y0-2.8), r'$\pi$', 7.5, MUTED)
label(ax, ((x0+x1)/2, y0-2.8), r'$\lambda$', 7.5, MUTED)
label(ax, (x0-3, y1-5), r'$\phi$', 7.5, MUTED)
arrow(ax, (46.5, 26), (53.5, 26), rad=None)
label(ax, (50, 28.6), r'$(\lambda,\phi)$', 7.5, MUTED)
panel_tag(ax, 25, 1.5, '(a)'); panel_tag(ax, (x0+x1)/2, 1.5, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=(cos(phi)cos(lambda), cos(phi)sin(lambda), sin(phi)); orthographic view az=-30, el=24; blue latitude 62 degrees'})
