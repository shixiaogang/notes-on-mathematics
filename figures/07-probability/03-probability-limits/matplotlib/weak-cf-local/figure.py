from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Mean 0, variance 1: Rademacher cos t, Unif(-sqrt3,sqrt3) sin(sqrt3 t)/(sqrt3 t), N(0,1) exp(-t^2/2), parabola 1-t^2/2.
fig, ax = figure(width_mm=100, height_mm=48)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.97, top=.96, bottom=.2)
t = np.linspace(1e-9, 4, 800); s3 = np.sqrt(3)
ax.axhline(0, color=GRID, lw=.6, zorder=0)
ax.plot(t, 1-t**2/2, color=PURPLE, lw=1.0, ls=DASH)
ax.plot(t, np.cos(t), color=YELLOW, lw=1.6); ax.plot(t, np.sin(s3*t)/(s3*t), color=GREEN, lw=1.4); ax.plot(t, np.exp(-t**2/2), color=BLUE, lw=1.4)
lab(ax, 3.3, -.88, r'$\cos t$', YELLOW); lab(ax, 2.55, .2, r'$\mathrm{e}^{-t^2/2}$', BLUE); lab(ax, 1.75, -.75, r'$1-t^2/2$', PURPLE, ha='right')
ax.set_xlim(0, 4); ax.set_ylim(-1.1, 1.08); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([-1, 0, 1])
axlab(ax, r'$t$')
save(fig, HERE, 'figure', {'fourth_coeffs': [1/24, 3/40, 1/8]})
