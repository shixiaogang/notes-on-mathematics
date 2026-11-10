from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Value at x=0.7, t=0.04 as a Gaussian-weighted average of the box.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.26, bottom=.27)
yy = np.linspace(-2, 2, 1600); x0, t = .7, .04
ax = axes[0]; w = gauss(x0-yy, t); b = (np.abs(yy) < .5)*1.
ax.fill_between(yy, 0, w*b, color=BLUE_FILL, lw=0)
ax.plot(yy, b, color=RED, lw=1.5); ax.plot(yy, w, color=PURPLE, lw=1.4)
dot(ax, x0, 0, INK, ms=3.8)
lab(ax, -1.45, 1.1, '$u_0(y)$', RED); lab(ax, 1.0, 1.2, '$G(0.7-y,\\,t)$', PURPLE, ha='left')
ax.set_xlim(-2, 2); ax.set_ylim(0, 1.55); ax.set_xticks([-1, 0, .7, 1.5]); ax.set_xticklabels(['-1', '0', '0.7', '1.5']); ax.set_yticks([0, 1]); axlab(ax, '$y$')
ax = axes[1]
ax.plot(yy, b, color=RED, lw=1.5); ax.plot(yy, box(yy, t), color=BLUE, lw=1.4)
v = float(box(np.array(x0), t)); dot(ax, x0, v, GREEN, ms=5)
ax.plot([x0, x0], [0, v], color=STROKE, lw=.7, ls=DOT)
lab(ax, 1.25, .5, '$u(x,0.04)$', BLUE, ha='center')
ax.set_xlim(-2, 2); ax.set_ylim(0, 1.25); ax.set_xticks([-1, 0, .7, 1.5]); ax.set_xticklabels(['-1', '0', '0.7', '1.5']); ax.set_yticks([0, 1]); axlab(ax)
tags(fig, axes)
save(fig, HERE, 'figure', {'u(.7,.04)': v, 'quadrature': float(np.trapezoid(w*b, yy))})
print(v, np.trapezoid(w*b, yy))
