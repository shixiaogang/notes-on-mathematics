from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: space-time view of the two d'Alembert examples with characteristics.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2, sharey=True)
xs = np.linspace(-5, 5, 801); ts = np.linspace(0, 3.5, 561); X, TT = np.meshgrid(xs, ts)
ext = [xs[0], xs[-1], ts[0], ts[-1]]
for ax, Z, starts, l in zip(axs, [wave_tent(X, TT), wave_box(X, TT)], [[-1, 0, 1], [-1, 1]], 'ab'):
    style(ax); field(ax, Z, ext, vmax=1.)
    for s in starts:
        ax.plot([s, s+3.5], [0, 3.5], color=LINE, lw=1.0); ax.plot([s, s-3.5], [0, 3.5], color=LINE, lw=1.0)
        ax.plot([s], [0], 'o', ms=3.4, color=RED, clip_on=False, zorder=5)
    ax.set_xlim(-5, 5); ax.set_ylim(0, 3.5); ax.set_xticks([-4, -2, 0, 2, 4]); sub(ax, l, '$x$')
axs[0].set_ylabel('$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'c=1; tent and box solutions; characteristics x +- t = s'})
