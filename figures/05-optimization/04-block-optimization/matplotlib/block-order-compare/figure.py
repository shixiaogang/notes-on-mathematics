from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Three orders on f=1/2 x^T Q x, Q=(1-c)I+c 11^T, n=30, c=0.9. Exact coordinate updates.
n = 30; c = .9; Q = (1-c)*np.eye(n) + c*np.ones((n, n)); R = 60
def run(order_fn, x0, rng):
    x = x0.copy(); g = [.5*x@Q@x]
    for r in range(R):
        for i in order_fn(rng):
            x[i] -= Q[i]@x/Q[i, i]
        g.append(.5*x@Q@x)
    return np.array(g)/g[0]
cyc = lambda rng: np.arange(n); shu = lambda rng: rng.permutation(n); ran = lambda rng: rng.integers(0, n, n)
rng0 = np.random.default_rng(11); x0 = rng0.standard_normal(n) + .0
def avg(fn, seeds=30):
    G = []
    for s in range(seeds):
        G.append(run(fn, x0, np.random.default_rng(100+s)))
    return np.exp(np.mean(np.log(np.maximum(np.array(G), 1e-300)), 0))
gc, gs, gr = run(cyc, x0, rng0), avg(shu), avg(ran)
fig, ax = figure(width_mm=88, height_mm=56)
panel(fig, .125, .97, .97, .17)
r = np.arange(R+1)
ax.semilogy(r, gc, color=YELLOW, lw=1.6); ax.semilogy(r, gs, color=GREEN, lw=1.4); ax.semilogy(r, gr, color=PURPLE, lw=1.4)
ax.set_xlabel('轮数', labelpad=1); ax.set_ylabel('相对目标值', labelpad=1); ax.set_xlim(0, R)
ax.text(42, .085, '固定循环', fontsize=7.5, color=INK)
ax.text(26, 2e-5, '每轮打乱', fontsize=7.5, color=INK)
ax.text(34, 3e-3, '独立随机', fontsize=7.5, color=INK)
save(fig, HERE, 'figure', {'n': n, 'c': c, 'final': [float(gc[-1]), float(gs[-1]), float(gr[-1])]})
print(gc[[10,30,60]], gs[[10,30,60]], gr[[10,30,60]])
