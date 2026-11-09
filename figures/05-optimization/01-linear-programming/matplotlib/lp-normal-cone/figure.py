from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"lp-common"))
from lp_fig import *
HERE = Path(__file__).resolve().parent
# Normal-cone reading of complementary slackness at the vertices (2,2) and (3,0).
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panels(fig, .07, .985, .975, .2, .24)
a, b = axes
xl, yl = (-.3, 6.6), (-1.6, 5.2)
for ax in axes:
    region(ax, workshop()); setup(ax, xl, yl, range(0, 7), range(-1, 6))
    line(ax, WS_A[0], 4, xl, yl, lw=.85); line(ax, WS_A[1], 6, xl, yl, lw=.85)
V = np.array([2., 2.]); n1, n2 = WS_A[0], WS_A[1]; p = WS_P
a.fill([V[0], V[0]+n1[0]*2.2, V[0]+n2[0]*1.5], [V[1], V[1]+n1[1]*2.2, V[1]+n2[1]*1.5], facecolor=PURPLE_FILL, edgecolor='none', zorder=2)
arrow(a, V, V+n1, PURPLE); arrow(a, V, V+n2, PURPLE); arrow(a, V, V+p, BLUE, lw=1.6)
a.plot([V[0]+n1[0], V[0]+p[0], V[0]+n2[0]], [V[1]+n1[1], V[1]+p[1], V[1]+n2[1]], color=PURPLE, lw=.85, ls=(0, (2, 2)), zorder=3)
dot(a, V, RED, ms=5.4)
a.text(2.72, 3.25, '$\\bm{n}_1$'.replace('\\bm{n}', 'n'), fontsize=8, color=PURPLE, ha='right')
a.text(4.1, 2.75, '$n_2$', fontsize=8, color=PURPLE)
a.text(5.1, 3.95, '$\\mathbf{p}$', fontsize=8, color=BLUE)
V = np.array([3., 0.]); n3 = np.array([0., -1.])
b.fill([V[0], V[0]+n2[0]*1.6, V[0]], [V[1], V[1]+n2[1]*1.6, V[1]-1.4], facecolor=PURPLE_FILL, edgecolor='none', zorder=2)
arrow(b, V, V+n2, PURPLE); arrow(b, V, V+n3, PURPLE); arrow(b, V, V+p, BLUE, lw=1.6)
dot(b, V, GREEN, ms=5)
b.text(5.1, .8, '$n_2$', fontsize=8, color=PURPLE)
b.text(2.82, -1.05, '$n_3$', fontsize=8, color=PURPLE, ha='right')
b.text(6.05, 1.65, '$\\mathbf{p}$', fontsize=8, color=BLUE)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'p=(3,2)=1*(1,1)+1*(2,1) at (2,2)', 'b': 'p=1.5*(2,1)-0.5*(0,-1) at (3,0), outside cone'})
