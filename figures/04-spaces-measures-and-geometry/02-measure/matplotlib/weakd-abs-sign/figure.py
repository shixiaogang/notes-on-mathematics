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
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.985, top=.95, bottom=.27, wspace=.28)
a = axes[0]; x = np.array([-1.4, 0, 1.4]); a.plot(x, np.abs(x), color=BLUE, lw=1.4)
a.plot([-1, .5], [1, .5], 'o', ms=3.6, color=BLUE, mew=0); a.text(-.86, 1.03, r'$(-1,1)$', ha='left', va='bottom'); a.text(.62, .47, r'$(0.5,\,0.5)$', ha='left', va='top')
a.set_xlim(-1.4, 1.4); a.set_ylim(0, 1.5); a.set_xticks([-1, 0, 1]); a.set_yticks([0, 1]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel(r'$|x|$', labelpad=2)
b = axes[1]
b.fill_between([-1, 0], -1, 0, color=RED_FILL, lw=0); b.fill_between([0, .5], 0, 1, color=GREEN_FILL, lw=0)
b.plot([-1.4, 0], [-1, -1], color=BLUE, lw=1.4); b.plot([0, 1.4], [1, 1], color=BLUE, lw=1.4); b.axhline(0, color=MUTED, lw=.85)
b.plot([0, 0], [-1, 1], 'o', ms=3.6, mfc='white', mec=BLUE, mew=.9, zorder=5, clip_on=False)
b.text(-.5, -.5, '$-1$', ha='center', va='center'); b.text(.25, .5, '$0.5$', ha='center', va='center')
b.set_xlim(-1.4, 1.4); b.set_ylim(-1.35, 1.35); b.set_xticks([-1, 0, .5, 1]); b.set_xticklabels(['-1', '0', '.5', '1']); b.set_yticks([-1, 0, 1]); b.set_xlabel('$x$', labelpad=1); b.set_ylabel(r'$\mathrm{sgn}\,x$', labelpad=2)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '|x| and sgn x; int_{-1}^{0.5} sgn = -1+0.5'})
