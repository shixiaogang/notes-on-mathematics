from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
from math import comb
# Target: 5 items, 2 defective, draw 2 without replacement; X = number of defectives.
# p(k) = C(2,k)C(3,2-k)/C(5,2) = 0.3, 0.6, 0.1. Threshold x=1.5: F(1.5)=P(X<=1.5)=0.9.
p = [comb(2, k)*comb(3, 2-k)/comb(5, 2) for k in range(3)]
x0 = 1.5
fig, axs = figure(width_mm=104, height_mm=46, ncols=2)
ax = axs[0]; style(ax)
for k in range(3):
    inside = k <= x0
    ax.bar(k, p[k], width=.45, color=BLUE_FILL if inside else 'white', edgecolor=BLUE, linewidth=.9)
    ax.text(k, p[k]+.025, f'{p[k]:.1f}', ha='center', va='bottom', fontsize=7.5)
ax.axvline(x0, color=RED, lw=1.3)
ax.text(x0+.06, .66, '$x=1.5$', color=RED, fontsize=7.5, va='top')
ax.set_xlim(-.6, 2.6); ax.set_ylim(0, .72); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .3, .6])
ax.set_ylabel('$p_X(k)$')
sub(ax, 'a', '$k$')
ax = axs[1]; style(ax)
step_cdf(ax, [0, 1, 2], p, -1, 3)
ax.axvline(x0, color=RED, lw=1.3, zorder=1)
ax.plot([x0], [.9], 'o', ms=4.2, color=RED, zorder=5)
ax.set_xlim(-1, 3); ax.set_ylim(0, 1.08); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .3, .9, 1])
ax.set_ylabel('$F_X(x)$')
sub(ax, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'pmf': p, 'cdf': list(np.cumsum(p)), 'threshold': x0})
