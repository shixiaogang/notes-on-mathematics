from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f=1+x-x^2 on (0,1). (a) even reflection f(|x|); (b) zero extension; (c) -3f(-x)+4f(-x/2)=1+x+2x^2 for x<0.
f = lambda x: 1+x-x**2
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.27, wspace=.27)
xr = np.linspace(0, 1, 300); xl = np.linspace(-1, 0, 300)
axes[0].plot(xl, f(-xl), color=GREEN, lw=1.4)
axes[1].plot(xl, 0*xl, color=GREEN, lw=1.4); axes[1].plot([0, 0], [0, 1], color=MUTED, lw=.85, ls=(0, (2, 2)))
axes[1].plot([0], [0], 'o', mfc='white', mec=GREEN, ms=3.2, mew=.9)
axes[2].plot(xl, 1+xl+2*xl**2, color=GREEN, lw=1.4)
for ax in axes:
    ax.plot(xr, f(xr), color=BLUE, lw=1.4); ax.plot([0], [1], 'o', color=BLUE, ms=3.2)
    ax.axvline(0, color=MUTED, lw=.85); ax.set_xlim(-1.03, 1.03); ax.set_ylim(-.15, 2.2); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
axes[0].text(.55, 1.48, '$f$', ha='center'); axes[0].text(-.55, 1.48, '$Ef$', ha='center')
axes[1].text(.55, 1.48, '$f$', ha='center'); axes[1].text(-.55, .17, '$0$', ha='center')
axes[2].text(.55, 1.48, '$f$', ha='center'); axes[2].text(-.42, 1.48, '$Ef$', ha='center')
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1+x-x^2; even reflection, zero extension, 1+x+2x^2'})
