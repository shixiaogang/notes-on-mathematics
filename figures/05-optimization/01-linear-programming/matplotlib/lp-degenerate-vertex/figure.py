from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Degenerate vertex: x1<=3 passes through (3,0) without cutting the polygon.
A = np.array([[1., 1, 1, 0, 0], [2, 1, 0, 1, 0], [1, 0, 0, 0, 1]]); b = np.array([4., 6, 3])
out = {}
for B in ([0, 2, 1], [0, 2, 3], [0, 2, 4]):
    out[str([i+1 for i in B])] = np.linalg.solve(A[:, B], b).round(9).tolist()
xl, yl = (-.4, 5.3), (-.9, 4.6)
fig, ax = figure(width_mm=90, height_mm=62)
region(ax, workshop())
line(ax, WS_A[1], 6, xl, yl, lw=1.4); line(ax, (1, 0), 3, xl, yl, lw=1.4)
ax.plot(xl, [0, 0], color=EDGE, lw=1.4, zorder=2)
dot(ax, (3, 0), RED, ms=5.4)
ax.text(3.08, .15, '$(3,0)$', fontsize=7.5, color=INK)
ax.text(3.08, 2.8, '$x_1=3$', fontsize=7.5, color=INK)
ax.text(.95, 4.4, '$2x_1+x_2=6$', fontsize=7.5, color=INK, ha='left')
ax.text(4.0, .13, '$x_2=0$', fontsize=7.5, color=INK)
ax.text(3.18, -.5, '$\\{1,3,2\\},\\ \\{1,3,4\\},\\ \\{1,3,5\\}$', fontsize=7.5, color=INK)
setup(ax, xl, yl, range(0, 5), range(0, 5))
save(fig, HERE, 'figure', out)
