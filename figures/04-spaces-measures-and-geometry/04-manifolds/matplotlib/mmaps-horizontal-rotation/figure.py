"""Rotation Q(y)=(y1,-y3,y2): the point a=(0,1,0) goes to N, so the output needs the south chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
pl = Placed(View(28, 18), 22, 26, 19)
sphere_disc(ax, pl)
for lat in (-30, 0, 30):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.45, hidden=False)
th = np.linspace(0, 2*np.pi, 721)
sphere_curve(ax, pl, np.c_[0*th, np.cos(th), np.sin(th)], BLUE, lw=1.0, hidden_lw=.5)
a, N = np.array([0, 1.0, 0]), np.array([0, 0, 1.0])
s = np.linspace(0, np.pi/2-.1, 60)
xy = pl(np.c_[0*s, np.cos(s), np.sin(s)])
ax.plot(xy[:, 0], xy[:, 1], color=RED, lw=1.5, zorder=6)
arrow(ax, xy[-6], pl(N), color=RED, lw=1.5, scale=7.5, zorder=7)
dot(ax, pl(a), INK); dot(ax, pl(N), INK)
label(ax, pl(a)+[3.0, -1.8], '$a$', halo=True); label(ax, pl(N)+[-2.6, 2.2], r'$N$', halo=True)
Qhat = lambda u: np.c_[2*u[:, 0], 1-np.sum(u**2, 1)]/(np.sum(u**2, 1)+1+2*u[:, 1])[:, None]
def planes(c, sc, xr, yr, xn, yn):
    cx, cy = c
    arrow(ax, (cx+sc*xr[0], cy), (cx+sc*xr[1], cy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, cy+sc*yr[0]), (cx, cy+sc*yr[1]), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+sc*xr[1]-.2, cy+2.3), xn, 7.5, MUTED); label(ax, (cx+2.7, cy+sc*yr[1]-.3), yn, 7.5, MUTED)
    return lambda u: np.c_[cx+sc*u[:, 0], cy+sc*u[:, 1]]
A = planes((60, 11), 15, (-.9, .9), (-.25, 1.9), '$u_1$', '$u_2$')
B = planes((96, 24), 27, (-.55, .55), (-.55, .62), '$w_1$', '$w_2$')
d = .5; c = np.array([0, 1.0])
ss = np.linspace(-d, d, 81)
for k in np.linspace(-d, d, 5):
    for line in (np.c_[np.full_like(ss, k), ss], np.c_[ss, np.full_like(ss, k)]):
        uv = line+c
        col = BLUE
        ax.plot(*A(uv).T, color=col, lw=.8, zorder=3)
        ax.plot(*B(Qhat(uv)).T, color=col, lw=.8, zorder=3)
P, O = A(c[None])[0], B(Qhat(c[None]))[0]
dot(ax, P, INK); dot(ax, O, INK)
label(ax, P+[-12.4, 0], '$(0,1)$', 7.5, halo=True)
label(ax, O+[10.5, -9.5], '$(0,0)$', 7.5, halo=True)
ax.plot([O[0]+.8, O[0]+7.6], [O[1]-.8, O[1]-8.4], color=MUTED, lw=.5, zorder=8)
arrow(ax, (72.5, 25), (82, 25), color=INK, lw=.9, rad=.0)
label(ax, (77, 28), r'$\hat Q$')
panel_tag(ax, 22, 1.7, '(a)'); panel_tag(ax, 78, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Q(y)=(y1,-y3,y2); hat Q(u)=(2u1,1-|u|^2)/(|u|^2+1+2u2) at u near (0,1), J=diag(1/2,-1/2)'})
