from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

fig, axes = figure(width_mm=108, height_mm=50, ncols=2, width_ratios=[1.15, 1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.2, wspace=.24)
a = axes[0]
a.plot([-.5, 0], [0, 0], color=BLUE, lw=1.4, solid_capstyle='butt')
a.plot([0, 1], [0, .5], color=BLUE, lw=1.4, solid_capstyle='butt')
a.plot([1, 1.5], [1, 1], color=BLUE, lw=1.4, solid_capstyle='butt')
a.plot([1], [.5], 'o', ms=4.2, mfc='white', mec=BLUE, mew=1, zorder=4)
a.plot([1], [1], 'o', ms=4.2, color=BLUE, mew=0, zorder=4)
a.plot([.5, .5], [0, .25], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.plot([.5, 1.24], [.25, .25], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.plot([1, 1.24], [1, 1], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.annotate('', xy=(1.24, 1), xytext=(1.24, .25), arrowprops=dict(arrowstyle='<->', color=INK, lw=.85, shrinkA=0, shrinkB=0))
a.text(1.27, .625, r'$0.75$', ha='left', va='center', color=INK)
a.set_xlim(-.5, 1.55); a.set_ylim(-.04, 1.14)
a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '0.5', '1']); a.set_yticks([0, .25, .5, 1]); a.set_yticklabels(['0', '0.25', '0.5', '1'])
a.text(.36, .3, r'$F$', color=BLUE, ha='center', va='center')
b = axes[1]
b.fill_between([0, 1], [0, 0], [.5, .5], color=BLUE_FILL, lw=0)
b.plot([-.5, 0, 0, 1, 1, 1.5], [0, 0, .5, .5, 0, 0], color=BLUE, lw=1.4, solid_joinstyle='miter')
b.plot([1, 1], [0, .5], color=GREEN, lw=1.4)
b.plot([1], [.5], 'o', ms=4.2, color=GREEN, mew=0, zorder=4)
b.text(1.06, .5, r'$\frac{1}{2}\delta_1$', color=GREEN, ha='left', va='center')
b.text(.5, .24, r'$\frac{1}{2}\lambda|_{[0,1]}$', color=BLUE, ha='center', va='center')
b.set_xlim(-.5, 1.55); b.set_ylim(-.04, 1.14); b.set_xticks([0, .5, 1]); b.set_xticklabels(['0', '0.5', '1']); b.set_yticks([0, .5, 1]); b.set_yticklabels(['0', '0.5', '1'])
fig.text(.31, .018, '(a)', ha='center', va='bottom', color=INK); fig.text(.78, .018, '(b)', ha='center', va='bottom', color=INK)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F piecewise: ramp x/2 on [0,1), jump 1/2 at x=1'})
