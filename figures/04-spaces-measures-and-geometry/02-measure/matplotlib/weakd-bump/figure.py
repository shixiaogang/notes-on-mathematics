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
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.985, top=.95, bottom=.28, wspace=.34)
a = axes[0]; s = np.linspace(-.8, 2.2, 700); y = np.where(s > 0, np.exp(-1/np.where(s > 0, s, 1)), 0)
a.plot(s, y, color=BLUE, lw=1.4); a.set_xlim(-.8, 2.2); a.set_ylim(0, .78); a.set_xticks([0, 1, 2]); a.set_yticks([0, .5]); a.set_xlabel('$s$', labelpad=1); a.set_ylabel('$E(s)$', labelpad=2)
b = axes[1]; x = np.linspace(-1.5, 1.5, 700)
b.plot(x, bump(x), color=YELLOW, lw=1.4); b.set_xlim(-1.5, 1.5); b.set_ylim(0, .5); b.set_xticks([-1, 0, 1]); b.set_yticks([0, .25]); b.set_xlabel('$x$', labelpad=1); b.set_ylabel(r'$\psi(x)$', labelpad=2)
c = axes[2]; x = np.linspace(0, 3, 900)
c.plot(x, bump((x-2)/.5), color=YELLOW, lw=1.4); c.plot([1.5, 2.5], [0, 0], color=GREEN, lw=2.2, solid_capstyle='butt', clip_on=False)
c.plot([0, 3], [0, 0], 'o', ms=3.6, mfc='white', mec=INK, mew=.8, clip_on=False, zorder=5)
c.text(2, .42, r'$\varphi$', ha='center', color=INK); c.text(.22, .05, r'$\Omega$', ha='left', color=INK)
c.set_xlim(-.15, 3.15); c.set_ylim(0, .5); c.set_xticks([0, 1.5, 2, 2.5, 3]); c.set_xticklabels(['0', '', '$x_0$', '', '3']); c.set_yticks([0, .25]); c.set_xlabel('$x$', labelpad=1)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'E(s)=exp(-1/s) for s>0; psi(x)=E(1-x^2); phi(x)=psi((x-2)/0.5) on Omega=(0,3)'})
