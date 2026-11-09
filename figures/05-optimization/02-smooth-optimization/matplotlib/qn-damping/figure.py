from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# Powell 阻尼：tau=s^T y/s^T B s，theta=1（tau>=0.2），否则 0.8/(1-tau)。修正后 s^T r/s^T B s=max(tau,0.2)。
tau = np.linspace(-2, 1, 601)
theta = np.where(tau >= .2, 1., .8/(1-tau))
after = np.maximum(tau, .2)
fig, (ax, bx) = figure(width_mm=112, height_mm=48, ncols=2)
ax.plot(tau, theta, color=GREEN, lw=1.4)
ax.axvline(.2, color=STROKE, lw=.85, ls=(0, (4, 2)))
ax.axvline(-.4, color=MUTED, lw=.7, ls=(0, (1.2, 1.4)))
ax.plot([-.4], [4/7], 'o', ms=3.4, color=GREEN, mew=0, zorder=6)
ax.text(-.5, .66, '$\\theta=4/7$', color=INK, ha='right')
ax.set_xlim(-2, 1); ax.set_ylim(0, 1.1); ax.set_xlabel('$\\tau$', labelpad=1); ax.set_ylabel('$\\theta$', labelpad=1); ax.set_xticks([-2, -1, 0, 1])
bx.axhline(0, color=STROKE, lw=.6)
bx.plot(tau, tau, color=RED, lw=1.2, ls=(0, (4, 2)))
bx.plot(tau, after, color=GREEN, lw=1.4)
bx.text(-1.85, -.8, '修正前', color=INK, ha='left')
bx.text(-1.75, .36, '修正后', color=INK, ha='left')
bx.set_xlim(-2, 1); bx.set_ylim(-2, 1.1); bx.set_xlabel('$\\tau$', labelpad=1); bx.set_ylabel('曲率比', labelpad=1); bx.set_xticks([-2, -1, 0, 1])
panel(fig, .085, .985, .985, .27, .3); tags(fig, [ax, bx])
save(fig, HERE, 'figure', {'rule': 'theta=1 if tau>=.2 else .8/(1-tau)', 'example_tau': -.4, 'example_theta': 4/7})
