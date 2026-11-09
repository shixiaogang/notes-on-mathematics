from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Nine uniformly spaced parameter values for three scalarizations on the dented front (dense grid search).
u = np.linspace(0, 1, 20001); v = bump(u); z = np.array([-.1, -.1])
pts = {}
W = np.linspace(.1, .9, 9)
pts['w'] = [(u[i], v[i]) for i in (int(np.argmin(w*u+(1-w)*v)) for w in W)]
T = np.linspace(.1, .9, 9)
pts['t'] = [(t, float(bump(t))) for t in T]
pts['c'] = [(u[i], v[i]) for i in (int(np.argmin(np.maximum(w*(u-z[0]), (1-w)*(v-z[1])))) for w in W)]
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panels(fig, .07, .99, .985, .26, .16)
for ax, k in zip(axes, 'wtc'):
    setup(ax, (0, 1.05), (0, 1.05), [0, .5, 1], [0, .5, 1], yl='$f_2$' if k == 'w' else '', equal=True)
    if k != 'w': ax.set_yticklabels([])
    ax.plot(u, v, color=BLUE, lw=1.1, zorder=2); P = np.array(pts[k]); ax.plot(P[:, 0], P[:, 1], 'o', color=GREEN, ms=4, mew=0, zorder=4)
tags(fig, axes)
save(fig, HERE, 'figure', {k: [list(map(float, p)) for p in pts[k]] for k in pts}); print(np.round(pts['w'], 3).tolist())
