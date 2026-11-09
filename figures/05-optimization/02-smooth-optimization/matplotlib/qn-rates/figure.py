from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# n=50 旋转 log cosh（c 对数等距于 [0.1,100]），强 Wolfe。(a)四种方法的解距离；(b)BFGS 的 Dennis-More 比值。
fun, grad, H, rng = rotated_logcosh(50, .1, 100, 7); x0 = rng.standard_normal(50)*.8
n = 50
def gd(T):
    x = x0.copy(); e = [np.linalg.norm(x)]
    for _ in range(T):
        d = -grad(x); a, _e = strong_wolfe(fun, grad, x, d, a0=1/(101.), c2=.9); x = x+a*d; e.append(np.linalg.norm(x))
    return np.array(e)
from numpy.linalg import solve, norm
def newton(T):
    # Hessian Q^T diag(c+sech^2(Qx)) Q，由 H* 的特征结构重建
    rng2 = np.random.default_rng(7); Q, _ = np.linalg.qr(rng2.standard_normal((n, n))); c = np.logspace(-1, 2, n)
    x = x0.copy(); e = [norm(x)]
    for _ in range(T):
        z = Q@x; Hx = Q.T@np.diag(c+1/np.cosh(z)**2)@Q; d = -solve(Hx, grad(x)); a, _e = strong_wolfe(fun, grad, x, d, c2=.9); x = x+a*d; e.append(norm(x))
        if e[-1] < 1e-13: break
    return np.array(e)
r = run_quasi_newton(fun, grad, x0, np.eye(n), 'bfgs', T=120, gtol=1e-11)
errb = norm(r['x'], axis=1)
l = run_lbfgs(fun, grad, x0, 5, T=120, gtol=1e-11)
# L-BFGS 解距离需要重放：用目标差换算的等价量 sqrt(2f/L) 不准，这里直接记录
def lb(rr, T):
    x = x0.copy(); S, Y = [], []; e = [norm(x)]
    for t in range(T):
        g = grad(x)
        if norm(g) < 1e-11: break
        gamma = float(S[-1]@Y[-1])/float(Y[-1]@Y[-1]) if S else 1.
        d = -two_loop(g, S, Y, gamma); a, _e = strong_wolfe(fun, grad, x, d, a0=1. if S else .01, c2=.9)
        xn = x+a*d; s, y = xn-x, grad(xn)-g; S.append(s); Y.append(y)
        if len(S) > rr: S.pop(0); Y.pop(0)
        x = xn; e.append(norm(x))
    return np.array(e)
eg, en, el = gd(120), newton(30), lb(5, 120)
egl, ell = gd(6000), lb(5, 6000)
first = lambda e: int(np.argmax(e <= 1e-8)) if np.any(e <= 1e-8) else -1
fig, (ax, bx) = figure(width_mm=112, height_mm=56, ncols=2)
ax.semilogy(eg, color=YELLOW, lw=1.5, ls=(0, (4, 2))); ax.semilogy(el, color=PURPLE, lw=1.4, ls=(0, (1.2, 1.4))); ax.semilogy(errb, color=GREEN, lw=1.4); ax.semilogy(en, color=BLUE, lw=1.4)
ax.set_xlim(0, 120); ax.set_ylim(1e-11, 30); ax.set_yticks([1e-10, 1e-5, 1]); ax.minorticks_off(); ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('解距离', labelpad=1)
tt = len(errb)
ax.text(70, eg[70]*2.3, '梯度下降', color=INK); ax.text(72, 3e-5, 'L-BFGS', color=INK); ax.text(46, 1e-9, 'BFGS', color=INK); ax.text(10, 1e-7, 'Newton', color=INK)
Hn = norm(H, 'fro'); dm, fro = [], []
for t in range(len(r['x'])-1):
    B = np.linalg.inv(r['W'][t]); s = r['x'][t+1]-r['x'][t]
    if norm(s) < 1e-12: break
    dm.append(norm((B-H)@s)/(norm(H, 2)*norm(s))); fro.append(norm(B-H, 2)/norm(H, 2))
bx.semilogy(dm, color=GREEN, lw=1.4); bx.semilogy(fro, color=RED, lw=1.4, ls=(0, (4, 2)))
bx.set_xlabel('$t$', labelpad=1); bx.set_ylim(1e-6, 3); bx.set_yticks([1e-5, 1e-2, 1]); bx.minorticks_off(); bx.set_xlim(0, len(dm))
bx.text(len(dm)*.62, 1.2, '谱范数误差', color=INK, ha='center', va='bottom', fontsize=7.5)
bx.text(len(dm)*.32, 1.2e-3, '沿步方向的误差', color=INK, ha='center')
panel(fig, .1, .985, .985, .25, .25); tags(fig, [ax, bx])
save(fig, HERE, 'figure', {'problem': 'rotated logcosh n=50 c in [0.1,100] seed 7', 'bfgs_iters': tt-1, 'dm_last': dm[-1], 'B_err_last': fro[-1], 'newton_iters': len(en)-1, 'iters_to_1e-8': dict(gd=first(egl), lbfgs5=first(ell), bfgs=first(errb), newton=first(en))})
