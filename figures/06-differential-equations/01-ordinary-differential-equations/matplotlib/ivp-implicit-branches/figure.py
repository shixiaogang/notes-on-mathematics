from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x x'=-t 的隐式解 t^2+x^2=1 含两支，初值选上半支，端点处斜率无界且方程无定义。
fig, ax = figure(width_mm=84, height_mm=66)
panel(fig, .1, .98, .975, .13)
ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.3, 1.3); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
slope_field(ax, lambda t, x: -t/x, nt=19, nx=17, length_mm=2.4, skip=lambda t, x: abs(x) < .11)
ax.axhline(0, color=STROKE, lw=1.2, zorder=2)
th = np.linspace(0, np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color=BLUE, lw=1.4, zorder=4)
ax.plot(np.cos(th), -np.sin(th), color=YELLOW, lw=1.6, zorder=4)
dot(ax, 0, 1); hollow(ax, -1, 0); hollow(ax, 1, 0)
save(fig, HERE, 'figure', {'formula': "x'=-t/x, x(0)=1", 'branches': 'x=+-sqrt(1-t^2)'})
