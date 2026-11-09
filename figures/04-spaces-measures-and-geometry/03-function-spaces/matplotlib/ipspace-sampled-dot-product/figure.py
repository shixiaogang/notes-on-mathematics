from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f=1+x, g=x on [-1,1]; N=4 midpoint samples, h=1/2; h*sum f_i g_i = 0.625; exact integral 2/3.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.3, wspace=.22)
x = np.linspace(-1, 1, 401); xs = np.array([-.75, -.25, .25, .75])
f = lambda t: 1+t
g = lambda t: t
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(x, f(x), color=BLUE, lw=1.4); ax.plot(x, g(x), color=GREEN, lw=1.4)
ax.vlines(xs, g(xs), f(xs), color=GRID, lw=.85)
ax.plot(xs, f(xs), 'o', ms=3.6, color=BLUE, mew=0); ax.plot(xs, g(xs), 'o', ms=3.6, color=GREEN, mew=0)
ax.text(.55, 1.75, '$f$', color=INK); ax.text(.55, .22, '$g$', color=INK)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.15, 2.2); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_xticklabels(['-1', '-1/2', '0', '1/2', '1'])
ax.set_yticks([-1, 0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
xx = np.linspace(-1, 1, 401); y = f(xx)*g(xx)
vals = f(xs)*g(xs)
ax.axhline(0, color=MUTED, lw=.85)
ax.bar(xs, vals, width=.5, color=[RED_FILL if v < 0 else BLUE_FILL for v in vals], edgecolor=[RED if v < 0 else BLUE for v in vals], lw=.85)
ax.plot(xx, y, color=BLUE, lw=1.4)
ax.text(.47, 1.72, '$fg$', color=INK)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-.5, 2.2); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_xticklabels(['-1', '-1/2', '0', '1/2', '1']); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
print('sum', float(.5*vals.sum()))
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1+x, g=x, midpoints -3/4,-1/4,1/4,3/4, h=1/2; h*sum f g = 5/8; integral = 2/3'})
