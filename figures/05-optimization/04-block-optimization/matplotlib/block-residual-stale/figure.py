from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Lasso N=60, n=30, correlated columns, gamma=2: cyclic coordinate prox. Residual of the block about to be updated versus the full residual.
rng = np.random.default_rng(4); N, n = 60, 30
z = rng.standard_normal(N); A = .5*z[:, None] + rng.standard_normal((N, n)); b0 = A@(rng.standard_normal(n)*(rng.random(n) < .3)) + .3*rng.standard_normal(N); gam = 2.
L = (A**2).sum(0); S = lambda v, t: np.sign(v)*np.maximum(abs(v)-t, 0)
def full(x):
    g = A.T@(A@x-b0); return np.linalg.norm(L*(x-S(x-g/L, gam/L)))
x = np.zeros(n); blk, fu = [], []
for r in range(14):
    for i in range(n):
        g = A[:, i]@(A@x-b0); new = S(x[i]-g/L[i], gam/L[i]); blk.append(abs(L[i]*(x[i]-new))); x[i] = new; fu.append(full(x))
blk, fu = np.array(blk), np.array(fu); t = np.arange(1, len(blk)+1)
fig, ax = figure(width_mm=100, height_mm=56)
panel(fig, .125, .975, .97, .17)
m = blk > 1e-9
ax.semilogy(t[m], blk[m], 'o', color=YELLOW, ms=1.8, mew=0)
ax.semilogy(t, fu, color=GREEN, lw=1.4)
ax.set_xlabel('单坐标更新次数', labelpad=1); ax.set_ylabel('残差范数', labelpad=1); ax.set_xlim(0, len(t))
ax.text(190, fu[190]*2.5, '完整残差', fontsize=7.5, color=INK)
ax.set_ylim(max(1e-6, blk[m].min()/2), fu.max()*2)
save(fig, HERE, 'figure', {'N': N, 'n': n, 'gamma': gam, 'zero_block_fraction': float((~m).mean())})
print((~m).mean(), fu[-1], np.sum(x != 0))
