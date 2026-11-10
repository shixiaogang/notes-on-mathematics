from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x'=2 sqrt|x|，x(0)=0 的零解与从零离开的解族，说明除以零点前必须检查。
fig, ax = figure(width_mm=92, height_mm=50)
panel(fig, .085, .98, .965, .16)
ax.set_xlim(-.1, 4); ax.set_ylim(-.2, 5.2); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 2, 4])
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
slope_field(ax, lambda t, x: 2*np.sqrt(abs(x)), nt=14, nx=9, length_mm=2.5)
t = np.linspace(0, 4, 800)
for c in (0, 1, 2):
    ax.plot(t, np.where(t >= c, (t - c)**2, 0), color=YELLOW, lw=1.6, zorder=3)
ax.plot(t, 0*t, color=BLUE, lw=1.4, zorder=4)
dot(ax, 0, 0)
save(fig, HERE, 'figure', {'formula': "x'=2 sqrt|x|", 'departures_c': [0, 1, 2]})
