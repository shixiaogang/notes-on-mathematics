from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Pushing (1,1) to a vertex: the numbers are the steps worked out in the text.
A = np.hstack([WS_A, np.eye(2)]); c = np.array([-3., -2., 0., 0.])
x0 = np.array([1., 1., 2., 3.])
def push(x, w):
    assert np.allclose(A@w, 0) and c@w <= 0
    t = min(x[j]/-w[j] for j in range(4) if w[j] < 0)
    return x+t*w, t
x1, t1 = push(x0, np.array([1., 0., -1., -2.]))
x2, t2 = push(x1, np.array([-1., 2., -1., 0.]))
xl, yl = (-.4, 4.4), (-.4, 4.6)
fig, ax = figure(width_mm=92, height_mm=62)
region(ax, workshop())
levels(ax, WS_P, [c@x0*-1, c@x1*-1, c@x2*-1], xl, yl)
arrow(ax, x0[:2], x1[:2]); arrow(ax, x1[:2], x2[:2])
dot(ax, x0[:2], GREEN, ms=5); dot(ax, x1[:2], GREEN, ms=5); dot(ax, x2[:2], RED, ms=5.4)
ax.text(.92, .68, '$(1,1)$', fontsize=7.5, ha='right', color=INK)
ax.text(2.62, 1.12, '$(5/2,1)$', fontsize=7.5, color=INK)
ax.text(2.13, 2.12, '$(2,2)$', fontsize=7.5, color=INK)
ax.text(.13, 4.73, '', fontsize=7.5)
for v, x_, y_ in [(5, .32, 4.05), (9.5, 3.82, .35), (10, 3.82, 1.25)]:
    pass
ax.text(.06, 2.5, '$5$', fontsize=7.5, color=BLUE)
ax.text(3.2, .22, '$9.5$', fontsize=7.5, color=BLUE)
ax.text(3.45, .44, '$10$', fontsize=7.5, color=BLUE)
setup(ax, xl, yl, range(0, 5), range(0, 5))
save(fig, HERE, 'figure', {'x0': x0.tolist(), 'x1': x1.tolist(), 't1': t1, 'x2': x2.tolist(), 't2': t2})
