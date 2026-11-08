from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Picard condition for A(x_n)=(x_n/n) on l^2. Data g^(1)_n=1/n^2 and g^(2)_n=1/n; formal solutions n g_n.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.96, bottom=.28, wspace=.22)
n = np.arange(1, 13)
ax = axes[0]
ax.plot(n, 1/n, color=RED, lw=1.0, marker='o', ms=3.2)
ax.plot(n, 1/n**2, color=BLUE, lw=1.0, marker='o', ms=3.2)
ax.text(12.5, .125, '$1/n$', va='center', fontsize=7.5)
ax.text(12.5, .0, '$1/n^2$', va='center', fontsize=7.5)
ax.set_xlim(.4, 18.6)
ax.set_ylim(-.04, 1.1); ax.set_xticks([1, 4, 8, 12]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$n$', labelpad=0)
ax = axes[1]
ax.plot(n, np.ones_like(n), color=RED, lw=1.0, marker='o', ms=3.2)
ax.plot(n, 1/n, color=BLUE, lw=1.0, marker='o', ms=3.2)
ax.text(12.5, 1.0, '$x_n=1$', va='center', fontsize=7.5)
ax.text(12.5, .083, '$x_n=1/n$', va='center', fontsize=7.5)
ax.set_xlim(.4, 18.6)
ax.set_ylim(-.04, 1.25); ax.set_xticks([1, 4, 8, 12]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A(x_n)=(x_n/n); sigma_n=1/n; x_n=n g_n; g=1/n^2 gives 1/n, g=1/n gives 1'})
