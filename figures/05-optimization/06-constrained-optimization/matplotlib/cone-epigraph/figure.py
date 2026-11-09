from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# (a) epigraph of f(x)=||(x-1,1/2)||. (b) the set ||(2u,2t-1)||<=2t+1 computed on a grid is t>=u^2/2.
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .07, .985, .985, .25, .22)
a, b = axes
x = np.linspace(-1, 3, 400); f = np.hypot(x-1, .5)
a.fill_between(x, f, 2.6, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
a.plot(x, f, color=BLUE, lw=1.5, zorder=2)
p = 2.2; fp = np.hypot(p-1, .5)
dot(a, (p, 2.3), GREEN); arrow(a, (p, 2.3), (p, fp+.03), color=GREEN); dot(a, (p, fp), GREEN, ms=3.5)
dot(a, (1, .5))
setup(a, (-1, 3), (0, 2.6), [-1, 0, 1, 2, 3], [0, 1, 2], xl='$x$', yl='$t$', equal=False)
a.text(p+.08, 2.25, '$(x,t)$', fontsize=7.5); a.text(1, .24, '$(1,0.5)$', color=RED, fontsize=7.5, ha='center')
U, T = grid2((-2, 2), (-.6, 2.4), 800)
ok = np.sqrt(4*U**2+(2*T-1)**2) <= 2*T+1
b.contourf(U, T, ok.astype(float), levels=[.5, 1.5], colors=[BLUE_FILL], zorder=1)
u = np.linspace(-2, 2, 300); b.plot(u, u**2/2, color=BLUE, lw=1.5, zorder=2)
dot(b, (1, .5), GREEN); hollow(b, (1, .2), RED)
setup(b, (-2, 2), (-.6, 2.4), [-2, -1, 0, 1, 2], [0, 1, 2], xl='$u$', yl='$t$', equal=False)
b.text(.85, .62, '$(1,0.5)$', fontsize=7.5, ha='right'); b.text(1.12, .1, '$(1,0.2)$', fontsize=7.5, va='center')
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'f': '||(x-1,1/2)||', 'rotated': 'computed on grid; boundary t=u^2/2'})
