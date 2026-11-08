"""The stabilizer of e3 (frames rotating about N) and its left translate R H (frames over p, all sending e3 to p)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 54
fig, ax = canvas(W, H)
view = View(50, 24)
pa, pb = Placed(view, 27, 25, 19), Placed(view, 79, 25, 19)
N = np.array([0, 0, 1.0])
lat, lon = np.radians(24), np.radians(112)
p = spherical(lat, lon)
e1p = np.cross(N, p); e1p /= np.linalg.norm(e1p)   # first column of R
e2p = np.cross(p, e1p)                              # second column of R
R = np.column_stack([e1p, e2p, p])
assert abs(np.linalg.det(R)-1) < 1e-12
PHI = (0.0, 2*np.pi/3, 4*np.pi/3)
COL = (BLUE, GREEN, PURPLE)
def frame(place, centre, a, b, phi, c, L=.5):
    v = np.cos(phi)*a+np.sin(phi)*b
    arrow(ax, place(centre), place(centre+L*v), color=c, lw=1.15, scale=6.5, zorder=8)
def patch(place, centre, a, b, h=.56):
    pts = np.array([centre+s*h*a+t*h*b for s, t in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    ax.add_patch(Polygon(place(pts), closed=True, fc=YELLOW_FILL, ec=YELLOW, lw=.7, zorder=4))
for pl in (pa, pb):
    sphere_disc(ax, pl)
    sphere_curve(ax, pl, parallel(0.0), MUTED, lw=.6, hidden_lw=.45)
# (a) the stabilizer at N: the frames turn about the axis, N stays put.
patch(pa, N, np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
for phi, c in zip(PHI, COL):
    frame(pa, N, np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), phi, c)
arrow(ax, pa(N), pa(1.42*N), color=RED, lw=1.15, scale=6.5, zorder=8)
dot(ax, pa(N), INK, zorder=9)
label(ax, pa(N)+[-3.6, -1.8], '$N$', halo=True, zorder=10)
label(ax, pa(1.42*N)+[3.6, -.4], '$e_3$', color=RED)
# (b) left translate: the same three frames carried to p by R.
patch(pb, p, e1p, e2p)
for phi, c in zip(PHI, COL):
    frame(pb, p, e1p, e2p, phi, c)
arrow(ax, pb(p), pb(p+.5*p), color=RED, lw=1.15, scale=6.5, zorder=8)
dot(ax, pb(p), INK, zorder=9)
label(ax, pb(p)+[3.4, -2.0], '$p$', halo=True, zorder=10)
label(ax, pb(p+.5*p)+[1.5, 2.6], r'$Re_3$', color=RED)
dot(ax, pb(N), MUTED, size=1.0)
label(ax, pb(N)+[-3.4, 1.4], '$N$', 7.5, MUTED)
panel_tag(ax, 27, 1.5, '(a)'); panel_tag(ax, 79, 1.5, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'frames (cos phi a + sin phi b, Re3) for phi=0,2pi/3,4pi/3; p=(lat 24deg, lon 112deg); R=[e1,e2,p]'})
