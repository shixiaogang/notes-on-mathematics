from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：分段常值输入下的解在切换点有折角；左右导数不同。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .09, .985, .96, .27, .26)
a, b = axes
a.plot([0, 1], [1, 1], color=STROKE, lw=1.4); a.plot([1, 3], [0, 0], color=STROKE, lw=1.4)
hollow(a, 1, 1); a.plot([1], [0], 'o', ms=4.2, color=STROKE, mew=0, zorder=6)
a.set_xlim(0, 3); a.set_ylim(-.15, 1.25); a.set_xticks([0, 1, 2, 3]); a.set_yticks([0, 1]); a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$g$', labelpad=1)
t1 = np.linspace(0, 1, 200); t2 = np.linspace(1, 3, 300); x1 = 1 - np.exp(-1)
b.plot(t1, 1 - np.exp(-t1), color=BLUE, lw=1.4, zorder=3); b.plot(t2, x1*np.exp(-(t2 - 1)), color=BLUE, lw=1.4, zorder=3)
dot(b, 0, 0); b.plot([1], [x1], 'o', ms=3.6, color=BLUE, mew=0, zorder=6)
d = .45
b.plot([1 - d, 1], [x1 - d*np.exp(-1), x1], color=PURPLE, lw=1.1, zorder=4)
b.plot([1, 1 + d], [x1, x1 - d*x1], color=PURPLE, lw=1.1, zorder=4)
b.plot([1, 1 + d], [x1, x1 + d*np.exp(-1)], color=PURPLE, lw=.9, ls=(0, (3, 2)), zorder=4)
b.plot([1 - d, 1], [x1 + d*x1, x1], color=PURPLE, lw=.9, ls=(0, (3, 2)), zorder=4)
b.set_xlim(0, 3); b.set_ylim(-.05, .95); b.set_xticks([0, 1, 2, 3]); b.set_yticks([0, x1]); b.set_yticklabels(['0', '0.632']); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "x'=-x+g, g=1 on [0,1), 0 after", 'left_right_slopes': [float(np.exp(-1)), float(-x1)]})
