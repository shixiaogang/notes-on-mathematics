"""One tangent vector at p=(0,3/5,4/5): two equivalent curves, the tangent plane, and the records in both stereographic charts."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 54
fig, ax = canvas(W, H)
p = np.array([0, .6, .8]); e1 = np.array([1.0, 0, 0]); e2 = np.array([0, .8, -.6])
from matplotlib.patches import Rectangle
pl = Placed(View(72, 20), 25, 12, 31)
clip = Rectangle((1, 7), 49, 46, transform=ax.transData)
BEFORE = set(map(id, ax.get_children()))
sphere_disc(ax, pl)
for lat in (-30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.4, hidden=False)
inv = lambda u: np.c_[2*u[:, 0], 2*u[:, 1], np.sum(u**2, 1)-1]/(np.sum(u**2, 1)+1)[:, None]
tt = np.tan(np.linspace(-1.5705, 1.5705, 2401))
gamma1 = inv(np.c_[tt, np.full_like(tt, 3.0)])
sphere_curve(ax, pl, gamma1, BLUE, lw=1.3, hidden=False)
th = np.linspace(-np.pi, np.pi, 721)
gamma2 = np.c_[.6*np.sin(th), .6*np.cos(th), np.full_like(th, .8)]
sphere_curve(ax, pl, gamma2, GREEN, lw=1.3, hidden=False)
a, b = .47, .34
corners = np.array([p+a*e1+b*e2, p+a*e1-b*e2, p-a*e1-b*e2, p-a*e1+b*e2])
xy = pl(corners)
ax.add_patch(Polygon(xy, fc='none', ec=YELLOW, lw=1.1, zorder=4))
P = pl(p)
arrow(ax, P, pl(p+.4*e1), color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, P, INK, zorder=9)
label(ax, P+[2.8, -2.4], '$p$', halo=True); label(ax, pl(p+.4*e1)+[1.4, 2.4], r'$\bm{v}$'.replace(r'\bm{v}', 'v'), color=RED, halo=True)
label(ax, xy[2]+[9.2, -2.8], '$T_pS^2$', 7.5, color=YELLOW, halo=True)
label(ax, pl(inv(np.array([[-1.1, 3.0]]))[0])+[2.5, 2.6], r'$\gamma_1$', color=BLUE, halo=True)
label(ax, pl(gamma2[np.argmin(abs(th+.72))])+[-1.0, -3.2], r'$\gamma_2$', color=GREEN, halo=True)
for artist in ax.get_children():
    if id(artist) not in BEFORE and artist.get_zorder() < 8:
        artist.set_clip_path(clip)
def axes(c, s, xr, yr, xn, yn):
    cx, cy = c
    arrow(ax, (cx+s*xr[0], cy), (cx+s*xr[1], cy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, cy+s*yr[0]), (cx, cy+s*yr[1]), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+s*xr[1], cy+2.1), xn, 7.5, MUTED); label(ax, (cx+2.4, cy+s*yr[1]), yn, 7.5, MUTED)
    return lambda u: np.c_[cx+s*u[:, 0], cy+s*u[:, 1]]
# (b) north chart: gamma_1 is the line u2=3, gamma_2 the circle of radius 3.
c1 = (66, 21); s1 = 3.15
A = axes(c1, s1, (-4.3, 4.3), (-3.7, 4.6), '$u_1$', '$u_2$')
s_ = np.linspace(-4.1, 4.1, 2)
ax.plot(*A(np.c_[s_, np.full(2, 3.0)]).T, color=BLUE, lw=1.3, zorder=3)
ax.plot(*A(3*np.c_[np.cos(th), np.sin(th)]).T, color=GREEN, lw=1.3, zorder=3)
P1 = A(np.array([[0, 3.0]]))[0]
arrow(ax, P1, P1+[s1*1, 0], color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, P1, INK, zorder=9)
label(ax, P1+[-3.0, 2.6], '$(0,3)$', 7.5, halo=True)
label(ax, P1+[s1+5.0, 2.5], '$(1,0)$', 7.5, RED, halo=True)
# (c) south chart: tau maps the line to a circle through the origin and the circle to radius 1/3.
c2 = (95.5, 25); s2 = 36.0
B = axes(c2, s2, (-.40, .40), (-.40, .55), '$w_1$', '$w_2$')
ax.plot(*B(np.c_[np.sin(th)/6, 1/6+np.cos(th)/6]).T, color=BLUE, lw=1.3, zorder=3)
ax.plot(*B(np.c_[np.cos(th)/3, np.sin(th)/3]).T, color=GREEN, lw=1.3, zorder=3)
P2 = B(np.array([[0, 1/3]]))[0]
arrow(ax, P2, P2+[s2/9, 0], color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, P2, INK, zorder=9)
label(ax, P2+[-4.2, 2.6], r'$(0,\frac{1}{3})$', 7.5, halo=True)
label(ax, P2+[s2/9+3.6, 2.8], r'$(\frac{1}{9},0)$', 7.5, RED, halo=True)
panel_tag(ax, 25.5, 1.7, '(a)'); panel_tag(ax, c1[0], 1.7, '(b)'); panel_tag(ax, c2[0], 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=(0,3/5,4/5); gamma1(t)=sigma_N^{-1}(t,3); gamma2(s)=(0.6 sin(s/3),0.6 cos(s/3),0.8); arrow in (a) drawn 2.5 times true R^3 length 0.2; J=diag(1/9,-1/9)'})
