from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：高频小扰动的导数巨大，积分很小。epsilon=0.2。
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, .095, .985, .95, .29, .46)
a, b, c = axes
e = .2
t = np.linspace(0, 2, 8000)
a.plot(t, e*np.sin(t/e**2), color=RED, lw=.95); a.set_ylim(-.3, .3); a.set_yticks([-.2, 0, .2]); a.set_ylabel('$\\delta$', labelpad=1)
b.plot(t, np.cos(t/e**2)/e, color=RED, lw=.95); b.set_ylim(-6, 6); b.set_yticks([-5, 0, 5]); b.set_ylabel('$\\dot{\\delta}$', labelpad=1)
c.plot(t, e**3*(1 - np.cos(t/e**2)), color=RED, lw=.95); c.set_ylim(-.3, .3); c.set_yticks([-.2, 0, .2]); c.set_ylabel('$\\int\\delta$', labelpad=1)
for ax in axes:
    ax.set_xlim(0, 2); ax.set_xticks([0, 1, 2]); ax.set_xlabel('$t$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'epsilon': e, 'delta': 'e sin(t/e^2)'})
