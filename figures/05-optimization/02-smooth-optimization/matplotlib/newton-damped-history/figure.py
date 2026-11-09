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

def run(x, full=False, c=.1, n=9):
    F_ = [f(x)]; A = []
    for t in range(n):
        G = grad(x); d = np.linalg.solve(hess(x), -G); s = G@d; a = 1.
        if not full:
            while f(x+a*d) > f(x)+c*a*s: a /= 2
        x = x+a*d; F_.append(f(x)); A.append(a)
    return np.array(F_), A
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, .125, .985, .96, .225, .36)
a, b = axes; p0 = np.array([-1., 1.2])
Fd, A = run(p0.copy(), n=8); Ff, _ = run(p0.copy(), full=True, n=6)
Fd = np.clip(Fd, 1e-20, None); Ff = np.clip(Ff, 1e-20, None)
a.semilogy(range(len(Ff)), Ff, color=YELLOW, lw=1.4, marker='o', ms=3.2, mew=0); a.semilogy(range(len(Fd)), Fd, color=GREEN, lw=1.4, marker='o', ms=3.2, mew=0)
a.text(1.25, 9e3, '整步', ha='left', va='center'); a.text(4.7, 1e-1, '阻尼', ha='left', va='center')
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$f(x^{(t)})$', labelpad=1); a.set_ylim(1e-18, 1e5); a.set_yticks([1e-15, 1e-10, 1e-5, 1]); a.set_xticks(range(0, 9, 2))
b.plot(range(len(A)), A, color=GREEN, lw=1.4, marker='o', ms=3.6, mew=0); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$\\alpha^{(t)}$', labelpad=1); b.set_ylim(0, 1.1); b.set_yticks([.0625, .5, 1]); b.set_yticklabels(['1/16', '1/2', '1']); b.set_xticks(range(0, 8, 2))
tags(fig, axes); save(fig, HERE, 'figure', {'start': [-1, 1.2], 'alpha': A, 'f_damped': Fd.tolist(), 'f_full': Ff.tolist()})
