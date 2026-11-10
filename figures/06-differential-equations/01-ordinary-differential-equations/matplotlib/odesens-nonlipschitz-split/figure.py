from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=2 sqrt|x| 在 x=0 处不 Lipschitz，同一初值有一族解，Gronwall 结论失效。
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
panel(fig, .085, .985, .955, .29, .24)
ax = axes[0]; x = np.linspace(-1, 1, 801); ax.plot(x, 2*np.sqrt(np.abs(x)), color=BLUE, lw=1.4)
ax.plot(x, 4*np.abs(x), color=PURPLE, lw=.85, ls=(0, (3, 2)))
ax.text(.55, .8, '$2\\sqrt{|x|}$', color=BLUE, fontsize=7.5, ha='left', va='top'); ax.text(.46, 2.25, '$L|x|$', color=PURPLE, fontsize=7.5, ha='right')
ax.set_xlim(-1, 1); ax.set_ylim(0, 2.6); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; t = np.linspace(0, 2, 401)
ax.plot(t, 0*t, color=BLUE, lw=1.4)
for c, col in ((0, BLUE), (.5, YELLOW), (1, PURPLE)):
    ax.plot(t, np.where(t > c, (t-c)**2, 0), color=col, lw=1.4)
ax.plot([0], [0], 'o', ms=4.4, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(1.32, 3.2, '$c=0$', color=BLUE, fontsize=7.5, ha='right'); ax.text(1.46, 1.25, '$c=0.5$', color=YELLOW, fontsize=7.5, ha='center'); ax.text(1.75, .92, '$c=1$', color=PURPLE, fontsize=7.5, ha='center')
ax.set_xlim(0, 2); ax.set_ylim(0, 4); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 2, 4]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '2 sqrt|x|', 'solutions': 'x=(t-c)^2 for t>c, 0 otherwise'})
