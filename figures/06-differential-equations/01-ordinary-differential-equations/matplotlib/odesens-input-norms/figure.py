from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：输入差的积分范数何时控制解的差。三种情形：短脉冲、高频振荡、平方依赖。
fig, axes = figure(width_mm=112, height_mm=62, ncols=3, nrows=2, sharex='col')
panel(fig, .085, .985, .97, .205, .36, .16)
ts = np.linspace(0, 2, 8001)
A, w_ = 5., .02
spike = lambda t: A if 1 <= t < 1+w_ else 0.
hf = lambda t: np.sin(40*t)
A2, w2 = 10., .01
sp2 = lambda t: A2 if 1 <= t < 1+w2 else 0.
# additive first two: x'=-x+g, error solves e'=-e+r
e1 = rk4(lambda t, e: -e+spike(t), 0., ts); e2 = rk4(lambda t, e: -e+hf(t), 0., ts); e3 = rk4(lambda t, e: sp2(t)**2, 0., ts)
axes[0, 0].plot(ts, [spike(t) for t in ts], color=RED, lw=1.1); axes[0, 1].plot(ts, hf(ts), color=RED, lw=.7); axes[0, 2].plot(ts, [sp2(t) for t in ts], color=RED, lw=1.1)
for ax, e in zip(axes[1], (e1, e2, e3)): ax.plot(ts, e, color=BLUE, lw=1.4)
axes[1, 0].set_ylim(-.01, .12); axes[1, 0].set_yticks([0, .1]); axes[1, 1].set_ylim(-.01, .06); axes[1, 1].set_yticks([0, .05]); axes[1, 2].set_ylim(0, 1.2); axes[1, 2].set_yticks([0, 1])
axes[0, 0].set_yticks([0, 5]); axes[0, 1].set_yticks([-1, 0, 1]); axes[0, 2].set_yticks([0, 10])
for ax in axes[1]: ax.set_xticks([0, 1, 2]); ax.set_xlim(0, 2); ax.set_xlabel('$t$', labelpad=0)
axes[0, 0].set_ylabel('$r(t)$', labelpad=1); axes[1, 0].set_ylabel('解的差', labelpad=1)
tags(fig, axes[1])
save(fig, HERE, 'figure', {'spike': [A, w_], 'hf': 'sin 40t', 'quad': [A2, w2], 'finals': [float(e1[-1]), float(np.max(np.abs(e2))), float(e3[-1])]})
