from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Tail of the box solution on a log axis, and the sqrt(t) front of a level set.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.12, wspace=.28, bottom=.27)
xx = np.linspace(.5, 4, 300); cc = shades(3)
def tail(x, t):
    s = 2*np.sqrt(t); return .5*(erfc((x-.5)/s)-erfc((x+.5)/s))
ax = axes[0]
for t, c in zip((.01, .1, 1.), cc): ax.semilogy(xx, tail(xx, t), color=c, lw=1.4)
lab(ax, 1.25, 2e-14, '$t=0.01$', cc[0], ha='right'); lab(ax, 3.2, 1e-5, '$0.1$', cc[1], ha='left'); lab(ax, 3.2, .07, '$1$', cc[2], ha='left')
ax.set_xlim(.5, 4); ax.set_ylim(1e-16, 2); ax.minorticks_off(); ax.set_xticks([1, 2, 3, 4]); ax.set_yticks([1, 1e-8, 1e-16]); ax.set_yticklabels(['1', '$10^{-8}$', '$10^{-16}$']); axlab(ax, yl='$u(x,t)$')
ax = axes[1]; T = np.linspace(.0004, 1, 400)
xs = xx*0
lv = 1e-3; fr = []
for t in T:
    a, b = .5, 30.
    for _ in range(70):
        m = .5*(a+b)
        if tail(np.array(m), t) > lv: a = m
        else: b = m
    fr.append(.5*(a+b))
fr = np.array(fr)
ax.plot(T, fr, color=BLUE, lw=1.4)
ax.plot(T, .5+(fr[-1]-.5)*T, color=YELLOW, lw=1.2, ls=DASH)
lab(ax, .05, 3.4, r'$u=10^{-3}$', BLUE, ha='left'); lab(ax, .66, 2.5, '直线', YELLOW, ha='left', va='top')
ax.set_xlim(0, 1); ax.set_ylim(.4, 4); ax.set_xticks([0, .5, 1]); ax.set_yticks([1, 2, 3, 4]); axlab(ax, '$t$', '$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u(2,.01)': float(tail(np.array(2.), .01)), 'u(3,.1)': float(tail(np.array(3.), .1))})
