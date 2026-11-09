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
fig.set_layout_engine(None); fig.subplots_adjust(left=.07, right=.985, top=.95, bottom=.27, wspace=.25)
x = np.linspace(0, 2, 2001); h = np.sin(np.pi*x); dx = x[1]-x[0]; vals = []
for ax, (x0, r) in zip(axes, [(1., .9), (.5, .4)]):
    p = np.e*bump((x-x0)/r); y = h*p; vals.append(float(np.sum(y)*dx))
    ax.fill_between(x, 0, y, where=y >= 0, color=GREEN_FILL, lw=0); ax.fill_between(x, 0, y, where=y <= 0, color=RED_FILL, lw=0)
    ax.axhline(0, color=MUTED, lw=.85)
    ax.plot(x, h, color=BLUE, lw=1.4); ax.plot(x, p, color=YELLOW, lw=1.4)
    ax.set_xlim(0, 2); ax.set_ylim(-1.15, 1.25); ax.set_xticks([0, .5, 1, 1.5, 2]); ax.set_xticklabels(['0', '', '1', '', '2']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=1)
    ax.spines['bottom'].set_position(('data', -1.15))
axes[0].text(1.62, -.82, '$h$', color=INK); axes[0].text(1.05, 1.07, r'$\varphi$', color=INK)
axes[1].text(1.62, -.82, '$h$', color=INK); axes[1].text(.56, 1.07, r'$\varphi$', color=INK)
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h=sin(pi x); phi=e*psi((x-x0)/r), (x0,r)=(1,.9) and (.5,.4)', 'readings': vals})
print(vals)
