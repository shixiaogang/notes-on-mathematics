"""One family of equal geodesic caps on the unit sphere and their exact images in the (theta,phi) chart and the north stereographic chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
r = .2
centres = [(t, f) for t in (.6435, 1.25, 1.9, 2.5) for f in (np.pi/2-1.1, np.pi/2, np.pi/2+1.1)]
def sph(t, f):
    return np.array([np.sin(t)*np.cos(f), np.sin(t)*np.sin(f), np.cos(t)])
def cap(c):
    return cap_boundary(sph(*c), r, 361)
is_p = lambda c: abs(c[0]-.6435) < 1e-6 and abs(c[1]-np.pi/2) < 1e-6
# (a) the sphere
pl = Placed(View(78, 24), 20.5, 28, 17.5)
sphere_disc(ax, pl, fill='white')
for lat in (-60, -30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), GRID, lw=.5, hidden=False, zorder=2)
for c in centres:
    b = cap(c)
    if pl.view.depth(sph(*c)) < .3:
        continue
    ax.add_patch(Polygon(pl(b), fc=RED_FILL if is_p(c) else BLUE_FILL, ec=RED if is_p(c) else BLUE, lw=.9, zorder=3))
t0 = .6435; p = sph(t0, np.pi/2)
et = np.array([np.cos(t0)*0, np.cos(t0)*1, -np.sin(t0)]); ef = np.array([-1.0, 0, 0])
s = .55
arrow(ax, pl(p), pl(p+s*et), color=GREEN, lw=1.3, scale=7)
arrow(ax, pl(p), pl(p+s*.6*ef), color=YELLOW, lw=1.3, scale=7)
dot(ax, pl(p), INK)
label(ax, pl(p)+[1.5, 2.8], '$p$', halo=True)
label(ax, pl(p+s*et)+[3.4, -1.0], r'$\partial_\theta$', color=GREEN, halo=True)
label(ax, pl(p+s*.6*ef)+[3.0, 1.8], r'$\partial_\phi$', color=YELLOW, halo=True)
panel_tag(ax, 20.5, 3, '(a)')
# (b) the (phi, theta) chart, theta increasing downward
x0, y1, sc = 46.0, 44.5, 9.0
def B(tf):
    tf = np.atleast_2d(tf)
    return np.c_[x0+sc*tf[:, 1], y1-sc*tf[:, 0]]
ax.plot(*np.array([[x0, y1], [x0+sc*np.pi, y1], [x0+sc*np.pi, y1-sc*np.pi], [x0, y1-sc*np.pi], [x0, y1]]).T, color=STROKE, lw=.8, zorder=2)
for c in centres:
    b = cap(c); tf = np.c_[np.arccos(np.clip(b[:, 2], -1, 1)), np.mod(np.arctan2(b[:, 1], b[:, 0]), 2*np.pi)]
    ax.add_patch(Polygon(B(tf), fc=RED_FILL if is_p(c) else BLUE_FILL, ec=RED if is_p(c) else BLUE, lw=.9, zorder=3))
P = B([t0, np.pi/2])[0]
arrow(ax, P, P+[0, -sc*s], color=GREEN, lw=1.3, scale=7)
arrow(ax, P, P+[sc*s, 0], color=YELLOW, lw=1.3, scale=7)
dot(ax, P, INK)
label(ax, P+[-2.6, 1.8], '$p$', halo=True)
label(ax, P+[2.8, -sc*s+.4], r'$\partial_\theta$', color=GREEN, halo=True)
label(ax, P+[sc*s+.8, 2.2], r'$\partial_\phi$', color=YELLOW, halo=True)
label(ax, (x0+sc*np.pi/2, y1+2.4), r'$\phi$', 7.5, MUTED); label(ax, (x0-2.4, y1-sc*np.pi/2), r'$\theta$', 7.5, MUTED)
panel_tag(ax, x0+sc*np.pi/2, 3, '(b)')
# (c) north stereographic chart
c0 = np.array([94.5, 12.0]); s2 = 3.0
def C(y):
    return c0+s2*(y[:, :2]/(1-y[:, 2])[:, None])
arrow(ax, c0+[-s2*4.8, 0], c0+[s2*4.8, 0], color=MUTED, lw=.75, scale=5.5)
arrow(ax, c0+[0, -1.2], c0+[0, s2*5.0], color=MUTED, lw=.75, scale=5.5)
label(ax, c0+[s2*4.8-1, 2.2], '$u_1$', 7.5, MUTED); label(ax, c0+[2.8, s2*5.0], '$u_2$', 7.5, MUTED)
for c in centres:
    ax.add_patch(Polygon(C(cap(c)), fc=RED_FILL if is_p(c) else BLUE_FILL, ec=RED if is_p(c) else BLUE, lw=.9, zorder=3))
Q = C(p[None])[0]
dot(ax, Q, INK)
label(ax, Q+[-3.2, 0], '$p$', halo=True)
panel_tag(ax, c0[0], 3, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'equal caps of angular radius 0.2 on S^2 and exact images under (theta,phi) and sigma_N; p=(0,3/5,4/5)'})
