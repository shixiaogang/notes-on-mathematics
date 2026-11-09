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

"""Degenerate 3-D configurations: coincident points, collinear points with rotation about their line, non-collinear points."""
W, H = 112, 42
fig, ax = canvas(W, H)
V = View(35, 28)
def fan(pl, axis_dir, centre, pts, colour):
    """Circle traced by points around an axis through centre."""
    a = np.asarray(axis_dir, float); a /= np.linalg.norm(a)
    for p in pts:
        p = np.asarray(p, float); rel = p-centre; par = rel@a*a; perp = rel-par
        e2 = np.cross(a, perp); t = np.linspace(0, 2*np.pi, 241)
        c = centre+par+np.cos(t)[:, None]*perp+np.sin(t)[:, None]*e2
        ax.plot(*pl(c).T, color=colour, lw=.65, ls=(0, (2.2, 1.8)), zorder=2)
def line3(pl, a, b, colour, lw=1.1, dashed=False):
    ax.plot(*pl(np.array([a, b], float)).T, color=colour, lw=lw, ls=(0, (2.2, 1.8)) if dashed else '-', zorder=3)
# (a) coincident: a single point; a frame turning about it
pl = Placed(V, 18, 23, 11)
def rodrigues(w, ang):
    w = np.asarray(w, float)/np.linalg.norm(w); K = np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*K@K
for ang, c in ((0, BLUE), (1.05, GREEN)):
    R = rodrigues((.6, -.3, .9), ang)
    for v in R.T:
        arrow(ax, pl(np.zeros(3)), pl(v*1.05), color=c, lw=.95, scale=5.5)
dot(ax, pl(np.zeros(3)), INK); panel_tag(ax, 18, 1.7, '(a)')
# (b) collinear points on the z axis, with circles around the line
pl = Placed(V, 56, 22, 12)
line3(pl, (0, 0, -1.15), (0, 0, 1.2), BLUE)
pts = np.array([[0, 0, -.8], [0, 0, 0.1], [0, 0, .9]])
for p in pts: dot(ax, pl(p), BLUE)
ring = [(.75, 0, .9), (.75, 0, 0.1), (.75, 0, -.8)]
fan(pl, (0, 0, 1), np.zeros(3), ring, GREEN)
d = pl(np.array(ring[1]))
dot(ax, d, GREEN); arrow(ax, pl(np.array([.75, 0, .1])), pl(np.array([.5303, .5303, .1])), color=RED, lw=.9, scale=5.5, rad=.2)
panel_tag(ax, 56, 1.7, '(b)')
# (c) three non-collinear points: rotation about the line through two moves the third
pl = Placed(V, 92, 22, 12)
A, B, C = np.array([-.7, -.35, -.35]), np.array([.7, -.15, .1]), np.array([-.05, .5, .55])
tri = np.array([A, B, C, A])
ax.fill(*pl(tri).T, color=BLUE_FILL, zorder=1)
ax.plot(*pl(tri).T, color=BLUE, lw=1.1, zorder=3)
for p in (A, B, C): dot(ax, pl(p), BLUE)
ab = B-A
ab = ab/np.linalg.norm(ab); line3(pl, A-.28*ab, B+.28*ab, MUTED, lw=.7, dashed=True)
fan(pl, ab, A, [C], RED)
panel_tag(ax, 92, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'orthographic view; (b) points on the z axis; (c) circle of C about line AB'})
