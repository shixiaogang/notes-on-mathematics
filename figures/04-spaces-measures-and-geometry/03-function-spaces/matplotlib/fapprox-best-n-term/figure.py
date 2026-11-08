from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f=3*1_[0,3/4)-1_[3/4,1) with Haar coefficients 2, 1, 0, sqrt2 for phi, psi00, psi10, psi11.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.27, wspace=.3)
def step(ax, xs, ys, c, lw=1.4):
    for a, b, y in zip(xs[:-1], xs[1:], ys): ax.plot([a, b], [y, y], color=c, lw=lw, solid_capstyle='butt')
    for i in range(1, len(ys)):
        ax.plot([xs[i], xs[i]], [ys[i-1], ys[i]], color=c, lw=.85, ls=(0, (2, 2)))
fx, fy = [0, .75, 1], [3, -1]
ax = axes[0]
step(ax, fx, fy, BLUE); step(ax, [0, .5, 1], [3.0, 1.0], GREEN, 1.3)
ax.text(.25, 3.3, '$2\\varphi+\\psi_{0,0}$', ha='center'); ax.text(.875, -1.72, '$f$', ha='center')
ax = axes[1]
step(ax, fx, fy, BLUE); step(ax, [0, .5, .75, 1], [2, 4, 0], GREEN, 1.3)
ax.text(.03, 1.2, r'$2\varphi+\sqrt{2}\psi_{1,1}$', ha='left'); ax.text(.875, -1.72, '$f$', ha='center')
for ax in axes[:2]:
    ax.set_xlim(0, 1); ax.set_ylim(-2.2, 4.8); ax.set_xticks([0, .5, .75, 1]); ax.set_xticklabels(['0', '1/2', '3/4', '1']); ax.set_yticks([-1, 0, 1, 2, 3, 4]); ax.axhline(0, color=MUTED, lw=.85); ax.set_xlabel('$x$', labelpad=0)
ax = axes[2]
names = [r'$\varphi$', r'$\psi_{0,0}$', r'$\psi_{1,0}$', r'$\psi_{1,1}$']; c = [2, 1, 0, np.sqrt(2)]; cols = [GREEN, BLUE, BLUE, GREEN]
ax.bar(range(4), c, width=.58, color=cols)
ax.set_xticks(range(4)); ax.set_xticklabels(names); ax.set_ylim(0, 2.4); ax.set_yticks([0, 1, 2]); ax.set_ylabel(r'$\vert c\vert$', labelpad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=2 phi + psi00 + sqrt2 psi11; best two terms keep phi, psi11'})
