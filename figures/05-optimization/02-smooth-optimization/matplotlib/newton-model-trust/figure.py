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

def contourm(ax, p, a, b, c, d, lv, lv2):
    X, Y = grid2(a, b, c, d)
    F = .5*(X-1)**2+(Y-X**2)**2
    G, H_ = grad(p), hess(p); DX, DY = X-p[0], Y-p[1]
    M = f(p)+G[0]*DX+G[1]*DY+.5*(H_[0,0]*DX**2+2*H_[0,1]*DX*DY+H_[1,1]*DY**2)
    ax.contour(X, Y, F, levels=lv, colors=[BLUE], linewidths=.75)
    ax.contour(X, Y, M, levels=lv2, colors=[YELLOW], linewidths=1.0, linestyles=[(0, (3, 1.6))])
    ax.set_xlim(a, b); ax.set_ylim(c, d); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=0)
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .105, .985, .965, .2, .36)
a, b = axes
p = np.array([.5, 0.]); dd = np.linalg.solve(hess(p), -grad(p))
contourm(a, p, -.3, 1.3, -.7, 1.2, [.02, .08, .2, .4, .8], [.02, .08, .2, .4, .8])
a.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6); a.plot(*p, 'o', ms=4.4, color=GREEN, mew=0, zorder=6); a.plot(*(p+dd), 'o', ms=4.4, color=GREEN, mew=0, zorder=6)
arrow(a, p, p+dd); a.text(p[0]+.05, p[1]-.17, '$x^{(0)}$'); a.text(*(p+dd+np.array([-.28, .06])), '$x^{(1)}$'); a.text(1.03, 1.03, '$x^*$')
p2 = np.array([-1., 1.2]); dd2 = np.linalg.solve(hess(p2), -grad(p2))
contourm(b, p2, -2.1, 1.7, -2.4, 3.2, [.1, .5, 1.2, 2.04, 4, 8], [-3, -1, .5, 2.04, 4, 8, 16])
b.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6); b.plot(*p2, 'o', ms=4.4, color=GREEN, mew=0, zorder=6)
s = .16; arrow(b, p2, p2+s*dd2); b.text(p2[0]-.1, p2[1]+.28, '$x^{(0)}$', ha='center'); b.text(1.05, 1.22, '$x^*$')
tags(fig, axes); save(fig, HERE, 'figure', {'objective': '0.5(x1-1)^2+(x2-x1^2)^2', 'x_a': [.5, 0], 'x_b': [-1, 1.2], 'model_minimizer_b': [9, -19], 'arrow_scale_b': s})
