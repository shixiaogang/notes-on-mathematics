"""Two charts on overlapping caps of the unit sphere and the transition between their images.

Each chart is the orthogonal projection of a spherical cap onto the tangent plane at the cap centre,
so the two discs and the lens in the planes are the true images of the regions drawn on the sphere.
"""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common'))
from mfd3d import *

W, H = 112, 66
fig, ax = canvas(W, H)
pl = Placed(View(-55, 24), 56, 44.5, 19.5)
sphere_disc(ax, pl, fill='white')
c1 = spherical(np.radians(22), np.radians(-77)); c2 = spherical(np.radians(22), np.radians(-33))
r1 = r2 = np.radians(36)
b1, b2 = cap_boundary(c1, r1), cap_boundary(c2, r2)
def lens(a, b, ca, cb, ra, rb):
    pts = np.r_[a[a@cb >= np.cos(rb)], b[b@ca >= np.cos(ra)]]
    return pts
L = lens(b1, b2, c1, c2, r1, r2)
def order(pts2):
    c = pts2.mean(0); return pts2[np.argsort(np.arctan2(*(pts2-c).T[::-1]))]
ax.add_patch(Polygon(pl(b1), fc=BLUE_FILL, ec=BLUE, lw=1.2, zorder=2))
ax.add_patch(Polygon(pl(b2), fc=GREEN_FILL, ec=GREEN, lw=1.2, zorder=2))
ax.add_patch(Polygon(order(pl(L)), fc=YELLOW_FILL, ec='none', zorder=2.2))
ax.plot(*pl(b1).T, color=BLUE, lw=1.2, zorder=2.4); ax.plot(*pl(b2).T, color=GREEN, lw=1.2, zorder=2.4)
p3 = spherical(np.radians(20), np.radians(-55))
dot(ax, pl(p3), INK); label(ax, pl(p3)+[2.3, 2.1], '$p$')
label(ax, pl(c1)+[-5.8, -2.5], '$U$', color=BLUE); label(ax, pl(c2)+[6.5, -2.5], '$V$', color=GREEN)
label(ax, (56+18.5, 44.5+15.5), '$M$', color=MUTED)
for lat in (-40, -10, 20, 50, 75):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.4, hidden=False, zorder=2.6)
for lon in range(0, 180, 30):
    for sign in (0, 180):
        sphere_curve(ax, pl, meridian(np.radians(lon+sign)), MUTED, lw=.4, hidden=False, zorder=2.6)

def chart(center):
    e1 = np.cross([0, 0, 1], center); e1 /= np.linalg.norm(e1)
    e2 = np.cross(center, e1)
    return lambda P: np.stack([np.asarray(P)@e1, np.asarray(P)@e2], -1)
phi, psi = chart(c1), chart(c2)
scale = 17.0
left = np.array([21, 16.2]); right = np.array([91, 16.2])
def panel(c, a, b, cc, cd, col, fill, tag, cname):
    x, y = c
    ax.add_patch(Polygon([(x-15.5, y-12.2), (x+15.5, y-12.2), (x+15.5, y+12.2), (x-15.5, y+12.2)], fc='white', ec=MUTED, lw=.75, zorder=1))
    ax.add_patch(Polygon(c+scale*a, fc=fill, ec=col, lw=1.2, zorder=2))
    q = np.r_[a[b1@cd >= np.cos(r2)] if cname == 'phi' else a[b2@cc >= np.cos(r1)],
              b[b2@cc >= np.cos(r1)] if cname == 'phi' else b[b1@cd >= np.cos(r2)]]
    return q
# Image discs and the image of the same lens in both planes.
phi_b1, phi_b2 = phi(b1), phi(b2); psi_b1, psi_b2 = psi(b1), psi(b2)
for c, disc, col, fill in ((left, phi_b1, BLUE, BLUE_FILL), (right, psi_b2, GREEN, GREEN_FILL)):
    x, y = c
    ax.add_patch(Polygon([(x-15.5, y-12.2), (x+15.5, y-12.2), (x+15.5, y+12.2), (x-15.5, y+12.2)], fc='white', ec=MUTED, lw=.75, zorder=1))
    ax.add_patch(Polygon(c+scale*disc, fc=fill, ec=col, lw=1.2, zorder=2))
lensL = order(left+scale*phi(L)); lensR = order(right+scale*psi(L))
ax.add_patch(Polygon(lensL, fc=YELLOW_FILL, ec=YELLOW, lw=.85, zorder=2.2))
ax.add_patch(Polygon(lensR, fc=YELLOW_FILL, ec=YELLOW, lw=.85, zorder=2.2))
ax.plot(*(left+scale*phi_b1).T, color=BLUE, lw=1.2, zorder=2.4); ax.plot(*(right+scale*psi_b2).T, color=GREEN, lw=1.2, zorder=2.4)
pl_, pr_ = left+scale*phi(p3), right+scale*psi(p3)
dot(ax, pl_, INK); dot(ax, pr_, INK)
label(ax, pl_+[-4.8, 2.0], r'$\varphi(p)$', halo=True); label(ax, pr_+[4.8, 2.0], r'$\psi(p)$', halo=True)
label(ax, left+[-11.6, 9.6], '$\u211d^2$', 7.5, MUTED); label(ax, right+[11.6, 9.6], '$\u211d^2$', 7.5, MUTED)
arrow(ax, pl(c1)+[-10.5, -9.5], left+[-3, 13.2], rad=.0)
arrow(ax, pl(c2)+[10.5, -9.5], right+[3, 13.2], rad=.0)
label(ax, (27, 36.8), r'$\varphi$'); label(ax, (85, 36.8), r'$\psi$')
arrow(ax, pl_+[3.6, -1.4], pr_+[-3.6, -1.4], color=INK, lw=1.0, rad=.0)
label(ax, ((pl_[0]+pr_[0])/2, pl_[1]+.9), r'$\psi\circ\varphi^{-1}$', 8)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'caps of angular radius 36 deg around lat 22, lon -77/-33; charts = orthogonal projection to tangent plane at cap centres'})
