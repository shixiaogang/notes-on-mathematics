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

# f=x1^2+4x2^2，x0=(4,1)，步长 1/8 的负梯度步到 x1=(3,0)。
# 满足割线条件的对称矩阵族 B(a)=[[a,2-a],[2-a,6+a]]。
A = np.diag([2., 8.]); x0 = np.array([4., 1.]); g0 = A@x0
x1 = x0-.125*g0; g1 = A@x1
B = lambda a: np.array([[a, 2-a], [2-a, 6+a]])
fig, axs = figure(width_mm=112, height_mm=58, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
ax, bx = axs
X, Y = np.meshgrid(np.linspace(-6.2, 5.2, 900), np.linspace(-3.4, 3.4, 900))
vals = [(.9, GREEN, '-'), (2., BLUE, '-'), (5., PURPLE, (0, (1.2, 1.4)))]
mins = []
for a, c, ls in vals:
    b = B(a); m = lambda P, Q: g1[0]*(P-x1[0])+g1[1]*(Q-x1[1])+.5*(b[0, 0]*(P-x1[0])**2+2*b[0, 1]*(P-x1[0])*(Q-x1[1])+b[1, 1]*(Q-x1[1])**2)
    # 过 x0 的模型等值线：所有成员在 x0 的切向相同
    ax.contour(X, Y, m(X, Y), levels=[m(x0[0], x0[1])], colors=[c], linewidths=1.2, linestyles=[ls])
    p = x1-np.linalg.solve(b, g1); mins.append(p)
    ax.plot([p[0]], [p[1]], 'o', ms=3, color=c, mew=0, zorder=6)
ax.plot([x0[0], x1[0]], [x0[1], x1[1]], color=STROKE, lw=.95)
ax.plot([x0[0], x1[0]], [x0[1], x1[1]], 'o', ms=3.2, color=STROKE, mew=0, zorder=6)
ax.text(x0[0]+.25, x0[1]+.35, '$x^{(0)}$', color=INK)
ax.text(x1[0]-.1, x1[1]+.3, '$x^{(1)}$', color=INK, ha='right')
n0 = np.array([-g0[1], g0[0]])/np.linalg.norm(g0)
ax.plot([x0[0]-1.2*n0[0], x0[0]+1.2*n0[0]], [x0[1]-1.2*n0[1], x0[1]+1.2*n0[1]], color=RED, lw=.95)
ax.set_aspect('equal'); ax.set_xlim(-6.2, 5.2); ax.set_ylim(-3.4, 3.4)
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1); ax.set_xticks([-4, 0, 4]); ax.set_yticks([-2, 0, 2])
aa = np.linspace(-.5, 5, 400)
lam = [np.linalg.eigvalsh(B(a))[0] for a in aa]
bx.axhline(0, color=STROKE, lw=.85)
bx.plot(aa, lam, color=BLUE, lw=1.4)
bx.plot([.4], [0], 'o', ms=3.4, color=RED, mew=0, zorder=6)
bx.text(.4, -.62, '$a=0.4$', color=INK, ha='left')
for a, name, c, dy in [(.9, '$a=0.9$', GREEN, .5), (2., '$a=2$', BLUE, .42)]:
    l = np.linalg.eigvalsh(B(a))[0]
    bx.plot([a], [l], 'o', ms=3.4, color=c, mew=0, zorder=6)
    bx.text(a-.04, l+dy, name, color=INK, ha='center')
bx.set_xlabel('$a$', labelpad=1); bx.set_ylabel('$\\lambda_{\\min}(B(a))$', labelpad=1)
bx.set_xlim(-.5, 5); bx.set_ylim(-3.1, 3)
panel(fig, .075, .985, .985, .22, .3); tags(fig, [ax, bx])
save(fig, HERE, 'figure', {'family': 'B(a)=[[a,2-a],[2-a,6+a]]', 'det': '10a-4', 'a': [v[0] for v in vals], 'model_minimizers': [m.tolist() for m in mins]})
