"""Retraction of the ball union onto the circle (24 samples, eps=.3) and the geometry of the key step (eps=.7)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 62
fig, ax = canvas(W, H)
# (a) 24 samples on unit circle, eps=.3
u = 19; o = np.array([26, 33])
n = 24
ang = np.arange(n)*2*np.pi/n
P = np.stack([np.cos(ang), np.sin(ang)], 1)
for p in P:
    ax.add_patch(Circle(o+u*p, u*.3, fc=BLUE_FILL, ec='none', zorder=1))
th = np.linspace(0, 2*np.pi, 721)
ax.plot(o[0]+u*np.cos(th), o[1]+u*np.sin(th), color=BLUE, lw=1.4, zorder=3)
for p in P:
    dot(ax, o+u*p, INK, size=.65, zorder=5)
for a, s in ((.5, 1.24), (1.25, .8), (2.0, 1.22), (2.75, .78), (3.5, 1.2), (4.25, .77), (5.0, 1.25), (5.75, .79)):
    x = s*np.array([np.cos(a), np.sin(a)]); q = x/np.linalg.norm(x)
    arrow(ax, o+u*x, o+u*q, color=RED, lw=.95, scale=5.5)
panel_tag(ax, o[0], 1.4, '(a)')
# (b) proof, unit circle tau=1, eps=.7, q at the top, x=(1-T)q on the inner normal, T=.3, p at 44 deg, q' at 10 deg
eps = .7; T = .3
u = 24; o2 = np.array([87, 18])
pt = lambda a: np.array([np.sin(np.radians(a)), np.cos(np.radians(a))])
q = pt(0); p = pt(-44); qp = pt(12)
x = (1-T)*q
print('a=', np.linalg.norm(p-q), '|x-p|=', np.linalg.norm(x-p), 'b=', np.linalg.norm(qp-q), 'T bound', eps*eps)
print('max seg dist to qp', max(np.linalg.norm(q+t*(x-q)-qp) for t in np.linspace(0, 1, 101)))
ax.add_patch(Circle(o2+u*p, u*eps, fc=YELLOW_FILL, ec=YELLOW, lw=.8, zorder=1))
ax.add_patch(Circle(o2+u*qp, u*eps, fc=GREEN_FILL, ec=GREEN, lw=.8, zorder=1))

tt = np.radians(np.linspace(-62, 62, 401))
ax.plot(o2[0]+u*np.sin(tt), o2[1]+u*np.cos(tt), color=BLUE, lw=1.4, zorder=3)
ax.plot(*zip(o2+u*q, o2+u*x), color=RED, lw=1.3, zorder=5)
for z, s, off in ((q, r'$\mathbf{q}$', (0, 3)), (x, r'$\mathbf{x}$', (-3.2, -.4)), (p, r'$\mathbf{p}$', (-2.8, 2.0)), (qp, r"$\mathbf{q}'$", (2.2, 2.4))):
    dot(ax, o2+u*z, INK, size=1.0, zorder=6); label(ax, o2+u*z+off, s, 8, halo=True)
label(ax, o2+u*(q+x)/2+(2.2, 0), '$T$', 7.5, RED, halo=True)
label(ax, o2+u*pt(40)+(2.6, 2.5), '$M$', 8, BLUE)
panel_tag(ax, 87, 1.4, '(b)')
# clip the two discs to the panel
for art in ax.patches[-2:]:
    pass
save(fig, OUT, 'figure', {'formula': '(a) 24 samples, eps=.3; (b) tau=1, eps=.7, T=.3, p at 44deg, q prime at 12deg'})
