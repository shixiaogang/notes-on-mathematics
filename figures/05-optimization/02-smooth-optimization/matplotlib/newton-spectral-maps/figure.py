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

fig, ax = figure(width_mm=86, height_mm=56)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.975, top=.97, bottom=.15)
lam = np.linspace(-2, 4, 400); w = np.array([-.561553, 3.561553]); eps = .3; dl = 1.
ax.plot(lam, lam, color=MUTED, lw=.85, ls=':'); ax.plot(lam, lam+dl, color=GREEN, lw=1.4); ax.plot(lam, np.abs(lam), color=PURPLE, lw=1.4); ax.plot(lam, np.maximum(lam, eps), color=YELLOW, lw=1.4)
for v in w:
    ax.axvline(v, color=MUTED, lw=.7, ls=(0, (1, 2)))
    for y, c in ((v+dl, GREEN), (abs(v), PURPLE), (max(v, eps), YELLOW)): ax.plot([v], [y], 'o', ms=3.8, color=c, mew=0, zorder=5)
ax.axhspan(-2.2, 0, color=RED_FILL, lw=0, zorder=0)
ax.text(1.0, 2.15, '平移', ha='right'); ax.text(-1.3, 1.6, '取绝对值', ha='center'); ax.text(1.6, .9, '下限截断', ha='left'); ax.text(-1.2, -1.75, '$\\tilde\\lambda=\\lambda$', ha='left')
ax.set_xlim(-2, 4); ax.set_ylim(-2.2, 5); ax.set_xlabel('$\\lambda$', labelpad=1); ax.set_ylabel('$\\tilde\\lambda$', labelpad=1)
save(fig, HERE, 'figure', {'eigs': w.tolist(), 'shift': dl, 'floor': eps})
