"""Diffeomorphism F(y)=(2y1,y2,y3/2) from the unit sphere to an ellipsoid; p=(0,3/5,4/5) and two tangent vectors."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
A = np.array([2.0, 1.0, .5])
W, H = 112, 44
fig, ax = canvas(W, H)
view = View(115, 28)
unit = 14.5
S = Placed(view, 18.5, 25, unit); T = Placed(view, 79, 25, unit)
inv_f = view.f/A
# ellipsoid outline: y on the great circle orthogonal to A^{-1}f, mapped by A
n = inv_f/np.linalg.norm(inv_f)
e1 = np.cross(n, [.2, .3, .9]); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
s = np.linspace(0, 2*np.pi, 721)
circ = np.cos(s)[:, None]*e1+np.sin(s)[:, None]*e2
ax.add_patch(Polygon(T(A*circ), fc=BLUE_FILL, ec=STROKE, lw=.95, zorder=1))
sphere_disc(ax, S)
def on_both(pts, color, lw=1.2, zorder=3, hidden=False):
    split_plot(ax, S(pts), pts@view.f >= 0, color, lw=lw, hidden=hidden, zorder=zorder)
    split_plot(ax, T(A*pts), pts@inv_f >= 0, color, lw=lw, hidden=hidden, zorder=zorder)
for lat in (-60, -30, 0, 30, 60):
    on_both(parallel(np.radians(lat)), MUTED, lw=.4)
for lon in (0, 60, 120, 180, 240, 300):
    on_both(meridian(np.radians(lon)), MUTED, lw=.4)
p = np.array([0, .6, .8]); v = np.array([.2, 0, 0]); w = np.array([0, -.16, .12])
lat0 = np.arcsin(.8)
on_both(parallel(lat0), GREEN, lw=1.2)
on_both(meridian(np.pi/2), BLUE, lw=1.2)
k = 2.4
P = S(p); Q = T(A*p)
arrow(ax, P, S(p+k*v), color=RED, lw=1.4, scale=7, zorder=8)
arrow(ax, P, S(p+k*w), color=YELLOW, lw=1.4, scale=7, zorder=8)
arrow(ax, Q, T(A*(p+k*v)), color=RED, lw=1.4, scale=7, zorder=8)
arrow(ax, Q, T(A*(p+k*w)), color=YELLOW, lw=1.4, scale=7, zorder=8)
dot(ax, P, INK, zorder=9); dot(ax, Q, INK, zorder=9)
label(ax, P+[2.8, -2.4], '$p$', halo=True)
label(ax, Q+[6.5, -2.6], '$F(p)$', halo=True)
label(ax, S(p+k*v)+[-.8, 2.6], '$v$', color=RED, halo=True)
label(ax, S(p+k*w)+[2.6, .8], '$w$', color=YELLOW, halo=True)
label(ax, T(A*(p+k*v))+[1.5, 3.0], r'$\mathrm{d}F_p(v)$', 7.5, color=RED, halo=True)
label(ax, T(A*(p+k*w))+[8.5, 1.6], r'$\mathrm{d}F_p(w)$', 7.5, color=YELLOW, halo=True)
arrow(ax, (36, 33), (49.5, 33), color=STROKE, lw=.9, rad=-.18)
arrow(ax, (49.5, 24), (36, 24), color=STROKE, lw=.9, rad=-.18)
label(ax, (42.8, 37.5), '$F$'); label(ax, (42.8, 19.2), '$F^{-1}$')
panel_tag(ax, 18.5, 1.6, '(a)'); panel_tag(ax, 79, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F(y)=(2y1,y2,y3/2); p=(0,.6,.8); v=(.2,0,0); w=(0,-.16,.12); vectors drawn 2.4x true length'})
