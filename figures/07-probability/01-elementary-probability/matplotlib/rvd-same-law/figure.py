from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: fair die, X(w)=w and Y(w)=7-w. Pointwise the two records never agree, yet both mass tables are 1/6 on {1,...,6}.
fig, axs = figure(width_mm=104, height_mm=44, ncols=2)
w = np.arange(1, 7)
ax = axs[0]; style(ax)
for k in w:
    ax.plot([k, k], [k, 7-k], color=LINE, lw=.85, zorder=1)
ax.plot(w, w, 'o', ms=4.2, color=BLUE, zorder=3, label='$X$')
ax.plot(w, 7-w, 's', ms=4.2, mfc=YELLOW_FILL, mec=YELLOW, mew=1.1, zorder=3, label='$Y$')
ax.set_xticks(w); ax.set_yticks(w); ax.set_xlim(.4, 6.6); ax.set_ylim(.4, 6.8)
ax.set_ylabel('取值')
ax.legend(loc='upper center', ncols=2, handletextpad=.3, columnspacing=1.2, borderaxespad=0, bbox_to_anchor=(.5, 1.08))
sub(ax, 'a', r'$\omega$')
ax = axs[1]; style(ax)
bars(ax, w-.15, np.full(6, 1/6), width=.28)
ax.bar(w+.15, np.full(6, 1/6), width=.28, color=YELLOW_FILL, edgecolor=YELLOW, linewidth=.9)
ax.set_xticks(w); ax.set_ylim(0, .25); ax.set_yticks([1/6]); ax.set_yticklabels(['1/6'])
ax.set_ylabel('概率')
sub(ax, 'b', '取值')
save(fig, HERE(__file__), 'figure', {'X': w.tolist(), 'Y': (7-w).tolist(), 'mass': '1/6 each'})
