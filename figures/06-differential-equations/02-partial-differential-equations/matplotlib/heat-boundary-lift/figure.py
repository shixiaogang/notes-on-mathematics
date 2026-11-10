from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Lift for u(0,t)=0, u(1,t)=1, u0=0: w=x, v=u-w.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.105, wspace=.26, bottom=.27)
k = np.arange(1, 1201); xx = np.linspace(0, 1, 1201)
def v(t): return (2*(-1.)**k/(k*pi))[:, None]*np.exp(-(k*pi)**2*t)[:, None]*np.sin(np.outer(k, pi*xx))
V = lambda t: v(t).sum(0)
ts = (.005, .03, .1); cc = shades(3)
ax = axes[0]
ax.plot(xx, -xx, color=RED, lw=1.5, label='')
for t, c in zip(ts, cc): ax.plot(xx, V(t), color=c, lw=1.4)
ax.axhline(0, color=STROKE, lw=.6)
lab(ax, .35, -.47, '$v(\\cdot,0)=-x$', RED, ha='right')
ax.set_xlim(0, 1); ax.set_ylim(-1.08, .1); ax.set_xticks([0, .5, 1]); ax.set_yticks([-1, -.5, 0]); axlab(ax, yl='$v$')
ax = axes[1]
ax.plot(xx, xx, color=YELLOW, lw=1.3, ls=DASH)
for t, c in zip(ts, cc): ax.plot(xx, xx+V(t), color=c, lw=1.4)
dot(ax, 0, 0, RED); dot(ax, 1, 1, RED)
lab(ax, .42, .5, '$w=x$', YELLOW, ha='right')
ax.set_xlim(0, 1); ax.set_ylim(-.04, 1.08); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); axlab(ax, yl='$u$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u(.5,.1)': float(.5+V(.1)[600])})
