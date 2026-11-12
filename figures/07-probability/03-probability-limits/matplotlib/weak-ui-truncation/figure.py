from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# (a) X_n = n w.p. 1/n: E X_n = 1, E h_5(X_n) = min(n,5)/n -> 0. (b) Bin(n,2/n): E X_n^2 = 6-4/n -> 6;
# tail E[X_n^2 1{X_n^2>25}] computed exactly from the pmf.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; ns = np.arange(1, 41)
ax.plot(ns, np.ones_like(ns, dtype=float), 'o', ms=2.6, color=RED, mew=0)
ax.plot(ns, np.minimum(ns, 5)/ns, 'o', ms=2.6, color=GREEN, mew=0)
ax.axhline(0, color=BLUE, lw=1.0, ls=DASH)
lab(ax, 39, 1.04, r'$\mathrm{E}[X_n]$', RED, ha='right', va='bottom'); lab(ax, 12, .5, r'$\mathrm{E}[h_5(X_n)]$', GREEN)
ax.set_xlim(0, 41); ax.set_ylim(-.05, 1.2); ax.set_xticks([1, 10, 20, 30, 40]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$n$')
ax = axes[1]; ns = np.arange(3, 61); m2 = []; tl = []
for n in ns:
    p = binom_pmf(int(n), 2/n); k = np.arange(n+1); m2.append(float((p*k**2).sum())); tl.append(float((p*k**2*(k > 5)).sum()))
m2 = np.array(m2); tl = np.array(tl); assert np.allclose(m2, 6-4/ns)
ax.plot(ns, m2, 'o', ms=2.6, color=GREEN, mew=0); ax.plot(ns, tl, 'o', ms=2.6, color=RED, mew=0)
ax.axhline(6, color=BLUE, lw=1.0, ls=DASH)
lab(ax, 58, 6.15, r'$6$', BLUE, ha='right', va='bottom'); lab(ax, 30, 4.4, r'$\mathrm{E}[X_n^2]$', GREEN); lab(ax, 30, 1.1, '尾部积分', RED)
ax.set_xlim(0, 62); ax.set_ylim(0, 7); ax.set_xticks([3, 20, 40, 60]); ax.set_yticks([0, 2, 4, 6])
axlab(ax, r'$n$')
tags(fig, axes)
save(fig, HERE, 'figure', {'max_tail_integral': float(tl.max())})
