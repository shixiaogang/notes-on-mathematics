from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Multiplier sets. (a) budget tau=2 with duplicated g1: l1+l2=1/2. (b) min x, x<=0, -x<=0: l2=1+l1. (c) min x, x^2<=0: stationarity residual is 1.
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panels(fig, .08, .985, .985, .32, .42)
a, b, c = axes
a.plot([.5, 0], [0, .5], color=PURPLE, lw=2.2, zorder=3); dot(a, (.25, .25), PURPLE, ms=4)
setup(a, (-.02, .8), (-.02, .8), [0, .5], [0, .5], xl='$\\lambda_1$', yl='$\\lambda_2$')
ls = np.linspace(0, 2, 10); b.plot(ls, 1+ls, color=PURPLE, lw=2.2, zorder=3)
arrow(b, (1.6, 2.6), (2, 3), color=PURPLE, lw=1.4, z=4)
setup(b, (-.05, 2.2), (-.05, 3.3), [0, 1, 2], [0, 1, 2, 3], xl='$\\lambda_1$', yl='$\\lambda_2$', equal=False)
l = np.linspace(0, 4, 10); c.plot(l, 1+0*l, color=RED, lw=1.6)
c.axhline(0, color=MUTED, lw=.7)
setup(c, (0, 4), (-.2, 1.4), [0, 2, 4], [0, 1], xl='$\\lambda$', yl='驻定残差', equal=False)
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'a': 'l1+l2=.5', 'b': 'l2=1+l1', 'c': 'residual 1+l*g prime 0 =1'})
