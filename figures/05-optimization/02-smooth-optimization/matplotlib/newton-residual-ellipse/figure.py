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

fig, ax = figure(width_mm=100, height_mm=56)
fig.set_layout_engine(None); fig.subplots_adjust(left=.115, right=.975, top=.97, bottom=.15)
H_ = np.diag([1., 100.]); G = np.array([1., 10.]); ng = np.linalg.norm(G); dN = np.linalg.solve(H_, -G)
th = np.linspace(0, 2*np.pi, 400)
a_, b_, c_, d_ = -4, 2.4, -.22, .05
xx = np.array([a_, b_]); yy = -xx/10
ax.fill_between(xx, yy, d_, color=RED_FILL, lw=0, zorder=0)
ax.plot(xx, yy, color=STROKE, lw=1.1, zorder=2)
for eta, lw_ in ((.25, 1.3), (.05, 1.3)):
    ax.plot(dN[0]+eta*ng*np.cos(th), dN[1]+eta*ng/100*np.sin(th), color=GREEN, lw=lw_, zorder=3)
bad = np.array([1.5, -.0975])
ax.plot(*dN, 'o', ms=4.6, color=GREEN, mew=0, zorder=5); ax.plot(*bad, 'o', ms=4.6, color=RED, mew=0, zorder=5); ax.plot(0, 0, 'o', ms=3.6, color=INK, mew=0, zorder=5)
ax.text(dN[0]+.08, dN[1]+.005, '$d_N$', ha='left', va='bottom'); ax.text(bad[0]+.08, bad[1]+.01, '$d$', ha='left', va='bottom'); ax.text(.08, .012, '$0$', ha='left')
ax.text(-3.1, -.09, '$\\eta=0.25$', ha='right', va='center') if 0 else None
ax.text(-2.1, -.066, '$\\eta=0.25$', ha='center', va='bottom', fontsize=7.5); ax.text(-1, -.16, '', ); ax.text(1.6, -.03, '上坡', ha='center', va='center', fontsize=7.5); ax.text(-3.5, -.2, '下坡', ha='left', va='center', fontsize=7.5)
ax.set_xlim(a_, b_); ax.set_ylim(c_, d_); ax.set_xlabel('$d_1$', labelpad=1); ax.set_ylabel('$d_2$', labelpad=1); ax.set_yticks([-.2, -.1, 0]); ax.set_yticklabels(['-0.2', '-0.1', '0'])
save(fig, HERE, 'figure', {'H': 'diag(1,100)', 'g': [1, 10], 'etas': [.25, .05], 'bad_d': bad.tolist(), 'g_dot_bad_d': float(G@bad)})
