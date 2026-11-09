from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# 10-variable sign QP with symmetric +-1 weights (seed 7): low-rank coordinate solver for the SDP.
rng = np.random.default_rng(7); n = 10
W = rng.choice([-1., 1.], size=(n, n)); W = np.triu(W, 1); W = W+W.T
vals = []
for b in range(2**(n-1)):
    x = np.array([1.]+[1. if (b >> i) & 1 else -1. for i in range(n-1)]); vals.append(x@W@x)
pstar = min(vals)
V = rng.normal(size=(n, n)); V /= np.linalg.norm(V, axis=1, keepdims=True)
prim, dual, best = [], [], []
g = rng.normal(size=(2000, n))
T = 15
for t in range(T+1):
    X = V@V.T; prim.append(float(np.sum(W*X)))
    y = np.array([(W[i]@X[i]) for i in range(n)])   # candidate dual variable
    lam = np.linalg.eigvalsh(W-np.diag(y))[0]; dual.append(float(y.sum()+n*lam))
    if t == T: break
    for i in range(n):
        s = W[i]@V; V[i] = -s/np.linalg.norm(s)
X = V@V.T
S = np.sign(g@V.T); S[S == 0] = 1
rv = np.einsum('ij,jk,ik->i', S, W, S)
vals_r, cnt = np.unique(rv, return_counts=True)
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .105, .985, .985, .25, .28)
a, b = axes
ts = np.arange(T+1)
a.plot(ts, prim, color=GREEN, lw=1.5, zorder=3); a.plot(ts, dual, color=PURPLE, lw=1.5, zorder=3)
a.axhline(pstar, color=RED, lw=1.1, ls=(0, (4, 2)), zorder=2)
ylo = -53; yhi = -30
setup(a, (0, T), (ylo, yhi), [0, 5, 10, 15], [-50, -40, -30], xl='$t$', yl='目标值', equal=False)
a.text(T-.5, pstar+.5, '$f^*$', color=RED, fontsize=8, ha='right')
fig.canvas.draw()
b.bar(vals_r, cnt/cnt.sum(), width=2.4, color=GREEN_FILL, edgecolor=GREEN, lw=.9, zorder=2)
L = dual[-1]
b.axvline(L, color=PURPLE, lw=1.4); b.axvline(pstar, color=RED, lw=1.1, ls=(0, (4, 2)))
m = (cnt/cnt.sum()).max()
setup(b, (L-4.5, vals_r.max()+3), (0, m*1.2), None, None, xl='目标值', yl='频率', equal=False)
b.text(L-.5, m*1.1, '$L$', color=PURPLE, fontsize=8, ha='right'); b.text(pstar+.4, m*1.1, '$f^*$', color=RED, fontsize=8)
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'seed': 7, 'n': n, 'pstar': pstar, 'L_final': L, 'prim_final': prim[-1], 'prim0': prim[0], 'dual0': dual[0], 'best_rounding': float(vals_r.min()), 'rounding': dict(zip(map(str, vals_r.tolist()), (cnt/cnt.sum()).round(4).tolist())), 'rank': int(np.linalg.matrix_rank(X, tol=1e-5)), 'first_t_prim_below_pstar': int(next((i for i, p in enumerate(prim) if p < pstar), -1)), 'mean_rounding': float(rv.mean())})
