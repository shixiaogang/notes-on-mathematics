from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x'=2t/(1+e^x), x(0)=0 的隐式解 x+e^x-1=t^2：严格单调的 B 使 x 由 t 唯一解出。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .085, .985, .96, .26, .27)
a, b = axes
B_ = lambda x: x + np.exp(x) - 1
def inv(y):
    lo, hi = -20., 10.
    for _ in range(200):
        m = (lo + hi)/2
        if B_(m) < y: lo = m
        else: hi = m
    return (lo + hi)/2
x = np.linspace(-2, 1.4, 400)
a.plot(x, B_(x), color=BLUE, lw=1.4, zorder=3)
x1 = inv(1.); print('x(1)=', x1)
a.plot([-2, x1], [1, 1], color=PURPLE, lw=.95, ls=(0, (4, 2)), zorder=2)
a.plot([x1, x1], [-3, 1], color=PURPLE, lw=.95, ls=(0, (4, 2)), zorder=2)
a.plot([x1], [1], 'o', ms=3.6, color=PURPLE, mew=0, zorder=5)
a.set_xlim(-2, 1.4); a.set_ylim(-3, 4); a.set_xticks([-2, -1, 0, x1, 1]); a.set_xticklabels(['$-2$', '$-1$', '0', '0.443', '1'])
a.set_yticks([-2, 0, 1, 2, 4]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$B(x)$', labelpad=1)
t = np.linspace(-2, 2, 301); xs = np.array([inv(s**2) for s in t])
b.plot(t, xs, color=BLUE, lw=1.4, zorder=3); dot(b, 0, 0)
b.plot([1], [x1], 'o', ms=3.6, color=PURPLE, mew=0, zorder=5)
b.set_xlim(-2, 2); b.set_ylim(-.15, 1.5); b.set_xticks([-2, -1, 0, 1, 2]); b.set_yticks([0, .5, 1, 1.5]); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'B': 'x+e^x-1', 'x_at_t1': x1})
