"""Figure eight alpha(t)=(sin 2t, sin t) on (-pi,pi): parameter interval, whole image, and zoom at the origin."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 54
fig, ax = canvas(W, H)
y0 = 30
x = lambda t: 4+(np.asarray(t)+np.pi)/(2*np.pi)*32
ax.plot([x(-np.pi), x(np.pi)], [y0, y0], color=BLUE, lw=1.3, zorder=2)
ax.plot([x(-1), x(1)], [y0, y0], color=GREEN, lw=2.4, solid_capstyle='butt', zorder=3)
ax.plot([x(2.75), x(np.pi)], [y0, y0], color=RED, lw=2.4, solid_capstyle='butt', zorder=3)
ax.plot([x(-np.pi), x(-2.75)], [y0, y0], color=YELLOW, lw=2.4, solid_capstyle='butt', zorder=3)
for t, s in ((-np.pi, r'$-\pi$'), (0, '$0$'), (np.pi, r'$\pi$')):
    label(ax, (float(x(t)), y0-4), s, 7.5, MUTED)
for t in (-np.pi, np.pi):
    dot(ax, (float(x(t)), y0), BLUE, size=1.4, hollow=True)
dot(ax, (float(x(0)), y0), INK, size=1.3)
for k in (3, 10, 20):
    dot(ax, (float(x(np.pi-1/k)), y0), INK, size=.9)
label(ax, (float(x(np.pi-.3)), y0+4), '$t_k$', 7.5, halo=True)
panel_tag(ax, float(x(0)), 1.6, '(a)')
# (b) figure eight
c = np.array([62., 29.]); u = 19.
tt = np.linspace(-np.pi, np.pi, 1441)
def al(t): return np.c_[c[0]+u*np.sin(2*t), c[1]+u*np.sin(t)]
ax.plot(*al(tt[1:-1]).T, color=BLUE, lw=1.3, zorder=2)
ax.plot(*al(np.linspace(-1, 1, 300)).T, color=GREEN, lw=2.4, solid_capstyle='butt', zorder=3)
ax.plot(*al(np.linspace(2.75, np.pi-1e-3, 100)).T, color=RED, lw=2.4, solid_capstyle='butt', zorder=3)
ax.plot(*al(np.linspace(-np.pi+1e-3, -2.75, 100)).T, color=YELLOW, lw=2.4, solid_capstyle='butt', zorder=3)
from matplotlib.patches import Rectangle
sq = .3
ax.add_patch(Rectangle((c[0]-u*sq, c[1]-u*sq), 2*u*sq, 2*u*sq, fc='none', ec=MUTED, lw=.7, ls=(0, (2.2, 1.8)), zorder=4))
dot(ax, c, INK, zorder=8)
label(ax, c+[9.5, 3.0], '$t=0$', 7.5, halo=True)
label(ax, c+[-13, 21], '$t>0$', 7.5, MUTED); label(ax, c+[-13, -21], '$t<0$', 7.5, MUTED)
panel_tag(ax, c[0], 1.6, '(b)')
# (c) zoom near origin
c2 = np.array([98.5, 29.]); zo = 12.5/.3
def alz(t): return np.c_[c2[0]+zo*np.sin(2*t), c2[1]+zo*np.sin(t)]
from matplotlib.patches import Rectangle as R
clip = R((c2[0]-12.5, c2[1]-12.5), 25, 25, transform=ax.transData, fc='none', ec=MUTED, lw=.7, ls=(0, (2.2, 1.8)), zorder=4)
ax.add_patch(clip)
for seg, col, lw in ((np.linspace(-1, 1, 400), GREEN, 2.0), (np.linspace(2.6, np.pi-1e-3, 300), RED, 2.0), (np.linspace(-np.pi+1e-3, -2.6, 300), YELLOW, 2.0)):
    ln, = ax.plot(*alz(seg).T, color=col, lw=lw, solid_capstyle='butt', zorder=3); ln.set_clip_path(clip)
dot(ax, c2, INK, zorder=8)
for k, m in ((10, '$k=10$'), (20, '$k=20$')):
    t = np.pi-1/k
    Pk = alz(np.array([t]))[0]
    dot(ax, Pk, INK, size=1.1, zorder=8)
Pk3 = alz(np.array([np.pi-1/10]))[0]
label(ax, Pk3+[3.0, 3.2], '$\\alpha(t_{10})$', 7.5, halo=True)
panel_tag(ax, c2[0], 1.6, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'alpha(t)=(sin 2t, sin t), t in (-pi,pi); green t in (-1,1), red t in (2.75,pi), yellow t in (-pi,-2.75); t_k=pi-1/k'})
