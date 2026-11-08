from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# x^n on [0,1]: sup norm 1, L2 norm (2n+1)^(-1/2), L1 norm 1/(n+1).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.97, top=.97, bottom=.3, wspace=.25)
x = np.linspace(0, 1, 500); ax = axes[0]
ns = [1, 2, 5, 20]; cols = [BLUE, GREEN, YELLOW, RED]
tx = [.6, .72, .79, .91]
for n, c, t in zip(ns, cols, tx):
    ax.plot(x, x**n, color=c, lw=1.4)
ax.text(.42, .56, '$n=1$', ha='right', color=INK, fontsize=7.5)
ax.text(.66, .33, '$2$', ha='center', fontsize=7.5)
ax.text(.8, .22, '$5$', ha='center', fontsize=7.5)
ax.text(.945, .09, '$20$', ha='center', fontsize=7.5)
ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.08); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; n = np.arange(1, 41)
ax.plot(n, np.ones_like(n, float), color=BLUE, lw=1.4)
ax.plot(n, (2*n+1.)**-.5, color=GREEN, lw=1.4)
ax.plot(n, 1/(n+1.), color=YELLOW, lw=1.4)
ax.text(30, 1.05, r'$\Vert x^n\Vert_\infty=1$', ha='center', va='bottom')
ax.text(30, .2, r'$\Vert x^n\Vert_2$', ha='center', va='bottom')
ax.text(30, .05, r'$\Vert x^n\Vert_1$', ha='center', va='bottom')
ax.set_xlim(1, 41); ax.set_ylim(0, 1.25); ax.set_xticks([1, 20, 40]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^n; norms 1, (2n+1)^(-1/2), 1/(n+1)'})
