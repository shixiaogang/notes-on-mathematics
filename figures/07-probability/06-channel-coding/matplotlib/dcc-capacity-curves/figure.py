from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Capacity of BSC(p), C = 1 - h2(p) (blue), and of BEC(eps), C = 1 - eps (green), plotted against the corruption
# probability (flip probability p or erasure probability eps). Red dots at probability 0.1: 0.531 versus 0.9.
x = np.linspace(0, 1, 801)
fig, ax = figure(width_mm=90, height_mm=52)
panel(fig, left=.12, right=.97, top=.95, bottom=.18)
ax.plot(x, 1-h2(x), color=BLUE, lw=1.4); ax.plot(x, 1-x, color=GREEN, lw=1.4)
for y in (1-float(h2(.1)), .9): dot(ax, .1, y)
lab(ax, .13, 1-float(h2(.1))-.03, r'$0.531$', RED); lab(ax, .13, .91, r'$0.9$', RED)
lab(ax, .2, .34, r'BSC: $1-h_2(p)$', BLUE); lab(ax, .56, .5, r'BEC: $1-\varepsilon$', GREEN)
ax.set_xlim(0, 1); ax.set_ylim(0, 1.05); ax.set_xlabel(r'$p$ (BSC), $\varepsilon$ (BEC)', labelpad=1); ax.set_ylabel(r'$C$ / bit', labelpad=1)
save(fig, HERE, 'figure', {'bsc_0.1': 1-float(h2(.1)), 'bec_0.1': .9})
