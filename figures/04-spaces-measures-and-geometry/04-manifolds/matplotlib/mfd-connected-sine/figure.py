"""Left: coordinate balls chained along a path on the sphere. Right: the topologist sine curve, connected but not path connected."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 104, 46
fig, ax = canvas(W, H)
pl = Placed(View(5, 20), 22, 25, 18)
sphere_disc(ax, pl, fill='white')
s = np.linspace(0, 1, 401)
lat = lambda a: np.radians(-32+58*a+9*np.sin(2*np.pi*a))
lon = lambda a: np.radians(-40+84*a)
path = spherical(lat(s), lon(s))
cs = [spherical(lat(a), lon(a)) for a in np.linspace(0, 1, 6)]
caps = [cap_boundary(c, np.radians(16.5), 361) for c in cs]
for b in caps:
    ax.add_patch(Polygon(pl(b), fc=BLUE_FILL, ec='none', zorder=2))
for b in caps:
    ax.plot(*pl(b).T, color=BLUE, lw=.85, zorder=3)
ax.plot(*pl(path).T, color=INK, lw=1.3, zorder=4)
dot(ax, pl(cs[0]), INK); dot(ax, pl(cs[-1]), INK)
label(ax, pl(cs[0])+[-3.2, -1.5], '$p$', halo=True); label(ax, pl(cs[-1])+[2.8, 1.5], '$q$', halo=True)
# (b) sin(1/x), sampled in 1/x so that the oscillation is resolved.
x0, y0, X, Yv = 56, 23, 43, 14
tt = np.linspace(1, 90, 40000)
xs, ys = 1/tt, np.sin(tt)
ax.plot(x0+X*xs, y0+Yv*ys, color=BLUE, lw=.65, zorder=3)
ax.plot([x0, x0], [y0-Yv, y0+Yv], color=RED, lw=1.5, zorder=4)
arrow(ax, (x0-2.5, y0), (x0+X+4.5, y0), color=MUTED, lw=.75)
ax.plot([x0+X]*2, [y0-1, y0+1], color=MUTED, lw=.75)
label(ax, (x0+X, y0-3), '$1$', 7.5, MUTED); label(ax, (x0+X+3.5, y0-3), '$y_1$', 7.5, MUTED)
label(ax, (x0-3.4, y0+Yv), '$1$', 7.5, MUTED); label(ax, (x0-3.4, y0-Yv), '$-1$', 7.5, MUTED)
panel_tag(ax, 22, 1.6, '(a)'); panel_tag(ax, x0+X/2, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'caps of angular radius 16.5 deg along an analytic latitude-longitude path; y2=sin(1/y1), 1/y1 in [1,90]'})
