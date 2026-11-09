"""Geodesics joining (1,0,0) and (1,0,pi) on the unit cylinder, and the same geodesics as straight segments to the lifts in the plane."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 50
fig, ax = canvas(W, H)
pl = Placed(View(12, 16), 17, 11.5, 7.0)
zmin, zmax = -.4, 4.0
th = np.linspace(0, 2*np.pi, 361)
vd = pl.view
n = lambda t: np.c_[np.cos(t), np.sin(t), 0*t]
def cyl(t, z, color, lw=1.2, hidden=True, zorder=3):
    P = np.c_[np.cos(t), np.sin(t), z]
    split_plot(ax, pl(P), n(t)@vd.f >= 0, color, lw=lw, hidden=hidden, zorder=zorder)
cyl(th, np.full_like(th, zmin), STROKE, lw=.95, zorder=2)
top = np.c_[np.cos(th), np.sin(th), np.full_like(th, zmax)]
ax.plot(*pl(top).T, color=STROKE, lw=.95, zorder=2)
for sgn in (-1, 1):
    a = np.arctan2(vd.f[1], vd.f[0])+sgn*np.pi/2
    ax.plot(*pl(np.array([[np.cos(a), np.sin(a), zmin], [np.cos(a), np.sin(a), zmax]])).T, color=STROKE, lw=.95, zorder=2)
h = np.pi
ax.plot(*pl(np.array([[1.0, 0, 0], [1.0, 0, h]])).T, color=BLUE, lw=1.4, zorder=4)
t = np.linspace(0, 2*np.pi, 601)
cyl(t, h*t/(2*np.pi), GREEN, lw=1.3)
t2 = np.linspace(0, 4*np.pi, 1201)
cyl(t2, h*t2/(4*np.pi), PURPLE, lw=1.1)
A, B = np.array([1.0, 0, 0]), np.array([1.0, 0, h])
dot(ax, pl(A), INK); dot(ax, pl(B), INK)
label(ax, pl(A)+[-3.4, 1.0], '$p_0$', halo=True); label(ax, pl(B)+[-3.4, 1.4], '$p_1$', halo=True)
panel_tag(ax, 17, 3, '(a)')
ox, oy, sc = 62.0, 18.0, 3.05
xmin, xmax = -2*np.pi-.8, 4*np.pi+.8
ax.plot([ox+sc*xmin, ox+sc*xmax], [oy, oy], color=MUTED, lw=.75, zorder=1)
for k in (-1, 0, 1, 2):
    x = 2*np.pi*k
    ax.plot([ox+sc*x]*2, [oy-1, oy+sc*(h+1.6)], color=GRID, lw=.85, zorder=1)
    dot(ax, (ox+sc*x, oy), INK if k == 0 else MUTED, size=1.1, hollow=(k != 0))
    dot(ax, (ox+sc*x, oy+sc*h), INK, size=1.2)
    label(ax, (ox+sc*x, oy-3.2), f'${k}$' if k == 0 else (r'$2\pi$' if k == 1 else (r'$-2\pi$' if k == -1 else r'$4\pi$')), 7.5, MUTED)
col = {0: BLUE, 1: GREEN, 2: PURPLE, -1: GREEN}
for k in (0, 1, 2, -1):
    ax.plot([ox, ox+sc*2*np.pi*k], [oy, oy+sc*h], color=col[k], lw=1.4 if k == 0 else 1.2, ls='-' if k >= 0 else (0, (3, 2)), zorder=3)
label(ax, (ox-3.4, oy+sc*h*.55), r'$\pi$', 7.5, BLUE, halo=True)
label(ax, (ox+sc*1.25*np.pi-1.0, oy+sc*h*.77), r'$\pi\sqrt{5}$', 7.5, GREEN, halo=True)
label(ax, (ox+sc*3.1*np.pi+1.0, oy+sc*h*.86+.3), r'$\pi\sqrt{17}$', 7.5, PURPLE, halo=True)
label(ax, (ox+sc*xmax-1, oy+2.2), '$s$', 7.5, MUTED)
panel_tag(ax, ox+sc*np.pi, 3, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'k-turn helix (cos t, sin t, t/(2k)), length sqrt(pi^2+(2 pi k)^2); h=pi'})
