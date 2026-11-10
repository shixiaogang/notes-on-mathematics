from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：自治方程的解平移后仍是解；非自治方程不然。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .26, .26)
a, b = axes
tau = 1.5
t = np.linspace(0, 6, 500)
sol = lambda t: np.exp(t)/(9 + np.exp(t))
a.set_xlim(0, 6); a.set_ylim(0, 1.15); a.set_xticks([0, 2, 4, 6]); a.set_yticks([0, .5, 1])
b.set_xlim(0, 6); b.set_ylim(-1.5, 1.5); b.set_xticks([0, 2, 4, 6]); b.set_yticks([-1, 0, 1])
for ax in axes:
    ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
slope_field(a, lambda s, x: x*(1 - x), nt=15, nx=8)
slope_field(b, lambda s, x: np.cos(s), nt=15, nx=8)
a.plot(t, sol(t), color=BLUE, lw=1.4, zorder=3); a.plot(t, sol(t - tau), color=YELLOW, lw=1.6, zorder=3)
b.plot(t, np.sin(t), color=BLUE, lw=1.4, zorder=3); b.plot(t, np.sin(t - tau), color=YELLOW, lw=1.6, zorder=3)
tags(fig, axes)
save(fig, HERE, 'figure', {'tau': tau, 'a': "x'=x(1-x), x=e^t/(9+e^t)", 'b': "x'=cos t, x=sin t"})
