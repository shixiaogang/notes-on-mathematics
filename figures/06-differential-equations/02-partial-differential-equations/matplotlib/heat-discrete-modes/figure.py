from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Eigenvectors of the N=3 discrete Dirichlet Laplacian against the continuous modes.
fig, axes = figure(width_mm=112, height_mm=42, ncols=3, sharey=True)
panel(fig, left=.09, wspace=.12, bottom=.32)
g = np.array([.25, .5, .75])
for k, ax in zip((1, 2, 3), axes):
    ax.plot(X, np.sin(k*pi*X), color=BLUE, lw=1.4)
    v = np.sin(k*pi*g)
    ax.vlines(g, 0, v, color=GREEN, lw=1.3); ax.plot(g, v, 'o', ms=4.4, color=GREEN, mew=0, zorder=5)
    ax.axhline(0, color=STROKE, lw=.7); dot(ax, 0, 0, RED); dot(ax, 1, 0, RED)
    ax.set_xlim(0, 1); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([-1, 0, 1]); axlab(ax)
tags(fig, axes)
K = 16*np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2.]])
save(fig, HERE, 'figure', {'eig': [float(x) for x in np.linalg.eigvalsh(K)]})
