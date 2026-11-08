from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Legendre partial sums of sgn on [-1,1] and squared truncation errors of sgn and |x|, exact by Gauss-Legendre quadrature of polynomials on [0,1].
from numpy.polynomial import legendre as L
N = 60
t, w = L.leggauss(80); t01 = (t+1)/2; w01 = w/2
def Pk(k, z): return L.legval(z, [0]*k+[1])
def coef(k, kind):
    # returns the coefficient of normalized e_k=sqrt((2k+1)/2)P_k
    if kind == 'sgn':
        if k % 2 == 0: return 0.
        return np.sqrt((2*k+1)/2)*2*np.sum(w01*Pk(k, t01))
    if k % 2: return 0.
    return np.sqrt((2*k+1)/2)*2*np.sum(w01*t01*Pk(k, t01))
cs = np.array([coef(k, 'sgn') for k in range(N+1)]); ca = np.array([coef(k, 'abs') for k in range(N+1)])
es = 2-np.cumsum(cs**2); ea = 2/3-np.cumsum(ca**2)
for n in (1, 3, 5, 15, 41): print('sgn', n, es[n])
for n in (0, 2, 4, 40): print('abs', n, ea[n])
print('c3^2', cs[3]**2, 'c5^2', cs[5]**2)
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.26, wspace=.26)
x = np.linspace(-1, 1, 2001)
def partial(n): return sum(cs[k]*np.sqrt((2*k+1)/2)*Pk(k, x) for k in range(1, n+1, 2))
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85)
ax.plot([-1, 0], [-1, -1], color=BLUE, lw=1.4); ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
ax.plot(x, partial(1), color=GREEN, lw=1.1); ax.plot(x, partial(5), color=YELLOW, lw=1.2); ax.plot(x, partial(15), color=RED, lw=1.2)
ax.text(.82, 1.58, '$s_1$'); ax.text(.3, 1.28, '$s_5$'); ax.text(.03, 1.3, '$s_{15}$')
ax.text(-.75, -1.42, r'$\mathrm{sgn}$', ha='center')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.7, 1.8); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ns = np.arange(1, 42, 2); ne = np.arange(2, 42, 2)
ax.semilogy(ns, es[ns], color=BLUE, lw=1.4, marker='o', ms=2.6, mew=0); ax.semilogy(ne, ea[ne], color=GREEN, lw=1.4, marker='s', ms=2.4, mew=0)
ax.text(24, .1, r'$\mathrm{sgn}$'); ax.text(14, 1.6e-4, r'$\vert x\vert$')
ax.set_xlim(0, 42); ax.set_xticks([0, 10, 20, 30, 40]); ax.set_ylim(3e-6, 2); ax.set_xlabel('$n$', labelpad=0); ax.set_ylabel(r'$\Vert f-s_n\Vert_2^2$', labelpad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'c_k=<e_k,f>; ||f-s_n||^2 = ||f||^2 - sum_{k<=n} c_k^2'})
