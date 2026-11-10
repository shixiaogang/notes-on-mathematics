from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：输入在 t=0 无界：t^{-1/2} 可积，1/t 不可积。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .09, .985, .96, .27, .26)
a, b = axes
t = np.linspace(.004, 1, 800)
a.plot(t, t**-.5, color=BLUE, lw=1.4, zorder=3); a.plot(t, 1/t, color=YELLOW, lw=1.6, zorder=3)
a.set_xlim(0, 1); a.set_ylim(0, 10); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '0.5', '1']); a.set_yticks([0, 5, 10]); a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$g$', labelpad=1)
t = np.linspace(1e-4, 1, 1500)
b.plot(np.r_[0, t], np.r_[0, 2*np.sqrt(t)], color=BLUE, lw=1.4, zorder=3); dot(b, 0, 0)
b.plot(t, np.log(t), color=YELLOW, lw=1.6, zorder=3)
b.axhline(0, color=GRID, lw=.65, zorder=0); b.axvline(0, color=RED, lw=.95, ls=(0, (4, 2)), zorder=1)
b.set_xlim(-.02, 1); b.set_ylim(-5, 2.3); b.set_xticks([0, .5, 1]); b.set_xticklabels(['0', '0.5', '1']); b.set_yticks([-4, -2, 0, 2]); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 't^-1/2 and 1/t', 'b': '2 sqrt t and ln t'})
