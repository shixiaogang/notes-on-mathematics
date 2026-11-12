from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# U_n uniform on the midpoints (2k-1)/(2n), k=1..n, versus U=Unif(0,1).
# (a) n=5: lattice masses 1/n (green stems) and the density of U (blue).
# (b) d_TV(U_n,U)=1 (purple), W_1(U_n,U)=1/(4n) (blue), MMD with Gaussian kernel sigma=0.1 (yellow);
#     MMD^2 = E k(U_n,U_n') - 2 E k(U_n,U) + E k(U,U'), the last two by exact erf formulas.
s = .1
c = math.sqrt(2*math.pi)*s


def ek_point_unif(y):
    # E k(y,U) = int_0^1 exp(-(y-u)^2/(2s^2)) du
    y = np.asarray(y, float)
    return c*(Phi((1-y)/s)-Phi(-y/s))


def ek_unif_unif():
    u = np.linspace(0, 1, 20001)
    return float(np.trapezoid(ek_point_unif(u), u))


EUU = ek_unif_unif()


def mmd(n):
    x = (2*np.arange(1, n+1)-1)/(2*n)
    K = np.exp(-(x[:, None]-x[None, :])**2/(2*s*s))
    a = K.mean(); b = ek_point_unif(x).mean()
    return math.sqrt(max(a-2*b+EUU, 0))


fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
n0 = 5
x0 = (2*np.arange(1, n0+1)-1)/(2*n0)
for xi in x0:
    ax.plot([xi, xi], [0, 1/n0], color=GREEN, lw=1.5)
    dot(ax, xi, 1/n0, GREEN, ms=3.6)
for k in range(n0+1):
    ax.plot([k/n0, k/n0], [0, 1.15], color=STROKE, lw=.65, ls=DOT)
ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
lab(ax, .5, 1.04, '$U$', BLUE, ha='center')
lab(ax, .1, .25, '$1/n$', GREEN, ha='center')
ax.set_xlim(-.05, 1.05); ax.set_ylim(0, 1.25); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .2, 1])
axlab(ax, '$x$', None)
ax = axs[1]
ns = np.arange(1, 101)
M = np.array([mmd(int(k)) for k in ns])
ax.loglog(ns, np.ones_like(ns, dtype=float), color=PURPLE, lw=1.4)
ax.loglog(ns, 1/(4*ns), color=BLUE, lw=1.4)
ax.loglog(ns, M, color=YELLOW, lw=1.6)
lab(ax, 30, 1.25, r'$d_{\mathrm{TV}}$', PURPLE, ha='center')
lab(ax, 12, .028, r'$W_1=1/(4n)$', BLUE, ha='left')
lab(ax, 3.2, 4e-4, 'MMD', YELLOW, ha='left')
ax.minorticks_off(); ax.set_xlim(1, 100); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['$1$', '$10$', '$100$'])
ax.set_ylim(1e-6, 3); ax.set_yticks([1e-6, 1e-4, 1e-2, 1]); ax.set_yticklabels(['$10^{-6}$', '$10^{-4}$', '$10^{-2}$', '$1$'])
axlab(ax, '$n$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'mmd': {str(k): float(mmd(k)) for k in (1, 2, 5, 10, 20)}})
