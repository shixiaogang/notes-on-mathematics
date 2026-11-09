from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# Squaring loses the sign: |u|<=t versus u^2<=t^2.
fig, axes = figure(width_mm=100, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .27, .2)
a, b = axes
lim = (-2.4, 2.4)
for ax in axes:
    setup(ax, lim, lim, [-2, 0, 2], [-2, 0, 2], xl='$u$', yl='$t$')
a.fill([0, 2.4, -2.4], [0, 2.4, 2.4], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
b.fill([0, 2.4, -2.4], [0, 2.4, 2.4], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.95, zorder=1)
b.fill([0, 2.4, -2.4], [0, -2.4, -2.4], facecolor=RED_FILL, edgecolor=RED, lw=.95, zorder=1)
p = (1, -2)
hollow(a, p, RED); dot(b, p, RED)
for ax in axes: ax.text(p[0]+.17, p[1]-.03, '$(1,-2)$', fontsize=7.5, va='center')
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'a': '|u|<=t', 'b': 'u^2<=t^2', 'point': p})
