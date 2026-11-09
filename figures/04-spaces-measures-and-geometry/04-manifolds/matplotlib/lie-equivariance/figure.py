"""A three-point cloud, its rotation by 90 degrees and a relabeling: the centroid is equivariant and invariant respectively."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 30
fig, ax = canvas(W, H)
X = np.array([[1.0, 0], [3, 0], [2, 3]])
R = np.array([[0.0, -1], [1, 0]])
perm = [1, 2, 0]
s = 3.3
def plot(cx, cy, pts, names, tag):
    ox, oy = cx, cy
    arrow(ax, (ox-13.5, oy), (ox+13.5, oy), color=MUTED, lw=.7, scale=5)
    arrow(ax, (ox, oy-3), (ox, oy+14.5), color=MUTED, lw=.7, scale=5)
    P = np.array([ox, oy])+s*pts
    poly = np.vstack([P, P[0]])
    ax.plot(poly[:, 0], poly[:, 1], color=BLUE, lw=.85, zorder=3)
    for q, n in zip(P, names):
        dot(ax, q, BLUE)
    return P
ya = 11
dx = 37.3
P1 = plot(18, ya, X, '123', '(a)')
for q, n, d in zip(P1, '123', ((-.6, -2.6), (.6, -2.6), (0, 2.2))):
    label(ax, q+d, n, 7.5, BLUE, halo=True)
m = X.mean(0); c = np.array([18, ya])+s*m; dot(ax, c, RED); label(ax, c+[6.5, 1.8], '$m$', color=RED, halo=True)
P2 = plot(18+dx, ya, X@R.T, '123', '(b)')
for q, n, d in zip(P2, '123', ((2.2, .2), (2.2, .2), (-1.9, .5))):
    label(ax, q+d, n, 7.5, BLUE, halo=True)
c = np.array([18+dx, ya])+s*R@m; dot(ax, c, RED); label(ax, c+[-6.2, -4.4], '$Rm$', color=RED, halo=True)
P3 = plot(18+2*dx, ya, X, '312', '(c)')
for q, n, d in zip(P3, '312', ((-.6, -2.6), (.6, -2.6), (0, 2.2))):
    label(ax, q+d, n, 7.5, BLUE, halo=True)
c = np.array([18+2*dx, ya])+s*m; dot(ax, c, RED); label(ax, c+[6.5, 1.8], '$m$', color=RED, halo=True)
panel_tag(ax, 18, 1.7, '(a)'); panel_tag(ax, 18+dx, 1.7, '(b)'); panel_tag(ax, 18+2*dx, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x1=(1,0),x2=(3,0),x3=(2,3); m=(2,1); R=rotation 90deg; relabel old 1,2,3 -> new 3,1,2'})
