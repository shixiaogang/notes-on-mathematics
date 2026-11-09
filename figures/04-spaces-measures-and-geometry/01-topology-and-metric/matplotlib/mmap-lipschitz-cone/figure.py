from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) x^2 on [0,1] inside cone y=1/4 +- 2|x-1/2|; (b) sqrt(x), chords from 0 with slopes 1,2,5,10.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.2, wspace=.2)
a = axes[0]
x = np.linspace(0, 1, 400)
c = lambda s: .25+s*2*np.abs(x-.5)
a.fill_between(x, c(-1), c(1), color=GREEN_FILL, lw=0, zorder=1)
a.plot(x, c(1), color=GREEN, lw=.95, zorder=2); a.plot(x, c(-1), color=GREEN, lw=.95, zorder=2)
a.plot(x, x**2, color=BLUE, lw=1.4, zorder=3)
a.plot([.5], [.25], 'o', ms=3.4, color=INK, mew=0, zorder=4)
a.text(.5, .34, r'$(\frac{1}{2},\frac{1}{4})$', ha='center', va='bottom', color=INK)
a.set_xlim(0, 1); a.set_ylim(-.8, 1.3); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '1/2', '1']); a.set_yticks([0, 1])
b = axes[1]
xx = np.linspace(0, 1, 600)
b.plot(xx, np.sqrt(xx), color=BLUE, lw=1.4, zorder=3)
for t, s in ((1, 1), (.25, 2), (.04, 5), (.01, 10)):
    b.plot([0, t], [0, np.sqrt(t)], color=RED, lw=.9, zorder=2)
    b.plot([t], [np.sqrt(t)], 'o', ms=2.8, color=RED, mew=0, zorder=4)
b.text(.72, .59, '$1$', color=INK, ha='center', va='center')
b.text(.185, .245, '$2$', color=INK, ha='center', va='center')
b.set_xlim(0, 1.03); b.set_ylim(0, 1.08); b.set_xticks([0, .25, 1]); b.set_xticklabels(['0', '1/4', '1']); b.set_yticks([0, 1])
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^2, cone 1/4+-2|x-1/2|; sqrt(x), chord slopes 1/sqrt(t)'})
