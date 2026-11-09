"""A plane in R3: two orthonormal frames of the same subspace; vertical and horizontal tangent directions."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 54
fig, ax = canvas(W, H)
view = View(-120, 24)
pa, pb = Placed(view, 30, 27, 14.5), Placed(view, 84, 27, 14.5)
e1, e2, e3 = np.eye(3)
def plane(pl, a, b, fc, ec, h=1.25, z=2):
    pts = np.array([h*(s*a+t*b) for s, t in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    ax.add_patch(Polygon(pl(pts), closed=True, fc=fc, ec=ec, lw=.8, zorder=z))
O = 0*e1
plane(pa, e1, e2, BLUE_FILL, STROKE)
ang = np.radians(38)
y1 = np.cos(ang)*e1+np.sin(ang)*e2; y2 = -np.sin(ang)*e1+np.cos(ang)*e2
for a, c in ((e1, BLUE), (e2, BLUE), (y1, GREEN), (y2, GREEN)):
    arrow(ax, pa(O), pa(a), color=c, lw=1.25, scale=6.5, zorder=5)
dot(ax, pa(O), INK, size=1.1, zorder=6)
label(ax, pa(1.13*e1)+[-1.4, -1.8], '$y_1$', color=BLUE, halo=True)
label(ax, pa(1.1*e2)+[.8, -2.6], '$y_2$', color=BLUE, halo=True)
label(ax, pa(1.12*y1)+[.4, 2.0], "$y_1'$", color=GREEN, halo=True)
label(ax, pa(1.14*y2)+[-1.6, 2.0], "$y_2'$", color=GREEN, halo=True)
# (b): Y=[e1,e2], vertical Delta=[e2,-e1], horizontal Delta=[.5 e3, 0].
plane(pb, e1, e2, BLUE_FILL, STROKE, z=1)
tilt = (e1+.5*e3)/np.linalg.norm(e1+.5*e3)
plane(pb, tilt, e2, 'none', RED, z=3)
arrow(ax, pb(O), pb(e1), color=BLUE, lw=1.25, scale=6.5, zorder=5)
arrow(ax, pb(O), pb(e2), color=BLUE, lw=1.25, scale=6.5, zorder=5)
arrow(ax, pb(e1), pb(e1+.75*e2), color=GREEN, lw=1.2, scale=6.5, zorder=6)
arrow(ax, pb(e1), pb(e1+.5*e3), color=RED, lw=1.2, scale=6.5, zorder=7)
dot(ax, pb(O), INK, size=1.1, zorder=7)
label(ax, pb(e1)+[-1.2, -2.7], '$y_1$', color=BLUE, halo=True)
label(ax, pb(e2)+[2.8, -.4], '$y_2$', color=BLUE, halo=True)
label(ax, pb(e1+.5*e3)+[3.4, 1.0], '$\\Delta_h$', color=RED, halo=True)
label(ax, pb(e1+.75*e2)+[-3.6, 2.4], '$\\Delta_v$', color=GREEN, halo=True)
panel_tag(ax, 30, 1.7, '(a)'); panel_tag(ax, 84, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Y=[e1,e2]; YQ rotates by 38deg; vertical Delta=[e2,-e1]; horizontal Delta=[.5 e3,0], tilted plane span(e1+.5 e3,e2)'})
