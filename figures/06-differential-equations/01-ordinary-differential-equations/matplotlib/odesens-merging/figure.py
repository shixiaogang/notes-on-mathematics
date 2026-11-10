from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=-2 sgn(x) sqrt|x| 前向唯一但轨道在有限时间并入 0，流映射不单射，反向不唯一。
fig, axes = figure(width_mm=100, height_mm=46, ncols=2)
panel(fig, .085, .985, .955, .29, .28)
def flow(x0, t): return np.sign(x0)*np.maximum(np.sqrt(np.abs(x0))-t, 0)**2
ax = axes[0]; t = np.linspace(0, 1.6, 401)
for x0 in (.25, .64, 1., 1.44, 2.25): ax.plot(t, flow(x0, t), color=BLUE, lw=1.2); ax.plot(t, flow(-x0, t), color=BLUE, lw=1.2)
ax.plot(t, 0*t, color=RED, lw=1.5); ax.vlines(1, -2.3, 2.3, color=MUTED, lw=.85, ls=(0, (2, 2)))
ax.text(1.04, 2.2, '$t=1$', color=MUTED, fontsize=7.5, va='top')
ax.set_xlim(0, 1.6); ax.set_ylim(-2.3, 2.3); ax.set_xticks([0, 1]); ax.set_yticks([-2, 0, 2]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
ax = axes[1]; s = np.linspace(-2.25, 2.25, 901); ax.plot(s, flow(s, 1.), color=BLUE, lw=1.4); ax.plot([-1, 1], [0, 0], color=RED, lw=2.2, solid_capstyle='butt')
ax.set_xlim(-2.25, 2.25); ax.set_ylim(-.28, .28); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([-.25, 0, .25]); ax.set_xlabel('$x_0$', labelpad=0); ax.set_ylabel('$\\varphi_1(x_0)$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '-2 sgn(x) sqrt|x|'})
