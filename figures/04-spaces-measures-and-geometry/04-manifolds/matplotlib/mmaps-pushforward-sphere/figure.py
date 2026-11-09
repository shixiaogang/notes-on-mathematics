"""Pushforward by the quarter-turn R: a curve through p, its image, the tangent planes, and the chart records."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 56
fig, ax = canvas(W, H)
pl = Placed(View(135, 42), 28, 26, 21)
sphere_disc(ax, pl)
for lat in (-30, 0, 30):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.45, hidden=False)
inv = lambda u: np.c_[2*u[:, 0], 2*u[:, 1], np.sum(u**2, 1)-1]/(np.sum(u**2, 1)+1)[:, None]
tt = np.tan(np.linspace(-1.5705, 1.5705, 2401))
g = inv(np.c_[tt, np.full_like(tt, 3.0)])
Rm = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.0]])
sphere_curve(ax, pl, g, BLUE, lw=1.3, hidden=False)
sphere_curve(ax, pl, g@Rm.T, GREEN, lw=1.3, hidden=False)
p = np.array([0, .6, .8]); q = Rm@p
def plate(c, e1, e2, a=.3, b=.21):
    xy = pl(np.array([c+a*e1+b*e2, c+a*e1-b*e2, c-a*e1-b*e2, c-a*e1+b*e2]))
    ax.add_patch(Polygon(xy, fc='none', ec=YELLOW, lw=1.0, zorder=4))
    return xy
e1 = np.array([1.0, 0, 0]); e2 = np.array([0, .8, -.6])
plate(p, e1, e2); plate(q, Rm@e1, Rm@e2)
v = np.array([.2, 0, 0])*2; w = Rm@v
arrow(ax, pl(p), pl(p+v), color=RED, lw=1.5, scale=7.5, zorder=8)
arrow(ax, pl(q), pl(q+w), color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, pl(p), INK, zorder=9); dot(ax, pl(q), INK, zorder=9)
label(ax, pl(p)+[2.8, -2.2], '$p$', halo=True); label(ax, pl(q)+[3.5, 3.4], r'$R_\theta(p)$', 7.5, halo=True)
label(ax, pl(p+v)+[-2.2, .6], r'$v$', color=RED, halo=True)
label(ax, pl(q+w)+[.5, -3.1], r'$\mathrm{d}R_\theta(v)$', 7.5, RED, halo=True)
cx, cy, s = 87, 28, 4.3
arrow(ax, (cx-5*s, cy), (cx+5*s, cy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (cx, cy-4.8*s), (cx, cy+5*s), color=MUTED, lw=.75, scale=5.5)
label(ax, (cx+5*s-.4, cy+2.3), '$u_1$', 7.5, MUTED); label(ax, (cx+2.6, cy+5*s-.3), '$u_2$', 7.5, MUTED)
sl = np.array([-4.4, 4.4])
ax.plot(cx+s*sl, cy+s*np.array([3, 3]), color=BLUE, lw=1.3, zorder=3)
ax.plot(cx+s*np.array([-3, -3]), cy+s*sl, color=GREEN, lw=1.3, zorder=3)
P, Q = np.array([cx, cy+3*s]), np.array([cx-3*s, cy])
arrow(ax, P, P+[s, 0], color=RED, lw=1.5, scale=7.5, zorder=8)
arrow(ax, Q, Q+[0, s], color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, P, INK, zorder=9); dot(ax, Q, INK, zorder=9)
label(ax, P+[-6.0, 2.3], '$(0,3)$', 7.5, halo=True); label(ax, Q+[5.8, -2.7], '$(-3,0)$', 7.5, halo=True)
label(ax, P+[s+4.6, -2.5], '$(1,0)$', 7.5, RED, halo=True); label(ax, Q+[5.0, s+.6], '$(0,1)$', 7.5, RED, halo=True)
panel_tag(ax, 28, 1.7, '(a)'); panel_tag(ax, cx, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'R=R_theta, theta=pi/2; v=d_u1|p=(.2,0,0) drawn at 2x; dR(v)=(0,.2,0)=d_u2|R(p); charts u2=3 and u1=-3'})
