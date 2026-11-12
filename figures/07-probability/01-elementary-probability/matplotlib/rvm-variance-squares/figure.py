from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
from matplotlib.patches import Rectangle
# Variance of the reward table as average squared distance from the mean 2:
# squares of side |x_i - 2| = 2, 1, 4 have areas 4, 1, 16; weights 1/2, 1/3, 1/6;
# 4/2 + 1/3 + 16/6 = 5.  The square for x=3 is drawn below the axis to avoid overlap.
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.02, right=.98, bottom=.02, top=.98)
m = 2.
ax.plot([-.8, 6.8], [0, 0], color=STROKE, lw=1.0)
spec = [(0., .5, 1, '$4\\times\\frac{1}{2}$'), (3., 1/3, -1, '$1\\times\\frac{1}{3}$'), (6., 1/6, 1, '$16\\times\\frac{1}{6}$')]
for x, p, up, s in spec:
    d = abs(x-m); x0 = min(x, m)
    y0 = 0 if up > 0 else -d
    ax.add_patch(Rectangle((x0, y0), d, d, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.9))
    dot(ax, x, 0, color=BLUE, ms=3+9*p)
    if d > 1.5:
        lab(ax, x0+d/2, d/2, s, INK, ha='center', va='center', fontsize=8)
    else:
        lab(ax, x0+d+.2, -d/2, s, INK, ha='left', va='center', fontsize=8)
for x in XV:
    lab(ax, x, .25, f'${x:g}$', INK, ha='center', va='bottom') if x == 3 else lab(ax, x, -.25, f'${x:g}$', INK, ha='center', va='top')
fulcrum(ax, m, 0, .4, .4)
lab(ax, m-.3, -.45, '$\\mu=2$', RED, ha='right', va='top')
ax.set_xlim(-.8, 6.8); ax.set_ylim(-1.6, 4.2); ax.set_aspect('equal')
ax.axis('off')
save(fig, HERE, 'figure', {'variance': float(((XV-m)**2*PV).sum())})
