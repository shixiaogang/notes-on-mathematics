from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: one-step factor on the negative real axis vs exact exp(z).
z = np.linspace(-25, 0, 800)
fig, ax = figure(width_mm=100, height_mm=56)
ax.plot(z, np.exp(z), color=BLUE, lw=1.4)
ax.plot(z, 1/(1-z), color=GREEN, lw=1.4)
ax.plot(z, (1+z/2)/(1-z/2), color=PURPLE, lw=1.4)
ax.axhline(0, color=STROKE, lw=.7); ax.axhline(-1, color=MUTED, lw=.8, ls=(0, (2, 2)))
ax.set_xlabel(r'$z=h\lambda$'); ax.set_ylabel(r'一步放大因子'); ax.set_ylim(-1.15, 1.15); ax.set_xlim(-25, 0)
ax.plot([-10], [1/11], 'o', color=GREEN, ms=3.8); ax.plot([-10], [-2/3], 'o', color=PURPLE, ms=3.8)
ax.text(-19.2, .18, '后向 Euler', color=GREEN); ax.text(-22.5, -.68, '梯形', color=PURPLE)
ax.text(-3.0, .56, r'$\mathrm{e}^{z}$', color=BLUE)
save(fig, Path(__file__).resolve().parent, 'figure', {'z=-10': [1/11, -2/3]})
