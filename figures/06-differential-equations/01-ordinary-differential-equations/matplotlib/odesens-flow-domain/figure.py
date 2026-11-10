from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=x^2 的流映射 phi_t(x)=x/(1-t x)，定义域 {t x<1} 依赖时间。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .08, .985, .955, .28, .28)
ax = axes[0]; x = np.linspace(.21, 3, 600); t = 1/x
ax.fill_between(np.r_[-3, 0, x], 0, np.r_[5, 5, t], color=BLUE_FILL, lw=0); ax.plot(x, t, color=STROKE, lw=1.3)
ax.hlines(1, -3, 1, color=BLUE, lw=1.1); ax.plot([1], [1], 'o', ms=4.2, color=RED, mew=0, zorder=5)
ax.text(1.6, 1.0, '$t=1/x_0$', color=STROKE, fontsize=7.5); ax.text(-1.0, 1.1, '$D_{1}$', color=BLUE, fontsize=7.5, ha='center', va='bottom')
ax.set_xlim(-3, 3); ax.set_ylim(0, 3); ax.set_xticks([-3, -1, 1, 3]); ax.set_yticks([0, 1, 2, 3]); ax.set_xlabel('$x_0$', labelpad=0); ax.set_ylabel('$t$', labelpad=1)
ax = axes[1]
for tv, c in ((.5, YELLOW), (1., BLUE)):
    s = np.linspace(-3, 1/tv-.03, 800); ax.plot(s, s/(1-tv*s), color=c, lw=1.4); ax.axvline(1/tv, color=c, lw=.85, ls=(0, (2, 2)))
s = np.linspace(-3, 3, 10); ax.plot(s, s, color=MUTED, lw=.85)
ax.text(-1.5, -.1, '$t=1$', color=BLUE, fontsize=7.5, ha='center'); ax.text(.55, 2.8, '$t=0.5$', color=YELLOW, fontsize=7.5, ha='right'); ax.text(-1.2, -2.1, '$t=0$', color=MUTED, fontsize=7.5, ha='left')
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3.5); ax.set_xticks([-3, -1, 1, 2]); ax.set_yticks([-2, 0, 2]); ax.set_xlabel('$x_0$', labelpad=0); ax.set_ylabel('$\\varphi_t(x_0)$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'flow': 'x/(1-t x)'})
