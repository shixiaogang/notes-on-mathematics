"""Height function on the sphere: at p the kernel is the latitude direction; at the pole the differential vanishes."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 104, 58
fig, ax = canvas(W, H)
view = View(72, 30)
pl = Placed(view, 30, 27, 22)
sphere_disc(ax, pl)
for lat in (-60, -30, 0, 30, 60):
    sphere_curve(ax, pl, parallel(np.radians(lat)), MUTED, lw=.4, hidden=False)
p = np.array([0, .6, .8]); e1 = np.array([1.0, 0, 0]); e2 = np.array([0, .8, -.6])
sphere_curve(ax, pl, parallel(np.arcsin(.8)), GREEN, lw=1.3, hidden=False)
a, b = .36, .32
corners = np.array([p+a*e1+b*e2, p+a*e1-b*e2, p-a*e1-b*e2, p-a*e1+b*e2])
ax.add_patch(Polygon(pl(corners), fc='none', ec=YELLOW, lw=1.1, zorder=4))
P = pl(p)
arrow(ax, P, pl(p+.3*e1), color=GREEN, lw=1.5, scale=7.5, zorder=8)
arrow(ax, P, pl(p+.3*e2), color=RED, lw=1.5, scale=7.5, zorder=8)
dot(ax, P, INK, zorder=9)
label(ax, P+[3.0, 1.8], '$p$', halo=True)
label(ax, pl(p+.3*e1)+[-2.6, 1.8], '$e_1$', color=GREEN, halo=True)
label(ax, pl(p+.3*e2)+[3.2, -.6], '$e_2$', color=RED, halo=True)
N = np.array([0, 0, 1.0]); f1 = np.array([.2, 0, 0]); f2 = np.array([0, .2, 0])
cn = np.array([N+f1+f2, N+f1-f2, N-f1-f2, N-f1+f2])
ax.add_patch(Polygon(pl(cn), fc='none', ec=YELLOW, lw=1.1, zorder=4))
dot(ax, pl(N), INK, zorder=9)
label(ax, pl(N)+[-3.6, 2.8], '$N$', halo=True)
# target axis
x0 = 88; y0 = 27; u = 22
arrow(ax, (x0, y0-u-3), (x0, y0+u+4), color=STROKE, lw=.85, scale=5.5)
label(ax, (x0+3, y0+u+3), 'ℝ', 7.5, MUTED)
for v, t in ((-1, '$-1$'), (0, '$0$'), (1, '$1$')):
    ax.plot([x0-1, x0+1], [y0+u*v]*2, color=STROKE, lw=.75)
    label(ax, (x0+3.6, y0+u*v), t, 7.5, MUTED)
ax.plot([x0-1, x0+1], [y0+u*.8]*2, color=STROKE, lw=.75)
label(ax, (x0+4.2, y0+u*.8-.3), '$0.8$', 7.5, MUTED)
dot(ax, (x0, y0+u*.8), INK, size=1.5)
dot(ax, (x0, y0+u), INK, size=1.2)
arrow(ax, (x0, y0+u*.8), (x0, y0+u*.8-u*.3*.6), color=RED, lw=1.5, scale=7.5, zorder=8)
label(ax, (x0-8.5, y0+u*.8-u*.09), r'$-0.6$', 7.5, RED, halo=True)
arrow(ax, (57, 30), (x0-4, 30), color=STROKE, lw=.9)
label(ax, ((57+x0-4)/2, 33), '$h$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h(y)=y3; p=(0,.6,.8); e1=(1,0,0), e2=(0,.8,-.6); dh(e1)=0, dh(e2)=-.6; vectors drawn at .3 of unit length, same factor on the target axis'})
