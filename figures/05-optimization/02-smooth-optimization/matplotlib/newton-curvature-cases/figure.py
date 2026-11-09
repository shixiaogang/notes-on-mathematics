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

fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .03, .985, .985, .155, .12)
cases = [(np.diag([2., .6]), np.array([1., .6])), (np.diag([1., -1.]), np.array([.8, -.5])), (np.diag([1., 0.]), np.array([.8, .5]))]
lims = (-1.9, 1.9)
for k, (ax, (H_, G)) in enumerate(zip(axes, cases)):
    X, Y = grid2(*lims, *lims)
    M = G[0]*X+G[1]*Y+.5*(H_[0,0]*X**2+H_[1,1]*Y**2)
    lv = [-.5, -.2, .1, .5, 1, 1.8] if k == 0 else ([-1.2, -.6, -.2, .1, .5, 1.2] if k == 1 else [-1.2, -.7, -.3, .1, .5, 1, 1.8])
    if k == 0: lv = [-.75, -.5, -.2, .2, .7, 1.4, 2.2]
    ax.contour(X, Y, M, levels=lv, colors=[YELLOW], linewidths=1.0, linestyles='solid')
    ax.plot([0], [0], 'o', ms=4.4, color=GREEN, mew=0, zorder=6)
    if k < 2:
        d = np.linalg.solve(H_, -G); arrow(ax, (0, 0), d, color=GREEN if k == 0 else RED)
        ax.plot(*d, 'o', ms=4.4, color=GREEN if k == 0 else RED, mew=0, zorder=6)
    ax.set_xlim(*lims); ax.set_ylim(*lims); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
wb = dict(fc='white', ec='none', pad=.8)
axes[0].text(.12, .1, '当前点', fontsize=7.5, bbox=wb, zorder=7); axes[1].text(.12, .1, '当前点', fontsize=7.5, bbox=wb, zorder=7); axes[2].text(.12, .1, '当前点', fontsize=7.5, bbox=wb, zorder=7)
axes[0].text(-.5, -1.42, '模型极小点', ha='center', fontsize=7.5, bbox=wb, zorder=7); axes[1].text(-.8, -.92, '模型鞍点', ha='center', fontsize=7.5, bbox=wb, zorder=7)
tags(fig, axes); save(fig, HERE, 'figure', {'model': 'g^T d + 0.5 d^T H d', 'cases': ['diag(2,.6),g=(1,.6)', 'diag(1,-1),g=(.8,-.5)', 'diag(1,0),g=(.8,.5)']})
