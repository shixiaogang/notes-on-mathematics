from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Band around f=0.5+0.3 sin(2 pi x) of half width 0.15 containing f_n=f+0.1 sin(9 pi x); x^4 and x^12 leaving the zero band.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.3, wspace=.18)
x = np.linspace(0, 1, 800); e = .15; ax = axes[0]
f = .5+.3*np.sin(2*np.pi*x)
ax.fill_between(x, f-e, f+e, color=BLUE_FILL, lw=0)
ax.plot(x, f, color=BLUE, lw=1.4)
ax.plot(x, f+.1*np.sin(9*np.pi*x), color=GREEN, lw=1.2)
ax.text(.26, .99, '$f+\\varepsilon$', ha='center', va='bottom', fontsize=7.5)
ax.text(.62, .62, '$f_n$', ha='left', va='bottom')
ax.text(.05, .3, '$f$', ha='left', va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 1.15); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.fill_between(x, -e, e, color=BLUE_FILL, lw=0)
ax.plot(x, 0*x, color=BLUE, lw=1.4)
for n, c, t in ((4, GREEN, .8), (12, YELLOW, .93)):
    ax.plot(x, x**n, color=c, lw=1.2)
    x0 = e**(1/n); ax.plot([x0], [e], 'o', ms=3.4, color=RED, mew=0)
ax.text(.8, .57, '$x^4$', ha='right')
ax.text(.93, .6, '$x^{12}$', ha='left')
ax.text(.05, .19, r'$\varepsilon=0.15$', ha='left', va='bottom', fontsize=7.5)
ax.set_xlim(0, 1.04); ax.set_ylim(-.25, 1.1); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=.5+.3sin(2pi x), f_n=f+.1 sin(9 pi x), eps=.15; x^4,x^12 cross eps at eps^(1/n)'})
