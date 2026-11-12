"""Dirichlet densities on the simplex p1+p2+p3=1 (equilateral-triangle chart, density w.r.t. (p1,p2)).
(a) alpha=(1,1,1): constant 2; (b) alpha=(2,3,5): peak near the mode (1/7,2/7,4/7), mean (0.2,0.3,0.5) red;
(c) alpha=(0.5,0.5,0.5): density grows towards edges and corners (colour clipped at 3).
White-to-blue scale, darker = larger; each panel uses its own levels."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *
import matplotlib.tri as mtri

def dens(P, a):
    lc = math.lgamma(sum(a))-sum(math.lgamma(x) for x in a)
    return np.exp(lc+sum((ai-1)*np.log(P[:, i]) for i, ai in enumerate(a)))
N = 120; pts = []
for i in range(N+1):
    for j in range(N+1-i):
        pts.append((i/N, j/N, 1-(i+j)/N))
P = np.clip(np.array(pts), 1e-4, 1); P /= P.sum(1, keepdims=True)
x, y = tri_xy(P); T = mtri.Triangulation(x, y)
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, left=.01, right=.99, top=.98, bottom=.14, wspace=.06)
cases = [((1, 1, 1), [0, 2.0001, 2.0002]), ((2, 3, 5), np.linspace(0, 11.2, 9)), ((.5, .5, .5), np.r_[np.linspace(0, 3, 9)[:-1], 3.001])]
facts = {}
for ax, (a, lev) in zip(axes, cases):
    f = dens(P, a); facts[str(a)] = float(dens(np.array([[.2, .3, .5]]), a)[0])
    if a == (1, 1, 1):
        ax.tripcolor(T, np.full_like(f, 2.), cmap=FIELD, vmin=0, vmax=4, shading='gouraud')
    else:
        ax.tricontourf(T, np.minimum(f, lev[-1]*.999), levels=lev, cmap=FIELD)
    tri_frame(ax, labels=('$e_1$', '$e_2$', '$e_3$'))
    m = np.array(a)/sum(a); mx, my = tri_xy(m); dot(ax, float(mx), float(my), ms=3.6)
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'density_at_(.2,.3,.5)': facts})
