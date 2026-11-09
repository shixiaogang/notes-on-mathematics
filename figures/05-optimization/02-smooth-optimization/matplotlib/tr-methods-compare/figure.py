from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# n=20 的扩展 Rosenbrock 函数上比较模型矩阵/子问题解法。
n = 20
def F(x): return np.sum(10*(x[1:]-x[:-1]**2)**2 + (1-x[:-1])**2)
def G(x):
    g = np.zeros(n); r = x[1:] - x[:-1]**2
    g[:-1] += -40*x[:-1]*r - 2*(1-x[:-1]); g[1:] += 20*r; return g
def Hv(x, v):
    r = x[1:] - x[:-1]**2; o = np.zeros(n)
    d = 80*x[:-1]**2 - 40*r + 2; o[:-1] += d*v[:-1] - 40*x[:-1]*v[1:]; o[1:] += 20*v[1:] - 40*x[:-1]*v[:-1]; return o
x0 = np.ones(n); x0[::2] = -1.2
def run(kind, maxit=1200):
    x = x0.copy(); D = 1.; B = np.eye(n)*20.; out = []; mv = 0; ev = 0
    for t in range(maxit):
        g = G(x); gn = np.linalg.norm(g); out.append((ev, mv, gn))
        if gn < 1e-7: break
        if kind == 'newton':
            p, why, _, c = tcg(g, None, D, min(.1, np.sqrt(gn))*gn, mv=lambda v: Hv(x, v)); mv += c; pr = -(g @ p + .5*p @ Hv(x, p))
        elif kind == 'cauchy':
            Hg = Hv(x, g); mv += 1; k = g @ Hg; a = D/gn if k <= 0 else min(D/gn, gn**2/k); p = -a*g; pr = -(g @ p + .5*a*a*k)
        else:
            p, why, _, c = tcg(g, B, D, min(.1, np.sqrt(gn))*gn, maxit=n*2); mv += c; pr = -(g @ p + .5*p @ B @ p)
        ev += 1; ar = F(x) - F(x + p); rho = ar/pr if pr > 0 else -1
        if kind == 'sr1':
            y = G(x + p) - g; w = y - B @ p; den = w @ p
            if abs(den) > 1e-8*np.linalg.norm(w)*np.linalg.norm(p): B = B + np.outer(w, w)/den
        if rho < .25: D *= .5
        elif rho >= .75 and abs(np.linalg.norm(p) - D) < 1e-8: D = min(2*D, 100.)
        if rho >= .25: x = x + p
    return np.array(out)
R = {k: run(k) for k in ('newton', 'sr1', 'cauchy')}
fig, ax = figure(width_mm=96, height_mm=58)
for k, c in (('newton', GREEN), ('sr1', PURPLE), ('cauchy', YELLOW)):
    ax.semilogy(R[k][:, 0], np.minimum.accumulate(R[k][:, 2]), color=c, lw=1.5); print(k, R[k][-1], len(R[k]))
ax.set_xlabel('外层轮数（含被拒绝的轮）', labelpad=1); ax.set_ylabel(r'$\Vert\nabla f\Vert_2$', labelpad=1); ax.set_xlim(0, 400)
ax.text(32, 1e-5, 'Hessian', fontsize=7.5); ax.text(98, 3e-4, 'SR1', fontsize=7.5); ax.text(300, .6, 'Cauchy', fontsize=7.5)
save(fig, HERE, 'figure', {'f': 'sum 10(x_{i+1}-x_i^2)^2+(1-x_i)^2', 'n': n, 'summary': {k: [float(v) for v in R[k][-1]]+[len(R[k])] for k in R}})
