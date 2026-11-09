from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Hypervolume comparison flips with the reference point: S1={(1,6),(6,1)}, S2={(3,3)}.
S = [np.array([[1., 6.], [6., 1.]]), np.array([[3., 3.]])]
def rects(P, r):
    xs = np.r_[P[:, 0], r[0]]; return [(xs[i], xs[i+1], P[i, 1]) for i in range(len(P))]
def hv(P, r): return sum((b-a)*(r[1]-y) for a, b, y in rects(P, r))
R = [np.array([7., 7.]), np.array([20., 20.])]
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .07, .985, .985, .19, .22)
out = []
for ax, r in zip(axes, R):
    m = r[0]*1.08; step = 2 if r[0] < 10 else 5; setup(ax, (0, m), (0, m), range(0, int(m)+1, step), range(0, int(m)+1, step), equal=True)
    for a, b, y in rects(S[0], r): ax.fill([a, b, b, a], [y, y, r[1], r[1]], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.8, zorder=1)
    for a, b, y in rects(S[1], r): ax.fill([a, b, b, a], [y, y, r[1], r[1]], facecolor='none', edgecolor=GREEN, lw=1.3, zorder=2)
    ax.plot(S[0][:, 0], S[0][:, 1], 'o', color=BLUE, ms=5, mew=0, zorder=4); ax.plot(S[1][:, 0], S[1][:, 1], 's', color=GREEN, ms=4.8, mew=0, zorder=4); dot(ax, r, PURPLE)
    ax.text(r[0]*.97, r[1]*1.02, '$r$', color=PURPLE, ha='right'); out.append((hv(S[0], r), hv(S[1], r)))
tags(fig, axes)
save(fig, HERE, 'figure', {'hv': out}); print(out)
