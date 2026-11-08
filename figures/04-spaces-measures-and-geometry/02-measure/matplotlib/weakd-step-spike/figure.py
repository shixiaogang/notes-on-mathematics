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
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.985, top=.95, bottom=.27, wspace=.25)
a = axes[0]; x = np.linspace(-.75, .75, 3001)
for e, ls in zip([.5, .25, .1], ['-', '--', ':']):
    a.plot(x, rho(x, e), color=YELLOW, lw=1.4, ls=ls)
a.text(.32, 1.25, r'$\varepsilon=.5$', ha='left'); a.text(.16, 3.1, r'$\varepsilon=.25$', ha='left'); a.text(.09, 7.6, r'$\varepsilon=.1$', ha='left')
a.set_xlim(-.75, .75); a.set_ylim(0, 9); a.set_xticks([-.5, 0, .5]); a.set_yticks([0, 4, 8]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel(r"$H_\varepsilon'=\rho_\varepsilon$", labelpad=2)
b = axes[1]; x = np.linspace(-1.25, 1.25, 4001); x = x[x != 0]; g = .25/np.sqrt(np.abs(x))
m = np.abs(x) <= .25
b.fill_between(x[m], 0, np.minimum(g[m], 1.6), color=RED_FILL, lw=0)
for e, ls in zip([1, .5, .25], ['-', '--', ':']):
    b.plot(x, np.e*bump(x/e), color=YELLOW, lw=1.4, ls=ls)
b.plot(x[x < 0], g[x < 0], color=BLUE, lw=1.4); b.plot(x[x > 0], g[x > 0], color=BLUE, lw=1.4)
b.text(.95, .31, '$g$', ha='left', va='bottom'); b.text(.55, .93, r'$\varphi_\varepsilon$', ha='left', va='center')
b.set_xlim(-1.25, 1.25); b.set_ylim(0, 1.6); b.set_xticks([-1, 0, 1]); b.set_yticks([0, 1]); b.set_xlabel('$x$', labelpad=1)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'rho_eps for eps=.5,.25,.1; phi_eps=e*psi(x/eps), eps=1,.5,.25; g=.25|x|^(-1/2)'})
