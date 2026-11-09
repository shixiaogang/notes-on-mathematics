from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
def axes_box(ax, x0, y0, w, h, xlim, ylim):
    """Plain axes at mm position on the canvas (data coordinates in the returned callable)."""
    sx, sy = w/(xlim[1]-xlim[0]), h/(ylim[1]-ylim[0])
    return (lambda x, y: (x0+(np.asarray(x)-xlim[0])*sx, y0+(np.asarray(y)-ylim[0])*sy))
def axis(ax, a, b, **kw):
    arrow(ax, a, b, color=MUTED, lw=.75, scale=5.5, zorder=2)

"""Denominator c=3-u-v of the example homography; equal image errors have algebraic size c*err."""
W, H = 112, 50
fig, ax = canvas(W, H)
Hm = np.array([[2, 0, 0], [0, 2, 0], [-1, -1, 3.0]])
# (a) source plane levels
s, cx, cy = 12, 7, 9
P = lambda p: (cx+s*p[0], cy+s*p[1])
for c, col, lw in ((2, BLUE, .8), (1, BLUE, .8), (.5, BLUE, .8)):
    a = 3-c
    ax.plot([P((max(a-2.6, 0), a-max(a-2.6, 0)))[0], P((a-max(a-2.6, 0), max(a-2.6, 0)))[0]], [P((max(a-2.6, 0), a-max(a-2.6, 0)))[1], P((a-max(a-2.6, 0), max(a-2.6, 0)))[1]], color=col, lw=lw, zorder=2)
ax.plot([P((.2, 2.8))[0], P((2.8, .2))[0]], [P((.2, 2.8))[1], P((2.8, .2))[1]], color=RED, lw=1.25, zorder=3)
axis(ax, P((-.2, 0)), P((3.25, 0))); axis(ax, P((0, -.2)), P((0, 3.1)))
pts = [(0, 0, GREEN), (1, 1, GREEN), (1.25, 1.25, GREEN)]
for u, v, col in pts: dot(ax, P((u, v)), col)
label(ax, P((3.25, 0))+np.array([-.4, 2.0]), '$u$', 7.5, MUTED, ha='right'); label(ax, P((0, 3.1))+np.array([1.5, -.5]), '$v$', 7.5, MUTED, ha='left')
for a, txt in ((1, '2'), (2, '1'), (2.5, r'$\frac{1}{2}$')):
    label(ax, P((a, 0))+np.array([0, -2.8]), txt, 7.5, BLUE)
label(ax, P((1.45, 1.55))+np.array([1.5, 2.2]), '$c=0$', 7.5, RED, ha='left', halo=True)
panel_tag(ax, 28, 1.7, '(a)')
# (b) image with circles of equal radius
sc, cx2, cy2 = 7.0, 64, 9
Q = lambda p: (cx2+sc*p[0], cy2+sc*p[1])
def proj(u, v):
    z = Hm@np.array([u, v, 1.0]); return z[:2]/z[2]
t = np.linspace(0, 1.25, 60)
for k in np.linspace(0, 1.25, 6):
    a = np.array([proj(k, x) for x in t]); b = np.array([proj(x, k) for x in t])
    ax.plot(cx2+sc*a[:, 0], cy2+sc*a[:, 1], color=GREEN, lw=.6, zorder=2); ax.plot(cx2+sc*b[:, 0], cy2+sc*b[:, 1], color=GREEN, lw=.6, zorder=2)
th = np.linspace(0, 2*np.pi, 121); r = .2
for u, v, col in pts:
    q = proj(u, v)
    ax.plot(cx2+sc*(q[0]+r*np.cos(th)), cy2+sc*(q[1]+r*np.sin(th)), color=RED, lw=.8, zorder=4); dot(ax, Q(q), col, zorder=5)
label(ax, Q((0, 0))+np.array([-2, -1.4]), '(0,0)', 7, MUTED, ha='right'); label(ax, Q((2, 2))+np.array([-5.2, 2.6]), '(2,2)', 7, MUTED, ha='right'); label(ax, Q((5, 5))+np.array([-1.4, 2.2]), '(5,5)', 7, MUTED, ha='right')
panel_tag(ax, 82, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'c=3-u-v; H=[2,0,0;0,2,0;-1,-1,3]; points (0,0),(1,1),(1.25,1.25)'})
