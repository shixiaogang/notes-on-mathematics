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
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.085, right=.985, top=.94, bottom=.29, wspace=.3)
def stem(ax, k, v, c):
    ax.vlines(k, 0, v, color=c, lw=1.1); ax.plot(k, v, 'o', ms=3.4, color=c, mew=0, clip_on=False)
k = np.arange(-3, 5); a = (k >= 1).astype(float); w = {-1: .25, 0: .5, 1: .25}
b = np.array([.25*(ki-1 >= 1)+.5*(ki >= 1)+.25*(ki+1 >= 1) for ki in k], float)
stem(axes[0], k, a, BLUE); axes[0].set_ylabel('$a_k$', labelpad=2); axes[0].set_xlabel('$k$', labelpad=1)
j = np.arange(-3, 5); wv = np.array([w.get(int(i), 0.) for i in j])
stem(axes[1], j, wv, YELLOW); axes[1].set_ylabel('$w_j$', labelpad=2); axes[1].set_xlabel('$j$', labelpad=1)
stem(axes[2], k, b, GREEN); axes[2].set_ylabel('$b_k$', labelpad=2); axes[2].set_xlabel('$k$', labelpad=1)
axes[2].text(.0, .33, r'$\frac{1}{4}$', ha='center'); axes[2].text(.55, .86, r'$\frac{3}{4}$', ha='right')
for ax in axes:
    ax.set_xlim(-3.5, 4.5); ax.set_ylim(0, 1.15); ax.set_xticks([-2, 0, 2, 4]); ax.set_yticks([0, .5, 1])
letters(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'a_k=1(k>=1); w=(1/4,1/2,1/4); b_k=sum_j w_j a_(k-j)'})
