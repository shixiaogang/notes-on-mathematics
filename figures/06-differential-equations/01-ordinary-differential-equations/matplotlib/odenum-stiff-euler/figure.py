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

# Target: explicit Euler on the stiff system: h=0.03 is stable, h=0.05 is not.
T = 1.2
fig, ax = figure(width_mm=112, height_mm=52, ncols=2)
tt = np.linspace(0, T, 500)
for a, h, c in zip(ax, (.03, .05), (GREEN, RED)):
    n = int(round(T/h)); x = np.array([1., 0.]); xs = [x.copy()]
    for k in range(n):
        x = x+h*g2(k*h, x); xs.append(x.copy())
    xs = np.array(xs)
    a.plot(tt, exact_stiff(tt)[1], color=BLUE, lw=1.4)
    a.plot(h*np.arange(n+1), xs[:, 1], 'o-', color=c, lw=.95, ms=2.4)
    a.plot([0], [0], 'o', color=RED, ms=4.5, zorder=5, clip_on=False)
    a.set_xlabel(r'$t$'); a.set_xlim(0, T)
ax[0].set_ylabel(r'$x_2$'); ax[0].set_ylim(0, 1.6); ax[1].set_ylim(-30, 30); ax[1].set_xlim(0, .6)
panel(ax[0], r'(a) $h=0.03$', -.3); panel(ax[1], r'(b) $h=0.05$', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'explicit Euler, stiff system'})
