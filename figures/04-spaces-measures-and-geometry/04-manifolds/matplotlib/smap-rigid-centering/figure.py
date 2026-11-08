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

"""Rigid example: x=(1,0),(0,2),(-1,0),(0,-2); y=R90 x+(3,1).  Raw pairs, centred, aligned."""
W, H = 112, 40
fig, ax = canvas(W, H)
x = np.array([[1, 0], [0, 2], [-1, 0], [0, -2.0]]); R = np.array([[0, -1], [1, 0.0]]); t = np.array([3, 1.0]); y = x@R.T+t
s = 4.2
def frame(cx, cy, l, r, b, tp):
    axis(ax, (cx-l, cy), (cx+r, cy)); axis(ax, (cx, cy-b), (cx, cy+tp))
def link(p, q, c=MUTED):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=.55, ls=(0, (2.2, 1.8)), zorder=1)
# (a) raw
cx, cy = 13, 19
frame(cx, cy, 8, 30, 12, 15)
X = cx+s*x[:, 0], cy+s*x[:, 1]; Y = cx+s*y[:, 0], cy+s*y[:, 1]
for i in range(4):
    link((X[0][i], X[1][i]), (Y[0][i], Y[1][i]))
for i in range(4):
    dot(ax, (X[0][i], X[1][i]), BLUE); dot(ax, (Y[0][i], Y[1][i]), GREEN)
dot(ax, (cx, cy), BLUE, hollow=True, zorder=8); dot(ax, (cx+s*3, cy+s), GREEN, hollow=True, zorder=8)
panel_tag(ax, 19, 1.7, '(a)')
# (b) centred
cx2 = 62; s2 = 4.6
frame(cx2, cy, 13, 13, 12, 12)
for i in range(4):
    a = (cx2+s2*x[i, 0], cy+s2*x[i, 1]); q = y[i]-t; b_ = (cx2+s2*q[0], cy+s2*q[1])
    link(a, b_); dot(ax, a, BLUE); dot(ax, b_, GREEN)
panel_tag(ax, cx2, 1.7, '(b)')
# (c) after rotation
cx3 = 94
frame(cx3, cy, 13, 13, 12, 12)
for i in range(4):
    q = y[i]-t; p = (cx3+s2*q[0], cy+s2*q[1])
    dot(ax, p, GREEN, size=2.1, zorder=6); dot(ax, p, BLUE, size=1.05, zorder=7)
panel_tag(ax, cx3, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x as listed; y=R90 x+(3,1); (b) centred pairs; (c) R90 x_i prime overlays y_i prime'})
