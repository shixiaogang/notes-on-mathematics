"""North stereographic chart: coordinate cells, their images on the sphere, and the density 4/(1+r^2)^2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
inv = lambda u1, u2: np.c_[2*u1, 2*u2, u1**2+u2**2-1]/(u1**2+u2**2+1)[:, None]
# (a) chart
c = np.array([20., 26.]); s = 4.0
for k in range(-4, 5):
    ax.plot([c[0]+k*s]*2, [c[1]-4*s, c[1]+4*s], color=BLUE, lw=.55, zorder=1)
    ax.plot([c[0]-4*s, c[0]+4*s], [c[1]+k*s]*2, color=BLUE, lw=.55, zorder=1)
def cell(cx, cy, h=.5):
    return [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)]
cells = [(0, 1, YELLOW, YELLOW_FILL), (0, 3, RED, RED_FILL)]
for cx, cy, col, fil in cells:
    ax.add_patch(Polygon([c+s*np.array(pp) for pp in cell(cx, cy)], fc=fil, ec=col, lw=1.1, zorder=3))
label(ax, c+s*np.array([0, 1]), '$A$', 7.5, halo=True); label(ax, c+s*np.array([0, 3]), '$B$', 7.5, halo=True)
arrow(ax, c-[0, 4*s+.1], c+[0, 4.5*s], color=MUTED, lw=.75, scale=5.5); arrow(ax, c-[4*s+.1, 0], c+[4.5*s, 0], color=MUTED, lw=.75, scale=5.5)
label(ax, c+[4.5*s+.2, 2.2], '$u_1$', 7.5, MUTED); label(ax, c+[2.6, 4.5*s], '$u_2$', 7.5, MUTED)
panel_tag(ax, c[0], 1.7, '(a)')
# (b) sphere
pl = Placed(View(90, 8), 61, 26, 19)
sphere_disc(ax, pl)
tt = np.tan(np.linspace(-1.5707, 1.5707, 1601))
for k in range(-2, 3):
    sphere_curve(ax, pl, inv(np.full_like(tt, k), tt), BLUE, lw=.4, hidden=False)
    sphere_curve(ax, pl, inv(tt, np.full_like(tt, k)), BLUE, lw=.4, hidden=False)
for cx, cy, col, fil in cells:
    h = .5
    uu = np.r_[np.linspace(cx-h, cx+h, 30), np.full(30, cx+h), np.linspace(cx+h, cx-h, 30), np.full(30, cx-h)]
    vv = np.r_[np.full(30, cy-h), np.linspace(cy-h, cy+h, 30), np.full(30, cy+h), np.linspace(cy+h, cy-h, 30)]
    pts = inv(uu, vv)
    ax.add_patch(Polygon(pl(pts), fc=fil, ec=col, lw=1.1, zorder=3))
pA = pl(inv(np.array([0.]), np.array([1.])))[0]; pB = pl(inv(np.array([0.]), np.array([3.])))[0]
label(ax, pA, '$A$', 7.5, halo=True); label(ax, pB+[0,4.6], '$B$', 7.5, halo=True)
panel_tag(ax, 61, 1.7, '(b)')
# (c) density
x0, y0 = 90, 9; sx, sy = 4.2, 7.5
G = lambda r, v: np.c_[x0+sx*r, y0+sy*v]
arrow(ax, G(0, 0)[0], G(4.5, 0)[0], color=MUTED, lw=.75, scale=5.5); arrow(ax, G(0, 0)[0], G(0, 4.8)[0], color=MUTED, lw=.75, scale=5.5)
label(ax, G(4.5, 0)[0]+[.5, 2.2], '$r$', 7.5, MUTED)
r = np.linspace(0, 4.3, 300); ax.plot(*G(r, 4/(1+r**2)**2).T, color=BLUE, lw=1.4, zorder=3)
dot(ax, G(1, 1)[0], YELLOW, size=1.3); dot(ax, G(3, .04)[0], RED, size=1.3)
for rr, nm in ((1, '$1$'), (3, '$3$')):
    ax.plot([G(rr, 0)[0, 0]]*2, [y0-1, y0+1], color=MUTED, lw=.75); label(ax, G(rr, 0)[0]+[0, -2.7], nm, 7.5, MUTED)
ax.plot([x0-1, x0+1], [G(0, 4)[0, 1]]*2, color=MUTED, lw=.75); label(ax, G(0, 4)[0]+[-2.6, 0], '$4$', 7.5, MUTED)
panel_tag(ax, x0+sx*2, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sqrt(det G)=4/(1+r^2)^2 in the north stereographic chart; A=[-.5,.5]x[.5,1.5], B=[-.5,.5]x[2.5,3.5]'})
