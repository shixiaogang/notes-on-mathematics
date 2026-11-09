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

fig, ax = figure(width_mm=92, height_mm=66)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.985, top=.975, bottom=.13)
a, b, c, d = -.4, 1.6, -.5, 2.2
X, Y = grid2(a, b, c, d); F = .5*(X-1)**2+(Y-X**2)**2
region(ax, a, b, c, d)
ax.contour(X, Y, F, levels=[.005, .03, .1, .2, .4, .8, 1.5], colors=[BLUE], linewidths=.75, zorder=2)
x = np.array([.5, 0.]); P = [x.copy()]
for t in range(5):
    x = x+np.linalg.solve(hess(x), -grad(x)); P.append(x.copy())
P = np.array(P)
ax.plot(P[:,0], P[:,1], color=GREEN, lw=1.4, marker='o', ms=4, mew=0, zorder=5)
ax.plot(*XS, 'o', ms=4.8, color=RED, mew=0, zorder=6)
ax.text(.53, -.13, '$x^{(0)}$', va='center'); ax.text(.7, .6, '$x^{(1)}$', ha='right'); ax.text(.89, .93, '$x^{(2)}$', ha='right'); ax.text(1.05, 1.08, '$x^*$')
ax.text(-.32, 1.75, '不定', fontsize=7.5); ax.text(-.32, -.3, '正定', fontsize=7.5)
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=0)
save(fig, HERE, 'figure', {'start': [.5, 0], 'iterates': P.tolist()})
