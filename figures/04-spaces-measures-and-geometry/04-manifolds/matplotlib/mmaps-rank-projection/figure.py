"""Orthogonal projection pi of the sphere: rank 2 off the equator, rank 1 on it; two preimages of one point give different pushed vectors."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
pl = Placed(View(33, 6), 21, 27, 18)
sphere_disc(ax, pl)
sphere_curve(ax, pl, parallel(0.0), MUTED, lw=.7, hidden_lw=.45)
p = np.array([0, .6, .8]); q = np.array([0, .6, -.8]); a = np.array([1.0, 0, 0])
def plate(c, e1, e2, d=.28):
    pts = np.array([c+d*e1+d*e2, c+d*e1-d*e2, c-d*e1-d*e2, c-d*e1+d*e2])
    ax.add_patch(Polygon(pl(pts), fc=YELLOW_FILL, ec=YELLOW, lw=.95, zorder=4))
e = np.array([1.0, 0, 0]); ep = np.array([0, .8, -.6]); eq = np.array([0, .8, .6])
plate(p, e, ep); plate(q, e, eq); plate(a, np.array([0, 1.0, 0]), np.array([0, 0, 1.0]))
dot(ax, pl(p), INK, zorder=9); dot(ax, pl(q), INK, zorder=9); dot(ax, pl(a), INK, zorder=9)
label(ax, pl(p)+[0, 3.5], '$p$', halo=True); label(ax, pl(q)+[0, -3.5], '$q$', halo=True); label(ax, pl(a)+[3.1, 3.1], '$a$', halo=True)
cx, cy, r = 62, 26, 18
ax.add_patch(Circle((cx, cy), r, fc='white', ec=STROKE, lw=.95, zorder=1))
arrow(ax, (cx-r-3, cy), (cx+r+3.8, cy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (cx, cy-r-2), (cx, cy+r+2.6), color=MUTED, lw=.75, scale=5.5)
label(ax, (cx+r+4.2, cy+2.2), '$y_1$', 7.5, MUTED); label(ax, (cx+2.7, cy+r+2.3), '$y_2$', 7.5, MUTED)
d = .28; P = np.array([cx, cy+.6*r])
xs = r*d; ys = r*d*.8
ax.add_patch(Polygon([P+[xs, ys], P+[xs, -ys], P+[-xs, -ys], P+[-xs, ys]], fc=YELLOW_FILL, ec=YELLOW, lw=.95, zorder=4))
A = np.array([cx+r, cy])
ax.plot([A[0], A[0]], [A[1]-r*d, A[1]+r*d], color=YELLOW, lw=1.8, zorder=4, solid_capstyle='butt')
dot(ax, P, INK, zorder=9); dot(ax, A, INK, zorder=9)
label(ax, P+[8.9, 3.2], r'$\pi(p)=\pi(q)$', 7, halo=True); label(ax, A+[-3.7, 2.6], r'$\pi(a)$', 7, halo=True)
Bx, By, s = 99, 13, 14
ax.plot([Bx-11, Bx+11], [By, By], color=MUTED, lw=.75)
arrow(ax, (Bx, By-5.5), (Bx, By+s*1.44+6), color=MUTED, lw=.75, scale=5.5)
label(ax, (Bx+3.0, By+s*1.44+5.2), '$y_2$', 7.5, MUTED)
arrow(ax, (Bx, By), (Bx, By+s*1.44), color=RED, lw=1.5, scale=7.5, zorder=8)
arrow(ax, (Bx, By), (Bx, By-s*.16), color=BLUE, lw=1.5, scale=6, zorder=9)
dot(ax, (Bx, By), INK, zorder=10)
label(ax, (Bx-7, By+s*1.44), r'$1.44$', 7.5, RED, halo=True)
label(ax, (Bx-7.3, By-2.7), r'$-0.16$', 7.5, BLUE, halo=True)
panel_tag(ax, 21, 1.7, '(a)'); panel_tag(ax, cx, 1.7, '(b)'); panel_tag(ax, Bx, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'pi(y)=(y1,y2); hat pi(u)=2u/(|u|^2+1); J(0,3)=diag(.2,-.16), J(0,1/3)=diag(1.8,1.44), J(1,0)=diag(0,1); patches half-side .28 in unit tangent frames'})
