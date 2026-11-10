from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: the four RK4 stage points of the first step, h=1/2.
h = .5
k1 = f(0, X0); y2 = X0+h/2*k1; k2 = f(0, y2); y3 = X0+h/2*k2; k3 = f(0, y3); y4 = X0+h*k3; k4 = f(0, y4)
xn = X0+h/6*(k1+2*k2+2*k3+k4)
t = np.linspace(0, .56, 200)
fig, ax = figure(width_mm=100, height_mm=62)
ax.plot(t, exact(t), color=BLUE, lw=1.4)
L = .05
for (tt, yy, s, lab, dx, dy) in ((0, X0, k1, r'$k_1$', .012, -.0085), (h/2, y2, k2, r'$k_2$', .006, -.0085), (h/2, y3, k3, r'$k_3$', -.02, .0075), (h, y4, k4, r'$k_4$', .01, -.009)):
    ax.plot([tt-L, tt+L], [yy-L*s, yy+L*s], color=PURPLE, lw=1.4, zorder=4)
    ax.plot([tt], [yy], 'o', color=PURPLE, ms=3.6, zorder=5)
    ax.text(tt+dx, yy+dy, lab, color=PURPLE, ha='center')
ax.plot([0, h], [X0, xn], color=GREEN, lw=1.2, zorder=3)
ax.plot([0], [X0], 'o', color=RED, ms=4.8, zorder=6)
ax.plot([h], [xn], 'o', color=GREEN, ms=4.2, zorder=6)
ax.set_xticks([0, h/2, h]); ax.set_xticklabels([r'$t_0$', r'$t_0+h/2$', r'$t_1$'])
ax.set_xlim(-.07, .62); ax.set_ylim(.185, .32); ax.set_xlabel(r'$t$'); ax.set_ylabel(r'$x$')
ax.annotate(r'$x^{(1)}$', xy=(h, xn), xytext=(.57, .278), color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.7))
save(fig, Path(__file__).resolve().parent, 'figure', {'stages': [k1, k2, k3, k4], 'x1': xn})
