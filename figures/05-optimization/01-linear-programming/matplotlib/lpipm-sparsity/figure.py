from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Sparsity of A and of the normal matrix with and without one dense column.
rng = np.random.default_rng(20261109)
m, n = 40, 80
A = np.zeros((m, n))
for j in range(n):
    A[rng.choice(m, 2, replace=False), j] = 1.
A2 = A.copy(); dense = 37; A2[:, dense] = 1.
Mdense = (A2 @ A2.T) != 0; Msparse = (np.delete(A2, dense, 1) @ np.delete(A2, dense, 1).T) != 0
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
def show(ax, B, lab):
    ax.spy(B, markersize=1.4, color=BLUE, aspect='auto'); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(True); sp.set_linewidth(.75)
    ax.set_xlabel(lab, labelpad=2)
show(axs[0], A2 != 0, '(a) $\\mathbf{A}$')
show(axs[1], Mdense, '(b) $\\mathbf{A}\\mathbf{D}\\mathbf{A}^{\\top}$')
show(axs[2], Msparse, '(c) 去掉该列后')
save(fig, OUT, 'figure', {'seed': 20261109, 'nnz_A': int((A2 != 0).sum()), 'nnz_M_dense': int(Mdense.sum()), 'nnz_M_sparse': int(Msparse.sum())})
print(int((A2 != 0).sum()), int(Mdense.sum()), int(Msparse.sum()))
