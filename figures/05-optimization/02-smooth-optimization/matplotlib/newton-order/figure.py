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

fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .115, .985, .96, .215, .36)
a, b = axes
x = np.array([.5, 0.]); E = [np.linalg.norm(x-XS)]
for t in range(5):
    x = x+np.linalg.solve(hess(x), -grad(x)); E.append(np.linalg.norm(x-XS))
x = np.array([.5, 0.]); Eg = [np.linalg.norm(x-XS)]
for t in range(60):
    G = grad(x); s = 1.
    while f(x-s*G) > f(x)-.1*s*G@G: s /= 2
    x = x-s*G; Eg.append(np.linalg.norm(x-XS))
a.semilogy(range(len(E)), E, color=GREEN, lw=1.4, marker='o', ms=3.4, mew=0)
a.semilogy(range(len(Eg)), Eg, color=YELLOW, lw=1.4)
a.text(4.9, 1e-7, 'Newton', ha='left', va='center'); a.text(38, 1.2e-1, '梯度下降', ha='center', va='bottom')
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$\\Vert x^{(t)}-x^*\\Vert_2$', labelpad=1); a.set_xlim(0, 60); a.set_ylim(1e-9, 3)
def orbit(e0, m, n):
    E_ = [e0]
    for k in range(n): E_.append(m(E_[-1]))
    return np.array(E_)
m2 = lambda e: e+np.expm1(-e) if e > 1e-3 else e*e/2-e**3/6
m15 = lambda e: 1.25*e**1.5/(2+3.75*e**.5)
m1 = lambda e: 2*e/3
E2 = orbit(.8, m2, 5); E15 = orbit(.8, m15, 7); E1 = orbit(.8, m1, 60)
for Ee, c, m_, lab in ((E2, GREEN, 'o', ''), (E15, PURPLE, 's', ''), (E1, YELLOW, '^', '')):
    Ee = Ee[Ee > 1e-11]
    b.loglog(Ee[:-1], Ee[1:], color=c, lw=1.4, marker=m_, ms=2.8, mew=0)
t = np.array([1e-11, 1.]); b.loglog(t, t, color=MUTED, lw=.85, ls=':')
b.text(1e-2, 1e-6, '$e^x-2x$', ha='left', va='center'); b.text(1.5e-5, 2e-9, '$x^2+|x|^{5/2}$', ha='left', va='center')
b.text(1e-6, 4e-6, '$x^4$', ha='center', va='bottom')
b.set_xlabel('$e^{(t)}$', labelpad=1); b.set_ylabel('$e^{(t+1)}$', labelpad=1); b.set_xlim(1e-8, 2); b.set_ylim(1e-10, 2)
b.set_xticks([1e-8, 1e-4, 1]); b.set_yticks([1e-10, 1e-5, 1])
tags(fig, axes); save(fig, HERE, 'figure', {'a': 'running objective from (0.5,0); gradient descent with Armijo c=0.1', 'b': {'exp': 'e+e^{-e}-1', 'x2_plus': '1.25 e^1.5/(2+3.75 e^.5)', 'x4': '2e/3'}})
