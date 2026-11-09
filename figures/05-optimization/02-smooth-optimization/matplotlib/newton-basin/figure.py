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

fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, .095, .985, .96, .215, .32)
phi = lambda x: np.sqrt(1+x**2); a, b = axes
x0 = 2.; d1 = x0/phi(x0); d2 = phi(x0)**-3; x = np.linspace(-9.5, 4.5, 500)
a.plot(x, phi(x), color=BLUE, lw=1.4); a.plot(x, phi(x0)+d1*(x-x0)+.5*d2*(x-x0)**2, color=YELLOW, lw=1.4, ls=(0, (4, 1.8)))
a.plot([x0], [phi(x0)], 'o', ms=4.4, color=GREEN, mew=0, zorder=5); a.plot([0], [1], 'o', ms=4.6, color=RED, mew=0, zorder=5)
xn = -8.; mn = phi(x0)+d1*(xn-x0)+.5*d2*(xn-x0)**2; a.plot([xn], [phi(xn)], 'o', ms=4.4, color=GREEN, mew=0, zorder=5)
a.plot([xn, xn], [mn, phi(xn)], color=MUTED, lw=.85, ls=':')
a.text(2.3, phi(x0)-1.2, '$x^{(0)}$', ha='left'); a.text(-7.5, phi(xn)+.25, '$x^{(1)}$', ha='left'); a.text(.0, -.15, '$x^*$', ha='center')
a.text(3.0, 4.2, '$\\varphi$', ha='left'); a.text(-5, -1.1, '$m$', ha='center')
a.set_xlim(-9.5, 4.5); a.set_ylim(-2.5, 9.5); a.set_xlabel('$x$', labelpad=1); a.set_yticks([0, 4, 8])
T = 6
for x00, c, lw_ in ((.9, GREEN, 1.4), (1., MUTED, 1.1), (1.1, RED, 1.4)):
    X_ = [x00]
    for t in range(T): X_.append(-X_[-1]**3)
    b.semilogy(range(T+1), np.abs(X_), color=c, lw=lw_, marker='o', ms=3.2, mew=0)
b.text(5.9, 1e4, '$x^{(0)}=1.1$', ha='right'); b.text(5.9, 1.6, '$x^{(0)}=1$', ha='right'); b.text(3.2, 1e-3, '$x^{(0)}=0.9$', ha='right')
b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$|x^{(t)}|$', labelpad=1); b.set_xlim(0, 6); b.set_ylim(1e-5, 1e6); b.set_yticks([1e-4, 1, 1e4])
tags(fig, axes); save(fig, HERE, 'figure', {'phi': 'sqrt(1+x^2)', 'newton_map': '-x^3'})
