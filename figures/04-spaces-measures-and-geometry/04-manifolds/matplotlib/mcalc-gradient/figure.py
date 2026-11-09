"""Gradients: the same f under two constant metrics, and the height function on the sphere."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
def panel(cx, cy, s, G, tag, grad, cmax, ctan):
    cl = plt_clip = (cx-1.8*s, cy-1.55*s, 3.5*s, 3.1*s)
    A = lambda x, y: np.c_[np.atleast_1d(cx+s*x), np.atleast_1d(cy+s*y)]
    from matplotlib.patches import Rectangle
    clip = Rectangle(cl[:2], cl[2], cl[3], transform=ax.transData)
    for c in (-1, 0, 1, ctan, 2):
        x = np.array([-3, 3.]); y = c-x
        l, = ax.plot(*A(x, y).T, color=PURPLE, lw=.85 if c == ctan else .55, ls='-' if c == ctan else (0, (2.2, 1.8)), zorder=2)
        l.set_clip_path(clip)
    t = np.linspace(0, 2*np.pi, 361)
    ax.plot(*A(np.cos(t)/np.sqrt(G[0]), np.sin(t)/np.sqrt(G[1])).T, color=BLUE, lw=1.4, zorder=3)
    arrow(ax, A(-1.75, 0)[0], A(1.75, 0)[0], color=MUTED, lw=.7, scale=5, zorder=1)
    arrow(ax, A(0, -1.45)[0], A(0, 1.5)[0], color=MUTED, lw=.7, scale=5, zorder=1)
    arrow(ax, A(0, 0)[0], A(*grad)[0], color=RED, lw=1.4, scale=7.5, zorder=8)
    n = np.sqrt(G[0]*grad[0]**2+G[1]*grad[1]**2)
    u = np.array(grad)/n
    dot(ax, A(*u)[0], INK, size=1.2, zorder=9)
    return A
A = panel(20, 27, 10.5, (1, 1), '(a)', (1, 1), 2, 2**.5)
label(ax, A(1, 1)[0]+[2.4, 2.0], '$(1,1)$', 7.5, RED, halo=True)
panel_tag(ax, 20, 1.7, '(a)')
B = panel(58, 27, 10.5, (1, 4), '(b)', (1, .25), 2, 1.25**.5)
label(ax, B(1, .25)[0]+[4.2, 2.8], r'$(1,\frac{1}{4})$', 7.5, RED, halo=True)
panel_tag(ax, 58, 1.7, '(b)')
# (c) sphere
pl = Placed(View(30, 18), 94, 26, 16)
sphere_disc(ax, pl)
for lat in (-60, -30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), PURPLE, lw=.55, hidden=False)
for lon in (-40, -5, 30, 65, 100):
    for lat in (-50, -20, 10):
        q = spherical(np.radians(lat), np.radians(lon))
        gr = np.array([0, 0, 1.])-q[2]*q
        arrow(ax, pl(q), pl(q+.42*gr), color=RED, lw=.75, scale=5, zorder=6)
p = np.array([0, .6, .8]); gr = np.array([0, -.48, .36])
arrow(ax, pl(p), pl(p+gr), color=RED, lw=1.4, scale=7.5, zorder=8); dot(ax, pl(p), INK, size=1.2, zorder=9)
label(ax, pl(p)+[3.2, -.6], '$p$', halo=True)
N = np.array([0, 0, 1.]); dot(ax, pl(N), INK, size=1.0, zorder=9); label(ax, pl(N)+[2.8, 1.2], '$N$', 7.5, halo=True)
panel_tag(ax, 94, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=x+y; unit balls of G=I, diag(1,4); gradients (1,1), (1,1/4); level line through touching point; sphere: grad h = e3-(e3.q)q, drawn at 0.42 scale, except p drawn at true length (0,-.48,.36)'})
