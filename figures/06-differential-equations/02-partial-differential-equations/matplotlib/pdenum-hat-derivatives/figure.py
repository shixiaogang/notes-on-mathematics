from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Hats and piecewise-constant derivatives on the mesh h=1/4; overlap gives stiffness entries.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.075, wspace=.24, bottom=.28)
h = .25; xs = np.array([.25, .5, .75])
ax = axes[0]
for i, c, lw in ((.25, YELLOW, 1.1), (.5, GREEN, 1.5), (.75, PURPLE, 1.1)):
    ax.plot([i-h, i, i+h], [0, 1, 0], color=c, lw=lw)
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, 1.15); ax.set_xticks([0, .25, .5, .75, 1]); ax.set_xticklabels(['0', '1/4', '1/2', '3/4', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1)
lab(ax, .25, 1.03, r'$\varphi_1$', YELLOW, ha='center'); lab(ax, .5, 1.03, r'$\varphi_2$', GREEN, ha='center'); lab(ax, .75, 1.03, r'$\varphi_3$', PURPLE, ha='center')
ax = axes[1]
ax.fill_between([.25, .5], -4, 4, color=RED_FILL, lw=0)
ax.axhline(0, color=STROKE, lw=.6)
ax.plot([.25, .5, .5, .75], [4, 4, -4, -4], color=GREEN, lw=1.5)
ax.plot([0, .25, .25, .5], [4, 4, -4, -4], color=YELLOW, lw=1.2)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-5.4, 5.8); ax.set_xticks([0, .25, .5, .75, 1]); ax.set_xticklabels(['0', '1/4', '1/2', '3/4', '1']); ax.set_yticks([-4, 0, 4]); ax.set_xlabel('$x$', labelpad=1)
lab(ax, .38, 4.5, r"$\varphi_2'$", GREEN, ha='center'); lab(ax, .12, 4.5, r"$\varphi_1'$", YELLOW, ha='center')
tags(fig, axes); save(fig, HERE, 'figure', {'h': h, 'k12': -1/h, 'k22': 2/h})
