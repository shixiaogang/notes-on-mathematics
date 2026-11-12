from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Masses of the sum of 1, 2, 3 fair dice by repeated discrete convolution.
d = np.ones(6)/6; p2 = np.convolve(d, d); p3 = np.convolve(p2, d)
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.07, right=.98, bottom=.3, top=.95, wspace=.3)
for ax, p, s0 in zip(axes, (d, p2, p3), (1, 2, 3)):
    x = np.arange(s0, s0+len(p)); bars(ax, x, p, w=.75)
    ax.set_ylim(0, .2); ax.set_yticks([0, .1, .2]); ax.set_xlim(.3, 18.7); ax.set_xticks([1, 6, 12, 18]); axlab(ax, '$s$')
axes[2].bar([10], [p3[7]], width=.75, color=RED_FILL, edgecolor=RED, linewidth=.9)
tags(fig, axes)
save(fig, HERE, 'figure', {'p3(10)': float(p3[7]), 'p3(10)*216': float(p3[7]*216)})
