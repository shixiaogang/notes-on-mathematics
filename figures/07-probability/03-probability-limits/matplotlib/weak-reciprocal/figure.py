from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# (a) P(1/U_n > y) = (ceil(n/y)-1)/n for the lattice uniform, n=5,20, vs limit 1/y (y>=1).
# (b) X_n ~ N(0,1/n^2): P(|1/X_n| <= y) = P(|Z| >= n/y) = 2(1-Phi(n/y)), n=1,4,16.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; y = np.linspace(1, 10, 3000)
for n, c, lw in ((5, YELLOW, 1.5), (20, GREEN, 1.2)): ax.plot(y, (np.ceil(n/y)-1)/n, color=c, lw=lw)
ax.plot(y, 1/y, color=BLUE, lw=1.4)
lab(ax, 3.1, .5, r'$1/y$', BLUE); lab(ax, 6.5, .25, r'$n=5$', YELLOW)
ax.set_xlim(1, 10); ax.set_ylim(0, 1.05); ax.set_xticks([1, 4, 7, 10]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$y$')
ax = axes[1]; y = np.linspace(1e-3, 60, 2000)
for n, c in ((1, BLUE), (4, GREEN), (16, YELLOW)): ax.plot(y, 2*(1-Phi(n/y)), color=c, lw=1.4)
lab(ax, 4, .82, r'$n=1$', BLUE); lab(ax, 45, .5, r'$n=16$', YELLOW, ha='center')
ax.set_xlim(0, 60); ax.set_ylim(0, 1.05); ax.set_xticks([0, 20, 40, 60]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'tail_limit': '1/y'})
