from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：有限时间指数上界 eps*exp(L t) 与真实距离的比较。半对数坐标，解析解。
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
panel(fig, .115, .985, .955, .27, .3)
t = np.linspace(0, 6, 601); eps = .01
true = (eps*np.exp(t), eps*np.exp(-t), logistic(t, .26)-logistic(t, .25))
for ax, d in zip(axes, true):
    ax.semilogy(t, eps*np.exp(t), color=RED, lw=1.4); ax.semilogy(t, np.abs(d), color=BLUE, lw=1.4, ls=(0, (4, 1.5)) if ax is axes[0] else '-')
    ax.set_xlim(0, 6); ax.set_ylim(1e-5, 10); ax.set_xticks([0, 3, 6]); ax.set_xlabel('$t$', labelpad=0); ax.set_yticks([1e-4, 1e-2, 1])
axes[0].set_ylabel('$|y-x|$', labelpad=1); axes[1].set_yticklabels([]); axes[2].set_yticklabels([])
axes[1].text(2.1, .8, '上界', color=RED, fontsize=7.5); axes[1].text(2.9, 2e-3, '真实', color=BLUE, fontsize=7.5, va='top')
tags(fig, axes)
save(fig, HERE, 'figure', {'eps': eps, 'L': 1, 'cases': ["x'=x", "x'=-x", "x'=x(1-x), x0=.25"]})
