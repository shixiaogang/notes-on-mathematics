from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Threshold problem with tied minimizers along a flat edge.
fig, ax = figure(width_mm=80, height_mm=56)
setup(ax, (0, 8), (0, 6.2), range(0, 9, 2), range(0, 7, 2))
t = np.linspace(0, 1, 100); cu = 1+3*t; cv = 1+2*(1-t)**2
ax.fill(np.r_[1, 1, cu, 7.6, 7.6], np.r_[5.6, 3, cv, 1, 5.6], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
ax.plot(cu, cv, color=BLUE, lw=1.1, zorder=3); ax.plot([1, 1], [3, 5.6], color=BLUE, lw=1.1, zorder=3); ax.plot([4, 7.6], [1, 1], color=BLUE, lw=1.1, zorder=3)
tau = 6.4; ax.plot([tau, tau], [0, 6.2], color=EDGE, lw=2, zorder=4); ax.text(tau+.15, 5.6, r'$\tau$', color=INK)
ax.plot([4, tau], [1, 1], color=YELLOW, lw=3, zorder=5, solid_capstyle='round'); dot(ax, (4, 1), RED, ms=6, z=8)
ax.text(3.8, .42, "$z'$", color=INK); hollow(ax, (5.6, 1), EDGE, z=8); ax.text(5.5, 1.25, '$z$', color=INK)
save(fig, HERE, 'figure', {'tau': tau})
