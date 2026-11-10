from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：冷却方程的方向场、不同初温的解，以及某点切线的斜率等于场的取值。
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, .08, .985, .97, .15)
ax.set_xlim(0, 40); ax.set_ylim(0, 90); ax.set_xticks(range(0, 41, 10)); ax.set_yticks([0, 20, 40, 60, 80])
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
f = lambda t, x: -.1*(x - 20)
slope_field(ax, f, nt=16, nx=10)
t = np.linspace(0, 40, 400)
for x0, c in [(80, BLUE), (50, YELLOW), (5, YELLOW)]:
    ax.plot(t, 20 + (x0 - 20)*np.exp(-.1*t), color=c, lw=1.4, zorder=3)
    dot(ax, 0, x0)
ax.axhline(20, color=BLUE, lw=1.0, zorder=2)
t1 = 10; x1 = 20 + 60*np.exp(-1); s = f(t1, x1)
tt = np.array([t1 - 5, t1 + 5])
ax.plot(tt, x1 + s*(tt - t1), color=PURPLE, lw=1.1, zorder=4)
ax.plot([t1], [x1], 'o', ms=3.4, color=PURPLE, mew=0, zorder=5)
ax.text(t1 + 5.4, x1 - 8, f'斜率 {s:.2f}', color=INK, fontsize=7.5, va='center')
save(fig, HERE, 'figure', {'formula': "x'=-0.1(x-20)", 'x0': [80, 50, 5], 'tangent_at': [t1, x1, s]})
