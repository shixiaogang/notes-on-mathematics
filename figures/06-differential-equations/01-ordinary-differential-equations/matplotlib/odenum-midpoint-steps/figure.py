from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: midpoint method first step, h=1/2.
h = .5; k1 = f(0, X0); y = X0+h/2*k1; k2 = f(h/2, y); xn = X0+h*k2
t = np.linspace(0, .56, 200)
fig, ax = figure(width_mm=92, height_mm=58)
ax.plot(t, exact(t), color=BLUE, lw=1.4)
ax.plot([0, h/2], [X0, y], color=GREEN, lw=1.0, ls=(0, (4, 2)))
ax.plot([0, h], [X0, xn], color=GREEN, lw=1.4)
ax.plot([h/2-.06, h/2+.06], [y-.06*k2, y+.06*k2], color=PURPLE, lw=1.4)
ax.plot([h/2], [y], 'o', color=PURPLE, ms=4)
ax.plot([0], [X0], 'o', color=RED, ms=4.8, zorder=5)
ax.plot([h], [xn], 'o', color=GREEN, ms=4.2, zorder=5)
ax.set_xticks([0, h/2, h]); ax.set_xticklabels([r'$t_0$', r'$t_0+h/2$', r'$t_1$'])
ax.set_xlim(-.02, .6); ax.set_ylim(.19, .31); ax.set_xlabel(r'$t$'); ax.set_ylabel(r'$x$')
ax.annotate('中点斜率', xy=(h/2+.05, y+.05*k2), xytext=(.31, .225), color=PURPLE, arrowprops=dict(arrowstyle='-', color=PURPLE, lw=.7))
ax.text(.11, .2, '沿起点斜率走半步', color=GREEN)
ax.annotate(r'$x^{(1)}$', xy=(h, xn), xytext=(.54, .28), color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
ax.text(.13, .247, r'$x(t)$', color=BLUE, ha='right')
save(fig, Path(__file__).resolve().parent, 'figure', {'k1': k1, 'y': y, 'k2': k2, 'x1': xn})
