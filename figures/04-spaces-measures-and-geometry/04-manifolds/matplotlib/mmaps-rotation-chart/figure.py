"""Rotation about the vertical axis by pi/2 on the sphere and in the north chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 104, 50
fig, ax = canvas(W, H)
pl = Placed(View(135, 26), 26, 27, 19)
sphere_disc(ax, pl)
for lat in (-30, 0, 30):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.45, hidden=False)
z = np.arcsin(.8)
sphere_curve(ax, pl, parallel(z), BLUE, lw=1.1, hidden_lw=.55)
p, q, N = spherical(z, np.pi/2), spherical(z, np.pi), np.array([0, 0, 1.0])
lon = np.linspace(np.pi/2, np.pi-.12, 80)
xy = pl(spherical(np.full_like(lon, z), lon))
ax.plot(xy[:-1, 0], xy[:-1, 1], color=RED, lw=1.5, zorder=6)
arrow(ax, xy[-6], pl(q), color=RED, lw=1.5, scale=7.5, zorder=7)
ax.plot(*pl(np.array([[0, 0, 1.0], [0, 0, 1.28]])).T, color=INK, lw=.9, zorder=8)
dot(ax, pl(N), INK); label(ax, pl(N)+[-2.8, .6], '$N$', halo=True)
dot(ax, pl(p), INK); dot(ax, pl(q), INK)
label(ax, pl(p)+[3.6, -2.2], '$p$', halo=True)
label(ax, pl(q)+[-1.0, -3.2], r'$R_\theta(p)$', 7.5, halo=True)
cx, cy, s = 78, 26, 4.8
arrow(ax, (cx-4.5*s, cy), (cx+4.5*s, cy), color=MUTED, lw=.75, scale=5.5)
arrow(ax, (cx, cy-4.3*s), (cx, cy+4.5*s), color=MUTED, lw=.75, scale=5.5)
label(ax, (cx+4.5*s-.4, cy+2.3), '$u_1$', 7.5, MUTED); label(ax, (cx+2.6, cy+4.5*s-.3), '$u_2$', 7.5, MUTED)
t = np.linspace(0, 2*np.pi, 361)
ax.plot(cx+3*s*np.cos(t), cy+3*s*np.sin(t), color=BLUE, lw=1.1, zorder=2)
a = np.linspace(np.pi/2, np.pi-.1, 60)
ax.plot(cx+3*s*np.cos(a), cy+3*s*np.sin(a), color=RED, lw=1.5, zorder=5)
arrow(ax, (cx+3*s*np.cos(a[-5]), cy+3*s*np.sin(a[-5])), (cx-3*s, cy), color=RED, lw=1.5, scale=7.5, zorder=6)
dot(ax, (cx, cy+3*s), INK); dot(ax, (cx-3*s, cy), INK); dot(ax, (cx, cy), INK, size=1.1)
label(ax, (cx+6.0, cy+3*s+2.4), '$(0,3)$', 7.5, halo=True)
label(ax, (cx-3*s-.5, cy-2.9), '$(-3,0)$', 7.5, halo=True)
panel_tag(ax, 26, 1.7, '(a)'); panel_tag(ax, cx, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=(0,.6,.8); R_theta at theta=pi/2 sends p to (-.6,0,.8); sigma_N(p)=(0,3); chart image (-3,0)'})
