"""Hexagon on the unit circle: union of open balls at r=.4,.7,1.05 and the Cech complex underneath."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
from matplotlib.patches import Circle, Polygon
OUT = Path(__file__).resolve().parent

W, H = 112, 72
fig, ax = canvas(W, H)
P = np.array([[np.cos(k*np.pi/3), np.sin(k*np.pi/3)] for k in range(6)])
u = 9.0
th = np.linspace(0, 2*np.pi, 721)
for r, cx, tag in ((.4, 19, '(a)'), (.7, 56, '(b)'), (1.05, 93, '(c)')):
    o = np.array([cx, 50])
    for p in P:
        ax.add_patch(Circle(o+u*p, u*r, fc=BLUE_FILL, ec='none', zorder=1))
    for p in P:
        ax.add_patch(Circle(o+u*p, u*r, fc='none', ec=BLUE, lw=.5, zorder=2))
    ax.plot(o[0]+u*np.cos(th), o[1]+u*np.sin(th), color=MUTED, lw=.75, ls=(0, (2.2, 1.8)), zorder=3)
    for p in P:
        dot(ax, o+u*p, INK, size=.95, zorder=5)
    dot(ax, o, RED, size=.8, zorder=5, hollow=(r <= 1))
    label(ax, (cx, 30.3), f'$r={r}$', 7.5, MUTED)
    o2 = np.array([cx, 15.8])
    v = 9.0
    Q = o2+v*P
    if r > 1:
        ax.add_patch(Polygon(Q, fc=YELLOW_FILL, ec='none', zorder=1))
        for a in range(6):
            for b in range(a+1, 6):
                ax.plot(*zip(Q[a], Q[b]), color=YELLOW, lw=.7, zorder=2)
    if r > .5:
        for a in range(6):
            ax.plot(*zip(Q[a], Q[(a+1) % 6]), color=GREEN, lw=1.2, zorder=3)
    for q in Q:
        dot(ax, q, INK, size=.95, zorder=5)
    panel_tag(ax, cx, 1.4, tag)
save(fig, OUT, 'figure', {'formula': 'unit hexagon vertices; Cech complex by radius: edge at r>.5 for neighbours, all simplices for r>1'})
