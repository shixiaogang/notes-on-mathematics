"""Stereographic projection from N, its cross-section with the worked point, and the transition u/|u|^2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common'))
from mfd3d import *
from matplotlib.patches import Ellipse

W, H = 112, 88
fig, ax = canvas(W, H)
# (a) three-dimensional view, plane drawn first because the camera is above it.
view = View(52, 23)
pl = Placed(view, 27, 70, 11.0)
disc_r = 2.25
ax.add_patch(Ellipse(pl.c, 2*disc_r*11, 2*disc_r*11*np.sin(np.radians(23)), fc=YELLOW_FILL, ec=MUTED, lw=.75, zorder=1))
# Upper hemisphere: silhouette arc above the equator together with the projected equator.
eq = parallel(0.0, 721)
ax.add_patch(Circle(pl.c, 11, fc='none', ec='none'))
t = np.linspace(0, 1, 2)
sil_top = pl.c+11*np.c_[np.cos(np.linspace(0, np.pi, 361)), np.sin(np.linspace(0, np.pi, 361))]
front = eq[view.depth(eq) >= 0]
front = front[np.argsort(pl(front)[:, 0])]
half = np.r_[sil_top, pl(front)]
ax.add_patch(Polygon(half, fc=BLUE_FILL, ec='none', zorder=2))
ax.plot(*sil_top.T, color=STROKE, lw=.95, zorder=3)
ax.plot(*pl(front).T, color=STROKE, lw=.95, zorder=3)
for lat in (30, 60):
    pts = parallel(np.radians(lat), 361)
    vis = view.depth(pts) >= 0
    split_plot(ax, pl(pts), vis, MUTED, lw=.5, hidden=False, zorder=2.5)
ph = np.radians(38); lon = np.radians(68)
p = spherical(ph, lon); u_r = np.cos(ph)/(1-np.sin(ph)); u = np.array([u_r*np.cos(lon), u_r*np.sin(lon), 0.0]); Np = np.array([0, 0, 1.0])
for a, b, vis in ((Np, p, False), (p, u, True)):
    xy = pl(np.array([a, b]))
    ax.plot(*xy.T, color=BLUE, lw=1.2 if vis else .7, ls='-' if vis else (0, (2.2, 1.8)), zorder=5)
dot(ax, pl(Np), INK); dot(ax, pl(p), INK); dot(ax, pl(u), INK)
label(ax, pl(Np)+[0, 2.9], '$N$'); label(ax, pl(p)+[2.8, 1.8], '$p$'); label(ax, pl(u)+[3.2, 2.0], r'$\sigma_N(p)$', halo=True)
label(ax, pl.c+[-19, 4.0], '$S^2$', color=MUTED)
label(ax, pl.c+[-18.5, -11.8], '赤道平面', 7.5, MUTED)

# (b) cross-section x=0 in the (y,z) plane with the worked point p=(0,3/5,4/5).
U = 12.2; ox, oy = 66, 67.5
Sx = lambda y, z: (ox+U*y, oy+U*z)
th = np.linspace(0, 2*np.pi, 361)
ax.add_patch(Circle((ox, oy), U, fc=BLUE_FILL, ec=STROKE, lw=.95, zorder=1))
ax.plot([ox-1.2*U, ox+3.55*U], [oy, oy], color=MUTED, lw=.75, zorder=2)
N, Sp = Sx(0, 1), Sx(0, -1); P = Sx(.6, .8); a3 = Sx(3, 0); a13 = Sx(1/3, 0)
ax.plot(*zip(N, a3), color=BLUE, lw=1.2, zorder=4)
ax.plot(*zip(Sp, P), color=GREEN, lw=1.2, zorder=4)
for q, t_ in ((N, '$N$'), (Sp, '$S$')):
    dot(ax, q, INK)
label(ax, (N[0]-3, N[1]+.8), '$N$'); label(ax, (Sp[0]-3, Sp[1]-.8), '$S$')
dot(ax, P, INK); label(ax, (P[0]+11.2, P[1]+1.6), r'$p=(0,\frac{3}{5},\frac{4}{5})$')
dot(ax, a3, BLUE); dot(ax, a13, GREEN)
label(ax, (a3[0], a3[1]-3.1), r'$u_2=3$', color=BLUE); label(ax, (a13[0]+8.6, a13[1]-3.3), r'$w_2=\frac{1}{3}$', color=GREEN)
arrow(ax, (a13[0]+4.4, a13[1]-2.5), (a13[0]+.9, a13[1]-.6), color=MUTED, lw=.75, scale=5)
label(ax, (ox+3.55*U+1, oy+2.6), '$y_2$', 7.5, MUTED, ha='right')
panel_tag(ax, 27, 50.6, '(a)'); panel_tag(ax, 75, 50.6, '(b)')

# (c,d) the transition: circles of radius 1/2,1,2 and rays through the origin.
s = 6.0
def plane(cx, cy, map_, name):
    R = 3.45
    ax.annotate('', xy=(cx+R*s, cy), xytext=(cx-R*s, cy), arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=.75, mutation_scale=6, shrinkA=0, shrinkB=0))
    ax.annotate('', xy=(cx, cy+R*s), xytext=(cx, cy-R*s), arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=.75, mutation_scale=6, shrinkA=0, shrinkB=0))
    t = np.linspace(0, 2*np.pi, 361)
    for r, col, lw in ((2, BLUE, 1.3), (.5, GREEN, 1.3), (1, MUTED, .85)):
        z = r*np.c_[np.cos(t), np.sin(t)]
        w = map_(z)
        ax.plot(cx+s*w[:, 0], cy+s*w[:, 1], color=col, lw=lw, zorder=3)
    return lambda v: (cx+s*v[0], cy+s*v[1])
inv = lambda z: z/np.sum(z**2, axis=-1, keepdims=True)
cy = 27.5
cL, cR = 29, 83
A = plane(cL, cy, lambda z: z, 'u'); B = plane(cR, cy, inv, 'w')
P1 = np.array([0, 3.0]); P2 = P1/9
dot(ax, A(P1), INK); dot(ax, B(P2), INK)
label(ax, (A(P1)[0]+8.2, A(P1)[1]), r'$\bm{u}=(0,3)$'.replace(r'\bm{u}', 'u'))
label(ax, (B(P2)[0]+13.4, B(P2)[1]+11.8), r'$w=(0,\frac{1}{3})$')
arrow(ax, (B(P2)[0]+8.5, B(P2)[1]+10.2), (B(P2)[0]+.8, B(P2)[1]+1.0), color=MUTED, lw=.75, scale=5)
label(ax, (cL+3.3*s, cy+2.6), '$u_1$', 7.5, MUTED); label(ax, (cR+3.3*s, cy+2.6), '$w_1$', 7.5, MUTED)
label(ax, (cL+13.3, cy+7.3), '$r=2$', 7.5, BLUE); label(ax, (cR+6.3, cy-5.4), r'$r=\frac{1}{2}$', 7.5, BLUE)
label(ax, (cL+6.3, cy-5.4), r'$r=\frac{1}{2}$', 7.5, GREEN); label(ax, (cR+13.3, cy-8.2), '$r=2$', 7.5, GREEN)
arrow(ax, (cL+3.45*s+1.2, cy-4), (cR-3.45*s-1.2, cy-4), color=INK, lw=1.0)
label(ax, ((cL+cR)/2, cy-1.5), r'$\tau$')
panel_tag(ax, cL, 2.2, '(c)'); panel_tag(ax, cR, 2.2, '(d)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sigma_N(y)=(y1,y2)/(1-y3); sigma_S(y)=(y1,y2)/(1+y3); tau(u)=u/|u|^2; worked point p=(0,3/5,4/5)'})
