from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Secants at x0=1, h=0.5 on u=x^3 compared with the tangent.
u = lambda x: x**3; du = lambda x: 3*x**2
x0, h = 1., .5; X = np.linspace(.3, 1.62, 300)
fig, ax = figure(width_mm=86, height_mm=52)
ax.plot(X, u(X), color=BLUE, lw=1.4)
def line(s, c, ls='-', lw=1.1):
    t = np.array([.55, 1.62]); ax.plot(t, u(x0)+s*(t-x0), color=c, ls=ls, lw=lw)
fw = (u(x0+h)-u(x0))/h; bw = (u(x0)-u(x0-h))/h; ce = (u(x0+h)-u(x0-h))/(2*h)
line(du(x0), PURPLE, DASH, 1.0); line(fw, YELLOW); line(bw, YELLOW, DOT, 1.2); line(ce, GREEN, '-', 1.3)
ax.plot([x0-h, x0+h], [u(x0-h), u(x0+h)], 'o', ms=3.8, color=GREEN, mew=0, zorder=5)
ax.plot([x0], [u(x0)], 'o', ms=4.6, color=RED, mew=0, zorder=6)
lab(ax, 1.635, u(x0)+fw*.62, '前向', YELLOW, ha='left', va='center'); lab(ax, 1.635, u(x0)+bw*.62, '后向', YELLOW, ha='left', va='center'); lab(ax, 1.635, u(x0)+ce*.62, '中心', GREEN, ha='left', va='center')
ax.set_xlim(.3, 1.85); ax.set_xticks([x0-h, x0, x0+h]); ax.set_xticklabels(['$x-h$', '$x$', '$x+h$']); ax.set_yticks([])
ax.set_ylabel('$u$', labelpad=2)
save(fig, HERE, 'figure', {'x0': x0, 'h': h, 'tangent': float(du(x0)), 'forward': float(fw), 'backward': float(bw), 'central': float(ce)})
print(du(x0), fw, bw, ce)
