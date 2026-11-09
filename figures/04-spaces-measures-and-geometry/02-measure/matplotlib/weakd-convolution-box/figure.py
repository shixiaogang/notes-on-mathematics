from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def bump(t):
    """psi(t)=exp(-1/(1-t^2)) on |t|<1 and 0 elsewhere."""
    t = np.asarray(t, float); out = np.zeros_like(t); m = np.abs(t) < 1
    out[m] = np.exp(-1/(1-t[m]**2)); return out
C1 = 0.44399381623014  # integral of psi over [-1,1]
def rho(t, eps=1.0):
    """1-D mollifier rho_eps(t)=rho(t/eps)/eps."""
    return bump(np.asarray(t, float)/eps)/C1/eps
def mollify(fun, x, eps, n=4001):
    """f_eps(x)=int rho_eps(z) f(x-z) dz by the midpoint rule on [-eps,eps]."""
    z = (np.arange(n)+.5)/n*2*eps-eps; dz = 2*eps/n
    return np.array([np.sum(rho(z, eps)*fun(xi-z))*dz for xi in np.atleast_1d(x)])
def letters(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06, right=.985, top=.95, bottom=.28, wspace=.3)
def box(ax, l, r, c, h=1):
    ax.plot([l-.0, l, r, r], [0, h, h, 0], color=c, lw=1.4, solid_joinstyle='miter')
for ax, x in zip(axes[:2], [.5, 1.5]):
    l, r = max(0, x-1), min(1, x)
    ax.fill_between([l, r], 0, 1, color=GREEN_FILL, lw=0)
    box(ax, 0, 1, BLUE); box(ax, x-1, x, YELLOW, 1)
    ax.set_xlim(-.7, 2.7); ax.set_ylim(0, 1.3); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1]); ax.set_xlabel('$y$', labelpad=1)
    ax.text((l+r)/2, .45, r'$\frac{1}{2}$', ha='center', va='center', color=INK)
axes[0].text(1.05, 1.07, r'$f(y)$', ha='left', color=INK); axes[0].text(-.52, 1.07, r'$g(x-y)$', ha='left', color=INK)
axes[1].text(.05, 1.07, r'$f(y)$', ha='left', color=INK); axes[1].text(1.1, 1.07, r'$g(x-y)$', ha='left', color=INK)
c = axes[2]; x = np.array([-.7, 0, 1, 2, 2.7]); y = np.array([0, 0, 1, 0, 0])
c.plot(x, y, color=GREEN, lw=1.4); c.plot([.5, 1.5], [.5, .5], 'o', ms=3.6, color=GREEN, mew=0)
c.set_xlim(-.7, 2.7); c.set_ylim(0, 1.3); c.set_xticks([0, 1, 2]); c.set_yticks([0, .5, 1]); c.set_xlabel('$x$', labelpad=1); c.set_ylabel(r'$(f*g)(x)$', labelpad=2)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=g=indicator of [0,1]; overlap length at x=0.5 and x=1.5 is 0.5; f*g triangle on [0,2]'})
