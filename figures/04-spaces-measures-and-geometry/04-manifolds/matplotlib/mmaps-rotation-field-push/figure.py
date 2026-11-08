"""Pushing fields by R=R_theta (theta=pi/2) in the north chart."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 46
fig, ax = canvas(W, H)
s = 4.3
GX = (-3, -1.5, 0, 1.5, 3)
Rt = lambda v: np.array([-v[1], v[0]])
def axes(cx, cy):
    arrow(ax, (cx-3.95*s, cy), (cx+3.95*s, cy), color=MUTED, lw=.7, scale=5.5)
    arrow(ax, (cx, cy-4.2*s), (cx, cy+4.2*s), color=MUTED, lw=.7, scale=5.5)
    label(ax, (cx+3.95*s, cy+2.2), '$u_1$', 7.5, MUTED); label(ax, (cx+2.6, cy+4.2*s), '$u_2$', 7.5, MUTED)
def field(cx, cy, f, mark=None, mcol=RED):
    for x in GX:
        for y in GX:
            if x == 0 and y == 0 and f(np.array([0., 0.])).sum() == 0:
                continue
            P = np.array([cx+s*x, cy+s*y]); v = f(np.array([x, y], float))
            is_m = mark is not None and (x, y) in mark
            arrow(ax, P, P+s*v, color=mcol if is_m else BLUE, lw=1.4 if is_m else .85, scale=6.5 if is_m else 5, zorder=7 if is_m else 5)
            if is_m:
                dot(ax, P, INK, zorder=9)
cy = 25
axes(19.5, cy); field(19.5, cy, lambda u: np.array([.8, 0.]), mark=[(0, 3)])
axes(56, cy); field(56, cy, lambda u: np.array([0., .8]), mark=[(-3, 0)])
axes(92.5, cy); field(92.5, cy, lambda u: .28*Rt(u), mark=[(0, 3), (-3, 0)])
label(ax, (19.5-6, cy+3*s+2.3), '$p$', 7.5, halo=True)
label(ax, (56-3*s-.2, cy-2.7), r'$R_\theta(p)$', 7.5, halo=True)
panel_tag(ax, 19.5, 1.7, '(a)'); panel_tag(ax, 56, 1.7, '(b)'); panel_tag(ax, 92.5, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hat X=e1 pushed by R(pi/2) gives e2 (drawn at .8 unit); hat X(u)=(-u2,u1) (drawn at .28) is invariant'})
