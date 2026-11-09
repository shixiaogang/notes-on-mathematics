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

fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, .1, .985, .965, .215, .34)
A = np.diag([1., 25.]); p0 = np.array([5., 1.])
pts = [p0.copy()]
for t in range(14):
    x = pts[-1]; G = A@x; a = (G@G)/(G@A@G); pts.append(x-a*G)
pts = np.array(pts)
a_, b_ = axes
X, Y = grid2(-6, 6, -1.5, 1.5)
a_.contour(X, Y, .5*(X**2+25*Y**2), levels=[.5, 3, 8, 16, 25], colors=[BLUE], linewidths=.75)
a_.plot(pts[:,0], pts[:,1], color=YELLOW, lw=1.2, marker='o', ms=2.4, mew=0, zorder=3)
arrow(a_, p0, (0, 0), color=GREEN); a_.plot(0, 0, 'o', ms=4.8, color=RED, mew=0, zorder=6); a_.plot(*p0, 'o', ms=4.4, color=GREEN, mew=0, zorder=6)
a_.set_xlim(-6, 6); a_.set_ylim(-1.5, 1.5); a_.set_xlabel('$x_1$', labelpad=1); a_.set_ylabel('$x_2$', labelpad=0); a_.text(5.0, 1.12, '$x^{(0)}$', ha='center')
S = np.diag([1., 5.]); q0 = S@p0
X, Y = grid2(-6.5, 6.5, -6.5, 6.5)
b_.contour(X, Y, .5*(X**2+Y**2), levels=[.5, 3, 8, 16, 25], colors=[BLUE], linewidths=.75)
arrow(b_, q0, (0, 0), color=GREEN); b_.plot(0, 0, 'o', ms=4.8, color=RED, mew=0, zorder=6); b_.plot(*q0, 'o', ms=4.4, color=GREEN, mew=0, zorder=6)
b_.set_xlim(-6.5, 6.5); b_.set_ylim(-6.5, 6.5); b_.set_aspect('equal'); b_.set_xlabel('$y_1=x_1$', labelpad=1); b_.set_ylabel('$y_2=5x_2$', labelpad=0)
tags(fig, axes); save(fig, HERE, 'figure', {'objective': '0.5(x1^2+25 x2^2)', 'start': [5, 1], 'gd': 'exact line search'})
