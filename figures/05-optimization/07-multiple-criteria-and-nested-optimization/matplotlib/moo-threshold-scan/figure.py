from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Threshold constraints: (a) vertical lines on the dented front, (b) best error as a function of the budget.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
ax = axes[0]; setup(ax, (0, 1.2), (0, 1.2), [0, .5, 1], [0, .5, 1], equal=True)
u = np.linspace(0, 1, 2001); v = bump(u)
ax.fill(np.r_[u, 1, 1.2, 1.2, 0], np.r_[v, 0, 0, 1.2, 1.2], color=BLUE_FILL, lw=0, zorder=1); ax.plot(u, v, color=RED, lw=1.6, zorder=3)
for t in (.15, .35, .5, .8):
    ax.plot([t, t], [0, 1.2], color=EDGE, lw=1.1, zorder=2); dot(ax, (t, bump(t)), RED, ms=5.5)
ax.fill([0, .35, .35, 0], [0, 0, 1.2, 1.2], facecolor='none', edgecolor='none')
ax.text(.355, 1.1, r'$\tau$', color=INK, fontsize=8)
ax = axes[1]; setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2), r'$\tau$', r'$v(\tau)$')
ax.fill([0, 1, 1, 0], [0, 0, 9.5, 9.5], color=RED_FILL, lw=0, zorder=1)
steps = [(1, 2, 8, 'A'), (2, 4, 5, 'B'), (4, 6, 4, 'C'), (6, 8, 1, 'D')]
for a, b, y, k in steps:
    ax.plot([a, b], [y, y], color=GREEN, lw=1.6, zorder=3); dot(ax, (a, y), GREEN, ms=4.6); b < 8 and ax.plot([b], [y], 'o', mfc='white', mec=GREEN, ms=4, mew=.9, zorder=4)
    ax.text((a+b)/2, y+.32, k, ha='center', color=INK)
ax.text(.5, 4.6, '不可行', color=RED, fontsize=7.5, ha='center', rotation=90, va='center')
tags(fig, axes)
save(fig, HERE, 'figure', {'tau': [.15, .35, .5, .8]})
