from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# X ~ Unif(-1,1). Independent sum: triangle density (2-|x|)/4, cf (sin t/t)^2. Dependent sum 2X: Unif(-2,2), cf sin(2t)/(2t).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; x = np.linspace(-2.6, 2.6, 1001)
ax.plot(x, np.where(np.abs(x) < 1, .5, 0), color=BLUE, lw=1.4)
ax.plot(x, np.where(np.abs(x) < 2, .25, 0), color=YELLOW, lw=1.6)
ax.plot(x, np.maximum(0, (2-np.abs(x))/4), color=GREEN, lw=1.4)
lab(ax, -.55, .53, r'$X$', BLUE); lab(ax, 1.15, .32, r'$X+Y$', GREEN); lab(ax, -2.0, .27, r'$2X$', YELLOW)
ax.set_xlim(-2.6, 2.6); ax.set_ylim(0, .62); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, .25, .5])
axlab(ax, r'$x$')
ax = axes[1]; t = np.linspace(1e-9, 10, 1200)
ax.axhline(0, color=GRID, lw=.6, zorder=0)
ax.plot(t, np.sin(t)/t, color=BLUE, lw=1.4); ax.plot(t, (np.sin(t)/t)**2, color=GREEN, lw=1.4); ax.plot(t, np.sin(2*t)/(2*t), color=YELLOW, lw=1.6)
dot(ax, np.pi/2, 4/np.pi**2, RED, ms=3.8); dot(ax, np.pi/2, 0, RED, ms=3.8)
ax.set_xlim(0, 10); ax.set_ylim(-.3, 1.05); ax.set_xticks([0, np.pi/2, 5, 10]); ax.set_xticklabels(['$0$', r'$\pi/2$', '$5$', '$10$']); ax.set_yticks([0, .5, 1])
axlab(ax, r'$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'indep_at_pi/2': 4/np.pi**2, 'dep_at_pi/2': 0.0})
