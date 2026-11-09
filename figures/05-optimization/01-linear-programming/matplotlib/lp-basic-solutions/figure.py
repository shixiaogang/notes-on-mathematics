from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# All six basic solutions of the workshop in standard form, computed from the bases.
A = np.hstack([WS_A, np.eye(2)]); b = WS_B
xl, yl = (-.5, 5.2), (-.5, 6.8)
fig, ax = figure(width_mm=100, height_mm=68)
region(ax, workshop())
line(ax, WS_A[0], 4, xl, yl); line(ax, WS_A[1], 6, xl, yl)
ax.plot(xl, [0, 0], color=EDGE, lw=.85, zorder=2); ax.plot([0, 0], yl, color=EDGE, lw=.85, zorder=2)
import itertools
facts = {}
off = {(0, 2): (.14, .17, 'left'), (0, 3): (.0, -.0, 'left'), (1, 2): (-.08, -.44, 'center'), (1, 3): (.14, .1, 'left'), (2, 3): (.14, .12, 'left')}
place = {(2, 3): (.13, .13, 'left'), (0, 2): (.08, .14, 'left'), (1, 3): (.13, .05, 'left'), (0, 1): (.15, .1, 'left'), (0, 3): (.0, .16, 'center'), (1, 2): (.15, .02, 'left')}
for B in itertools.combinations(range(4), 2):
    x = np.zeros(4); x[list(B)] = np.linalg.solve(A[:, list(B)], b)
    feas = np.all(x >= -1e-9); facts[str(tuple(i+1 for i in B))] = x.tolist()
    p = x[:2]
    if feas:
        dot(ax, p, RED if np.allclose(p, (2, 2)) else BLUE, ms=5.2 if np.allclose(p, (2, 2)) else 4.4)
    else:
        hollow(ax, p)
    dx, dy, ha = place[B]
    ax.text(p[0]+dx, p[1]+dy, '$\\{%d,%d\\}$' % (B[0]+1, B[1]+1), fontsize=7.5, ha=ha, color=INK, zorder=7)
ax.text(.72, 4.95, '原料', fontsize=7.5, color=MUTED); ax.text(3.32, .35, '', fontsize=7.5)
ax.text(3.0, 1.22, '工时', fontsize=7.5, color=MUTED)
setup(ax, xl, yl, range(0, 6), range(0, 7))
save(fig, HERE, 'figure', facts)
