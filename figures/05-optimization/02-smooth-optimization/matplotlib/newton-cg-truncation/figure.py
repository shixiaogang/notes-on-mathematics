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

fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .095, .985, .97, .2, .34)
a, b = axes
def mesh(ax, G, H_, a0, b0, c0, d0, lv):
    X, Y = grid2(a0, b0, c0, d0)
    M = G[0]*X+G[1]*Y+.5*(H_[0,0]*X**2+2*H_[0,1]*X*Y+H_[1,1]*Y**2)
    ax.contour(X, Y, M, levels=lv, colors=[YELLOW], linewidths=1.0, linestyles='solid')
    ax.set_xlim(a0, b0); ax.set_ylim(c0, d0); ax.set_xlabel('$d_1$', labelpad=1); ax.set_ylabel('$d_2$', labelpad=0)
x = np.array([.5, 0.]); G = grad(x); H_ = hess(x)
mesh(a, G, H_, -.5, 1, -.3, 1.1, [-.122, -.1, -.06, 0, .08, .2, .4])
a.plot([0, 0, .25], [0, .25, .5], color=GREEN, lw=1.4, marker='o', ms=4, mew=0, zorder=5); a.plot([.25], [.5], 'o', ms=4.8, color=RED, mew=0, zorder=6)
a.text(.02, -.11, '$z_0=0$', ha='left', va='center'); a.text(-.05, .26, '$z_1$', ha='right', va='center'); a.text(.3, .53, '$z_2=d_N$', ha='left', va='bottom')
x = np.array([-.5, .75]); G = grad(x); H_ = hess(x)
mesh(b, G, H_, -3, 8, -9, 3.5, [-30, -15, -6, -1.5, 1.5, 6, 15, 30])
z1 = np.array([2.5, -5.]); p1 = np.array([40., -60.])
b.plot([0, z1[0]], [0, z1[1]], color=GREEN, lw=1.4, marker='o', ms=4, mew=0, zorder=5)
s = .05; arrow(b, z1, z1+s*p1, color=RED, lw=1.4)
dN = np.linalg.solve(H_, -G); b.plot(*dN, 'x', ms=5, color=RED, mew=1.2, zorder=6)
b.text(.3, .8, '$z_0=0$', ha='left', va='center'); b.text(3.0, -4.7, '$z_1$', ha='left', va='center'); b.text(5.0, -7.3, '$p_1$', ha='left', va='center'); b.text(-1.6, 2.0, '$d_N$', ha='center', va='center')
tags(fig, axes); save(fig, HERE, 'figure', {'a_point': [.5, 0], 'b_point': [-.5, .75], 'b_z1': z1.tolist(), 'b_p1': p1.tolist()})
