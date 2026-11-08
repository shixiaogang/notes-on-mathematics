"""Divergence as area growth: expanding field, rotating field, and the gradient of height on the sphere."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
def field(cx, cy, s, X):
    A = lambda v: np.array([cx, cy])+s*np.asarray(v, float)
    for x in np.arange(-1.5, 1.51, .75):
        for y in np.arange(-1.5, 1.51, .75):
            if abs(x) < 1e-9 and abs(y) < 1e-9: continue
            v = np.array([x, y]); w = X(v); arrow(ax, A(v), A(v+.28*w), color=MUTED, lw=.55, scale=3.8, zorder=2)
    return A
# (a)
A = field(19, 27, 10.5, lambda v: v)
sq = np.array([[.2, .2], [.9, .2], [.9, .9], [.2, .9]])
ax.add_patch(Polygon(A(sq), fc=BLUE_FILL, ec=BLUE, lw=1.0, zorder=3))
k = np.exp(.5)
ax.add_patch(Polygon(A(sq*k), fc='none', ec=RED, lw=1.2, zorder=4))
panel_tag(ax, 19, 1.7, '(a)')
# (b)
B = field(58, 27, 10.5, lambda v: np.array([-v[1], v[0]]))
ax.add_patch(Polygon(B(sq), fc=BLUE_FILL, ec=BLUE, lw=1.0, zorder=3))
a = .5; Rm = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
ax.add_patch(Polygon(B(sq@Rm.T), fc='none', ec=RED, lw=1.2, zorder=4))
panel_tag(ax, 58, 1.7, '(b)')
# (c)
pl = Placed(View(90, 12), 94, 26, 16)
sphere_disc(ax, pl)
for lat in (-40, 40):
    sphere_curve(ax, pl, parallel(np.radians(lat)), BLUE, lw=.8, hidden=False)
for lon in (15, 50, 90, 130, 165):
    for lat in (-65, -25, 15, 55):
        q = spherical(np.radians(lat), np.radians(lon))
        gr = np.array([0, 0, 1.])-q[2]*q
        arrow(ax, pl(q), pl(q+.42*gr), color=RED, lw=.75, scale=5, zorder=6)
label(ax, pl(spherical(np.radians(-10), np.radians(90)))+[12, -12], '$+$', 9, color=INK, halo=True)
label(ax, pl(spherical(np.radians(10), np.radians(90)))+[12, 12.5], '$-$', 9, color=INK, halo=True)
panel_tag(ax, 94, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'X=(x1,x2): flow e^t, square drawn at t=.5; X=(-x2,x1): rotation by .5; sphere: X=grad h (arrows 0.42 scale), div X=-2h'})
