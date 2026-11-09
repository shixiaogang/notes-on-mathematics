from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Cyclic exact block updates on f=1/2 x^T Q x, n=40, blocks of 8; perturbed block solves with residual norm: 0, fixed 1e-3, 0.1*||grad_J||.
rng = np.random.default_rng(9); n, p, R = 40, 8, 40
M = rng.standard_normal((80, n)); Q = M.T@M/80 + .05*np.eye(n); x0 = rng.standard_normal(n); blocks = [np.arange(i, i+p) for i in range(0, n, p)]
f = lambda x: .5*x@Q@x; P = [Q[np.ix_(J, J)] for J in blocks]
def run(mode):
    g = np.random.default_rng(1); x = x0.copy(); G = [f(x)]
    for r in range(R):
        for J, PJ in zip(blocks, P):
            gr = Q[J]@x; z = x[J]-np.linalg.solve(PJ, gr)
            if mode != 'exact':
                d = g.standard_normal(p); d /= np.linalg.norm(d); eps = 1e-3 if mode == 'abs' else .5*np.linalg.norm(gr)
                z = z + np.linalg.solve(PJ, eps*d)
            x[J] = z
        G.append(f(x))
    return np.array(G)/G[0]
fig, ax = figure(width_mm=88, height_mm=56)
panel(fig, .15, .97, .97, .17)
E_, A_, Rr = run('exact'), run('abs'), run('rel')
ax.semilogy(E_, color=GREEN, lw=1.4); ax.semilogy(A_, color=YELLOW, lw=1.6); ax.semilogy(Rr, color=PURPLE, lw=1.4)
ax.set_xlabel('轮数', labelpad=1); ax.set_ylabel('相对目标值', labelpad=1); ax.set_xlim(0, R)
ax.text(25, A_[25]*2.5, '固定绝对误差', fontsize=7.5, color=INK)
ax.text(27, Rr[27]*6, '相对误差', fontsize=7.5, color=INK); ax.text(16, E_[16]/60, '精确', fontsize=7.5, color=INK)
save(fig, HERE, 'figure', {'final': [float(E_[-1]), float(A_[-1]), float(Rr[-1])]})
print(E_[-1], A_[-1], Rr[-1])
