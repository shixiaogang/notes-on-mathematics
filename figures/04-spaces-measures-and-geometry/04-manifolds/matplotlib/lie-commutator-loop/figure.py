"""The four arcs of the group commutator exp(eX)exp(eY)exp(-eX)exp(-eY) applied to p, and the gap against e^2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *

W, H = 112, 62
fig, ax = canvas(W, H)
view = View(38, 30)
pl = Placed(view, 30, 33, 27)
def rot(u, th):
    u = np.asarray(u, float)/np.linalg.norm(u)
    K = np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])
    return np.eye(3)+np.sin(th)*K+(1-np.cos(th))*K@K
e1, e2, e3 = np.eye(3)
p = np.array([1, 1, 1.0])/np.sqrt(3)
EPS = .55
sphere_disc(ax, pl)
for lat in np.radians([0, 45]):
    sphere_curve(ax, pl, parallel(lat), GRID, lw=.5, hidden=False, zorder=2)
for lon in np.radians([0, 90, 180, 270]):
    sphere_curve(ax, pl, meridian(lon), GRID, lw=.5, hidden=False, zorder=2)
steps = [(e2, -EPS, GREEN), (e1, -EPS, BLUE), (e2, EPS, GREEN), (e1, EPS, BLUE)]
q = p.copy()
marks = [p.copy()]
for axis, th, c in steps:
    s = np.linspace(0, th, 60)
    arc = np.array([rot(axis, v)@q for v in s])
    sphere_curve(ax, pl, arc, c, lw=1.35, hidden=False, zorder=5)
    arrow(ax, pl(arc[-6]), pl(arc[-1]), color=c, lw=1.0, scale=6, zorder=6)
    q = rot(axis, th)@q
    marks.append(q.copy())
end = q
arrow(ax, pl(p), pl(end), color=RED, lw=1.2, scale=6.5, zorder=8)
dot(ax, pl(p), INK, zorder=9); label(ax, pl(p)+[2.2, -3.0], '$p$', halo=True, zorder=10)
dot(ax, pl(end), RED, zorder=9); ax.plot(*zip(pl(end)+[-.6, .3], pl(end)+[-13, 5.4]), color=RED, lw=.6, zorder=8)
label(ax, pl(end)+[-17.8, 6.2], r'$c(\varepsilon)p$', color=RED, halo=True, zorder=10)
# (b) gap against epsilon^2 on log-log axes.
x0, y0, wid, hgt = 72, 11, 37, 42
ax.plot([x0, x0+wid], [y0, y0], color=STROKE, lw=.95); ax.plot([x0, x0], [y0, y0+hgt], color=STROKE, lw=.95)
eps = np.geomspace(.04, 1.2, 80)
def gap(e):
    c = rot(e1, e)@rot(e2, e)@rot(e1, -e)@rot(e2, -e)
    return np.linalg.norm(c@p-p)
g = np.array([gap(e) for e in eps])
pred = eps**2*np.linalg.norm(np.cross(e3, p))
lx = lambda v: x0+wid*(np.log10(v)-np.log10(.03))/(np.log10(1.6)-np.log10(.03))
ly = lambda v: y0+hgt*(np.log10(v)+3.2)/(3.2+.3)
ax.plot(lx(eps), ly(g), color=RED, lw=1.4, zorder=4)
ax.plot(lx(eps), ly(pred), color=INK, lw=.75, ls=(0, (3, 2)), zorder=5)
for v, name in ((.1, '0.1'), (1.0, '1')):
    ax.plot([lx(v)]*2, [y0, y0-1], color=STROKE, lw=.8); label(ax, (lx(v), y0-3.3), name, 7.5, MUTED)
for v, name in ((.001, '$10^{-3}$'), (.1, '$10^{-1}$')):
    ax.plot([x0, x0-1], [ly(v)]*2, color=STROKE, lw=.8); label(ax, (x0-1.6, ly(v)), name, 7.5, MUTED, ha='right')
label(ax, (x0+wid+.2, y0-3.3), r'$\varepsilon$', 7.5, MUTED, ha='right')
label(ax, (lx(.42), ly(g[60])+4.4), r'$\Vert c(\varepsilon)p-p\Vert$', 7.5, RED, halo=True)
label(ax, (lx(.25), ly(.02)-6.0), r'$\varepsilon^2\Vert e_3\times p\Vert$', 7.5, INK, halo=True)
panel_tag(ax, 30, 1.7, '(a)'); panel_tag(ax, x0+wid/2, 1.7, '(b)')
print('gap at .55', np.linalg.norm(end-p), 'pred', EPS**2*np.linalg.norm(np.cross(e3, p)), 'end', end)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'c=exp(eX)exp(eY)exp(-eX)exp(-eY), X=[e1]x, Y=[e2]x, p=(1,1,1)/sqrt3, e=.55; c p - p ~ e^2 e3 x p'})
