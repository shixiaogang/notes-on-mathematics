from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Path of x*(tau) in the plane; kinks at tau=1 and tau=3.
fig, ax = figure(width_mm=86, height_mm=58)
for tau, ls, lw in [(1, ':', .95), (2, '--', .95), (3, ':', .95)]:
    ax.plot([0, tau], [tau, 0], color=ACTIVE, lw=lw, ls=ls, zorder=2)
    ax.text(.04, tau+.04, rf'$\tau={tau}$', fontsize=7.5, color=MUTED, va='bottom')
T = np.linspace(.001, 4, 800); P = np.array([budget(t)[0] for t in T])
ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.9, zorder=4)
ax.plot([1], [0], 'o', color=INK, ms=3.6, zorder=6); ax.plot([2], [1], 'o', color=INK, ms=3.6, zorder=6)
ax.plot([0], [0], 'o', color=GREEN, ms=3.4, zorder=6)
opt_point(ax, (1.5, .5))
ax.text(.5, .1, r"$(1,0)$", fontsize=7.5, ha='center', color=GREEN)
ax.text(1.68, .40, r"$(1/2,1/2)$", fontsize=7.5, ha='left', color=GREEN)
ax.text(2.1, 1.08, r'$\bm{0}$ ($\tau\geq3$)'.replace(r'\bm{0}', '0'), fontsize=7.5, color=GREEN)
ax.set_aspect('equal'); clean(ax, (-.08, 3.2), (-.25, 3.4), xlabel='$x_1$', ylabel='$x_2$')
ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2, 3])
save(fig, Path(__file__).resolve().parent, 'figure', {'kinks': [1, 3]})
