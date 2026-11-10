from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

LAM = 50.0
def exact_stiff(t):
    t = np.asarray(t, float)
    return np.exp(-t), LAM/(LAM-1)*(np.exp(-t)-np.exp(-LAM*t))
def g2(t, x):
    return np.array([-x[0], LAM*(x[0]-x[1])])

# Target: two time scales in the exact solution of the fast-chases-slow system.
fig, ax = figure(width_mm=112, height_mm=52, ncols=2)
t = np.linspace(0, 4, 600); s = np.linspace(0, .2, 300)
for a, tt in zip(ax, (t, s)):
    x1, x2 = exact_stiff(tt)
    a.plot(tt, x1, color=YELLOW, lw=1.4); a.plot(tt, x2, color=BLUE, lw=1.4)
    a.plot([0, 0], [1, 0], 'o', color=RED, ms=4.5, zorder=5, clip_on=False)
    a.set_xlabel(r'$t$')
ax[0].set_ylabel('状态'); ax[0].set_ylim(0, 1.08); ax[1].set_ylim(0, 1.08)
ax[0].set_xlim(0, 4); ax[1].set_xlim(0, .2)
ax[0].text(1.6, .42, r'$x_2$', color=BLUE); ax[0].text(.9, .22, r'$x_1$', color=YELLOW)
ax[1].text(.15, .78, r'$x_1$', color=YELLOW); ax[1].text(.075, 1.0, r'$x_2$', color=BLUE)
panel(ax[0], '(a)', -.3); panel(ax[1], '(b)', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': "x1'=-x1, x2'=50(x1-x2), x(0)=(1,0)"})
