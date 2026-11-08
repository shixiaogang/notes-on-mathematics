from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# x^n, narrow spikes n*1_(0,1/n), and the typewriter sequence h_{k,j}, first 15 terms.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.99, top=.97, bottom=.28, wspace=.2)
ax = axes[0]; x = np.linspace(0, 1, 500)
for n, c in ((2, BLUE), (8, GREEN), (30, YELLOW)): ax.plot(x, x**n, color=c, lw=1.4)
ax.text(.36, .42, '$n=2$', ha='center', fontsize=7.5); ax.text(.66, .26, '$8$', ha='center', fontsize=7.5); ax.text(.82, .08, '$30$', ha='center', fontsize=7.5)
ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4)
ax = axes[1]
for n, c in ((2, BLUE), (4, GREEN), (8, YELLOW)):
    ax.plot([0, 0, 1/n, 1/n, 1], [0, n, n, 0, 0], color=c, lw=1.4)
    ax.text(1/n+.03, n-.45, f'$n={n}$', ha='left', va='center', fontsize=7.5)
ax.set_xlim(0, 1.02); ax.set_ylim(0, 9); ax.set_xticks([0, 1]); ax.set_yticks([0, 2, 4, 8]); ax.set_xlabel('$x$', labelpad=-4)
ax = axes[2]; r = 0; cs = [BLUE, GREEN, YELLOW, RED]
for k in range(4):
    for j in range(2**k):
        r += 1; ax.plot([j/2**k, (j+1)/2**k], [r, r], color=cs[k], lw=2.2, solid_capstyle='butt')
x0 = .3
ax.plot([x0, x0], [.2, 15.8], color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(x0, 16.2, '$x_0$', ha='center', va='bottom', fontsize=7.5)
ax.set_xlim(0, 1); ax.set_ylim(0, 17.5); ax.set_xticks([0, 1]); ax.set_yticks([1, 15]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('项号', labelpad=-6)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^n; n 1_(0,1/n); h_{k,j}=1_[j/2^k,(j+1)/2^k), k<=3'})
