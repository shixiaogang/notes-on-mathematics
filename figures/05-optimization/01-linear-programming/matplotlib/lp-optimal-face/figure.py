from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Level lines sliding over the workshop polygon: unique vertex vs an optimal edge.
xl, yl = (-.4, 4.4), (-.4, 4.6)
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .975, .22, .26)
a, b = axes
region(a, workshop()); levels(a, WS_P, [4, 7], xl, yl); levels(a, WS_P, [10], xl, yl, lw=1.3)
dot(a, (2, 2), RED, ms=5.4)
for v, t in [(4, (.1, 1.98)), (7, (.1, 3.5))]:
    a.text(t[0], t[1], '$%d$' % v, color=BLUE, fontsize=7.5)
a.text(3.12, .55, '$10$', color=BLUE, fontsize=7.5)
a.text(2.16, 2.12, '$(2,2)$', color=INK, fontsize=7.5)
region(b, workshop()); p2 = np.array([2., 1.]); levels(b, p2, [2, 4], xl, yl); levels(b, p2, [6], xl, yl, lw=1.3)
b.plot([2, 3], [2, 0], color=RED, lw=2.0, zorder=5)
dot(b, (2, 2), RED, ms=5.2); dot(b, (3, 0), RED, ms=5.2); dot(b, (2.5, 1), 'white', ms=3.2, z=7)
hollow(b, (2.5, 1), RED, ms=4.6, z=7)
for v, t in [(2, (.56, 1.0)), (4, (1.32, 1.5)), (6, (3.18, .28))]:
    b.text(t[0], t[1], '$%d$' % v, color=BLUE, fontsize=7.5)
b.text(2.62, 1.05, '$(5/2,1)$', color=INK, fontsize=7.5)
b.text(3.2, .55, '', color=BLUE, fontsize=7.5)
setup(a, xl, yl, range(0, 5), range(0, 5)); setup(b, xl, yl, range(0, 5), range(0, 5))
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'max 3x1+2x2', 'b': 'max 2x1+x2, optimal edge from (2,2) to (3,0)'})
