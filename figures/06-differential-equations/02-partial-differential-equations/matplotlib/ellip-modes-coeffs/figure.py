from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# f=1 on (0,1), Dirichlet: f_k and u_k, truncations.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.075, wspace=.34, bottom=.27, right=.985)
ks = np.arange(1, 40, 2)
fk = 2*np.sqrt(2)/(ks*np.pi); uk = fk/(ks*np.pi)**2
ax = axes[0]
ax.loglog(ks, fk, 'o', ms=3, color=YELLOW, mew=0); ax.loglog(ks, uk, 'o', ms=3, color=BLUE, mew=0)
lab(ax, 7, fk[3]*1.5, '$f_k$', YELLOW); lab(ax, 7, uk[3]/6, '$u_k$', BLUE, va='top')
ax.set_xlim(.8, 50); ax.set_ylim(1e-6, 2); ax.minorticks_off(); ax.set_xticks([1, 10]); ax.set_xticklabels(['1', '10']); ax.set_yticks([1e-5, 1e-3, 1e-1]); ax.set_yticklabels([r'$10^{-5}$', r'$10^{-3}$', r'$10^{-1}$']); hat01(ax, '$k$')
def sumf(N): return sum(fk[i]*np.sqrt(2)*np.sin(ks[i]*np.pi*X) for i in range(len(ks)) if ks[i] <= N)
def sumu(N): return sum(uk[i]*np.sqrt(2)*np.sin(ks[i]*np.pi*X) for i in range(len(ks)) if ks[i] <= N)
ax = axes[1]
ax.plot(X, 1+0*X, color=BLUE, lw=1.4); ax.plot(X, sumf(9), color=GREEN, lw=1.1)
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, 1.35); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); hat01(ax, yl='$f$')
ax = axes[2]
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4); ax.plot(X, sumu(1), color=GREEN, lw=1.1, ls=DASH)
lab(ax, .5, .05, r'$k\leq 1$', GREEN, ha='center')
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, .15); ax.set_xticks([0, 1]); ax.set_yticks([0, .125]); ax.set_yticklabels(['0', '1/8']); hat01(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'f_k': '2 sqrt2/(k pi), odd k', 'u_k': 'f_k/(k pi)^2', 'S1(1/2)': float(sumu(1)[500]), 'S3': float(sumu(3)[500]), 'S5': float(sumu(5)[500])})
print(sumu(1)[500], sumu(3)[500], sumu(5)[500])
