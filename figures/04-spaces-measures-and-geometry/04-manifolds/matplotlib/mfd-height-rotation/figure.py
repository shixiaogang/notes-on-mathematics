"""Height levels and the rotation field on the sphere, and the same levels and field in the north chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 46
fig, ax = canvas(W, H)
LEVELS = (-.6, 0.0, .6, .8)
pl = Placed(View(50, 22), 18, 25, 15)
sphere_disc(ax, pl)
for z in LEVELS:
    pts = parallel(np.arcsin(z)); sphere_curve(ax, pl, pts, BLUE, lw=1.1, hidden_lw=.55)
N = np.array([0, 0, 1.0]); Sp = np.array([0, 0, -1.0]); p = np.array([0, .6, .8])
dot(ax, pl(N), INK); label(ax, pl(N)+[0, 2.7], '$N$')
dot(ax, pl(p), INK); label(ax, pl(p)+[-2.6, 2.1], '$p$', halo=True)
Rf = 15
for z in LEVELS:
    right = pl(spherical(np.arcsin(z), np.radians(50+90)))
    # label placed just outside the disc at the right end of the level circle
    label(ax, (pl.c[0]+Rf+1.2, pl(spherical(np.arcsin(z), np.radians(50+90)))[1]), f'{z:g}', 7.5, BLUE, ha='left')
# (b) rotation field on the same sphere.
pb = Placed(View(50, 22), 54, 25, 15)
sphere_disc(ax, pb)
for z in LEVELS:
    sphere_curve(ax, pb, parallel(np.arcsin(z)), BLUE, lw=.55, hidden=False)
for z, nlon in ((-.6, 12), (0.0, 14), (.6, 10), (.8, 8)):
    for lon in np.linspace(0, 2*np.pi, nlon, endpoint=False)+.15:
        q = spherical(np.arcsin(z), lon)
        if pb.view.depth(q) < .12:
            continue
        v = np.array([-q[1], q[0], 0.0])
        a, b = pb(q), pb(q+.3*v)
        arrow(ax, a, b, color=RED, lw=.9, scale=5.5, zorder=5)
dot(ax, pb(N), INK, zorder=6); label(ax, pb(N)+[0, 2.7], '$N$')
# (c) north chart: |u|=r levels with h=(r^2-1)/(r^2+1); field (-u2,u1).
cx, cy, s = 91.5, 23, 5.0
arrow(ax, (cx-3.5*s, cy), (cx+3.5*s, cy), color=MUTED, lw=.75, scale=5.5); arrow(ax, (cx, cy-3.5*s), (cx, cy+3.5*s), color=MUTED, lw=.75, scale=5.5)
label(ax, (cx+3.5*s-.6, cy+2.1), '$u_1$', 7.5, MUTED); label(ax, (cx+2.4, cy+3.5*s), '$u_2$', 7.5, MUTED)
t = np.linspace(0, 2*np.pi, 361)
for r, z in ((.5, -.6), (1, 0.0), (2, .6), (3, .8)):
    ax.plot(cx+s*r*np.cos(t), cy+s*r*np.sin(t), color=BLUE, lw=1.1, zorder=2)
    n = {.5: 5, 1: 7, 2: 10, 3: 13}[r]
    for ang in np.linspace(0, 2*np.pi, n, endpoint=False)+.3:
        u = r*np.array([np.cos(ang), np.sin(ang)]); v = np.array([-u[1], u[0]])*.28
        arrow(ax, (cx+s*u[0], cy+s*u[1]), (cx+s*(u[0]+v[0]), cy+s*(u[1]+v[1])), color=RED, lw=.9, scale=5.5, zorder=5)
    if r >= 1:
        label(ax, (cx+s*r*np.cos(-.62), cy+s*r*np.sin(-.62)-.2), f'{z:g}', 7, BLUE, halo=True)
dot(ax, (cx, cy+3*s), INK, zorder=7); label(ax, (cx-2.6, cy+3*s+2.2), '$p$', halo=True)
dot(ax, (cx, cy), INK, size=1.2); 
panel_tag(ax, 18, 1.7, '(a)'); panel_tag(ax, 54, 1.7, '(b)'); panel_tag(ax, cx, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h=y3 at levels -0.6,0,0.6,0.8; h_hat(u)=(|u|^2-1)/(|u|^2+1); X=(-y2,y1,0) and X_hat=(-u2,u1), arrows scaled 0.3 and 0.28'})
