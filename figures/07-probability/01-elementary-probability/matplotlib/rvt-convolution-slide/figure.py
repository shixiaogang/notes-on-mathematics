from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# f_X = f_Y = 1 on (0,1); overlap of f_X(x) and f_Y(z-x) at z = 0.7 and 1.4, and the triangle f_Z.
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.05, right=.98, bottom=.3, top=.95, wspace=.3)
def box(ax, a, b, c, lw=1.4, ls='-'):
    ax.plot([a-.6, a, a, b, b, b+.6], [0, 0, 1, 1, 0, 0], color=c, lw=lw, ls=ls)
for ax, z in zip(axes[:2], (.7, 1.4)):
    lo, hi = max(0, z-1), min(1, z)
    ax.fill_between([lo, hi], 0, 1, color=BLUE_FILL, lw=0)
    box(ax, 0, 1, BLUE); box(ax, z-1, z, PURPLE, lw=1.2, ls=DASH)
    ax.set_xlim(-.7, 2.1); ax.set_ylim(0, 1.25); ax.set_xticks([0, .7, 1] if z < 1 else [0, .4, 1.4]); ax.set_yticks([0, 1]); axlab(ax, '$x$')
    ax.tick_params(axis='x', labelsize=7)
    lab(ax, (lo+hi)/2, 1.06, f'{hi-lo:.1f}', INK, ha='center', va='bottom')
ax = axes[2]; z = np.linspace(-.2, 2.2, 400); ax.plot(z, np.clip(np.minimum(z, 2-z), 0, None), color=BLUE, lw=1.4)
dot(ax, .7, .7, RED); dot(ax, 1.4, .6, RED)
ax.set_xlim(-.2, 2.2); ax.set_ylim(0, 1.25); ax.set_xticks([0, .7, 1.4, 2]); ax.set_yticks([0, 1]); axlab(ax, '$z$')
tags(fig, axes)
save(fig, HERE, 'figure', {'overlap(0.7)': .7, 'overlap(1.4)': .6})
