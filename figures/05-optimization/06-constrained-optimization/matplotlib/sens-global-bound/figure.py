from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Value function of the budget quadratic and the affine lower bound from the multiplier at tau=2.
fig, ax = figure(width_mm=100, height_mm=56)
T = np.linspace(0, 5, 501); V = [value(t) for t in T]
ax.axvspan(-.7, 0, facecolor=RED_FILL, edgecolor='none', zorder=0)
ax.plot(T, V, color=BLUE, lw=1.4, zorder=3)
ax.plot([-.7, 5], [.25-.5*(-.7-2), .25-.5*3], color=PURPLE, lw=1.1, ls='--', zorder=2)
for t in (1, 3): ax.axvline(t, color=MUTED, lw=.85, ls=':', zorder=1)
opt_point(ax, (2, .25))
for t in (.5, 4):
    lo = .25-.5*(t-2); hi = value(t)
    ax.plot([t, t], [lo, hi], color=GREEN, lw=1.4, zorder=4)
    ax.plot([t, t], [lo, hi], 'o', color=GREEN, ms=2.8, zorder=5)
ax.text(-.35, 2.45, r'$+\infty$', ha='center', fontsize=8, color=RED)
ax.text(2.35, .55, r'$(2,\,V(2))$', fontsize=7.5)
ax.text(1.12, 1.5, r'$V(\tau)$', fontsize=8, color=BLUE)
ax.text(1.1, -.55, r'$V(2)-\lambda_1^{*}(\tau-2)$', fontsize=7.5, color=PURPLE, ha='left', va='top')
ax.axhline(0, color=GRID, lw=.5, zorder=0)
clean(ax, (-.7, 5), (-1.55, 3), xlabel=r'$\tau$', ylabel='最优值')
ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([-1, 0, 1, 2, 3])
save(fig, Path(__file__).resolve().parent, 'figure', {'bound': 'V(tau)>=0.25-0.5*(tau-2)', 'V(.5)': value(.5), 'V(4)': value(4)})
