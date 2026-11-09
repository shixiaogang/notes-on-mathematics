from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Distance to the ideal point after min-max normalization: range from A..D versus range widened by G=(1.5,36).
P = {k: np.array(CANDS[k], float) for k in 'ABCD'}
def norm(p, lo, hi): return (p-lo)/(hi-lo)
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .08, .985, .985, .19, .24)
R = [(np.array([1., 1.]), np.array([6., 8.])), (np.array([1., 1.]), np.array([6., 36.]))]
out = []
for ax, (lo, hi) in zip(axes, R):
    setup(ax, (-.06, 1.12), (-.06, 1.12), [0, .5, 1], [0, .5, 1], '归一化成本', '归一化误差', equal=True)
    Q = {k: norm(p, lo, hi) for k, p in P.items()}
    dist = {k: float(np.linalg.norm(q)) for k, q in Q.items()}; best = min(dist, key=dist.get); out.append(dist)
    for k, q in Q.items():
        ax.plot([0, q[0]], [0, q[1]], color=MUTED if k != best else GREEN, lw=.85 if k != best else 1.2, zorder=2)
        dot(ax, q, RED, ms=8 if k == best else 5)
    hollow(ax, (0, 0), INK)
    D = {'A': (.03, .03), 'B': (.03, .03), 'C': (.03, .03), 'D': (-.03, .05)}
    for k, q in Q.items(): ax.text(q[0]+D[k][0], q[1]+D[k][1], k, color=INK)
g = norm(np.array([1.5, 36.]), *R[1]); hollow(axes[1], g); axes[1].text(g[0]+.04, g[1]-.09, 'G', color=INK)
tags(fig, axes)
save(fig, HERE, 'figure', {'distances': out}); print(out, g)
