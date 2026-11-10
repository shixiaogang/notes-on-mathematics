from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x'=x^2 的有限时间爆炸；爆炸时刻依赖初值；公式的另一支不属于同一个解。
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, .075, .985, .97, .25, .27)
a, b = axes
for x0, c in [(1, BLUE), (.5, YELLOW), (2, YELLOW)]:
    T = 1/x0
    t = np.linspace(-1.5, T - 1e-3, 600)
    a.plot(t, x0/(1 - x0*t), color=c, lw=1.4, zorder=3)
    a.axvline(T, color=RED, lw=.95, ls=(0, (4, 2)), zorder=2)
    dot(a, 0, x0)
a.set_xlim(-1.5, 2.8); a.set_ylim(0, 8); a.set_xticks([-1, 0, .5, 1, 2]); a.set_xticklabels(['$-1$', '0', '0.5', '1', '2']); a.set_yticks([0, 2, 4, 6, 8])
t1 = np.linspace(-1.5, 1 - 1e-3, 400); t2 = np.linspace(1 + 1e-3, 3, 400)
b.plot(t1, 1/(1 - t1), color=BLUE, lw=1.4, zorder=3)
b.plot(t2, 1/(1 - t2), color=YELLOW, lw=1.6, ls=(0, (4, 2)), zorder=3)
b.axvline(1, color=RED, lw=.95, ls=(0, (4, 2)), zorder=2)
dot(b, 0, 1)
b.axhline(0, color=GRID, lw=.65, zorder=0)
b.set_xlim(-1.5, 3); b.set_ylim(-6, 6); b.set_xticks([-1, 0, 1, 2, 3]); b.set_yticks([-6, -3, 0, 3, 6])
for ax in axes:
    ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "x'=x^2, x=x0/(1-x0 t)", 'x0': [1, .5, 2]})
