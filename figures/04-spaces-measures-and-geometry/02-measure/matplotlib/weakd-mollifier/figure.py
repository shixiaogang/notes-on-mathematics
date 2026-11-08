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
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.085, right=.985, top=.95, bottom=.27, wspace=.3)
a = axes[0]; x = np.linspace(-1.3, 1.3, 1400)
for e, ls in zip([1, .5, .25], ['-', '--', ':']):
    a.plot(x, rho(x, e), color=YELLOW, lw=1.4, ls=ls)
a.text(.72, .45, r'$\varepsilon=1$', ha='left'); a.text(.48, 1.45, r'$\varepsilon=.5$', ha='left'); a.text(.26, 3.05, r'$\varepsilon=.25$', ha='left')
a.set_xlim(-1.3, 1.3); a.set_ylim(0, 3.7); a.set_xticks([-1, 0, 1]); a.set_yticks([0, 1, 2, 3]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel(r'$\rho_\varepsilon$', labelpad=2)
b = axes[1]; x = np.linspace(-1.3, 1.3, 521); eps = .5
b.plot(x, np.abs(x), color=BLUE, lw=1.4, ls='--'); fe = mollify(np.abs, x, eps); b.plot(x, fe, color=GREEN, lw=1.4)
v0 = float(mollify(np.abs, np.array([0.]), eps)[0]); b.plot([0], [v0], 'o', ms=3.4, color=GREEN, mew=0); b.text(0, v0+.2, '{:.3f}'.format(v0), ha='center', va='center')
b.plot([-.5, .5], [0, 0], color=YELLOW, lw=2.2, solid_capstyle='butt', clip_on=False)
b.set_xlim(-1.3, 1.3); b.set_ylim(0, 1.35); b.set_xticks([-1, -.5, 0, .5, 1]); b.set_xticklabels(['-1', '', '0', '', '1']); b.set_yticks([0, .5, 1]); b.set_xlabel('$x$', labelpad=1)
c = axes[2]
c.plot(x[x < 0], -np.ones(np.sum(x < 0)), color=BLUE, lw=1.4, ls='--'); c.plot(x[x > 0], np.ones(np.sum(x > 0)), color=BLUE, lw=1.4, ls='--')
c.plot(x, mollify(np.sign, x, eps), color=GREEN, lw=1.4)
c.set_xlim(-1.3, 1.3); c.set_ylim(-1.3, 1.3); c.set_xticks([-1, -.5, 0, .5, 1]); c.set_xticklabels(['-1', '', '0', '', '1']); c.set_yticks([-1, 0, 1]); c.set_xlabel('$x$', labelpad=1)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'rho_eps from psi=exp(-1/(1-t^2)); f_eps=int rho_eps(z) f(x-z) dz, midpoint rule 4001; eps=0.5', 'value_at_0': v0})
print(v0)
