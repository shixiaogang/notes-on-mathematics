from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# X has density 2x on (0,1); Y = X^2 then has F_Y(y) = y, i.e. density 1 on (0,1).
# Both routes give E[Y] = 1/2: integral of x^2*2x dx, or integral of y*1 dy.
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.09, right=.98, bottom=.3, wspace=.3)
x = np.linspace(0, 1, 401)
ax = axes[0]
ax.fill_between(x, 0, 2*x, color=BLUE_FILL, lw=0); ax.plot(x, 2*x, color=BLUE, lw=1.4)
ax.plot(x, x**2*2*x, color=GREEN, lw=1.4)
lab(ax, .42, 1.1, '$2x$', BLUE, ha='right'); lab(ax, .98, .9, '$x^2\\cdot 2x$', GREEN, ha='right')
lab(ax, .5, .45, '面积 1/2', GREEN, ha='center')
ax.set_xlim(0, 1.02); ax.set_ylim(0, 2.1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, 1, 2])
axlab(ax, '$x$')
ax = axes[1]
ax.fill_between(x, 0, 1+0*x, color=BLUE_FILL, lw=0); ax.plot(x, 1+0*x, color=BLUE, lw=1.4)
ax.plot(x, x, color=GREEN, lw=1.4)
lab(ax, .2, 1.07, '$f_Y(y)=1$', BLUE, ha='left'); lab(ax, .98, .62, '$y\\cdot 1$', GREEN, ha='right')
lab(ax, .62, .25, '面积 1/2', GREEN, ha='center')
ax.set_xlim(0, 1.02); ax.set_ylim(0, 2.1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, 1, 2])
axlab(ax, '$y$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E[X^2] via x': float(np.trapezoid(2*x**3, x)), 'E[Y] via y': float(np.trapezoid(x, x))})
