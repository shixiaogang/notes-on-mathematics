from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# (a) min (x-2)^2, x-1<=0: lam=2, L=(x-1)^2+1 lies below f on the feasible side. (b) min -x^2 on [-1,1]: three KKT points.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .07, .985, .985, .27, .22)
a, b = axes
x = np.linspace(-1, 2.6, 400); a.axvspan(-1, 1, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
a.plot(x, (x-2)**2, color=BLUE, lw=1.4); a.plot(x, (x-1)**2+1, color=PURPLE, lw=1.4)
setup(a, (-1, 2.6), (0, 5), [-1, 0, 1, 2], [0, 2, 4], xl='$x$', yl='', equal=False)
a.axvline(1, color=EDGE, lw=1.6); dot(a, (1, 1))
a.text(-.42, 4.25, '$f$', color=BLUE, fontsize=8); a.text(-.92, 1.5, '$\\mathcal{L}(\\cdot,\\lambda^{*})$'.replace('\\mathcal{L}', 'L'), color=PURPLE, fontsize=8)
x = np.linspace(-1.4, 1.4, 300); b.axvspan(-1, 1, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
b.plot(x, -x**2, color=BLUE, lw=1.4)
setup(b, (-1.4, 1.4), (-1.5, .35), [-1, 0, 1], [-1, 0], xl='$x$', yl='', equal=False)
b.axvline(-1, color=EDGE, lw=1.6); b.axvline(1, color=EDGE, lw=1.6)
dot(b, (-1, -1)); dot(b, (1, -1)); dot(b, (0, 0), YELLOW)
b.text(0, .1, 'KKT 点，最大点', color=INK, fontsize=7.5, ha='center')
b.text(-.05, -1.18, 'KKT 点，全局最小点', color=INK, fontsize=7.5, ha='center')
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'a': {'lambda': 2, 'L': '(x-1)^2+1'}, 'b': 'f=-x^2'})
