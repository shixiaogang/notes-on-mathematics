from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: density 1/2 on [0,1] and on [2,3] (zero in the gap). F is flat at 1/2 on [1,2];
# every m in [1,2] splits the mass in half, the quantile convention picks Q(1/2)=1.
fig, axs = figure(width_mm=104, height_mm=46, ncols=2)
ax = axs[0]; style(ax)
for a in (0, 2):
    ax.fill_between([a, a+1], 0, .5, color=BLUE_FILL, lw=0)
    ax.plot([a, a+1], [.5, .5], color=BLUE, lw=1.4)
    ax.plot([a, a], [0, .5], color=BLUE, lw=.85, ls=':'); ax.plot([a+1, a+1], [0, .5], color=BLUE, lw=.85, ls=':')
ax.plot([-.5, 0], [0, 0], color=BLUE, lw=1.4); ax.plot([1, 2], [0, 0], color=BLUE, lw=1.4); ax.plot([3, 3.5], [0, 0], color=BLUE, lw=1.4)
ax.set_xlim(-.5, 3.5); ax.set_ylim(0, .8); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .5])
ax.set_ylabel('$f(x)$')
sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
x = np.linspace(-.5, 3.5, 801)
F = np.clip(np.where(x < 1, x/2, np.where(x < 2, .5, (x-1)/2)), 0, 1)
ax.plot(x, F, color=BLUE, lw=1.4)
ax.plot([1, 2], [.5, .5], color=YELLOW, lw=2.6, zorder=3)
ax.plot([-.5, 1], [.5, .5], color=RED, lw=1.0, ls='--')
ax.plot([1, 2], [0, 0], color=RED, lw=2.4, clip_on=False, zorder=5)
ax.plot([1], [.5], 'o', ms=3.8, color=RED, zorder=6)
ax.set_xlim(-.5, 3.5); ax.set_ylim(0, 1.08); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .5, 1])
ax.set_ylabel('$F(x)$')
sub(ax, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'median_set': [1, 2], 'Q(1/2)': 1})
