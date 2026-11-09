"""RP1 in the chart x2=1 and the projective map (u,v)->(u,v)/(u+1) on a grid."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 56
fig, ax = canvas(W, H)
ox, oy, s = 18, 12, 10.5
arrow(ax, (ox-13, oy), (ox+14, oy), color=MUTED, lw=.7, scale=5)
arrow(ax, (ox, oy-6), (ox, oy+36), color=MUTED, lw=.7, scale=5)
label(ax, (ox+15.2, oy+.2), '$x_1$', 7.5, MUTED); label(ax, (ox+3.2, oy+35), '$x_2$', 7.5, MUTED)
ax.plot([ox-13, ox+14], [oy+s, oy+s], color=YELLOW, lw=1.2, zorder=3)
label(ax, (ox+20.5, oy+s), '$x_2=1$', 7.5, YELLOW, halo=True)
def line(u, c, lw=1.1):
    v = np.array([u, 1.0])
    k = min(3.3, 13/(abs(u)*s) if u else 3.3)
    ax.plot([ox-k*s*v[0]*.55, ox+k*s*v[0]], [oy-k*s*v[1]*.55, oy+k*s*v[1]], color=c, lw=lw, zorder=4)
for u, c in ((.5, BLUE), (-1.0, GREEN), (1.0, PURPLE)):
    line(u, c)
ax.plot([ox-12.5, ox+13.5], [oy, oy], color=RED, lw=1.2, zorder=5)
for u, c in ((.5, BLUE), (-1.0, GREEN), (1.0, PURPLE)):
    dot(ax, (ox+u*s, oy+s), c, zorder=8)
pt = (ox+2*s*.5, oy+4*s*.5)
dot(ax, (ox+1.0*s, oy+2*s), BLUE, size=1.5, zorder=8, hollow=True)
label(ax, (ox+1.0*s+7.0, oy+2*s), '$(2,4)$', 7.5, BLUE, halo=True)
label(ax, (ox+.5*s+1.0, oy+s-3.0), r'$\frac{1}{2}$', 7.5, BLUE, halo=True)
label(ax, (ox-9.3, oy-3), '$[1:0]$', 7.5, RED, halo=True)
# (b) source grid, (c) image grid.
xb, yb, ub, vb = 49, 26, 8.4, 11
xc, yc, uc, vc = 83, 26, 22, 11
lines_v = np.array([-1, -.5, 0, .5, 1])
lines_u = np.array([0, 1, 2, 3])
U = np.linspace(0, 3, 200)
for v in lines_v:
    ax.plot(xb+ub*U, yb+vb*v+0*U, color=BLUE, lw=.95, zorder=3)
    ax.plot(xc+uc*U/(U+1), yc+vc*v/(U+1), color=BLUE, lw=.95, zorder=3)
V = np.linspace(-1, 1, 50)
for u in lines_u:
    ax.plot(xb+ub*u+0*V, yb+vb*V, color=GREEN, lw=.95, zorder=3)
    ax.plot(xc+uc*u/(u+1)+0*V, yc+vc*V/(u+1), color=GREEN, lw=.95, zorder=3)
# dashed continuation to the vanishing point
for v in lines_v:
    ax.plot([xc+uc*.75, xc+uc], [yc+vc*v/4, yc], color=BLUE, lw=.6, ls=(0, (2.5, 2)), zorder=2)
dot(ax, (xc+uc, yc), RED, zorder=8, hollow=True)
label(ax, (xc+uc-1, yc-4.2), '$(1,0)$', 7.5, RED, halo=True)
P1, P2 = np.array([1, 1.0]), np.array([3, 1.0])
for q in (P1, P2):
    dot(ax, (xb+ub*q[0], yb+vb*q[1]), RED, zorder=8)
    img = q/(q[0]+1)
    dot(ax, (xc+uc*img[0], yc+vc*img[1]), RED, zorder=8)
label(ax, (xb+ub*1, yb+vb+3), '$(1,1)$', 7.5, RED, halo=True)
label(ax, (xb+ub*3+.5, yb+vb+3), '$(3,1)$', 7.5, RED, halo=True)
label(ax, (xc+uc*.5+.5, yc+vc*.5+3), r'$(\frac{1}{2},\frac{1}{2})$', 7.5, RED, halo=True)
label(ax, (xc+uc*.75+5.2, yc+vc*.25+3.4), r'$(\frac{3}{4},\frac{1}{4})$', 7.5, RED, halo=True)
arrow(ax, (xb+ub*3+2.8, yb), (xc-2.5, yc), color=STROKE, lw=.9, scale=6)
label(ax, ((xb+ub*3+xc)/2+.8, yb+3.2), r'$H$')
panel_tag(ax, ox+.5, 1.7, '(a)'); panel_tag(ax, xb+ub*1.5, 1.7, '(b)'); panel_tag(ax, xc+uc*.5, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'chart u=x1/x2; H=[[1,0,0],[0,1,0],[1,0,1]], (u,v)->(u,v)/(u+1); lines v=c meet at (1,0)'})
