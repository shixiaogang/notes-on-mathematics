from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：齐次型方程 x'=x/t+x^2/t^2：射线上斜率相同；代换 v=x/t 与 s=ln t 后化成 dv/ds=v^2。
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .075, .985, .97, .24, .27)
a, b = axes
a.set_xlim(0, 3.6); a.set_ylim(-3, 8); a.set_xticks([0, 1, 2, np.e]); a.set_xticklabels(['0', '1', '2', '$\\mathrm{e}$']); a.set_yticks([-2, 0, 2, 4, 6, 8])
f = lambda t, x: x/t + x**2/t**2
for v in (-1, -.5, .5, 1, 2):
    a.plot([0, 3.6], [0, 3.6*v], color=GRID, lw=.85, zorder=0)
slope_field(a, f, nt=13, nx=12, length_mm=2.5, skip=lambda t, x: x/t > 4 or x/t < -3)
t = np.linspace(.01, np.e - 2e-3, 800)
a.plot(t, t/(1 - np.log(t)), color=BLUE, lw=1.4, zorder=3)
t = np.linspace(.01, 3.6, 800)
a.plot(t, t/(2 - np.log(t)), color=YELLOW, lw=1.6, zorder=3)
a.plot(t, 0*t, color=BLUE, lw=1, zorder=2)
a.axvline(np.e, color=RED, lw=.95, ls=(0, (4, 2)), zorder=1)
dot(a, 1, 1); dot(a, 1, .5)
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$x$', labelpad=1)
s = np.linspace(-2.5, 1 - 2e-3, 800); b.plot(s, 1/(1 - s), color=BLUE, lw=1.4, zorder=3)
s = np.linspace(-2.5, 1.8, 800); b.plot(s, 1/(2 - s), color=YELLOW, lw=1.6, zorder=3)
b.plot([-2.5, 1.8], [0, 0], color=BLUE, lw=1, zorder=2)
b.axvline(1, color=RED, lw=.95, ls=(0, (4, 2)), zorder=1)
dot(b, 0, 1); dot(b, 0, .5)
b.set_xlim(-2.5, 1.8); b.set_ylim(-.3, 6); b.set_xticks([-2, -1, 0, 1]); b.set_yticks([0, 2, 4, 6]); b.set_xlabel('$s=\\ln t$', labelpad=1); b.set_ylabel('$v=x/t$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "x'=x/t+x^2/t^2", 'initial': 'x(1)=1 and x(1)=0.5', 'blowup': float(np.e)})
