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
M1 = 0.33445399770994083  # int |u| rho(u) du
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.105, right=.985, top=.95, bottom=.27, wspace=.27)
H = lambda t: (np.asarray(t) > 0).astype(float)
a = axes[0]; x = np.linspace(-.75, .75, 601)
a.plot([-.75, 0], [0, 0], color=BLUE, lw=1.4); a.plot([0, .75], [1, 1], color=BLUE, lw=1.4)
for e, ls in zip([.5, .25, .1], ['-', '--', ':']):
    a.plot(x, mollify(H, x, e), color=GREEN, lw=1.4, ls=ls)
a.text(.34, .78, r'$\varepsilon=.5$', ha='left'); a.text(.17, .55, r'$\varepsilon=.25$', ha='left'); a.text(.07, .32, r'$\varepsilon=.1$', ha='left')
a.set_xlim(-.75, .75); a.set_ylim(-.05, 1.15); a.set_xticks([-.5, 0, .5]); a.set_yticks([0, .5, 1]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel(r'$H,\ H_\varepsilon$', labelpad=2)
b = axes[1]; e = np.linspace(0, .55, 200)
b.plot(e, .5*np.ones_like(e), color=RED, lw=1.4, ls='--'); b.plot(e, M1*e, color=RED, lw=1.4)
pts = np.array([.1, .25, .5]); b.plot(pts, M1*pts, 'o', ms=3.4, color=RED, mew=0)
b.text(.03, .535, r'$\sup_K|H_\varepsilon-H|$', ha='left', va='bottom'); b.text(.3, .07, r'$\int_K|H_\varepsilon-H|$', ha='left', va='top')
b.set_xlim(0, .55); b.set_ylim(0, .7); b.set_xticks([0, .25, .5]); b.set_yticks([0, .25, .5]); b.set_xlabel(r'$\varepsilon$', labelpad=1)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'H_eps by midpoint rule; L1 error on K=[-1/2,1/2] equals eps*m1, m1=0.33445; sup error 1/2'})
