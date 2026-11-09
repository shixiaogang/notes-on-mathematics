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
panel(fig, .1, .985, .96, .215, .36)
a, b = axes
p = np.array([-1., 1.2]); G = grad(p); H_ = hess(p)
D = np.logspace(-3, 2.5, 200); N = [np.linalg.norm(np.linalg.solve(H_+t*np.eye(2), -G)) for t in D]
a.loglog(D, N, color=GREEN, lw=1.4)
marks = [.1, 1, 10]
for t in marks:
    n_ = np.linalg.norm(np.linalg.solve(H_+t*np.eye(2), -G)); a.plot([t], [n_], 'o', ms=4, color=GREEN, mew=0, zorder=5)
a.axvline(np.linalg.eigvalsh(H_)[0], color=MUTED, lw=.85, ls=':'); a.axvline(np.linalg.eigvalsh(H_)[1], color=MUTED, lw=.85, ls=':')
a.text(.044, .03, '$\\lambda_1$', ha='left'); a.text(11.5, 8, '$\\lambda_2$', ha='left')
a.set_xlabel('$\\delta$', labelpad=1); a.set_ylabel('$\\Vert d(\\delta)\\Vert_2$', labelpad=1); a.set_xlim(1e-3, 300); a.set_ylim(5e-3, 50); a.set_xticks([1e-2, 1, 100]); a.set_yticks([1e-2, 1])
def err(dfun, n, x0=(.9, .8)):
    x = np.array(x0); E = [np.linalg.norm(x-XS)]
    for t in range(n):
        d_ = np.linalg.solve(hess(x)+dfun(t, x)*np.eye(2), -grad(x)); x = x+d_; E.append(np.linalg.norm(x-XS))
    return E
E0 = err(lambda t, x: 0., 4); E1 = err(lambda t, x: .1, 26); E2 = err(lambda t, x: 1., 40); E3 = err(lambda t, x: np.linalg.norm(grad(x)), 7)
b.semilogy(range(len(E0)), E0, color=GREEN, lw=1.4, marker='o', ms=3.2, mew=0); b.semilogy(range(len(E3)), E3, color=PURPLE, lw=1.4, marker='s', ms=2.8, mew=0); b.semilogy(range(len(E1)), E1, color=YELLOW, lw=1.4); b.semilogy(range(len(E2)), E2, color=RED, lw=1.4)
b.text(.3, 3e-9, '$\\delta=0$', ha='left', va='center'); b.text(7.2, 5e-8, '$\\delta=\\Vert g\\Vert_2$', ha='left', va='center'); b.text(16.5, 2.2e-6, '$\\delta=0.1$', ha='left', va='center'); b.text(30, 8e-3, '$\\delta=1$', ha='center', va='bottom')
b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$\\Vert x^{(t)}-x^*\\Vert_2$', labelpad=1); b.set_ylim(1e-10, 1); b.set_xlim(0, 40); b.set_yticks([1e-10, 1e-5, 1])
tags(fig, axes); save(fig, HERE, 'figure', {'a_point': p.tolist(), 'b_start': [.9, .8], 'delta_cases': [0, .1, 1, 'norm g']})
