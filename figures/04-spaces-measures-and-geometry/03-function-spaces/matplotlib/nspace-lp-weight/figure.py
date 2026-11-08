from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# h1=1 on [0,1], h2=4 on [0,1/4]; L^p norms 1 and 4^(1-1/p).
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.3, wspace=.2)
ax = axes[0]
ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
ax.plot([0, .25, .25, 1], [4, 4, 0, 0], color=GREEN, lw=1.4)
ax.text(.62, 1.15, '$h_1$', ha='center', va='bottom'); ax.text(.3, 3.6, '$h_2$', ha='left', va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 4.6); ax.set_xticks([0, .25, 1]); ax.set_xticklabels(['0', '1/4', '1']); ax.set_yticks([0, 1, 4]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; p = np.linspace(1, 16, 300)
ax.plot(p, 0*p+1, color=BLUE, lw=1.4)
ax.plot(p, 4**(1-1/p), color=GREEN, lw=1.4)
ax.plot([1, 16], [4, 4], color=MUTED, lw=.85, ls=(0, (3, 2)))
for a in (1, 2, 4):
    v = 4**(1-1/a); ax.plot([a], [v], 'o', ms=3.4, color=GREEN, mew=0)
ax.text(2.3, 1.78, '$2$', ha='left', va='top', fontsize=7.5); ax.text(4.2, 2.55, '$2\\sqrt{2}$', ha='left', va='top', fontsize=7.5)
ax.text(12, 3.45, r'$\Vert h_2\Vert_p$', ha='center', va='center'); ax.text(12, 1.25, r'$\Vert h_1\Vert_p$', ha='center', va='bottom')
ax.set_xlim(1, 16); ax.set_ylim(0, 4.6); ax.set_xticks([1, 2, 4, 8, 16]); ax.set_yticks([0, 1, 4]); ax.set_xlabel('$p$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'h1=1, h2=4*1[0,1/4]; ||h1||_p=1, ||h2||_p=4^(1-1/p)'})
