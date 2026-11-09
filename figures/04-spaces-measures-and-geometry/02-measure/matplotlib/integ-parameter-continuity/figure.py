from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Rectangle

def labels(fig, axes, y=.03):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

# f(x,t)=t exp(-t x), t=2,1,.5,.25; envelope 1/(e x), touched at x=1/t.
fig, ax = figure(width_mm=102, height_mm=50)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.98, top=.97, bottom=.13)
x = np.linspace(0, 8, 900)
for t, c in ((2, BLUE), (1, GREEN), (.5, YELLOW), (.25, PURPLE)):
    ax.plot(x, t*np.exp(-t*x), color=c, lw=1.3, label=f'$t={t:g}$')
    ax.plot([1/t], [t*np.exp(-1)], 'o', ms=3.2, color=c, mew=0)
u = np.linspace(.25, 8, 500); ax.plot(u, 1/(np.e*u), color=RED, lw=1.2, dashes=(4, 2), label='$1/(ex)$')
ax.legend(loc='upper right', handlelength=2.2, borderaxespad=.1, labelspacing=.25)
ax.set_xlim(0, 8.7); ax.set_ylim(0, 2.1); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([0, 1, 2]); ax.text(8.65, .1, '$x$', ha='right', va='center', color=INK)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=t exp(-t x), t in {2,1,.5,.25}; envelope 1/(e x), attained at t=1/x'})
