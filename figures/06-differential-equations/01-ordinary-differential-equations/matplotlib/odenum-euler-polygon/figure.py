from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: Euler polygon following the direction field for two step sizes.
fig, ax = figure(width_mm=112, height_mm=54, ncols=2, sharey=True)
t = np.linspace(0, 1, 300)
for a, (h, n) in zip(ax, ((.5, 2), (.125, 8))):
    direction_field(a, f, np.linspace(.05, .95, 8), np.linspace(.18, .44, 8), .055, .28)
    a.plot(t, exact(t), color=BLUE, lw=1.4, zorder=3)
    xs = integrate(euler_step, f, h, n); tg = h*np.arange(n+1)
    a.plot(tg, xs, color=GREEN, lw=1.2, zorder=4)
    a.plot(tg, xs, 'o', color=GREEN, ms=3.8 if n < 5 else 2.8, zorder=5)
    a.plot([0], [X0], 'o', color=RED, ms=4.8, zorder=6)
    a.set_xlabel(r'$t$'); a.set_xlim(-.02, 1.04); a.set_ylim(.16, .45)
    a.annotate(f'误差 {abs(xs[-1]-float(exact(1.0))):.4f}', xy=(1, xs[-1]), xytext=(.54, .2), color=RED, arrowprops=dict(arrowstyle='-', color=RED, lw=.7))
ax[0].set_ylabel(r'$x$')
panel(ax[0], r'(a) $h=1/2$', -.3); panel(ax[1], r'(b) $h=1/8$', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x=x(1-x)'})
