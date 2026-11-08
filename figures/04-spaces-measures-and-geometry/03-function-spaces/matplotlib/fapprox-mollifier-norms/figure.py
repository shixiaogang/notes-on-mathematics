from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f = indicator of [0,1/2] on R, f_eps = rho_eps * f with the standard bump rho(u)=c^{-1}exp(-1/(1-u^2)).
# L^p errors for eps<=1/4: ||f_eps-f||_1 = 2 m1 eps; ||f_eps-f||_2^2 = 4 eps int_0^1 T(u)^2 du, T(u)=int_u^1 rho; sup error 1/2.
u = np.linspace(-1, 1, 200001)[1:-1]; du = u[1]-u[0]
rho = np.exp(-1/(1-u**2)); rho /= rho.sum()*du
mid = u > 0
m1 = 2*(u[mid]*rho[mid]).sum()*du
T = np.cumsum(rho[mid][::-1])[::-1]*du
I2 = (T**2).sum()*du
print('m1', m1, 'int T^2', I2)
Phi = np.cumsum(rho)*du
def feps(x, eps):
    # rho_eps*f(x) = P(x-eps Y in [0,1/2]) = Phi(x/eps)-Phi((x-1/2)/eps)
    return np.interp(x/eps, u, Phi, left=0, right=1)-np.interp((x-.5)/eps, u, Phi, left=0, right=1)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.97, bottom=.27, wspace=.27)
x = np.linspace(-.3, .8, 4001)
ax = axes[0]
ax.plot([-.3, 0], [0, 0], color=BLUE, lw=1.4); ax.plot([0, .5], [1, 1], color=BLUE, lw=1.4); ax.plot([.5, .8], [0, 0], color=BLUE, lw=1.4)
ax.plot([0, 0], [0, 1], color=BLUE, lw=.85, ls=(0, (2, 2))); ax.plot([.5, .5], [0, 1], color=BLUE, lw=.85, ls=(0, (2, 2)))
ax.plot(x, feps(x, .2), color=GREEN, lw=1.4); ax.plot(x, feps(x, .05), color=RED, lw=1.4)
ax.plot([0, .5], [.5, .5], 'o', ms=3, color=INK, mew=0)
ax.text(.25, 1.08, '$f$', ha='center'); ax.text(-.2, .3, r'$f_{0.2}$', ha='center'); ax.text(.11, .42, r'$f_{0.05}$', ha='center')
ax.set_xlim(-.3, .8); ax.set_ylim(-.06, 1.24); ax.set_xticks([0, .5]); ax.set_xticklabels(['0', '1/2']); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
e = np.geomspace(.005, .25, 30)
ax.loglog(e, 2*m1*e, color=BLUE, lw=1.4); ax.loglog(e, np.sqrt(4*e*I2), color=GREEN, lw=1.4); ax.loglog(e, .5*np.ones_like(e), color=RED, lw=1.4)
ax.text(.03, .0085, r'$\Vert f_\varepsilon-f\Vert_1$', color=INK); ax.text(.009, .135, r'$\Vert f_\varepsilon-f\Vert_2$', color=INK, rotation=0); ax.text(.0065, .6, r'$\Vert f_\varepsilon-f\Vert_\infty$', color=INK)
ax.set_xlim(.005, .25); ax.set_ylim(2.5e-3, 1.2); ax.set_xlabel(r'$\varepsilon$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1_[0,1/2]; f_eps=rho_eps*f; ||.||_1=2 m1 eps; ||.||_2^2=4 eps int_0^1 T^2; sup=1/2'})
