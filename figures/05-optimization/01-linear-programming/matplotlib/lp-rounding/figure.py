from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Rounding the relaxed optimum of max 3x1+x2, x1+x2<=4, 2x1+x2<=7, x>=0.
xl, yl = (2.0, 4.5), (-.5, 2.3)
fig, ax = figure(width_mm=92, height_mm=62)
region(ax, workshop((4., 7.)))
levels(ax, (3, 1), [9, 10, 10.5], xl, yl)
for i in range(2, 5):
    for j in range(0, 3):
        if i+j <= 4 and 2*i+j <= 7: dot(ax, (i, j), BLUE, ms=3.8, z=5)
arrow(ax, (3.5, 0), (3.94, 0), RED, lw=1.1, ms=6); arrow(ax, (3.5, 0), (3.06, 0), GREEN, lw=1.1, ms=6)
hollow(ax, (4, 0)); dot(ax, (3.5, 0), RED, ms=5.2); dot(ax, (3, 1), RED, ms=5.4, z=7)
ax.text(4.06, .09, '$(4,0)$', fontsize=7.5, color=INK); ax.text(2.82, -.22, '$(3,0)$', fontsize=7.5, color=INK, ha='right')
ax.text(3.68, -.3, '$(7/2,0)$', fontsize=7.5, color=INK, ha='left'); ax.text(3.2, 1.05, '$(3,1)$', fontsize=7.5, color=INK)
ax.text(2.32, 2.12, '$9$', fontsize=7.5, color=BLUE); ax.text(2.66, 2.12, '$10$', fontsize=7.5, color=BLUE); ax.text(2.85, 2.12, '$10.5$', fontsize=7.5, color=BLUE)
setup(ax, xl, yl, [2, 3, 4], [0, 1, 2])
save(fig, HERE, 'figure', {'relaxed': [3.5, 0], 'relaxed_value': 10.5, 'integer_opt': [3, 1], 'value': 10})
