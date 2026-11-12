"""Mutual information of equal-probability k x k bin labels.
(a) standard bivariate Gaussian rho = 0.5: I_k (blue dots) increasing to I = 0.144 (purple dashed);
(b) the same normalised, I_k / ln k;  (c) continuous parabola Y = X^2: I_k = ln(k/2) for even k (yellow), unbounded."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

K = np.arange(2, 33)
Ig = np.array([gauss_binned_mi(.5, int(k)) for k in K])
fig, axs = figure(width_mm=112, height_mm=40, ncols=3)
ax = axs[0]
ax.axhline(float(gauss_mi(.5)), color=PURPLE, lw=.9, ls='--')
ax.plot(K, Ig, 'o', color=BLUE, ms=2.2)
ax.set_ylim(0, .16); ax.set_xticks([2, 10, 20, 30]); ax.set_yticks([0, .05, .1, .144])
ax.set_xlabel('$k$', labelpad=0); ax.set_box_aspect(.85); tag(ax, '(a)', y=-.4)
gfmt(ax)
ax = axs[1]
ax.plot(K, Ig/np.log(K), 'o', color=BLUE, ms=2.2)
ax.set_ylim(0, .1); ax.set_xticks([2, 10, 20, 30]); ax.set_yticks([0, .05, .1])
ax.set_xlabel('$k$', labelpad=0); ax.set_box_aspect(.85); tag(ax, '(b)', y=-.4)
ax = axs[2]
Ke = K[K % 2 == 0]
ax.plot(Ke, np.log(Ke/2), 'o', color=YELLOW, ms=2.4)
kk = np.linspace(2, 32, 200); ax.plot(kk, np.log(kk/2), color=YELLOW, lw=.9)
ax.set_ylim(0, 3); ax.set_xticks([2, 10, 20, 30]); ax.set_yticks([0, 1, 2, 3])
ax.set_xlabel('$k$', labelpad=0); ax.set_box_aspect(.85); tag(ax, '(c)', y=-.4)
# check parabola formula numerically for k = 4, 8
x, w = grid_x(400000)
chk = {}
for k in (4, 8):
    ex = np.linspace(-1, 1, k+1); ey = (np.arange(k+1)/k)**2
    P = np.zeros((k, k))
    np.add.at(P, (np.clip(np.searchsorted(ex, x, 'right')-1, 0, k-1), np.clip(np.searchsorted(ey, x**2, 'right')-1, 0, k-1)), w)
    chk[str(k)] = [mi_table(P), math.log(k/2)]
save(fig, HERE, 'figure', {'gauss_Ik': dict(zip([int(k) for k in K], Ig.round(5).tolist())), 'parabola_check': chk})
