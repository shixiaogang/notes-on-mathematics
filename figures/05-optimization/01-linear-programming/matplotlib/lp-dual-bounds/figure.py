from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Dual prices of the workshop and the two-sided bounds on the number line.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .975, .22, .24)
a, b = axes
xl, yl = (-.3, 4.3), (-.3, 3.2)
R = np.array([[0, 2], [1, 1], [3, 0], [4.3, 0], [4.3, 3.2], [0, 3.2]], float)
a.fill(R[:, 0], R[:, 1], facecolor=PURPLE_FILL, edgecolor=PURPLE, lw=.95, zorder=1)
levels(a, (4, 6), [10, 12, 16], xl, yl)
for p in [(3, 0), (0, 2), (2, 1)]:
    dot(a, p, PURPLE, ms=4.6)
dot(a, (1, 1), RED, ms=5.4)
a.text(.62, .62, '$(1,1)$', fontsize=7.5, color=INK, ha='center'); a.text(3.1, .12, '$(3,0)$', fontsize=7.5, color=INK)
a.text(.1, 2.12, '$(0,2)$', fontsize=7.5, color=INK); a.text(2.14, .84, '$(2,1)$', fontsize=7.5, color=INK)
setup(a, xl, yl, range(0, 5), range(0, 4), '$u_1$', '$u_2$')
# number line: primal values at vertices, dual values at the four prices
P = WS_P; V = [(0, 0), (0, 4), (3, 0), (2, 2)]; pv = [P@np.array(v) for v in V]
U = [(1, 1), (3, 0), (0, 2), (2, 1)]; dv = [4*u[0]+6*u[1] for u in U]
b.axhline(0, color=EDGE, lw=.95, zorder=1)
for v in pv:
    b.plot([v], [.22], 'o', color=BLUE, ms=4.6, mew=0, zorder=4)
for v in set(dv):
    b.plot([v], [-.22], 'o', color=PURPLE, ms=4.6, mew=0, zorder=4)
b.plot([10, 10], [-.45, .45], color=RED, lw=1.1, zorder=3); b.plot([10], [0], 'o', color=RED, ms=5.2, mew=0, zorder=5)
b.text(2.2, .62, '可行产量的利润', fontsize=7.5, color=BLUE, ha='left'); b.text(9, -.75, '价格给出的上界', fontsize=7.5, color=PURPLE, ha='center')
for v, s in zip(pv, ['$0$', '$8$', '$9$', '']):
    b.text(v, .36, s, fontsize=7.5, color=BLUE, ha='center')
for v, s in [(12, '$12$'), (14, '$14$')]:
    b.text(v, -.54, s, fontsize=7.5, color=PURPLE, ha='center')
b.text(10, .54, '$10$', fontsize=7.5, color=RED, ha='center')
b.set_xlim(-.8, 15.5); b.set_ylim(-1.1, 1.1); b.set_yticks([]); b.set_xticks([0, 5, 10, 15])
for s in ('left', 'top', 'right'): b.spines[s].set_visible(False)
b.spines['bottom'].set_visible(False); b.tick_params(axis='x', length=0, labelbottom=False)
tags(fig, axes)
save(fig, HERE, 'figure', {'primal': pv, 'dual': dv})
