"""The same discs of radius 1/2 in the upper half-plane under the Euclidean metric and the metric (dx^2+dy^2)/y^2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 104, 50
fig, ax = canvas(W, H)
R = .3; s = 9.0
def axes(cx, cy):
    arrow(ax, (cx-2.45*s, cy), (cx+2.45*s, cy), color=MUTED, lw=.75, scale=5.5)
    arrow(ax, (cx, cy-1), (cx, cy+4.3*s), color=MUTED, lw=.75, scale=5.5)
    label(ax, (cx+2.45*s, cy+2.2), '$x$', 7.5, MUTED); label(ax, (cx+2.4, cy+4.3*s), '$y$', 7.5, MUTED)
ys = [.5, 1.0, 2.0, 3.0]
tt = np.linspace(0, 2*np.pi, 241)
def discs(cx, cy, hyp):
    for x in (-1.45, 1.45):
        for y in ys:
            if hyp:
                c, e = y*np.cosh(R), y*np.sinh(R)
            else:
                c, e = y, R
            pts = np.c_[cx+s*(x+e*np.cos(tt)), cy+s*(c+e*np.sin(tt))]
            ax.add_patch(Polygon(pts, fc=BLUE_FILL, ec=BLUE, lw=.9, zorder=2))
            dot(ax, (cx+s*x, cy+s*y), INK, size=.8)
    for y in (4, 2, 1, .5, .25):
        pts = (cx, cy+s*y)
        ax.plot([pts[0]-1.1, pts[0]+1.1], [pts[1]]*2, color=RED, lw=1.0, zorder=4)
c1, c2 = 27, 77
axes(c1, 7); axes(c2, 7)
discs(c1, 7, False)
discs(c2, 7, True)
panel_tag(ax, c1, 2.5, '(a)'); panel_tag(ax, c2, 2.5, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hyperbolic ball radius R about (x,y): Euclidean centre (x,y cosh R), radius y sinh R; R=1/2; ticks y=2^k spaced ln 2 in (b)'})
