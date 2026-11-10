from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Nonzero patterns: 1D three-point matrix and 2D five-point matrix on 4x4 interior points.
def lap2(m):
    I = np.eye(m); T = 2*I-np.eye(m, k=1)-np.eye(m, k=-1)
    return np.kron(I, T)+np.kron(T, I)
A1 = lap1d(17)*(1/17)**2; A2 = lap2(4)
fig, axes = figure(width_mm=100, height_mm=56, ncols=2)
panel(fig, left=.04, right=.96, wspace=.16, bottom=.14, top=.98)
for ax, A in zip(axes, (A1, A2)):
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            if A[i, j] != 0:
                c = BLUE if i == j else BLUE_FILL
                ax.add_patch(__import__('matplotlib').patches.Rectangle((j, n-1-i), 1, 1, fc=c, ec=STROKE, lw=.35))
    ax.set_xlim(0, n); ax.set_ylim(0, n); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    for s in ('top', 'right'): ax.spines[s].set_visible(True)
tags(fig, axes)
save(fig, HERE, 'figure', {'nnz_1d': int(np.count_nonzero(A1)), 'nnz_2d': int(np.count_nonzero(A2))})
print(np.count_nonzero(A1), np.count_nonzero(A2), np.linalg.eigvalsh(A2)[[0,-1]])
