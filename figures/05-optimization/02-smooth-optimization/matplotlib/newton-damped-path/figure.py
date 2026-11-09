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

def run_damped(x, c=.1, n=8):
    P = [x.copy()]; A = []
    for t in range(n):
        G = grad(x); d = np.linalg.solve(hess(x), -G); s = G@d; a = 1.
        while f(x+a*d) > f(x)+c*a*s: a /= 2
        x = x+a*d; P.append(x.copy()); A.append(a)
    return np.array(P), A
fig, axes = figure(width_mm=112, height_mm=62, ncols=2)
panel(fig, .1, .985, .97, .185, .36)
a_, b_ = axes
p0 = np.array([-1., 1.2])
x = p0.copy(); Q = [x.copy()]
for t in range(5):
    x = x+np.linalg.solve(hess(x), -grad(x)); Q.append(x.copy())
Q = np.array(Q)
X, Y = grid2(-4, 11, -70, 90, 800)
a_.contour(X, Y, .5*(X-1)**2+(Y-X**2)**2, levels=[10, 100, 1000, 4000], colors=[BLUE], linewidths=.75)
a_.plot(Q[:,0], Q[:,1], color=YELLOW, lw=1.3, marker='o', ms=3.2, mew=0, zorder=4)
a_.plot(*p0, 'o', ms=4.4, color=GREEN, mew=0, zorder=6); a_.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6)
a_.text(-1.0, 6.5, '$x^{(0)}$', ha='right'); a_.text(9.4, -19, '$x^{(1)}$', ha='left', va='center'); a_.text(9.2, 80.6, '$x^{(2)}$', ha='left', va='top'); a_.text(1.4, -62.5, '$x^{(3)}$', ha='left', va='center')
a_.set_xlim(-4, 11); a_.set_ylim(-70, 90); a_.set_xlabel('$x_1$', labelpad=1); a_.set_ylabel('$x_2$', labelpad=0)
P, A = run_damped(p0.copy())
a, b, c, d = -1.4, 1.4, -.8, 1.7
X, Y = grid2(a, b, c, d)
region(b_, a, b, c, d)
b_.contour(X, Y, .5*(X-1)**2+(Y-X**2)**2, levels=[.02, .1, .3, .6, 1, 2.04, 4], colors=[BLUE], linewidths=.75, zorder=2)
b_.plot(P[:,0], P[:,1], color=GREEN, lw=1.4, marker='o', ms=3.6, mew=0, zorder=5)
b_.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6)
b_.text(-.95, 1.32, '$x^{(0)}$', ha='left'); b_.text(-.44, -.18, '$x^{(1)}$', ha='right'); b_.text(.43, -.56, '$x^{(2)}$', ha='left', va='center'); b_.text(.5, .22, '$x^{(3)}$', ha='right'); b_.text(1.05, 1.12, '$x^*$')
b_.set_xlabel('$x_1$', labelpad=1); b_.set_ylabel('$x_2$', labelpad=0)
tags(fig, axes); save(fig, HERE, 'figure', {'start': [-1, 1.2], 'full': Q.tolist(), 'damped': P.tolist(), 'alpha': A})
