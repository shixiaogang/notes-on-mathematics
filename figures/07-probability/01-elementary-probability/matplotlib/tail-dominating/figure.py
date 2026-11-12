from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'tail-common'))
from tail_fig import *
# Indicator of the tail event (blue) and the function that dominates it (purple):
# (a) x/t on x>=0, t=2;  (b) (x-mu)^2/t^2, mu=0, t=1;  (c) e^{lambda(x-t)}, t=2, lambda=1.
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, left=.06, right=.985, wspace=.28, bottom=.22)
def ind(ax, xs, mask):
    y = mask.astype(float)
    ax.fill_between(xs, 0, y, where=mask, color=BLUE_FILL, lw=0, step=None)
    # draw indicator as two pieces to avoid vertical connectors
    edges = np.flatnonzero(np.diff(mask.astype(int))) + 1
    for seg in np.split(np.arange(len(xs)), edges):
        ax.plot(xs[seg], y[seg], color=BLUE, lw=1.4, solid_capstyle='butt')
ax = axes[0]; x = np.linspace(0, 4, 801); t = 2
ind(ax, x, x >= t); ax.plot(x, x/t, color=PURPLE, lw=1.4)
ax.plot([t, t], [0, 2.2], color=RED, lw=.9, ls=DASH)
lab(ax, 3.0, 1.7, '$x/t$', PURPLE, ha='right'); lab(ax, t, -.06, '$t$', RED, ha='center', va='top', zorder=7)
ax.set_xlim(0, 4); ax.set_ylim(0, 2.2); ax.set_xticks([]); ax.set_yticks([0, 1]); lab(ax, 1.0, -.03, '$x$', INK, transform=ax.transAxes, ha='right', va='top')
ax = axes[1]; x = np.linspace(-2, 2, 801)
ind(ax, x, np.abs(x) >= 1); ax.plot(x, x**2, color=PURPLE, lw=1.4)
for v in (-1, 1): ax.plot([v, v], [0, 2.2], color=RED, lw=.9, ls=DASH)
lab(ax, 0, 1.25, r'$\frac{(x-\mu)^2}{t^2}$', PURPLE, ha='center')
lab(ax, -1, -.06, r'$\mu-t$', RED, ha='center', va='top', zorder=7); lab(ax, 1, -.06, r'$\mu+t$', RED, ha='center', va='top', zorder=7)
ax.set_xlim(-2, 2); ax.set_ylim(0, 2.2); ax.set_xticks([]); ax.set_yticks([0, 1]); lab(ax, 1.0, -.03, '$x$', INK, transform=ax.transAxes, ha='right', va='top')
ax = axes[2]; x = np.linspace(-1, 3, 801); t = 2
ind(ax, x, x >= t); ax.plot(x, np.exp(x-t), color=PURPLE, lw=1.4)
ax.plot([t, t], [0, 2.2], color=RED, lw=.9, ls=DASH)
lab(ax, 1.9, 1.75, r'$\mathrm{e}^{\lambda(x-t)}$', PURPLE, ha='right'); lab(ax, t, -.06, '$t$', RED, ha='center', va='top', zorder=7)
ax.set_xlim(-1, 3); ax.set_ylim(0, 2.2); ax.set_xticks([]); ax.set_yticks([0, 1]); lab(ax, 1.0, -.03, '$x$', INK, transform=ax.transAxes, ha='right', va='top')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'indicator x>=2 vs x/2', 'b': 'indicator |x|>=1 vs x^2', 'c': 'indicator x>=2 vs exp(x-2)'})
