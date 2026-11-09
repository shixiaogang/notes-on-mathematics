from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# F=0 (x<0), 1/2+x/2 (0<=x<1), 1 (x>=1); mu_F=delta_0/2+lambda|[0,1]/2.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
a, b = axes
a.plot([-.5, 0], [0, 0], color=BLUE, lw=1.4)
a.plot([0, 1, 1.5], [.5, 1, 1], color=BLUE, lw=1.4)
a.plot([0, 0], [0, .5], color=RED, lw=1, ls=(0, (1.6, 1.4)))
a.plot([0], [.5], 'o', ms=4, color=BLUE, mew=0); a.plot([0], [0], 'o', ms=4, mfc='white', mec=BLUE, mew=1, clip_on=False, zorder=5)
a.text(.08, .24, r'$\frac{1}{2}$', ha='left', va='center'); a.text(.52, .90, r'$F$', ha='right', va='center')
a.set_xlim(-.55, 1.55); a.set_ylim(0, 1.2); a.set_xticks([0, 1]); a.set_xticklabels(['0', '1']); a.set_yticks([0, .5, 1]); a.set_yticklabels(['0', '1/2', '1'])
b.fill_between([0, 1], 0, .5, color=BLUE_FILL, lw=0); b.plot([0, 0, 1, 1], [0, .5, .5, 0], color=BLUE, lw=1.4)
b.annotate('', xy=(0, 1.08), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.25, shrinkA=0, shrinkB=0))
b.text(.08, 1.0, r'$\frac{1}{2}\delta_0$', ha='left', va='center'); b.text(.5, .25, r'$h=\frac{1}{2}$', ha='center', va='center')
b.set_xlim(-.55, 1.55); b.set_ylim(0, 1.2); b.set_xticks([0, 1]); b.set_xticklabels(['0', '1']); b.set_yticks([0, .5]); b.set_yticklabels(['0', '1/2'])
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.21, wspace=.2)
for ax, s in zip(axes, ['(a)', '(b)']):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'F piecewise, mu_F=delta_0/2+lambda|[0,1]/2'})
