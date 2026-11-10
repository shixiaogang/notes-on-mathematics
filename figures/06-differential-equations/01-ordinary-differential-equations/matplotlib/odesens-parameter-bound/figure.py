from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：logistic 右端参数由 1 变为 1.2 时解的差与两种上界。L=1，残差 0.2*x(1-x)。
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
panel(fig, .085, .985, .955, .29, .24)
t = np.linspace(0, 3, 601); x = logistic(t, .25); y = logistic(t, .25, 1.2); dth = .2
ax = axes[0]; ax.plot(t, x, color=BLUE, lw=1.4); ax.plot(t, y, color=YELLOW, lw=1.4); ax.plot([0], [.25], 'o', ms=4.4, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(2.2, .7, r'$\theta=1$', color=BLUE, fontsize=7.5, va='top'); ax.text(1.3, .86, r'$\tilde\theta=1.2$', color=YELLOW, fontsize=7.5)
ax.set_xlim(0, 3); ax.set_ylim(0, 1); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
ax = axes[1]
crude = dth/4*(np.exp(t)-1)
r = dth*y*(1-y); dt = t[1]-t[0]
fine = np.array([np.trapezoid(np.exp(t[i]-t[:i+1])*r[:i+1], dx=dt) if i else 0 for i in range(len(t))])
ax.plot(t, crude, color=RED, lw=1.4); ax.plot(t, fine, color=PURPLE, lw=1.4); ax.plot(t, np.abs(y-x), color=BLUE, lw=1.4)
ax.text(2.0, .6, '上界一', color=RED, fontsize=7.5, ha='right'); ax.text(2.95, .3, '上界二', color=PURPLE, fontsize=7.5, ha='right'); ax.text(2.25, .115, '真实差', color=BLUE, fontsize=7.5, ha='left')
ax.set_xlim(0, 3); ax.set_ylim(0, .8); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .4, .8]); ax.set_xlabel('$t$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'theta': [1, 1.2], 'x0': .25, 'crude': 'dth/4 (e^t-1)', 'fine': 'int e^{t-s} dth y(1-y) ds', 'T3': [float(crude[-1]), float(fine[-1]), float(abs(y-x)[-1])]})
