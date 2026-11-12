from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
from matplotlib.patches import Rectangle
# Signed cancellation W_n = n 1{U < 1/(2n)} - n 1{1/(2n) <= U < 1/n} on U ~ Unif(0,1):
# positive block area 1/2 (blue fill), negative block area 1/2 (red fill), so E W_n = 0 while E|W_n| = 1.
# (a) n = 2, (b) n = 4.
fig, axes = figure(width_mm=100, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.28, bottom=.33)
for ax, n in ((axes[0], 2), (axes[1], 4)):
    style(ax)
    ax.add_patch(Rectangle((0, 0), 1/(2*n), n, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    ax.add_patch(Rectangle((1/(2*n), -n), 1/(2*n), n, facecolor=RED_FILL, edgecolor=RED, lw=1.1))
    ax.axhline(0, color=LINE, lw=.85)
    lab(ax, 1/(4*n), n/2, r'$+\frac{1}{2}$', BLUE, ha='center', va='center')
    lab(ax, 3/(4*n), -n/2, r'$-\frac{1}{2}$', RED, ha='center', va='center')
    ax.set_xlim(0, .6); ax.set_ylim(-4.6, 4.6); tk = sorted({0, 1/(2*n), 1/n, .5}); ax.set_xticks(tk)
    ax.set_xticklabels(['$0$' if v == 0 else r'$\frac{1}{%d}$' % round(1/v) for v in tk])
    ax.set_yticks([-4, -2, 0, 2, 4])
    axlab(ax, '$U$', '$W_%d$' % n)
tags(fig, axes)
save(fig, HERE, 'figure', {'E_W_n': 0, 'E_abs_W_n': 1})
