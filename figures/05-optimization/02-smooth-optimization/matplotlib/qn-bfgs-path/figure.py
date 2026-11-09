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

# f=x1^2+4x2^2，x0=(4,1)，精确线搜索。绿：BFGS（W0=I）；黄：最速下降。
A = np.diag([2., 8.]); x0 = np.array([4., 1.])
f = lambda P, Q: P*P+4*Q*Q
def run(kind, T):
    x, W = x0.copy(), np.eye(2); xs = [x.copy()]; Bs = [np.linalg.inv(W)]
    for _ in range(T):
        g = A@x
        if np.linalg.norm(g) < 1e-12: break
        d = -W@g if kind == 'bfgs' else -g
        a = -float(g@d)/float(d@A@d)
        s = a*d; y = A@s
        if kind == 'bfgs':
            rho = 1/float(s@y); V = np.eye(2)-rho*np.outer(y, s)
            W = V.T@W@V+rho*np.outer(s, s); Bs.append(np.linalg.inv(W))
        x = x+s; xs.append(x.copy())
    return np.array(xs), Bs
xb, Bs = run('bfgs', 2); xg, _ = run('gd', 9)
fig, (ax, bx) = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1.45, 1]})
X, Y = np.meshgrid(np.linspace(-1.2, 4.6, 500), np.linspace(-1.6, 1.6, 500))
ax.contour(X, Y, f(X, Y), levels=[.5, 2, 5, 10, 20], colors=[BLUE], linewidths=.75)
ax.plot(xg[:, 0], xg[:, 1], '-o', color=YELLOW, lw=1.2, ms=2.4, mew=0)
ax.plot(xb[:, 0], xb[:, 1], '-o', color=GREEN, lw=1.4, ms=3.4, mew=0)
ax.plot([0], [0], 'o', ms=4, color=RED, mew=0, zorder=7)
ax.text(4.08, 1.14, '$x^{(0)}$', color=INK); ax.text(2.45, -.92, '$x^{(1)}$', color=INK); ax.text(-.5, .22, '$x^{(2)}$', color=INK)
ax.set_aspect('equal'); ax.set_xlim(-1.2, 4.6); ax.set_ylim(-1.6, 1.6); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1); ax.set_xticks([0, 2, 4]); ax.set_yticks([-1, 0, 1])
th = np.linspace(0, 2*np.pi, 400); C = np.stack([np.cos(th), np.sin(th)])
for B, c, ls, lw, lab, xy in [(Bs[0], YELLOW, (0, (4, 2)), 1.2, '$B^{(0)}$', (-.2, 1.06)), (Bs[1], GREEN, '-', 1.4, '$B^{(1)}$', (.95, -.1)), (Bs[2], BLUE, '-', 1.4, '$B^{(2)}$', (-.3, -.11))]:
    L = np.linalg.cholesky(B); E = np.linalg.solve(L.T, C)
    bx.plot(E[0], E[1], color=c, lw=lw, ls=ls); bx.text(*xy, lab, color=INK, ha='left')
bx.axhline(0, color=GRID, lw=.6); bx.axvline(0, color=GRID, lw=.6)
bx.set_aspect('equal'); bx.set_xlim(-1.25, 1.4); bx.set_ylim(-1.25, 1.25); bx.set_xlabel('$p_1$', labelpad=1); bx.set_ylabel('$p_2$', labelpad=1)
panel(fig, .075, .985, .985, .22, .3); tags(fig, [ax, bx])
save(fig, HERE, 'figure', {'f': 'x1^2+4x2^2', 'bfgs': xb.tolist(), 'B': [b.tolist() for b in Bs], 'gd_last': xg[-1].tolist()})
