"""SO(3) as the closed ball of radius pi with antipodal boundary points identified; the loop of rotations about e3."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 74, 62
fig, ax = canvas(W, H)
view = View(40, 18)
pl = Placed(view, 37, 32, 24/np.pi)
ax.add_patch(Circle(pl.c, 24, fc=BLUE_FILL, ec=STROKE, lw=.95, zorder=1))
pts = np.pi*parallel(0.0)
split_plot(ax, pl(pts), view.depth(pts) >= 0, MUTED, lw=.6, hidden_lw=.45, zorder=2)
e3 = np.array([0, 0, 1.0])
for sign, c in ((1, BLUE), (-1, BLUE)):
    a, b = pl(0*e3), pl(sign*np.pi*e3)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=c, lw=1.4, zorder=4)
arrow(ax, pl(.55*np.pi*e3), pl(.75*np.pi*e3), color=BLUE, lw=1.2, scale=7, zorder=5)
arrow(ax, pl(-.75*np.pi*e3), pl(-.5*np.pi*e3), color=BLUE, lw=1.2, scale=7, zorder=5)
top, bot = pl(np.pi*e3), pl(-np.pi*e3)
arrow(ax, (top[0]+5, top[1]-.6), (bot[0]+5, bot[1]+.6), color=MUTED, lw=.85, scale=5.5, zorder=3, rad=-.28)
dot(ax, top, RED, zorder=8, hollow=True); dot(ax, bot, RED, zorder=8, hollow=True)
label(ax, top+[-7.5, 1.4], r'$\pi e_3$', color=RED, halo=True)
label(ax, bot+[-8.0, -1.4], r'$-\pi e_3$', color=RED, halo=True)
w0 = np.array([.6, -.72, .35]); w0 *= np.pi/np.linalg.norm(w0)
for s, c in ((1, GREEN), (-1, GREEN)):
    dot(ax, pl(s*w0), c, zorder=8, hollow=True)
ax.plot(*pl(np.array([-w0, w0])).T, color=GREEN, lw=.65, ls=(0, (3, 2)), zorder=3)
label(ax, pl(w0)+[-1.5, 3.0], r'$\omega_0$', color=GREEN, halo=True)
label(ax, pl(-w0)+[1.5, -3.0], r'$-\omega_0$', color=GREEN, halo=True)
dot(ax, pl(0*e3), INK, zorder=8); label(ax, pl(0*e3)+[3.0, -.6], '$0$', halo=True)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'ball |w|<=pi; rotations about e3: w=theta e3, jumps from pi e3 to -pi e3; antipodal pair w0,-w0'})
