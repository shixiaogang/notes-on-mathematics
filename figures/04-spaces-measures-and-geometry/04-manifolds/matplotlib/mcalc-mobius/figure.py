"""Moebius strip: flat identified rectangle, frames along the centre line, and the strip in R^3."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
# (a) rectangle [0,1] x (-1,1), right edge glued to left with a flip
x0, y0, a, b = 9, 11, 42, 11
ax.add_patch(Polygon([(x0, y0-b), (x0+a, y0-b+0), (x0+a, y0+b), (x0, y0+b)], fc=BLUE_FILL, ec='none', zorder=1))
y0 = 22
ax.patches[-1].set_xy([(x0, y0-b), (x0+a, y0-b), (x0+a, y0+b), (x0, y0+b)])
ax.plot([x0, x0+a], [y0, y0], color=BLUE, lw=.8, ls=(0, (3, 2)), zorder=2)
ax.plot([x0, x0+a], [y0-b]*2, color=STROKE, lw=.8, zorder=2); ax.plot([x0, x0+a], [y0+b]*2, color=STROKE, lw=.8, zorder=2)
arrow(ax, (x0, y0-b), (x0, y0+b), color=RED, lw=1.2, scale=7, zorder=4)
arrow(ax, (x0+a, y0+b), (x0+a, y0-b), color=RED, lw=1.2, scale=7, zorder=4)
for k, t in enumerate((.1, .42, .74)):
    P = np.array([x0+a*t, y0])
    arrow(ax, P, P+[8.5, 0], color=GREEN, lw=1.3, scale=6.8, zorder=6)
    arrow(ax, P, P+[0, 7.2], color=PURPLE, lw=1.3, scale=6.8, zorder=6)
    dot(ax, P, INK, size=1.1, zorder=7)
label(ax, (x0+a*.1+10.4, y0-2.4), r'$\partial_t$', 7.5, GREEN, halo=True)
label(ax, (x0+a*.1-2.4, y0+6.6), r'$\partial_s$', 7.5, PURPLE, halo=True)
label(ax, (x0-3.2, y0-b+2), '$0$', 7.5, MUTED, zorder=9); label(ax, (x0+a+3.2, y0-b+2), '$1$', 7.5, MUTED)
panel_tag(ax, x0+a/2, 1.7, '(a)')
# (b) surface
R, hw = 2.0, .72
def S(t, s):
    return np.stack([(R+s*np.cos(t/2))*np.cos(t), (R+s*np.cos(t/2))*np.sin(t), s*np.sin(t/2)], -1)
pl = Placed(View(-55, 30), 83, 25, 7.4)
nt, ns = 360, 30
T = np.linspace(0, 2*np.pi, nt+1); Sg = np.linspace(-hw, hw, ns+1)
polys, depths = [], []
for i in range(nt):
    for j in range(ns):
        c = S(np.array([T[i], T[i+1], T[i+1], T[i]]), np.array([Sg[j], Sg[j], Sg[j+1], Sg[j+1]]))
        polys.append(pl(c)); depths.append(pl.view.depth(c.mean(0)))
order = np.argsort(depths)
ax.add_collection(PolyCollection([polys[k] for k in order], facecolors=BLUE_FILL, edgecolors=BLUE_FILL, linewidths=.25, zorder=1))
ts = np.linspace(0, 4*np.pi, 1441)
edge = S(ts, hw*np.ones_like(ts))
xy = pl(edge)
# edge curve with occlusion against the sorted surface: draw per segment using depth of nearest facet
Pc = np.array([p.mean(0) for p in polys]); Dc = np.array(depths)
vis = []
for q, d in zip(xy, pl.view.depth(edge)):
    near = np.sum((Pc-q)**2, 1) < 1.2**2
    vis.append(d >= Dc[near].max()-.6 if near.any() else True)
vis = np.array(vis)
split_plot(ax, xy, vis, STROKE, lw=.95, hidden=False, zorder=3)
tc = np.linspace(0, 2*np.pi, 721); cc = S(tc, 0*tc)
vc = np.array([d >= Dc[np.sum((Pc-q)**2, 1) < 1.2**2].max()-.55 for q, d in zip(pl(cc), pl.view.depth(cc))])
split_plot(ax, pl(cc), vc, BLUE, lw=.9, hidden=False, zorder=3)
def frame(t, ds_col=PURPLE):
    p = S(np.array(t), np.array(0.)); dt = S(np.array(t+1e-4), np.array(0.))-p; dt /= np.linalg.norm(dt)
    ds = S(np.array(t), np.array(1.))-p; ds /= np.linalg.norm(ds)
    P = pl(p)
    arrow(ax, P, pl(p+.72*dt), color=GREEN, lw=1.2, scale=6.2, zorder=8)
    arrow(ax, P, pl(p+.8*ds), color=ds_col, lw=1.2, scale=6.2, zorder=8)
    dot(ax, P, INK, size=1.0, zorder=9)
    return pl(p+.8*ds)
t0 = -.7
for tt in (t0+1.15, t0+.0):
    q = frame(tt)
label(ax, q+[-1.6, -2.4], r'$\partial_s$', 7.5, PURPLE, halo=True)
q = frame(t0+2*np.pi, RED)
label(ax, q+[1.4, 2.4], r'$-\partial_s$', 7.5, RED, halo=True)
frame(t0+4.3)
panel_tag(ax, 83, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'S(t,s)=((2+s cos(t/2))cos t,(2+s cos(t/2))sin t,s sin(t/2)), |s|<=0.72; frames at visible points of the centre line'})
