"""Why the straight line leaves the sphere; ambient acceleration on the equator and on the latitude through p=(0,3/5,4/5)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 46
fig, ax = canvas(W, H)
U = 15.5
# (a) straight line leaves the sphere
pa = Placed(View(15, 22), 19, 26, U)
sphere_disc(ax, pa, fill='white')
sphere_curve(ax, pa, parallel(0.0), GRID, lw=.5, hidden=False, zorder=2)
p = np.array([1.0, 0, 0]); v = np.array([0, 1.0, 0])
L = np.array([p+t*v for t in np.linspace(0, 1.15, 40)])
ax.plot(*pa(L).T, color=RED, lw=1.3, zorder=4)
arrow(ax, pa(L[-2]), pa(L[-1]), color=RED, lw=1.3, scale=7)
T = np.linspace(0, 1.15, 60)
ax.plot(*pa(np.c_[np.cos(T), np.sin(T), 0*T]).T, color=BLUE, lw=1.35, zorder=3)
dot(ax, pa(p), INK); label(ax, pa(p)+[-2.6, -2.6], '$p$', halo=True)
label(ax, pa(L[-1])+[1.0, 3.0], '$p+tv$', 7.5, RED, halo=True)
panel_tag(ax, 19, 3, '(a)')
# (b) equator
pb = Placed(View(15, 22), 58, 26, U)
sphere_disc(ax, pb, fill='white')
sphere_curve(ax, pb, parallel(0.0), BLUE, lw=1.35, hidden=True)
Q = np.array([np.cos(.3), np.sin(.3), 0])
vel = np.array([-np.sin(.3), np.cos(.3), 0])
arrow(ax, pb(Q), pb(Q+.62*vel), color=GREEN, lw=1.3, scale=7)
arrow(ax, pb(Q), pb(Q-.62*Q), color=RED, lw=1.3, scale=7)
dot(ax, pb(Q), INK)
label(ax, pb(Q+.62*vel)+[3.2, 1.8], r'$\dot\gamma$', color=GREEN, halo=True)
label(ax, pb(Q-.62*Q)+[-.8, 3.0], r'$\ddot\gamma$', color=RED, halo=True)
panel_tag(ax, 58, 3, '(b)')
# (c) latitude through p, unit-phi parametrisation
pc = Placed(View(20, 18), 94, 22.5, U)
sphere_disc(ax, pc, fill='white')
c0, s0 = .8, .6
pp = np.array([0, s0, c0])
sphere_curve(ax, pc, parallel(np.arcsin(c0)), BLUE, lw=1.35, hidden=True)
vel = np.array([-s0, 0, 0]); acc = np.array([0, -s0, 0])
an = np.dot(acc, pp)*pp; at = acc-an
k = 1.5
arrow(ax, pc(pp), pc(pp+k*vel), color=GREEN, lw=1.3, scale=7)
arrow(ax, pc(pp), pc(pp+k*acc), color=RED, lw=1.3, scale=7)
arrow(ax, pc(pp), pc(pp+k*at), color=PURPLE, lw=1.45, scale=7)
ax.plot(*np.array([pc(pp+k*at), pc(pp+k*acc)]).T, color=MUTED, lw=.75, ls=(0, (2.5, 1.8)), zorder=5)
ax.plot(*np.array([pc(pp+k*an), pc(pp+k*acc)]).T, color=MUTED, lw=.75, ls=(0, (2.5, 1.8)), zorder=5)
arrow(ax, pc(pp), pc(pp+k*an), color=MUTED, lw=1.0, scale=6)
dot(ax, pc(pp), INK)
label(ax, pc(pp)+[2.6, -1.2], '$p$', halo=True)
label(ax, pc(pp+k*vel)+[2.6, 1.2], r'$\dot\gamma$', color=GREEN, halo=True)
label(ax, pc(pp+k*acc)+[-2.8, -1.0], r'$\ddot\gamma$', color=RED, halo=True)
label(ax, pc(pp+k*at)+[-1.6, 2.6], r'$\ddot\gamma^{\mathrm{T}}$', color=PURPLE, halo=True)
label(ax, pc(pp+k*an)+[-.8, -3.0], r'$\ddot\gamma^{\mathrm{N}}$', 7.5, MUTED, halo=True)
panel_tag(ax, 94, 3, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'latitude theta0, cos=4/5: acc=-(3/5)e, normal part -(9/25)p, tangent part (12/25) toward north'})
