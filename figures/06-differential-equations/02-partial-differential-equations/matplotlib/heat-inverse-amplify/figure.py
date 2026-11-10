from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Amplification of backward recovery; two very different initial data with nearly equal final data.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.115, wspace=.37, bottom=.27)
ax = axes[0]; k = np.arange(1, 9); cc = shades(3)
for T, c in zip((.01, .05, .1), cc): ax.semilogy(k, np.exp((k*pi)**2*T), 'o-', ms=3, color=c, mew=0, lw=1)
lab(ax, 5.2, 1e16, '$T=0.1$', cc[2], ha='right'); lab(ax, 6.6, 1.5e7, '$0.05$', cc[1], ha='left', va='top'); lab(ax, 8.2, 1e4, '$0.01$', cc[0], ha='right')
ax.set_xlim(.7, 8.3); ax.set_ylim(.5, 1e20); ax.minorticks_off(); ax.set_xticks([1, 4, 8]); ax.set_yticks([1, 1e8, 1e16]); ax.set_yticklabels(['1', '$10^{8}$', '$10^{16}$']); axlab(ax, '$k$', r'$\mathrm{e}^{\lambda_k T}$')
ax = axes[1]; p = lambda x: np.sin(11*pi*x)*.12; 
ax.plot(X, tent(X), color=BLUE, lw=1.4); ax.plot(X, tent(X)+p(X), color=YELLOW, lw=1.1)
ax.set_xlim(0, 1); ax.set_ylim(-.06, .66); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax, yl='$u_0$')
ax = axes[2]; T = .05
ax.plot(X, uD(X, T), color=BLUE, lw=1.6); ax.plot(X, uD(X, T)+.12*np.exp(-(11*pi)**2*T)*np.sin(11*pi*X), color=YELLOW, lw=1.1, ls=DASH)
ax.set_xlim(0, 1); ax.set_ylim(-.06, .66); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax, yl='$u(x,T)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'max diff at T': float(.12*np.exp(-(11*pi)**2*T)), 'amp k=1,3,5,T=.05': [float(np.exp((j*pi)**2*T)) for j in (1, 3, 5)]})
