"""Local diffeomorphisms that are not injective: E(t)=(cos t,sin t) drawn as a helix over the circle, and the doubling map of the circle."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 56
fig, ax = canvas(W, H)
view = View(35, 24)
pl = Placed(view, 27, 18, 9.5)
c = .3
def helix(t):
    return np.c_[np.cos(t), np.sin(t), c*t]
def base(t):
    return np.c_[np.cos(t), np.sin(t), np.full_like(t, -.8)]
t = np.linspace(-.5, 11.2, 1600)
th = np.linspace(0, 2*np.pi, 721)
ax.plot(*pl(base(th)).T, color=BLUE, lw=1.3, zorder=2)
ax.plot(*pl(helix(t)).T, color=STROKE, lw=.95, zorder=3)
q0 = np.pi/3
d = .42
for k in (0, 1):
    t0 = q0+2*np.pi*k
    seg = np.linspace(t0-d, t0+d, 80)
    ax.plot(*pl(helix(seg)).T, color=GREEN if k == 0 else YELLOW, lw=2.2, solid_capstyle='butt', zorder=5)
    a, b = pl(helix(np.array([t0])))[0], pl(base(np.array([q0])))[0]
    ax.plot([a[0], b[0]], [a[1], b[1]], color=MUTED, lw=.6, ls=(0, (2.2, 1.8)), zorder=2)
    dot(ax, a, INK, zorder=8)
seg = np.linspace(q0-d, q0+d, 80)
ax.plot(*pl(base(seg)).T, color=RED, lw=2.2, solid_capstyle='butt', zorder=5)
Q = pl(base(np.array([q0])))[0]
dot(ax, Q, INK, zorder=8)
label(ax, Q+[3, -2.6], '$q$', halo=True)
a0 = pl(helix(np.array([q0])))[0]; a1 = pl(helix(np.array([q0+2*np.pi])))[0]
label(ax, a0+[7.5, 1.2], r'$t=\frac{\pi}{3}$', 7.5, halo=True)
label(ax, a1+[9, 1.2], r'$t=\frac{7\pi}{3}$', 7.5, halo=True)
label(ax, pl(base(np.array([3.6])))[0]+[-3, -3], '$S^1$', color=BLUE)
label(ax, pl(helix(np.array([11.0])))[0]+[3.5, .5], 'ℝ', color=STROKE)
panel_tag(ax, 27, 1.6, '(a)')
# (b) doubling map
r = 11.; c1 = np.array([60., 29.]); c2 = np.array([97., 29.])
def on(c0, a, rr=r):
    return np.c_[c0[0]+rr*np.cos(a), c0[1]+rr*np.sin(a)]
ax.plot(*on(c1, th).T, color=BLUE, lw=1.3, zorder=2)
ax.plot(*on(c2, th).T, color=BLUE, lw=1.3, zorder=2)
d2 = .42
for k, col in zip((0, 1), (GREEN, YELLOW)):
    a0 = np.pi/6+k*np.pi
    seg = np.linspace(a0-d2/2, a0+d2/2, 40)
    ax.plot(*on(c1, seg).T, color=col, lw=2.2, solid_capstyle='butt', zorder=5)
    pt = on(c1, np.array([a0]))[0]
    dot(ax, pt, INK, zorder=8)
seg = np.linspace(np.pi/3-d2, np.pi/3+d2, 40)
ax.plot(*on(c2, seg).T, color=RED, lw=2.2, solid_capstyle='butt', zorder=5)
Qq = on(c2, np.array([np.pi/3]))[0]
dot(ax, Qq, INK, zorder=8)
label(ax, on(c1, np.array([np.pi/6]), r+4.8)[0], r'$\frac{\pi}{6}$', 7.5)
label(ax, on(c1, np.array([7*np.pi/6]), r+5.2)[0], r'$\frac{7\pi}{6}$', 7.5)
label(ax, on(c2, np.array([np.pi/3]), r+4.8)[0], r'$\frac{\pi}{3}$', 7.5)
arrow(ax, (c1[0]+r+5, 29), (c2[0]-r-2, 29), color=STROKE, lw=.9)
label(ax, ((c1[0]+c2[0]+3)/2, 32.4), r'$\theta\mapsto 2\theta$', 7.5)
panel_tag(ax, (c1[0]+c2[0])/2, 1.6, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'helix (cos t,sin t,0.3 t) over circle, q at angle pi/3, half-width .42; doubling map arcs half-width .21 map onto arc half-width .42'})
