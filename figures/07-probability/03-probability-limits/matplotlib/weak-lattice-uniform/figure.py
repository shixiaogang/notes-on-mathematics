from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Lattice uniform U_n on {1/n,...,1} -> Unif(0,1). Test function f(x)=min(x^2,1).
# (a) n=5 right-endpoint Riemann bars, sum = E f(U_5) = 0.44 ; (b) E f(U_n)=(n+1)(2n+1)/(6n^2) -> 1/3.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; n = 5; k = np.arange(1, n+1)
ax.bar((k-1)/n, (k/n)**2, width=1/n, align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.7)
x = np.linspace(0, 1, 300); ax.plot(x, x**2, color=BLUE, lw=1.4)
for kk in k: dot(ax, kk/n, (kk/n)**2, GREEN, ms=3.4)
ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.08); ax.set_xticks([0, .2, .4, .6, .8, 1]); ax.set_yticks([0, .5, 1])
lab(ax, .08, .9, r'$f(x)=x^2$', BLUE)
axlab(ax, r'$x$')
ax = axes[1]; ns = np.arange(3, 51); vals = (ns+1)*(2*ns+1)/(6*ns**2)
ax.plot(ns, vals, 'o', ms=2.6, color=GREEN, mew=0)
ax.axhline(1/3, color=BLUE, lw=1.0, ls=DASH)
for m in (5, 10, 50): dot(ax, m, (m+1)*(2*m+1)/(6*m*m), RED, ms=3.6)
lab(ax, 5+1.5, .44+.01, '$0.44$', RED, va='bottom'); lab(ax, 11.5, .385+.008, '$0.385$', RED, va='bottom')
lab(ax, 49, 1/3-.012, '$1/3$', BLUE, ha='right', va='top')
ax.set_xlim(0, 52); ax.set_ylim(.3, .62); ax.set_xticks([3, 10, 20, 30, 40, 50]); ax.set_yticks([.3, .4, .5, .6])
axlab(ax, r'$n$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E_f_U_n': {int(m): float((m+1)*(2*m+1)/(6*m*m)) for m in (5, 10, 50)}, 'limit': 1/3})
