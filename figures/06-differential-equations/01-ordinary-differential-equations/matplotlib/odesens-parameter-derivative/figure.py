from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=theta x(1-x)，x0=1/4，theta=1；参数导数 P=t x(1-x)，变分方程 RK4 与有限差分对照。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .08, .985, .955, .28, .28)
ts = np.linspace(0, 5, 1001); dt = .2
def F(t, z):
    x, P = z; return np.array([x*(1-x), (1-2*x)*P+x*(1-x)])
Z = rk4(F, [.25, 0.], ts); x, P = Z[:, 0], Z[:, 1]
y = logistic(ts, .25, 1+dt)
ax = axes[0]; ax.plot(ts, x, color=BLUE, lw=1.4); ax.plot(ts, y, color=YELLOW, lw=1.4); ax.plot(ts, x+dt*P, color=GREEN, lw=1.4, ls=(0, (4, 2)))
ax.text(1.6, .9, '$\\theta=1.2$', color=YELLOW, fontsize=7.5, ha='right'); ax.text(1.75, .45, '$\\theta=1$', color=BLUE, fontsize=7.5, ha='left'); ax.text(3.1, 1.02, '$x+0.2P$', color=GREEN, fontsize=7.5)
ax.set_xlim(0, 5); ax.set_ylim(0, 1.15); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
ax = axes[1]; ax.plot(ts, P, color=BLUE, lw=1.4)
fd = (logistic(ts, .25, 1+1e-5)-logistic(ts, .25, 1-1e-5))/2e-5
idx = np.arange(0, len(ts), 50); ax.plot(ts[idx], fd[idx], 'o', ms=3, color=GREEN, mew=0, zorder=4)
ax.plot([np.log(3)], [np.log(3)/4], 'o', ms=4.4, color=RED, mew=0, zorder=5); ax.text(1.32, .2, '$(\\ln 3,\\ 0.275)$', color=RED, fontsize=7.5)
ax.set_xlim(0, 5); ax.set_ylim(0, .42); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, .2, .4]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$P$', labelpad=1)
tags(fig, axes)
i = np.argmin(abs(ts-np.log(3))); print('P(ln3)', P[i], np.log(3)/4)
save(fig, HERE, 'figure', {'x0': .25, 'theta': 1, 'exact': 'P=t x(1-x)'})
