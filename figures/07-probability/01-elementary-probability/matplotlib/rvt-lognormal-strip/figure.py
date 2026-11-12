from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X ~ N(0,1), Y = exp(X); strip [0.5,0.7] and its image carry the same probability.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.06, right=.98, bottom=.28, top=.95, wspace=.22)
a, b = .5, .7; mass = float(Phi(b)-Phi(a))
ax = axes[0]; x = np.linspace(-3.2, 3.2, 600); xs = np.linspace(a, b, 50)
ax.fill_between(xs, 0, phi(xs), color=BLUE_FILL, ec=BLUE, lw=.6)
ax.plot(x, phi(x), color=BLUE, lw=1.4); dot(ax, 0, 0, RED)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(0, .45); ax.set_xticks([-2, 0, a, b, 2]); ax.set_xticklabels(['$-2$', '0', '', '', '2']); ax.set_yticks([0, .2, .4]); axlab(ax, '$x$')
ax = axes[1]
def ln(y): return np.exp(-np.log(y)**2/2)/(y*np.sqrt(2*pi))
y = np.linspace(1e-3, 6, 800); ys = np.linspace(np.exp(a), np.exp(b), 60)
ax.fill_between(ys, 0, ln(ys), color=BLUE_FILL, ec=BLUE, lw=.6)
ax.plot(y, ln(y), color=BLUE, lw=1.4); dot(ax, 1, 0, RED)
ax.axvline(np.exp(.5), color=GREEN, lw=1.0, ymax=.9)
ax.set_xlim(0, 6); ax.set_ylim(0, .72); ax.set_xticks([0, 1, 2, 4, 6]); ax.set_yticks([0, .3, .6]); axlab(ax, '$y$')
lab(ax, np.exp(.5)+.08, .62, '均值', GREEN, ha='left')
tags(fig, axes)
save(fig, HERE, 'figure', {'mass': mass, 'image': [float(np.exp(a)), float(np.exp(b))], 'quad_image': float(np.trapezoid(ln(ys), ys))})
