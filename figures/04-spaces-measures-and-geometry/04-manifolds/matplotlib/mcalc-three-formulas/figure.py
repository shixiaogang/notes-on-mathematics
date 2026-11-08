"""Green, Gauss and classical Stokes: orientation of boundaries, with the hemisphere frame n, N, t."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
W, H = 112, 50
fig, ax = canvas(W, H)
# (a) annulus
c = np.array([19., 27.]); R, r = 15., 7.
th = np.linspace(0, 2*np.pi, 361)
ax.fill(np.r_[c[0]+R*np.cos(th), c[0]+r*np.cos(th[::-1])], np.r_[c[1]+R*np.sin(th), c[1]+r*np.sin(th[::-1])], fc=BLUE_FILL, ec='none', zorder=1)
ax.plot(c[0]+R*np.cos(th), c[1]+R*np.sin(th), color=BLUE, lw=1.3, zorder=3)
ax.plot(c[0]+r*np.cos(th), c[1]+r*np.sin(th), color=BLUE, lw=1.3, zorder=3)
for a, rad, sgn in ((-50, R, 1), (130, R, 1), (40, r, -1), (220, r, -1)):
    a = np.radians(a); p = c+rad*np.array([np.cos(a), np.sin(a)]); t = sgn*np.array([-np.sin(a), np.cos(a)])
    arrow(ax, p-1.6*t, p+1.6*t, color=BLUE, lw=1.3, scale=8.5, zorder=6)
label(ax, c+[0, -11.0], '$D$', color=INK, halo=True)
panel_tag(ax, c[0], 1.7, '(a)')
# (b) ball with outward normals
pl = Placed(View(25, 18), 56.5, 27, 15)
sphere_disc(ax, pl)
for pt in spherical(np.radians([55, 30, 2, -30, -55, 15, -12, 40, -40]), np.radians([-30, 80, 110, 90, -20, -60, 25, 25, 55])):
    if pl.view.depth(pt) < .05: continue
    arrow(ax, pl(pt), pl(pt*1.42), color=RED, lw=1.2, scale=6.8, zorder=7); dot(ax, pl(pt), RED, size=.9, zorder=8)
for pt in [(0, 1, 0), (-.42, .9, 0), (1, 0, 0)]:
    pass
label(ax, pl.c+[-3.5, -3], '$V$', halo=True)
sphere_curve(ax, pl, parallel(0), MUTED, lw=.4, hidden=False)
panel_tag(ax, 56.5, 1.7, '(b)')
# (c) hemisphere
pl = Placed(View(0, 24), 93, 15, 15)
t = np.linspace(0, np.pi/2, 60); ph = np.linspace(0, 2*np.pi, 241)
polys, dd = [], []
for i in range(59):
    for j in range(240):
        q = spherical(np.array([t[i], t[i], t[i+1], t[i+1]]), np.array([ph[j], ph[j+1], ph[j+1], ph[j]]))
        polys.append(pl(q)); dd.append(pl.view.depth(q.mean(0)))
o = np.argsort(dd)
ax.add_collection(PolyCollection([polys[k] for k in o], facecolors=BLUE_FILL, edgecolors=BLUE_FILL, linewidths=.25, zorder=1))
# silhouette great circle (upper part)
f = pl.view.f
e1 = np.cross(f, [0, 0, 1]); e1 /= np.linalg.norm(e1); e2 = np.cross(f, e1)
ss = np.linspace(0, 2*np.pi, 721)
sil = np.cos(ss)[:, None]*e1+np.sin(ss)[:, None]*e2
for a, b in runs(sil[:, 2] >= 0):
    ax.plot(*pl(sil[a:b]).T, color=STROKE, lw=.95, zorder=2)
eq = parallel(0)
sphere_curve(ax, pl, eq, BLUE, lw=1.3)
# boundary direction arrow (counterclockwise seen from above)
az = np.radians(-38)
q = np.array([np.cos(az), np.sin(az), 0]); N = np.array([0, 0, -1.]); tv = np.cross(q, N)
Q = pl(q)
arrow(ax, Q, pl(q+.95*tv), color=GREEN, lw=1.3, scale=7, zorder=8)
arrow(ax, Q, pl(q+.6*N), color=RED, lw=1.3, scale=7, zorder=8)
arrow(ax, Q, pl(q+.6*q), color=PURPLE, lw=1.3, scale=7, zorder=8)
dot(ax, Q, INK, size=1.2, zorder=9)
label(ax, pl(q+.95*tv)+[0.8, 2.6], r'$\bm{t}$'.replace(r'\bm{t}', 't'), color=GREEN, halo=True)
label(ax, pl(q+.6*N)+[2.8, 0], '$N$', color=RED, halo=True)
label(ax, pl(q+.6*q)+[-2.8, -1.0], '$n$', color=PURPLE, halo=True)
top = spherical(np.radians(60), np.radians(25))
arrow(ax, pl(top), pl(top*1.5), color=PURPLE, lw=1.3, scale=7, zorder=8); dot(ax, pl(top), INK, size=1.1, zorder=9)
label(ax, pl(top*1.5)+[2.8, 0.6], '$n$', color=PURPLE, halo=True)
label(ax, pl.c+[7, 7], '$S$', halo=True)
panel_tag(ax, 93, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'annulus radii 7,15 mm; ball; upper hemisphere; at q on equator N=-e3, t=q x N, n=q'})
