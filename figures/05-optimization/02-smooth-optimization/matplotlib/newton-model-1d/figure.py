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
F = lambda x: np.exp(x)-2*x; D = lambda x: np.exp(x)-2
x0 = 1.5; x1 = x0-D(x0)/np.exp(x0); xs = np.log(2)
m = lambda x: F(x0)+D(x0)*(x-x0)+.5*np.exp(x0)*(x-x0)**2
a = axes[0]; x = np.linspace(-.6, 2.15, 400)
a.plot(x, F(x), color=BLUE, lw=1.4); a.plot(x, m(x), color=YELLOW, lw=1.4, ls=(0, (4, 1.8)))
a.plot([x0], [F(x0)], 'o', ms=4.4, color=GREEN, mew=0, zorder=5); a.plot([x1], [m(x1)], 'o', ms=4.4, color=GREEN, mew=0, zorder=5)
a.plot([xs], [F(xs)], 'o', ms=4.6, color=RED, mew=0, zorder=5); a.plot([x1, x1], [m(x1), F(x1)], color=MUTED, lw=.85, ls=':')
a.text(x0+.02, F(x0)+.16, '$x^{(0)}$', ha='center'); a.text(x1+.05, m(x1)-.32, '$x^{(1)}$', ha='left'); a.text(xs-.04, F(xs)-.36, '$x^*$', ha='center')
a.text(1.92, 4.3, '$f$', color=INK); a.text(-.45, 3.7, '$m$', color=INK)
a.set_xlim(-.6, 2.15); a.set_ylim(0, 5.2); a.set_xlabel('$x$', labelpad=1); a.set_yticks([0, 2, 4])
b = axes[1]; b.axhline(0, color=STROKE, lw=.85)
b.plot(x, D(x), color=BLUE, lw=1.4); b.plot(x, D(x0)+np.exp(x0)*(x-x0), color=YELLOW, lw=1.4, ls=(0, (4, 1.8)))
b.plot([x0], [D(x0)], 'o', ms=4.4, color=GREEN, mew=0, zorder=5); b.plot([x1], [0], 'o', ms=4.4, color=GREEN, mew=0, zorder=5); b.plot([xs], [0], 'o', ms=4.6, color=RED, mew=0, zorder=5)
b.plot([x0, x0], [0, D(x0)], color=MUTED, lw=.85, ls=':')
b.text(x0-.06, D(x0)+.28, '$x^{(0)}$', ha='right'); b.text(x1+.04, -.72, '$x^{(1)}$', ha='left'); b.text(xs-.04, -.72, '$x^*$', ha='right')
b.text(2.0, 5.5, "$f'$", ha='right'); b.text(-.42, -4.0, "切线", ha='left')
b.set_xlim(-.6, 2.15); b.set_ylim(-5.2, 6.5); b.set_xlabel('$x$', labelpad=1); b.set_yticks([-4, 0, 4])
tags(fig, axes); save(fig, HERE, 'figure', {'f': 'exp(x)-2x', 'x0': x0, 'x1': float(x1), 'x_star': float(xs)})
