from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Sparsity: Jacobian with one dense row, the condensed matrix and the augmented matrix.
n = 20; m = 20
Jp = np.zeros((m, n), bool)
for i in range(m-1):
    Jp[i, i] = True
    if i+1 < n: Jp[i, i+1] = True
Jp[m-1, :] = True
Hc = (Jp.T.astype(int)@Jp.astype(int) > 0) | np.eye(n, dtype=bool)
Aug = np.block([[np.eye(n, dtype=bool), Jp.T], [Jp, np.eye(m, dtype=bool)]])
def fill(P):
    P = P.copy(); N = len(P); nz = 0
    for k in range(N):
        idx = np.where(P[k+1:, k])[0]+k+1; nz += 1+len(idx)
        for i in idx:
            P[i, idx] = True
    return nz
# order: pair each constraint right after its variables; dense row last
perm = []
for i in range(n):
    perm += [i]
    if i < m-1: perm += [n+i]
perm += [n+m-1]
AugP = Aug[np.ix_(perm, perm)]
fig, axs = figure(width_mm=112, height_mm=44, ncols=3, width_ratios=[1, 1, 1])
for ax, M, t in zip(axs, (Jp, Hc, AugP), ('(a)', '(b)', '(c)')):
    ax.spy(M, marker='s', markersize=1.15, color=BLUE, aspect='equal')
    ax.set_xticks([]); ax.set_yticks([]); tag(ax, '', t)
    for s in ax.spines.values(): s.set_visible(True); s.set_linewidth(.6); s.set_color(MUTED)
save(fig, OUT, 'figure', {'nnzJ': int(Jp.sum()), 'nnzH_lower_factor': fill(Hc), 'nnzAug_lower_factor': fill(AugP), 'nnzAug': int(Aug.sum()), 'n_aug': n+m})
