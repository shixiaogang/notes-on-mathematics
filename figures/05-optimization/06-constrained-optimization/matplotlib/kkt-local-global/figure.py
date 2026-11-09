from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# min x1 subject to x1 >= w(x2), w(y)=(y^2-1)^2+0.3*y: two wells give a local and a global minimizer.
fig, ax = figure(width_mm=84, height_mm=62)
w = lambda y: (y*y-1)**2+.3*y
wp = lambda y: 4*y*(y*y-1)+.3
def newton(y):
    for _ in range(40): y -= wp(y)/(12*y*y-4)
    return y
y1, y2 = newton(1.), newton(-1.)
ys = np.linspace(-1.75, 1.75, 500)
xl, yl = (-1.0, 2.6), (-1.75, 1.75)
ax.fill_betweenx(ys, w(ys), xl[1], where=w(ys) <= xl[1], facecolor=BLUE_FILL, edgecolor='none', zorder=1)
ax.plot(w(ys), ys, color=EDGE, lw=2.0, zorder=3)
for v in (-.5, 0, .5, 1, 1.5, 2): ax.axvline(v, color=BLUE, lw=.7, zorder=1.5)
setup(ax, xl, yl, range(-1, 3), [-1, 0, 1])
dot(ax, (w(y2), y2)); dot(ax, (w(y1), y1), YELLOW)
ax.text(w(y2)+.2, y2-.03, '全局最小点', color=RED, fontsize=7.5, va='center', bbox=dict(fc=BLUE_FILL, ec='none', pad=1), zorder=6)
ax.text(w(y1)+.2, y1-.0, '局部最小点', color=INK, fontsize=7.5, va='center', bbox=dict(fc=BLUE_FILL, ec='none', pad=1), zorder=6)
arrow(ax, (w(y1), y1), (w(y1)-.55, y1), color=BLUE)
ax.text(w(y1)-.3, y1+.18, '$-\\nabla f$', color=BLUE, fontsize=8, ha='center')
save(fig, HERE, 'figure', {'local': [float(w(y1)), float(y1)], 'global': [float(w(y2)), float(y2)]})
print(w(y1), y1, w(y2), y2)
