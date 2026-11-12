"""Unif(0,theta): theta=1 (blue) vs theta+h=1.25 (yellow). Inside (0,1) density falls by 0.2 (red area 0.2);
new mass on (1,1.25] (blue area 0.2) lies outside the old support, invisible to the score -1/theta."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, ax = figure(width_mm=72, height_mm=44)
th, h = 1.0, 0.25; lo = 1/(th+h)
ax.fill_between([0, th], [lo, lo], [1/th, 1/th], color=RED_FILL, lw=0)
ax.fill_between([th, th+h], [0, 0], [lo, lo], color=BLUE_FILL, lw=0)
ax.plot([-0.15, 0, 0, th, th, 1.5], [0, 0, 1/th, 1/th, 0, 0], color=BLUE, lw=1.4)
ax.plot([-0.15, 0, 0, th+h, th+h, 1.5], [0, 0, lo, lo, 0, 0], color=YELLOW, lw=1.5, ls=(0, (4, 2)))
ax.scatter([th], [0], s=16, color=RED, zorder=5, clip_on=False)
ax.set_xlim(-0.15, 1.5); ax.set_ylim(0, 1.2)
ax.set_xticks([0, 1, 1.25]); ax.set_xticklabels([r'$0$', r'$\theta$', r'$\theta+h$'])
ax.set_yticks([0, lo, 1]); ax.set_yticklabels([r'$0$', r'$\frac{1}{\theta+h}$', r'$\frac{1}{\theta}$'])
ax.set_xlabel(r'$x$', labelpad=1)
save(fig, HERE, 'figure', {'loss_inside': (1/th-lo)*th, 'gain_outside': lo*h})
