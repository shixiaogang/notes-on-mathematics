from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Scan of the anisotropic pair: uniform weights versus chord-normal refinement. Exact weighted solutions x(w).
F = lambda w: fm(xm(w))
def adaptive(k, lo=0., hi=1.):
    pts = [(float(hi), F(hi)), (float(lo), F(lo))]  # sorted by f1 ascending: w=1 first
    Ws = [hi, lo]
    while len(pts) < k:
        gaps = [np.linalg.norm((pts[i+1][1]-pts[i][1])/np.array([25, 12.5])) for i in range(len(pts)-1)]
        i = int(np.argmax(gaps)); p, q = pts[i][1], pts[i+1][1]
        w = abs(q[1]-p[1])/(abs(q[1]-p[1])+abs(q[0]-p[0])); pts.insert(i+1, (w, F(w)))
    return np.array([x[0] for x in pts]), np.array([x[1] for x in pts])
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
W = np.linspace(0, 1, 11); uni = F(W).T; aw, ad = adaptive(11)
Fc = F(np.linspace(0, 1, 800))
for ax, P in zip(axes, (uni, ad)):
    setup(ax, (0, 50), (0, 13), range(0, 51, 10), range(0, 14, 4))
    ax.plot(Fc[0], Fc[1], color=BLUE, lw=1.1, zorder=2); ax.plot(P[:, 0], P[:, 1], 'o', color=GREEN, ms=4.2, mew=0, zorder=4)
tags(fig, axes)
gap = lambda P: np.linalg.norm(np.diff(P[np.argsort(P[:, 0])]/np.array([48.5, 12.5]), axis=0), axis=1)
save(fig, HERE, 'figure', {'uniform_max_gap': float(gap(uni).max()), 'adaptive_max_gap': float(gap(ad).max()), 'adaptive_w': aw.tolist()}); print(gap(uni).max(), gap(uni).min(), gap(ad).max(), gap(ad).min(), np.round(aw, 3))
