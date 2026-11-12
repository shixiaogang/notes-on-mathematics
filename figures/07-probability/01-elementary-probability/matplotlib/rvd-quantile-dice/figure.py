from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: fair die. F has jumps at 1..6 and flats between; Q(p)=inf{x: F(x)>=p}=ceil(6p).
# p=0.4 falls inside the jump at 3 (F(3-)=1/3<0.4<=F(3)=1/2); p=1/2 hits the flat [3,4): Q(1/2)=3.
fig, axs = figure(width_mm=108, height_mm=48, ncols=2)
ax = axs[0]; style(ax)
step_cdf(ax, range(1, 7), [1/6]*6, 0, 7)
ax.plot([0, 3], [.4, .4], color=RED, lw=1.0, ls='--'); ax.plot([3], [.4], 'o', ms=3.6, color=RED, zorder=6)
ax.plot([3, 4], [.5, .5], color=YELLOW, lw=2.6, zorder=2, solid_capstyle='butt')
ax.plot([3, 3], [1/3, .5], color=RED, lw=2.0, zorder=3)
ax.text(.2, .43, '$p=0.4$', color=RED, fontsize=7.5)
ax.set_xlim(0, 7); ax.set_ylim(0, 1.08); ax.set_xticks(range(1, 7))
ax.set_yticks([0, 1/3, .5, 1]); ax.set_yticklabels(['0', '1/3', '1/2', '1'])
ax.set_ylabel('$F(x)$')
sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
for k in range(1, 7):
    a, b = (k-1)/6, k/6
    ax.plot([a, b], [k, k], color=BLUE, lw=1.4, solid_capstyle='butt')
    ax.plot([a], [k], 'o', ms=3.2, mfc='white', mec=BLUE, mew=.9, zorder=4)
    ax.plot([b], [k], 'o', ms=3.2, color=BLUE, zorder=4)
ax.plot([1/2, 1/2], [3, 4], color=YELLOW, lw=2.6, zorder=2)
ax.plot([.4], [3], 'o', ms=3.6, color=RED, zorder=6)
ax.plot([1/3, 1/2], [3, 3], color=RED, lw=2.0, zorder=3, solid_capstyle='butt')
ax.set_xlim(0, 1.04); ax.set_ylim(0, 6.6); ax.set_yticks(range(1, 7))
ax.set_xticks([0, 1/3, 1/2, 1]); ax.set_xticklabels(['0', '1/3', '1/2', '1'])
ax.set_ylabel('$Q(p)$')
sub(ax, 'b', '$p$')
save(fig, HERE(__file__), 'figure', {'Q(0.4)': 3, 'Q(0.5)': 3, 'rule': 'Q(p)=ceil(6p)'})
