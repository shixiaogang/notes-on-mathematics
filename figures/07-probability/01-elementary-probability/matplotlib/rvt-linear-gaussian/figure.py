from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Y = A Z with A = [[2,0],[1,1]]: circles ||z||=c map to ellipses, unit square to a parallelogram of area |det A| = 2.
from matplotlib.patches import Polygon
A = np.array([[2., 0.], [1., 1.]])
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.09, right=.98, bottom=.2, top=.97, wspace=.22)
th = np.linspace(0, 2*pi, 400); C = np.vstack([np.cos(th), np.sin(th)])
sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]).T
for ax, M_, lim in ((axes[0], np.eye(2), 3.2), (axes[1], A, 5.2)):
    P = M_ @ sq
    ax.add_patch(Polygon(P.T, closed=True, fc=BLUE_FILL, ec=BLUE, lw=.8, zorder=1))
    for c in (.5, 1, 1.5, 2):
        E = M_ @ (c*C); ax.plot(E[0], E[1], color=BLUE, lw=1.0 if c != 1 else 1.4, zorder=2)
    ax.axhline(0, color=STROKE, lw=.5, zorder=0); ax.axvline(0, color=STROKE, lw=.5, zorder=0)
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim*.75, lim*.75); ax.set_aspect('equal')
dot(axes[0], 1, 0, RED); dot(axes[1], 2, 1, RED)
axlab(axes[0], '$z_1$', '$z_2$'); axlab(axes[1], '$y_1$', '$y_2$')
axes[0].set_xticks([-2, 0, 2]); axes[0].set_yticks([-2, 0, 2]); axes[1].set_xticks([-4, 0, 4]); axes[1].set_yticks([-3, 0, 3])
tags(fig, axes)
S = A @ A.T; w, V = np.linalg.eigh(S)
save(fig, HERE, 'figure', {'Sigma': S.tolist(), 'det': float(np.linalg.det(A)), 'eig': w.tolist(), 'f(2,1)': float(np.exp(-.5)/(4*pi))})
