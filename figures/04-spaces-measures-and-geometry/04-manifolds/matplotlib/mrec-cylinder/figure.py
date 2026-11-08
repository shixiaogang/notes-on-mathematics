"""Cylinder: tangent plane, the graph g over it, and the isometric unrolling."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
from matplotlib.collections import PolyCollection
OUT = Path(__file__).resolve().parent

W, H = 112, 50
fig, ax = canvas(W, H)
rho = 1.0
place = Placed(View(-34, 38), 30, 25, 12.5)
def cyl(x, th):
    return np.stack([x, rho*np.sin(th), rho*np.cos(th)], -1)
X0, X1 = -1.55, 1.55
# surface facets, back to front, only the visible side
xs = np.linspace(X0, X1, 2); ths = np.linspace(-np.pi, np.pi, 241)
TH0 = .85; P0 = .55
polys, dep, col = [], [], []
for a, b in zip(ths[:-1], ths[1:]):
    mid = (a+b)/2
    nrm = np.array([0, np.sin(mid), np.cos(mid)])
    if nrm@place.view.f < -.01:
        continue
    corners = cyl(np.array([X0, X1, X1, X0]), np.array([a, a, b, b]))
    polys.append(place(corners)); dep.append(place.view.depth(cyl(0., mid))); col.append(BLUE_FILL)
order = np.argsort(dep)
ax.add_collection(PolyCollection([polys[k] for k in order], facecolors=[col[k] for k in order], edgecolors=[col[k] for k in order], linewidths=.3, zorder=1))
# silhouette & end circles
tt = np.linspace(-np.pi, np.pi, 721)
for x in (X0, X1):
    pts = cyl(np.full_like(tt, x), tt)
    vis = pts[:, 1]*place.view.f[1]+pts[:, 2]*place.view.f[2] >= 0
    split_plot(ax, place(pts), vis if x == X0 else np.ones_like(tt, bool), STROKE, lw=.85, hidden=False, zorder=2)
for th in (np.arctan2(place.view.f[1], place.view.f[2])+np.pi/2, np.arctan2(place.view.f[1], place.view.f[2])-np.pi/2):
    ax.plot(*place(cyl(np.array([X0, X1]), np.full(2, th))).T, color=STROKE, lw=.85, zorder=2)
# circular patch of geodesic radius rp around p=(0,0,1) in (x, s=rho th)
rp = .72
phi = np.linspace(0, 2*np.pi, 361)
patch = cyl(rp*np.cos(phi), rp*np.sin(phi)/rho)
ax.plot(*place(patch).T, color=RED, lw=1.1, zorder=4)
# tangent plane z=1 above the patch
pl = np.array([[-1.05, -1.05, 1], [1.05, -1.05, 1], [1.05, 1.05, 1], [-1.05, 1.05, 1]], float)
ax.add_patch(Polygon(place(pl), fc='none', ec=YELLOW, lw=1.1, zorder=5))
# samples on the patch, each hanging from its tangent coordinates u = (x, rho sin th)
pts = [(-.4, .62), (.2, .74), (.5, .3), (-.1, -.62), (.5, -.55), (-.55, -.25), (.05, .2)]
for x, th in pts:
    s = cyl(np.array(x), np.array(th))
    t = np.array([x, np.sin(th), 1.])
    ax.plot(*place(np.array([s, t])).T, color=GREEN, lw=.9, zorder=6)
    dot(ax, place(t), GREEN, size=.75, zorder=7, hollow=True); dot(ax, place(s), INK, size=.8, zorder=7)
p = np.array([0, 0, 1.])
dot(ax, place(p), RED, size=1.1, zorder=8)
label(ax, place(p)+(-2.2, 3), r'$\mathbf{p}$', 8, RED, halo=True)
label(ax, place(pl[2])+(5.5, 1.5), r'$T_{\mathbf{p}}M$', 7.5, MUTED)
label(ax, place(cyl(np.array(-.9), np.array(-1.3)))+(0, 0), '$M$', 8, BLUE)
panel_tag(ax, 30, 1.4, '(a)')
# (b) unrolled, s = rho*theta
ux = 13; o = np.array([88, 27])
sx, sy = 2.0*ux, 25.3
R = np.array([[o[0]-sx*.8, o[1]-sy*.75], [o[0]+sx*.8, o[1]-sy*.75], [o[0]+sx*.8, o[1]+sy*.75], [o[0]-sx*.8, o[1]+sy*.75]])
ax.add_patch(Polygon(R, fc=BLUE_FILL, ec=STROKE, lw=.8, zorder=1))
ax.plot(o[0]+ux*rp*np.cos(phi), o[1]+ux*rp*np.sin(phi), color=RED, lw=1.1, zorder=3)
for x, th in pts:
    dot(ax, (o[0]+ux*x, o[1]+ux*th*rho), INK, size=.8, zorder=4)
dot(ax, o, RED, size=1.1, zorder=5)
label(ax, o+(2.2, 1.8), r'$\mathbf{p}$', 8, RED)
label(ax, (o[0], R[0][1]-2.8), '$x$', 7.5, MUTED); label(ax, (R[0][0]-2.6, o[1]), r'$\rho\theta$', 7.5, MUTED)
panel_tag(ax, o[0], 1.4, '(b)')
save(fig, OUT, 'figure', {'formula': 'cylinder x, rho sin th, rho cos th, rho=1; tangent plane z=1; normal drop rho(1-cos th); unrolled (x, rho th)'})
