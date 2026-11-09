from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Cyclic exact block updates on a chain quadratic (tridiagonal Q, n=64); dense-block operation model.
n = 64; Q = 2.02*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
rng = np.random.default_rng(3); x0 = rng.standard_normal(n); f0 = .5*x0@Q@x0
sizes = [1, 4, 16, 64]; cols = [YELLOW, PURPLE, GREEN, BLUE]; R = 400
res = {}
for p in sizes:
    x = x0.copy(); blocks = [np.arange(i, min(i+p, n)) for i in range(0, n, p)]
    inv = [np.linalg.inv(Q[np.ix_(J, J)]) for J in blocks]; g = [f0]
    for r in range(R):
        for J, I in zip(blocks, inv):
            q = Q[J]@x - Q[np.ix_(J, J)]@x[J]; x[J] = -I@q
        g.append(.5*x@Q@x)
    setup = sum(len(J)**3/3 for J in blocks); per = sum(2*len(J)**2 + 3*len(J) for J in blocks)
    res[p] = (np.array(g)/f0, setup + per*np.arange(R+1))
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .125, .985, .97, .27, wspace=.32)
for p, c in zip(sizes, cols):
    g, W = res[p]; g = np.maximum(g, 1e-12)
    a.semilogy(np.arange(R+1), g, color=c, lw=1.4); b.loglog(W[1:], g[1:], color=c, lw=1.4)
a.text(262, 3e-9, '$p=1$', fontsize=7.5, color=INK); a.text(100, 1e-9, '$p=4$', fontsize=7.5, color=INK); a.text(46, 3e-11, '$p=16$', fontsize=7.5, color=INK); a.annotate('$p=64$', xy=(1.5, 1e-3), xytext=(30, .1), fontsize=7.5, color=INK, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.7, shrinkA=1, shrinkB=1))
a.set_xlabel('轮数', labelpad=1); a.set_ylabel('相对目标值', labelpad=1); a.set_ylim(1e-11, 2); a.set_xlim(0, 400)
b.plot([res[64][1][1]], [3e-11], 'o', color=BLUE, ms=4, mew=0, zorder=5)
b.set_xlabel('运算量（次）', labelpad=1); b.set_ylim(1e-11, 2); b.set_xlim(2e2, 2e6)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
import json
for p in sizes:
    g, W = res[p]; k = int(np.argmax(g <= 1e-10)); print(p, k, W[k])
save(fig, HERE, 'figure', {'n': n, 'diag': 2.02, 'sizes': sizes, 'final_gap': {str(p): float(res[p][0][-1]) for p in sizes}})
