from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：积分形式：状态增量等于沿解的速度曲线下面积；试探曲线不满足积分方程。
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
panel(fig, .095, .985, .96, .27, .42)
a, b, c = axes
x = lambda t: np.exp(t)/(9 + np.exp(t))
t = np.linspace(0, 4.5, 500); T = np.log(9)
a.plot(t, x(t)*(1 - x(t)), color=BLUE, lw=1.4, zorder=3)
tf = t[t <= T]; a.fill_between(tf, 0, x(tf)*(1 - x(tf)), color=BLUE_FILL, lw=0, zorder=1)
a.axvline(T, color=STROKE, lw=.85, ls=(0, (3, 2)), zorder=2)
a.set_xlim(0, 4.5); a.set_ylim(0, .3); a.set_xticks([0, T, 4]); a.set_xticklabels(['0', '$\\ln 9$', '4']); a.set_yticks([0, .1, .2, .3]); a.set_xlabel('$s$', labelpad=1); a.set_ylabel('$x(1-x)$', labelpad=1)
b.plot(t, x(t), color=BLUE, lw=1.4, zorder=3); dot(b, 0, .1)
b.plot([T, T], [.1, .5], color=STROKE, lw=1.1, zorder=2); b.plot([0, T], [.1, .1], color=STROKE, lw=.85, ls=(0, (3, 2)), zorder=2)
b.text(T + .12, .3, '0.4', fontsize=7.5, va='center')
b.plot([T], [.5], 'o', ms=3.4, color=BLUE, mew=0, zorder=5)
b.set_xlim(0, 4.5); b.set_ylim(0, 1); b.set_xticks([0, T, 4]); b.set_xticklabels(['0', '$\\ln 9$', '4']); b.set_yticks([0, .1, .5, 1]); b.set_yticklabels(['0', '0.1', '0.5', '1']); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=1)
t = np.linspace(0, 1, 200)
c.plot(t, np.exp(t), color=BLUE, lw=1.4, zorder=3); c.plot(t, 1 + t, color=YELLOW, lw=1.6, zorder=3)
c.plot(t, 1 + t + t**2/2, color=RED, lw=1.2, ls=(0, (4, 2)), zorder=3); dot(c, 0, 1)
c.set_xlim(0, 1.05); c.set_ylim(.9, 2.85); c.set_xticks([0, .5, 1]); c.set_xticklabels(['0', '0.5', '1']); c.set_yticks([1, 2, 2.72]); c.set_yticklabels(['1', '2', '2.72']); c.set_xlabel('$t$', labelpad=1); c.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'area': 'int_0^ln9 x(1-x) ds=0.4', 'trial': '1+t, image 1+t+t^2/2, exact e^t'})
