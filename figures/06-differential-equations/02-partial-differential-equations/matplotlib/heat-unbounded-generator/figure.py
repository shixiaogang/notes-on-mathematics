from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# 1-exp(-lambda_k t) does not vanish uniformly in k; discrete Laplacian eigenvalues grow without bound.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; k = np.arange(1, 400); cc = shades(3)
for t, c in zip((1e-2, 1e-3, 1e-4), cc[::-1]): ax.semilogx(k, 1-np.exp(-(k*pi)**2*t), color=c, lw=1.4)
lab(ax, 1.2, .78, '$t=10^{-2}$', cc[2], ha='left'); lab(ax, 60, .3, '$t=10^{-4}$', cc[0], ha='left')
ax.set_xlim(1, 400); ax.set_ylim(0, 1.05); ax.minorticks_off(); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['1', '10', '100']); ax.set_yticks([0, 1]); axlab(ax, '$k$', r'$1-\mathrm{e}^{-\lambda_k t}$')
ax = axes[1]
kc = np.arange(1, 81)
ax.loglog(kc, (kc*pi)**2, color=BLUE, lw=1.4)
for N, c in zip((9, 19, 79), (YELLOW, PURPLE, GREEN)):
    h = 1/(N+1); j = np.arange(1, N+1); ax.loglog(j, 4/h**2*np.sin(j*pi*h/2)**2, 'o', ms=2.4, color=c, mew=0)
    lab(ax, N*1.1, 4/h**2*.72, f'$N={N}$', c, ha='left', fontsize=7.5)
ax.set_xlim(.9, 250); ax.set_ylim(5, 2e5); ax.minorticks_off(); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['1', '10', '100']); ax.set_yticks([10, 1e3, 1e5]); ax.set_yticklabels(['10', '$10^3$', '$10^5$']); axlab(ax, '$k$', '特征值')
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': '4/h^2 sin^2(k pi h/2)'})
