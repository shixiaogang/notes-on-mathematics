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

# 强凸目标 f=x1^2+4x2^2 上一次 SR1 更新得到不定矩阵 B=[[0,4],[4,0]]；当前点 x=(-2,0.5)，g=(-4,4)，信赖域半径 1。
A = np.diag([2., 8.]); x = np.array([-2., .5]); g = A@x; B = np.array([[0., 4.], [4., 0.]])
pn = -np.linalg.solve(B, g)
lam, U = np.linalg.eigh(B); v = U[:, 0]; v = v if v@g < 0 else -v
pt = v
m = lambda P, Q: g[0]*P+g[1]*Q+.5*(B[0, 0]*P*P+2*B[0, 1]*P*Q+B[1, 1]*Q*Q)
fig, (ax, bx) = figure(width_mm=112, height_mm=56, ncols=2)
X, Y = np.meshgrid(np.linspace(-2, 2, 500), np.linspace(-2, 2, 500))
ax.contour(X, Y, m(X, Y), levels=[-16, -12, -8, -4, 0, 4, 8, 12], colors=[BLUE], linewidths=.75, negative_linestyles='solid')
th = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(th), np.sin(th), color=STROKE, lw=1.2)
ar = dict(arrowstyle='-|>', lw=1.3, mutation_scale=7, shrinkA=0, shrinkB=0)
ax.annotate('', xy=pn, xytext=(0, 0), arrowprops=dict(color=RED, **ar))
ax.annotate('', xy=pt, xytext=(0, 0), arrowprops=dict(color=GREEN, **ar))
ax.text(pn[0]-.1, pn[1]+.22, '$-B^{-1}g$', color=INK, ha='center'); ax.text(pt[0]+.12, pt[1]-.28, '$p_{\\Delta}$', color=INK)
ax.set_aspect('equal'); ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_xlabel('$p_1$', labelpad=1); ax.set_ylabel('$p_2$', labelpad=1); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
X, Y = np.meshgrid(np.linspace(-3.6, .6, 500), np.linspace(-1.1, 2.0, 500))
bx.contour(X, Y, X*X+4*Y*Y, levels=[1, 2, 5, 10, 18], colors=[BLUE], linewidths=.75)
bx.annotate('', xy=x+pn, xytext=x, arrowprops=dict(color=RED, **ar)); bx.annotate('', xy=x+pt, xytext=x, arrowprops=dict(color=GREEN, **ar))
bx.plot([x[0]], [x[1]], 'o', ms=3.4, color=STROKE, mew=0, zorder=6); bx.plot([0], [0], 'o', ms=4, color=RED, mew=0, zorder=7)
bx.text(x[0]-.1, x[1]-.34, '$x^{(1)}$', color=INK, ha='right')
bx.set_aspect('equal'); bx.set_xlim(-3.6, .6); bx.set_ylim(-1.1, 2.0); bx.set_xlabel('$x_1$', labelpad=1); bx.set_ylabel('$x_2$', labelpad=1)
panel(fig, .07, .99, .985, .23, .25); tags(fig, [ax, bx])
f = lambda z: float(z[0]**2+4*z[1]**2)
save(fig, HERE, 'figure', {'x': x.tolist(), 'g': g.tolist(), 'B': B.tolist(), 'quasi_newton_step': pn.tolist(), 'tr_step': pt.tolist(), 'f_x': f(x), 'f_qn': f(x+pn), 'f_tr': f(x+pt)})
