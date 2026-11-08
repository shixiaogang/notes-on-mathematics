from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# Graphs against y=x: (a) x/2 on (0,1); (b) x+1 on R; (c) x+1/x on [1,inf).
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.035, right=.985, top=.97, bottom=.235, wspace=.22)
a, b, c = axes
x = np.linspace(0.001, 1, 200)
a.plot(x, x, color=MUTED, lw=.9); a.plot(x, x/2, color=BLUE, lw=1.4)
a.plot([0], [0], 'o', ms=4.4, mfc='white', mec=RED, mew=1, zorder=5, clip_on=False)
a.set_xlim(0, 1); a.set_ylim(0, 1); a.set_xticks([0, 1]); a.set_yticks([0, 1])
a.text(.72, .76, '$y=x$', color=INK, ha='right', va='bottom', fontsize=7.5); a.text(.86, .36, '$T$', color=INK)
x = np.linspace(0, 4, 100)
b.plot(x, x, color=MUTED, lw=.9); b.plot(x, x+1, color=BLUE, lw=1.4)
b.set_xlim(0, 4); b.set_ylim(0, 5); b.set_xticks([0, 2, 4]); b.set_yticks([0, 5])
b.text(1.1, 2.8, '$T$', color=INK, ha='right')
x = np.linspace(1, 6, 400)
c.plot(x, x, color=MUTED, lw=.9); c.plot(x, x+1/x, color=BLUE, lw=1.4)
c.set_xlim(1, 6); c.set_ylim(1, 6.4); c.set_xticks([1, 3, 6]); c.set_yticks([1, 6])
c.text(2.1, 3.3, '$T$', color=INK, ha='right')
for ax, s in zip(axes, '(a) (b) (c)'.split()):
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x/2; x+1; x+1/x against y=x'})
