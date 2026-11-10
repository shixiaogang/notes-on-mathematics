from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：Logistic 方程是 alpha=2 的 Bernoulli 方程，w=1/x 把解变为线性方程的指数曲线。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .26, .26)
a, b = axes
t = np.linspace(0, 5, 500)
for x0, c in [(.1, BLUE), (.3, YELLOW), (2., YELLOW)]:
    a.plot(t, x0*np.exp(t)/(1 - x0 + x0*np.exp(t)), color=c, lw=1.4, zorder=3)
    b.plot(t, 1 + (1/x0 - 1)*np.exp(-t), color=c, lw=1.4, zorder=3)
    dot(a, 0, x0); dot(b, 0, 1/x0)
a.axhline(1, color=BLUE, lw=1, zorder=2); b.axhline(1, color=BLUE, lw=1, zorder=2)
a.set_xlim(0, 5); a.set_ylim(0, 2.2); a.set_xticks(range(6)); a.set_yticks([0, 1, 2]); a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$x$', labelpad=1)
b.set_xlim(0, 5); b.set_ylim(0, 10.5); b.set_xticks(range(6)); b.set_yticks([0, 1, 5, 10]); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$w=1/x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'x0': [.1, .3, 2], 'w': 'w=1+(w0-1)e^-t'})
