from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: inspection example F (0.3 on [0,1), 0.9 on [1,2)), zoomed at the jump x=1.
# Thresholds 1+1/n (n=2..6) approach from the right: F=0.9=F(1). Thresholds 1-1/n approach from the left: F=0.3=F(1-).
fig, ax = figure(width_mm=86, height_mm=48)
style(ax)
ax.plot([.3, 1], [.3, .3], color=BLUE, lw=1.4)
ax.plot([1, 1.7], [.9, .9], color=BLUE, lw=1.4)
ax.plot([1], [.3], 'o', ms=3.6, mfc='white', mec=BLUE, mew=.9, zorder=4)
ax.plot([1], [.9], 'o', ms=3.6, color=BLUE, zorder=4)
n = np.arange(2, 7)
ax.plot(1+1/n, np.full(n.size, .9), 'o', ms=3.0, color=GREEN, zorder=5)
ax.plot(1-1/n, np.full(n.size, .3), 'o', ms=3.0, color=GREEN, zorder=5)
ax.annotate('', xy=(1.04, .96), xytext=(1.5, .96), arrowprops=dict(arrowstyle='->', color=LINE, lw=.85))
ax.annotate('', xy=(.96, .36), xytext=(.5, .36), arrowprops=dict(arrowstyle='->', color=LINE, lw=.85))
ax.text(1.27, 1.0, r'$x=1+1/n$', ha='center', va='bottom', fontsize=7.5)
ax.text(.73, .40, r'$x=1-1/n$', ha='center', va='bottom', fontsize=7.5)
ax.plot([1, 1], [.3, .9], color=RED, lw=2.0, zorder=3)
ax.text(1.04, .6, r'$p_X(1)=0.6$', color=RED, fontsize=7.5, va='center')
ax.set_xlim(.3, 1.7); ax.set_ylim(0, 1.12); ax.set_xticks([.5, 1, 1.5]); ax.set_yticks([0, .3, .9])
ax.set_ylabel('$F_X(x)$'); ax.set_xlabel('$x$')
save(fig, HERE(__file__), 'figure', {'left_limit': .3, 'value': .9, 'jump': .6})
