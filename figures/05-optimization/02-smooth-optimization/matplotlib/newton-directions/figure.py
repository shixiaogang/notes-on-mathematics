from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿全章的目标 f(x)=0.5(x1-1)^2+(x2-x1^2)^2，最优解 (1,1)。
def f(x):
    u = x[1]-x[0]**2
    return .5*(x[0]-1)**2+u**2
def grad(x):
    u = x[1]-x[0]**2
    return np.array([x[0]-1-4*x[0]*u, 2*u])
def hess(x):
    u = x[1]-x[0]**2
    return np.array([[1-4*u+8*x[0]**2, -4*x[0]], [-4*x[0], 2.]])
XS = np.array([1., 1.])
def panel(fig, left, right, top, bottom, wspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def grid2(a, b, c, d, n=600):
    X, Y = np.meshgrid(np.linspace(a, b, n), np.linspace(c, d, n))
    return X, Y
def region(ax, a, b, c, d):
    t = np.linspace(a, b, 300); y = t**2+.25
    ax.fill_between(t, y, d, color=RED_FILL, lw=0, zorder=0)
    ax.plot(t, y, color=STROKE, lw=.85, ls=(0, (3, 2)), zorder=1)
    ax.set_xlim(a, b); ax.set_ylim(c, d)
def arrow(ax, p, q, color=GREEN, lw=1.3, z=4):
    ax.annotate('', xy=q, xytext=p, zorder=z, arrowprops=dict(arrowstyle='-|>,head_width=.17,head_length=.34', color=color, lw=lw, shrinkA=0, shrinkB=0))

fig, ax = figure(width_mm=100, height_mm=68)
fig.set_layout_engine(None); fig.subplots_adjust(left=.09, right=.985, top=.975, bottom=.12)
a_, b_, c_, d_ = -2.3, 2.5, -1.5, 2.2
X, Y = grid2(a_, b_, c_, d_); F = .5*(X-1)**2+(Y-X**2)**2
region(ax, a_, b_, c_, d_)
ax.contour(X, Y, F, levels=[.1, .4, 1.375, 3, 6, 12], colors=[BLUE], linewidths=.75, zorder=2)
p = np.array([-.5, .75]); G = grad(p); H_ = hess(p); w, Q = np.linalg.eigh(H_)
dN = np.linalg.solve(H_, -G); dS = np.linalg.solve(H_+np.eye(2), -G); dA = np.linalg.solve(Q@np.diag(np.abs(w))@Q.T, -G); dC = np.linalg.solve(np.array([[1, 2], [2, 6.]]), -G)
arrow(ax, p, p+dN, color=RED, lw=1.4, z=5); arrow(ax, p, p+dS, color=GREEN, lw=1.4, z=5); arrow(ax, p, p+dA, color=PURPLE, lw=1.4, z=5); arrow(ax, p, p+dC, color=YELLOW, lw=1.4, z=5); arrow(ax, p, p-G, color=MUTED, lw=1.0, z=5)
ax.plot(*p, 'o', ms=4.6, color=INK, mew=0, zorder=6); ax.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6)
wb = dict(fc='white', ec='none', pad=.6)
ax.text(*(p+dN+np.array([-.05, .1])), 'Newton', ha='center', bbox=wb, zorder=7); ax.text(*(p+dS+np.array([.07, -.17])), '平移', ha='left', bbox=wb, zorder=7); ax.text(*(p+dA+np.array([-.45, -.42])), '谱修正', ha='left', bbox=wb, zorder=7); ax.text(*(p+dC+np.array([-.05, -.1])), '修正Cholesky', ha='center', va='top', bbox=wb, zorder=7); ax.text(*(p-G+np.array([-.05, -.2])), '$-g$', ha='right', bbox=wb, zorder=7)
ax.text(1.05, 1.1, '$x^*$', zorder=7, bbox=wb)
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=0); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([-1, 0, 1, 2])
save(fig, HERE, 'figure', {'x': p.tolist(), 'g': G.tolist(), 'H': H_.tolist(), 'newton': dN.tolist(), 'shift_1': dS.tolist(), 'abs_eig': dA.tolist(), 'mod_chol': dC.tolist()})
