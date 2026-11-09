from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Two basis exchanges on the workshop and the ratio test of the first one.
A = np.hstack([WS_A, np.eye(2)]); b = WS_B
def step(B, q):
    AB = A[:, B]; xB = np.linalg.solve(AB, b); u = np.linalg.solve(AB, A[:, q])
    alpha, r = min((xB[i]/u[i], i) for i in range(len(B)) if u[i] > 1e-12)
    x = np.zeros(4); x[B] = xB-alpha*u; x[q] = alpha
    return x, B[:r]+[q]+B[r+1:], alpha, u, xB
x1, B1, a1, u1, xB1 = step([2, 3], 0)  # bases are 0-based here: slack basis, enter x1
x2, B2, a2, u2, xB2 = step(B1, 1)      # enter x2
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panels(fig, .07, .985, .975, .23, .26)
a, c = axes
xl, yl = (-.4, 4.4), (-.4, 4.6)
region(a, workshop())
arrow(a, (0, 0), x1[:2]); arrow(a, x1[:2], x2[:2])
dot(a, (0, 0), GREEN, ms=5); dot(a, x1[:2], GREEN, ms=5); dot(a, x2[:2], GREEN, ms=5)
a.text(.1, .15, '$\\{3,4\\}$', fontsize=7.5, color=INK); a.text(3.12, .16, '$\\{1,3\\}$', fontsize=7.5, color=INK)
a.text(2.14, 2.12, '$\\{1,2\\}$', fontsize=7.5, color=INK)
setup(a, xl, yl, range(0, 5), range(0, 5))
al = np.linspace(0, 4.2, 50)
for i, (name, ha, off) in enumerate([('$x_3$', 'left', .12), ('$x_4$', 'left', -.5)]):
    c.plot(al, xB1[i]-al*u1[i], color=BLUE, lw=1.4, zorder=3)
c.axhline(0, color=EDGE, lw=.85, zorder=2)
c.plot([a1, a1], [0, xB1[0]-a1*u1[0]], color=MUTED, lw=.85, ls=(0, (1.5, 1.5)), zorder=2)
dot(c, (a1, 0), RED, ms=5.2); dot(c, (a1, xB1[0]-a1*u1[0]), BLUE, ms=4.2)
c.text(2.55, 1.9, '$x_3=4-\\alpha$', fontsize=7.5, color=INK)
c.text(1.12, 3.75, '', fontsize=7.5)
c.text(.42, 5.72, '$x_4=6-2\\alpha$', fontsize=7.5, color=INK, ha='left')
c.text(3.08, .22, '$\\alpha=3$', fontsize=7.5, color=INK)
setup(c, (-.1, 4.3), (-1.2, 6.5), range(0, 5), range(0, 7), '$\\alpha$', '基分量')
tags(fig, axes)
save(fig, HERE, 'figure', {'first': {'u': u1.tolist(), 'alpha': a1, 'x': x1.tolist()}, 'second': {'u': u2.tolist(), 'alpha': a2, 'x': x2.tolist()}})
