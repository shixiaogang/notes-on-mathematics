from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Fair coin, eps = 0.05: exact P(|Xbar_n - 1/2| >= 0.05) from Bin(n,1/2) (blue) against the Chebyshev bound
# (1/4)/(n eps^2) = 100/n (purple), n = 10..5000 on log-log axes. Red dots at n = 400.
eps = .05
ns = np.unique(np.round(np.logspace(1, np.log10(5000), 160)).astype(int))
ex = []
for n in ns:
    pm = binpmf(n); K = np.arange(n+1)
    ex.append(pm[np.abs(K-n/2) >= eps*n-1e-9].sum())
ex = np.array(ex)
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
ax.plot(ns, np.minimum(1, .25/(ns*eps**2)), color=PURPLE, lw=1.4)
ax.plot(ns, ex, color=BLUE, lw=1.4)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(10, 5000); ax.set_ylim(1e-12, 2)
logticks(ax, [-12, -9, -6, -3, 0]); logticks(ax, [1, 2, 3], 'x')
pm = binpmf(400); K = np.arange(401); e400 = pm[np.abs(K-200) >= 20-1e-9].sum()
dot(ax, 400, e400); dot(ax, 400, .25)
lab(ax, 360, .25*3, r'$0.25$', RED, ha='right'); lab(ax, 450, e400/6, r'$0.051$', RED)
lab(ax, 1200, .25, r'$\frac{1}{4n\varepsilon^2}$', PURPLE)
lab(ax, 900, 1e-7, '精确值', BLUE)
axlab(ax, '$n$')
save(fig, HERE, 'figure', {'eps': eps, 'exact_400': float(e400), 'exact_1000': float(ex[np.argmin(abs(ns-1000))]),
     'exact_100': float(ex[np.argmin(abs(ns-100))])})
