from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Sine coefficients and partial sums of the tent at t=0 and t=0.02.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.105, wspace=.36, bottom=.27)
ax = axes[0]; k = np.arange(1, 40, 2); cc = shades(3)
ax.loglog(k, np.abs(cs(k)), 'o', ms=3.2, color=RED, mew=0)
for t, c in zip((.002, .02), cc[1:]):
    ax.loglog(k, np.abs(cs(k))*np.exp(-(k*pi)**2*t), 'o-', ms=3, color=c, mew=0, lw=.9)
lab(ax, 8, 3e-2, '$t=0$', RED, ha='left'); lab(ax, 15, 1.5e-3, '$0.002$', cc[1], ha='left', va='top'); lab(ax, 1.7, 1e-5, '$0.02$', cc[2], ha='center')
ax.set_xlim(.8, 50); ax.set_ylim(1e-6, 1); ax.minorticks_off(); ax.set_xticks([1, 10]); ax.set_xticklabels(['1', '10']); ax.set_yticks([1, 1e-3, 1e-6]); ax.set_yticklabels(['1', '$10^{-3}$', '$10^{-6}$']); axlab(ax, '$k$', r'$| a_k(t)|$')
def S(t, N): return sum(cs(j)*np.exp(-(j*pi)**2*t)*np.sqrt(2)*np.sin(j*pi*X) for j in range(1, N+1, 2))
ax = axes[1]
ax.plot(X, tent(X), color=RED, lw=1.5); ax.plot(X, S(0, 1), color=GREEN, lw=1.2, ls=DASH); ax.plot(X, S(0, 3), color=GREEN, lw=1.2)
lab(ax, .5, .32, '$k\\leq 1$', GREEN, ha='center'); lab(ax, .84, .34, '$k\\leq 3$', GREEN, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .56); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax, yl='$u$')
ax = axes[2]
ax.plot(X, uD(X, .02), color=BLUE, lw=1.4); ax.plot(X, S(.02, 1), color=GREEN, lw=1.2, ls=DASH)
lab(ax, .5, .125, '$k\\leq 1$', GREEN, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .56); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'c1,3,5': [float(cs(j)) for j in (1, 3, 5)], 'S1(.5,.02)': float(S(.02, 1)[400]), 'exact': float(uD(.5, .02)[0])})
