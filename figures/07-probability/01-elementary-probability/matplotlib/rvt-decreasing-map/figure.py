from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X ~ Exp(2), Y = exp(-X): preimage of {Y<=0.4} and the law F_Y(y)=y^2, f_Y(y)=2y.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.25)
ax = axes[0]; x = np.linspace(0, 3.2, 400); x0 = -np.log(.4)
ax.axvspan(x0, 3.2, color=BLUE_FILL, lw=0)
ax.plot(x, np.exp(-x), color=BLUE, lw=1.4); ax.axhline(.4, color=RED, lw=1.1)
ax.plot([x0, x0], [0, .4], color=STROKE, lw=.7, ls=DOT); dot(ax, x0, .4, RED, ms=3.6)
ax.set_xlim(0, 3.2); ax.set_ylim(0, 1.05); ax.set_xticks([0, x0, 2, 3]); ax.set_xticklabels(['0', '$-\\ln 0.4$', '2', '3']); ax.set_yticks([0, .4, 1]); axlab(ax, '$x$')
lab(ax, .35, .78, '$g(x)=\\mathrm{e}^{-x}$', BLUE, ha='left')
ax = axes[1]; y = np.linspace(0, 1, 300)
ax.plot(y, y**2, color=BLUE, lw=1.4); ax.plot(y, 2*y, color=PURPLE, lw=1.4); ax.plot(y, 1-y**2, color=YELLOW, lw=1.5, ls=DASH)
lab(ax, .62, .2, '$F_Y=y^2$', BLUE); lab(ax, .55, 1.25, '$f_Y=2y$', PURPLE, ha='right'); lab(ax, .08, .85, '$1-y^2$', YELLOW)
ax.set_xlim(0, 1); ax.set_ylim(0, 2.05); ax.set_xticks([0, .4, 1]); ax.set_yticks([0, 1, 2]); axlab(ax, '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'x0': float(x0), 'F(0.4)': .16})
