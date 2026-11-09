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

fig, ax = figure(width_mm=96, height_mm=54)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.975, top=.97, bottom=.165)
p = np.array([-1., 1.2]); G = grad(p); d = np.linalg.solve(hess(p), -G); s = G@d; c = .1
al = np.linspace(0, .19, 500); ph = np.array([f(p+t*d) for t in al])
ax.plot(al, ph, color=BLUE, lw=1.4); ax.plot(al, f(p)+c*al*s, color=STROKE, lw=1.1, ls=(0, (4, 1.8))); ax.plot(al[al < .1], f(p)+al[al < .1]*s, color=MUTED, lw=.85, ls=':')
ax.plot([.0625], [f(p+.0625*d)], 'o', ms=4.8, color=GREEN, mew=0, zorder=5); ax.plot([.125], [f(p+.125*d)], 'x', ms=5, color=RED, mew=1.2, zorder=5); ax.plot([0], [f(p)], 'o', ms=4, color=INK, mew=0, zorder=5, clip_on=False)
ax.text(.0655, f(p+.0625*d)-.34, '接受', ha='left'); ax.text(.128, f(p+.125*d)+.25, '拒绝', ha='center')
ax.text(.165, 1.6, 'Armijo线', ha='center', va='top', fontsize=7.5); ax.text(.0925, .06, '切线', ha='left', fontsize=7.5); 
ax.set_xlim(0, .19); ax.set_ylim(0, 4); ax.set_xlabel('$\\alpha$', labelpad=1); ax.set_ylabel('$\\varphi(\\alpha)$', labelpad=1); ax.set_xticks([0, .0625, .125]); ax.set_xticklabels(['0', '1/16', '1/8'])
save(fig, HERE, 'figure', {'x0': [-1, 1.2], 'd': d.tolist(), 'c': c, 'trial_values': {str(t): float(f(p+t*d)) for t in (1, .5, .25, .125, .0625)}})
