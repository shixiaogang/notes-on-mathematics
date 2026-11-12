from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Reward table X and three affine images: X-2 (shift), 2X (scale), -X (reflection).
# Red tick: mean; purple bracket: mean +/- standard deviation.
rows = [('$X$', 1, 0), ('$X-2$', 1, -2), ('$2X$', 2, 0), ('$-X$', -1, 0)]
fig, axes = figure(width_mm=112, height_mm=62, nrows=4, sharex=True)
panel(fig, left=.11, right=.98, bottom=.12, top=.98, hspace=.25)
facts = {}
for ax, (name, a, b) in zip(axes, rows):
    xs = a*XV+b
    m, v, _, _ = moments(xs, PV); s = np.sqrt(v)
    ax.bar(xs, PV, width=.5, color=BLUE_FILL, edgecolor=BLUE, lw=.9)
    ax.plot([m, m], [0, .62], color=RED, lw=1.3)
    ax.annotate('', xy=(m-s, .58), xytext=(m+s, .58), arrowprops=dict(arrowstyle='<->', color=PURPLE, lw=.9, shrinkA=0, shrinkB=0))
    lab(ax, m+s+.3, .58, f'$\\sigma={s:.2f}$', PURPLE, ha='left', va='center')
    ax.set_ylim(0, .7); ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.text(-.02, .3, name, transform=ax.transAxes, ha='right', va='center', color=INK)
    facts[name] = [m, v]
axes[-1].set_xlim(-8, 13); axes[-1].set_xticks([-6, -3, 0, 3, 6, 12])
axlab(axes[-1], '$x$')
save(fig, HERE, 'figure', facts)
