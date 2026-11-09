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
panel(fig, .115, .985, .96, .215, .36)
a, b = axes
def err(alpha_rule, n):
    x = np.array([.5, 0.]); E = [np.linalg.norm(x-XS)]
    for t in range(n):
        d = np.linalg.solve(hess(x), -grad(x)); x = x+alpha_rule*d; E.append(np.linalg.norm(x-XS))
    return E
E1 = err(1., 5); E5 = err(.5, 30); E9 = err(.9, 12)
a.semilogy(range(len(E1)), E1, color=GREEN, lw=1.4, marker='o', ms=3.2, mew=0); a.semilogy(range(len(E9)), E9, color=PURPLE, lw=1.4); a.semilogy(range(len(E5)), E5, color=YELLOW, lw=1.4)
a.text(.4, 1e-6, '$\\alpha=1$', ha='left', va='center'); a.text(10.8, 3e-8, '$\\alpha=0.9$', ha='left', va='center'); a.text(19, 1e-3, '$\\alpha=0.5$', ha='left', va='bottom')
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$\\Vert x^{(t)}-x^*\\Vert_2$', labelpad=1); a.set_ylim(1e-9, 3); a.set_xlim(0, 30)
t = np.linspace(0, 1.5, 300)
b.plot(t, -t+.5*t**2, color=BLUE, lw=1.4); b.plot(t, -.25*t, color=GREEN, lw=1.2, ls=(0, (4, 1.8))); b.plot(t, -.75*t, color=RED, lw=1.2, ls=(0, (4, 1.8)))
b.plot([1], [-.5], 'o', ms=4.6, color=INK, mew=0, zorder=5); b.plot([1, 1], [-.75, -.25], color=MUTED, lw=.85, ls=':')
b.text(1.22, -.27, '$c=1/4$', ha='center', va='bottom'); b.text(1.12, -.93, '$c=3/4$', ha='right', va='top'); b.text(1.03, -.5, '$\\alpha=1$', ha='left', va='top')
b.set_xlabel('$\\alpha$', labelpad=1); b.set_ylabel('$h(\\alpha)$', labelpad=1); b.set_xlim(0, 1.5); b.set_ylim(-1.2, .15); b.set_yticks([-1, -.5, 0]); b.set_xticks([0, .5, 1, 1.5])
tags(fig, axes); save(fig, HERE, 'figure', {'a': 'fixed alpha Newton from (0.5,0)', 'b': 'h(a)=-a+a^2/2, Armijo lines -c a'})
