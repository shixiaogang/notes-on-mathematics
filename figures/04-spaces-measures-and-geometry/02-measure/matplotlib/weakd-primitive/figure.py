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
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.985, top=.95, bottom=.27, wspace=.27)
x = np.linspace(-1.5, 1.5, 6001); dx = x[1]-x[0]
B = bump(x); dB = np.gradient(B, dx); PB = np.cumsum(B)*dx
a = axes[0]; a.axhline(0, color=MUTED, lw=.85); a.plot(x, dB, color=YELLOW, lw=1.4); a.plot(x, B, color=GREEN, lw=1.4)
a.text(-.5, .68, r'$\psi$', ha='center'); a.text(.18, .42, r'$\varphi$', ha='left')
a.set_xlim(-1.5, 1.5); a.set_ylim(-.9, .9); a.set_xticks([-1, 0, 1]); a.set_yticks([-.5, 0, .5]); a.set_xlabel('$x$', labelpad=1)
a.spines['bottom'].set_position(('data', -.9))
b = axes[1]; b.axhline(0, color=MUTED, lw=.85); b.plot(x, B, color=YELLOW, lw=1.4); b.plot(x, PB, color=GREEN, lw=1.4)
b.text(-.68, .3, r'$\psi$', ha='left'); b.text(.65, .47, r'$\int_{-\infty}^x\psi$', ha='left', va='bottom')
b.set_xlim(-1.5, 1.5); b.set_ylim(-.1, .62); b.set_xticks([-1, 0, 1]); b.set_yticks([0, .25, .5]); b.set_xlabel('$x$', labelpad=1)
b.spines['bottom'].set_position(('data', -.1))
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': "(a) phi=exp(-1/(1-x^2)), psi=phi'; (b) psi=exp(-1/(1-x^2)), primitive by cumulative sum"})
