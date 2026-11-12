from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: mass 1/5 on {1,2,3,4,5} versus on {1,2,3,4,12}. Median Q(1/2)=3 in both;
# the probability-weighted average sum x p(x) moves from 3 to 4.4.
fig, axs = figure(width_mm=108, height_mm=44, ncols=2, sharey=True)
for ax, vals, letter in [(axs[0], [1, 2, 3, 4, 5], 'a'), (axs[1], [1, 2, 3, 4, 12], 'b')]:
    style(ax)
    bars(ax, vals, [.2]*5, width=.5)
    avg = sum(vals)/5
    ax.axvline(3, color=RED, lw=1.3)
    ax.axvline(avg, color=PURPLE, lw=1.3, ls='--')
    ax.set_xlim(0, 13); ax.set_ylim(0, .3); ax.set_xticks(vals); ax.set_yticks([0, .2])
    if letter == 'a':
        ax.set_ylabel('$p(x)$')
    sub(ax, letter, '$x$')
save(fig, HERE(__file__), 'figure', {'median': 3, 'averages': [3.0, 4.4]})
