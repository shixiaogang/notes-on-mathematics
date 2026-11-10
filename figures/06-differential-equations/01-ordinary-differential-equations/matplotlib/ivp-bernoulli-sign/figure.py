from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x'=x-x^3，w=x^{-2} 丢失符号：x0=±0.4 映到同一条 w 曲线。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .09, .985, .96, .27, .26)
a, b = axes
t = np.linspace(0, 4, 400)
w = 1 + (.4**-2 - 1)*np.exp(-2*t)
a.plot(t, w**-.5, color=BLUE, lw=1.4, zorder=3); a.plot(t, -w**-.5, color=YELLOW, lw=1.6, zorder=3)
a.plot(t, 0*t, color=BLUE, lw=1, zorder=2)
dot(a, 0, .4); dot(a, 0, -.4); dot(a, 0, 0)
b.plot(t, w, color=BLUE, lw=1.4, zorder=3); dot(b, 0, .4**-2)
b.axhline(1, color=BLUE, lw=1, zorder=2)
a.set_xlim(0, 4); a.set_ylim(-1.15, 1.15); a.set_xticks(range(5)); a.set_yticks([-1, -.4, 0, .4, 1]); a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$x$', labelpad=1)
b.set_xlim(0, 4); b.set_ylim(0, 7); b.set_xticks(range(5)); b.set_yticks([0, 1, 3, 6.25]); b.set_yticklabels(['0', '1', '3', '6.25']); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$w=x^{-2}$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "x'=x-x^3", 'x0': [.4, -.4, 0], 'w': 'w=1+5.25 e^-2t'})
