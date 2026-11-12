from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Preimage of {X^2 <= 0.5} intersected with the support (0,1) and (-1,2).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.25)
r = np.sqrt(.5)
for ax, (a, b) in zip(axes, [(0, 1), (-1, 2)]):
    x = np.linspace(a, b, 400)
    lo = max(a, -r)
    ax.axvspan(lo, r, color=BLUE_FILL, lw=0)
    ax.plot(x, x**2, color=BLUE, lw=1.4)
    ax.axhline(.5, color=RED, lw=1.1)
    for e in ([lo, r] if lo > a else [r]):
        ax.plot([e, e], [0, .5], color=STROKE, lw=.7, ls=DOT); dot(ax, e, .5, RED, ms=3.6)
    ax.axhline(0, color=STROKE, lw=.6)
    ax.set_xlim(a-.05, b+.05); axlab(ax, '$x$')
    lab(ax, .3 if b == 1 else .95, .8 if b == 1 else 3.3, '$g(x)=x^2$', BLUE, ha='right', va='center')
axes[0].set_ylim(-.05, 1.05); axes[0].set_xticks([0, r, 1]); axes[0].set_xticklabels(['0', '$\\sqrt{0.5}$', '1']); axes[0].set_yticks([0, .5, 1])
axes[1].set_ylim(-.15, 4.1); axes[1].set_xticks([-1, 0, 1, 2]); axes[1].set_xticklabels(['$-1$', '0', '1', '2']); axes[1].set_yticks([0, .5, 2, 4])
lab(axes[0], .02, .53, '$y=0.5$', RED, va='bottom'); lab(axes[1], 1.1, .62, '$y=0.5$', RED, va='bottom')
tags(fig, axes)
save(fig, HERE, 'figure', {'sqrt_half': r})
