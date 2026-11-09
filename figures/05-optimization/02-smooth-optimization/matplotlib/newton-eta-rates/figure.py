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
panel(fig, .125, .985, .96, .215, .36)
a, b = axes; x0 = (.9, .8); AS = hess(XS)
def run(eta, n):
    x = np.array(x0); Gs = [np.linalg.norm(grad(x))]; R = []
    for t in range(n):
        G = grad(x); e = eta(t, np.linalg.norm(G)); d = np.linalg.solve(hess(x), -G+e*G)
        wn = np.linalg.norm(AS@(x-XS)); x = x+d; R.append(np.linalg.norm(AS@(x-XS))/wn); Gs.append(np.linalg.norm(grad(x)))
    return np.array(Gs), np.array(R)
cases = [(lambda t, g: .5, YELLOW, 'solid', 38), (lambda t, g: .1, PURPLE, 'solid', 13), (lambda t, g: 1/(t+2), BLUE, 'solid', 12), (lambda t, g: min(.5, g), GREEN, 'solid', 7)]
Out = []
for eta, c, ls, n in cases:
    Gs, R = run(eta, n); keep = Gs > 3e-14; a.semilogy(np.arange(len(Gs))[keep], Gs[keep], color=c, lw=1.4)
    k2 = keep[:-1] & (Gs[1:] > 3e-13); b.plot(np.arange(len(R))[k2], R[k2], color=c, lw=1.4, marker='o', ms=2.6, mew=0)
    Out.append(R[k2].tolist())
a.text(22, 2e-6, '$\\eta=0.5$', ha='left', va='bottom'); a.text(13.4, 1e-13, '$\\eta=0.1$', ha='left', va='center'); a.text(13, 1e-9, '$\\eta_t=\\frac{1}{t+2}$', ha='left', va='center'); a.text(3.8, 1e-13, '$\\eta_t=\\min\\{0.5,\\Vert g\\Vert_2\\}$', ha='left', va='bottom') if 0 else a.text(.3, 1e-11, '$\\eta_t=\\Vert g\\Vert_2$', ha='left', va='center')
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$\\Vert g^{(t)}\\Vert_2$', labelpad=1); a.set_ylim(1e-14, 2); a.set_xlim(0, 38); a.set_yticks([1e-12, 1e-6, 1])
b.axhline(.5, color=MUTED, lw=.85, ls=':'); b.axhline(.1, color=MUTED, lw=.85, ls=':')
b.set_xlabel('$t$', labelpad=1); b.set_ylabel('收缩比', labelpad=1); b.set_ylim(0, .8); b.set_xlim(0, 20); b.set_yticks([0, .1, .5])
tags(fig, axes); save(fig, HERE, 'figure', {'start': x0, 'residual': 'r=eta*g (exact relative size)', 'ratios': Out})
