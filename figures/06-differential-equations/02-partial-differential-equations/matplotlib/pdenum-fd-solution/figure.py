from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Three-point scheme for the running example at h=1/4 and h=1/8, with pointwise error.
X = np.linspace(0, 1, 801)
def fd(n):
    h = 1/n; xi = np.linspace(h, 1-h, n-1); b = PI**2*np.sin(PI*xi); b[-1] += 1/h**2
    return xi, np.linalg.solve(lap1d(n), b)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.25, bottom=.27)
ax = axes[0]; ax.plot(X, uex(X), color=BLUE, lw=1.4)
xi, U = fd(4); ax.plot(np.r_[0, xi, 1], np.r_[0, U, 1], color=GREEN, lw=1.2, marker='o', ms=3.8, mew=0)
ax.plot([0, 1], [0, 1], 'o', ms=4.6, color=RED, mew=0, zorder=6, clip_on=False)
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, 1.75); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=1)
ax = axes[1]; rec = {}
for n, c, sc in ((4, RED, 1), (8, YELLOW, 4)):
    xi, U = fd(n); e = U-uex(xi); rec[n] = float(e.max())
    ax.plot(np.r_[0, xi, 1], sc*np.r_[0, e, 0], color=c, lw=1.3, marker='o', ms=3.2, mew=0)
lab(ax, .5, .0585, '$h=1/4$', RED, ha='center', va='bottom'); lab(ax, .5, .0445, r'$h=1/8,\ \times 4$', YELLOW, ha='center', va='top')
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, .07); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .05]); ax.set_xlabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'max_error': rec}); print(rec)
