from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
from types_exact import types, class_prob
# Exact distribution of the per-symbol self-information -(1/n) log2 p(X_{1:n}) for i.i.d. blocks from
# p = (0.4,0.3,0.2,0.1), n = 10 (yellow), 50 (purple), 250 (blue), by enumerating type classes. Masses are
# collected into bins of width 0.02 bit and drawn as step curves (mass per bit). Red line: H = 1.846;
# gray dotted: H +- 0.1.
bins = np.arange(.9, 3.4001, .02)
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, left=.1, right=.97, bottom=.2, top=.95)
facts = {}
for n, col, lw in ((10, YELLOW, 1.5), (50, PURPLE, 1.3), (250, BLUE, 1.4)):
    K, lc, si = types(n); pr = class_prob(lc, si)
    h, _ = np.histogram(si/n, bins=bins, weights=pr)
    ax.stairs(h/.02, bins, color=col, lw=lw)
    m = np.abs(si/n-H) < .1; facts['P_within_0.1_n%d' % n] = float(pr[m].sum())
    facts['sd_n%d' % n] = float(np.sqrt((pr*(si/n-H)**2).sum()))
ax.axvline(H, color=RED, lw=1.2)
for s in (-.1, .1):
    ax.axvline(H+s, color=STROKE, lw=.85, ls=DOT)
ax.set_xlim(1.2, 2.6); ax.set_ylim(0, None)
lab(ax, H-.015, ax.get_ylim()[1]*.92, r'$H$', RED, ha='right')
ymax = ax.get_ylim()[1]
lab(ax, 2.15, ymax*.15, r'$n=10$', YELLOW); lab(ax, 2.02, ymax*.36, r'$n=50$', PURPLE); lab(ax, 1.97, ymax*.75, r'$n=250$', BLUE)
ax.set_xlabel(r'$-\frac{1}{n}\log_2 p(X_{1:n})$', labelpad=1)
save(fig, HERE, 'figure', facts)
