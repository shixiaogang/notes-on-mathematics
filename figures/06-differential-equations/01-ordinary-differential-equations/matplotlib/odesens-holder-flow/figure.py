from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=-x ln x（x>0）解唯一，x(t)=x0^{exp(-t)}，初值依赖连续但不 Lipschitz。
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
panel(fig, .09, .985, .955, .29, .28)
ax = axes[0]; t = np.linspace(0, 2, 401)
for x0 in (1e-8, 1e-6, 1e-4, 1e-2, .1, .3):
    ax.plot(t, x0**np.exp(-t), color=BLUE, lw=1.1)
ax.plot(t, 0*t, color=YELLOW, lw=1.6); ax.vlines(np.log(2), 0, 1, color=MUTED, lw=.85, ls=(0, (2, 2)))
ax.text(np.log(2)+.04, .94, '$t=\\ln 2$', color=MUTED, fontsize=7.5, va='top')
ax.set_xlim(0, 2); ax.set_ylim(-.02, 1); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
ax = axes[1]; x0 = np.linspace(0, .25, 1001)
ax.plot(x0, np.sqrt(x0), color=BLUE, lw=1.4); ax.plot(x0, 3*x0, color=PURPLE, lw=.85, ls=(0, (3, 2)))
ax.text(.145, .49, '$3x_0$', color=PURPLE, fontsize=7.5, ha='right')
ax.text(.13, .28, '$\\sqrt{x_0}$', color=BLUE, fontsize=7.5, va='top', ha='left')
ax.set_xlim(0, .25); ax.set_ylim(0, .55); ax.set_xticks([0, .1, .2]); ax.set_yticks([0, .25, .5]); ax.set_xlabel('$x_0$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'equation': "x'=-x ln x", 'flow': 'x0^(exp(-t))'})
