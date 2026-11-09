from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Reachable region with a vertical left edge (weak only), a decreasing front and a flat bottom edge.
fig, ax = figure(width_mm=78, height_mm=58)
setup(ax, (0, 8), (0, 6.2), range(0, 9, 2), range(0, 7, 2))
t = np.linspace(0, 1, 100); cu = 1+3*t; cv = 1+2*(1-t)**2
ux = np.r_[1, 1, cu, 7, 7]; vy = np.r_[5.6, 3, cv, 1, 5.6]
ax.fill(ux, vy, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
ax.plot(cu, cv, color=RED, lw=2, zorder=4, solid_capstyle='round')
ax.plot([1, 1], [3, 5.6], color=EDGE, lw=2, zorder=4); ax.plot([4, 7], [1, 1], color=EDGE, lw=2, zorder=4)
w = (1, 4.4); ax.fill([0, 1, 1, 0], [0, 0, 4.4, 4.4], color=GREEN_FILL, lw=0, zorder=1.2)
hollow(ax, w, EDGE); ax.text(1.2, 4.5, '$y$', color=INK)
arrow(ax, (1, 4.3), (1, 3.12), GREEN); dot(ax, (1, 3)); ax.text(.75, 2.72, '$y\'$', color=INK, ha='right')
hollow(ax, (5.6, 1), EDGE); dot(ax, (4, 1)); ax.text(5.55, 1.2, '$z$', color=INK); ax.text(3.8, .42, "$z'$", color=INK)
ax.text(.5, 2, '开象限内无可达点', color=MUTED, fontsize=7.5, ha='left', rotation=0) if 0 else None
save(fig, HERE, 'figure', {'region': 'left edge u=1, curve u=1+3t, v=1+2(1-t)^2, bottom edge v=1'})
