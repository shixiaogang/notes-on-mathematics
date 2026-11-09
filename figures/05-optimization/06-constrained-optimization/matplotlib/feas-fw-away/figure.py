from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
X, gp, st, v = fw(T=400, rule='exact'); Y, info = pairwise(T=4)
fig, axs = figure(width_mm=112, height_mm=46, ncols=3, gridspec_kw={'width_ratios': [1, 1, .95]})
for ax in axs[:2]: triangle(ax); contours(ax); active(ax, V[0], V[1]); dot(ax, bary(XS)); off(ax, (-.08, 1.08), (-.13, .93))
path(axs[0], bary(X)[:26], YELLOW, lw=1.1, ms=2.4); path(axs[1], bary(Y)[:4], GREEN)
ax = axs[2]; T = np.arange(1, 400); ax.loglog(T, f(X[1:400])-FS, color=YELLOW, lw=1.4); ax.loglog([1, 2], [f(Y[1])-FS, f(Y[2])-FS], '-o', color=GREEN, lw=1.4, ms=3, mew=0)
ax.loglog([2, 3], [f(Y[2])-FS, 1e-7], color=GREEN, lw=1.1, ls=(0, (2, 1.5)))
setup(ax, (1, 400), (1e-7, 3), [1, 10, 100], [1e-6, 1e-3, 1], xl='$t$', yl='$f-f^*$')
panels(fig, .01, .985, .985, .1, .1); fig.axes[2].set_position([.74, 13.8/46, .225, .68]); tags(fig, axs)
save(fig, HERE, 'figure', {'exact_FW': X[:4].tolist(), 'pairwise': Y.tolist()})
