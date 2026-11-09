"""At p=(0,3/5,4/5): north-chart frame and south-chart frame on the sphere, and their records in each chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 52
fig, ax = canvas(W, H)
p = np.array([0, .6, .8]); e1 = np.array([1., 0, 0]); e2 = np.array([0, -.8, .6])
pl = Placed(View(90, 42), 24, 26, 22)
sphere_disc(ax, pl)
for lat in (-30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.4, hidden=False)
for lon in range(0, 180, 45):
    sphere_curve(ax, pl, meridian(np.radians(lon)), MUTED, lw=.4, hidden=False)
P = pl(p); L = .46
A1, A2 = pl(p+.62*L*e1), pl(p+L*e2)
B1, B2 = pl(p+1.3*L*e1), pl(p-L*e2)
arrow(ax, P, B1, color=GREEN, lw=1.4, scale=7.5, zorder=7); arrow(ax, P, A1, color=BLUE, lw=1.4, scale=7.5, zorder=8)
arrow(ax, P, A2, color=BLUE, lw=1.4, scale=7.5, zorder=8); arrow(ax, P, B2, color=GREEN, lw=1.4, scale=7.5, zorder=7)
def arc(sign, col):
    s = np.linspace(.18, np.pi/2-.18, 60)
    pts = pl(p+.17*(np.cos(s)[:, None]*e1+sign*np.sin(s)[:, None]*e2))
    ax.plot(pts[:-1, 0], pts[:-1, 1], color=col, lw=.8, zorder=6); arrow(ax, pts[-3], pts[-1], color=col, lw=.8, scale=5.5, zorder=6)
arc(1, BLUE); arc(-1, GREEN)
dot(ax, P, INK, zorder=9); label(ax, P+[3.4, -1.0], '$p$', halo=True)
label(ax, A2+[3.8, 1.2], r'$\partial_{u_2}$', 7.5, BLUE, halo=True)
label(ax, A1+[-2.2, 3.0], r'$\partial_{u_1}$', 7.5, BLUE, halo=True)
label(ax, B2+[3.8, -1.2], r'$\partial_{w_2}$', 7.5, GREEN, halo=True)
label(ax, B1+[-1.2, -3.0], r'$\partial_{w_1}$', 7.5, GREEN, halo=True)
panel_tag(ax, 24, 1.7, '(a)')
def axes(cx, cy, xr, yr, s, xn, yn):
    arrow(ax, (cx+xr[0]*s, cy), (cx+xr[1]*s, cy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, cy+yr[0]*s), (cx, cy+yr[1]*s), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+xr[1]*s+.4, cy+2.2), xn, 7.5, MUTED); label(ax, (cx+2.6, cy+yr[1]*s), yn, 7.5, MUTED)
# (b) north chart
cx, cy, s = 64, 14, 4.8
axes(cx, cy, (-1.6, 2.2), (-1, 5), s, '$u_1$', '$u_2$')
P1 = np.array([cx, cy+3*s])
arrow(ax, P1, P1+[8, 0], color=BLUE, lw=1.4, scale=7.5, zorder=8); arrow(ax, P1, P1+[0, 8], color=BLUE, lw=1.4, scale=7.5, zorder=8)
dot(ax, P1, INK, zorder=9); label(ax, P1+[-5, -.2], '$(0,3)$', 7.5, halo=True)
panel_tag(ax, cx, 1.7, '(b)')
# (c) south chart
cx, cy, s = 94, 14, 60
axes(cx, cy, (-.14, .24), (-.1, .42), s, '$w_1$', '$w_2$')
P2 = np.array([cx, cy+s/3])
arrow(ax, P2, P2+[8, 0], color=GREEN, lw=1.4, scale=7.5, zorder=8); arrow(ax, P2, P2+[0, 8], color=GREEN, lw=1.4, scale=7.5, zorder=8)
dot(ax, P2, INK, zorder=9); label(ax, P2+[-4.8, -.2], r'$(0,\frac{1}{3})$', 7.5, halo=True)
panel_tag(ax, cx, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=(0,.6,.8); d/du1=(1/5,0,0), d/du2=(0,-4/25,3/25); J=diag(1/9,-1/9); arrows normalised to the same drawn length'})
