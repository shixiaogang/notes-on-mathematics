from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: exact curve vs grid values vs an interpolant, running example, h=0.25.
t = np.linspace(0, 1, 300)
h, n = .25, 4
xs = integrate(euler_step, f, h, n)
tg = h*np.arange(n+1)
fig, ax = figure(width_mm=92, height_mm=52)
ax.plot(t, exact(t), color=BLUE, lw=1.4)
ax.plot(tg, xs, color=GREEN, lw=.95, ls=(0, (4, 2)))
ax.plot(tg, xs, 'o', color=GREEN, ms=4.2)
ax.plot([0], [X0], 'o', color=RED, ms=5, zorder=5)
ax.set_xlabel(r'$t$'); ax.set_ylabel(r'$x$')
ax.set_xticks(tg); ax.set_xticklabels([r'$t_0$', r'$t_1$', r'$t_2$', r'$t_3$', r'$t_4$'])
ax.set_xlim(-.02, 1.08); ax.set_ylim(.17, .43)
ax.text(.62, .375, r'$x(t)$', color=BLUE)
ax.annotate('网格值', xy=(.5, xs[2]), xytext=(.56, .275), color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
ax.annotate('插值', xy=(.875, xs[3]+.5*(xs[4]-xs[3])), xytext=(.93, .325), color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
ax.text(.03, .188, r'$x_0$', color=RED)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x=x(1-x), x(0)=0.2, h=.25', 'grid': xs.tolist()})
