from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# Preimage of a value band. (a) f(x)=x^2 on [0,2], band [1,2) -> [1,sqrt 2). (b) g(x)=1+sin(3x), band [1.5,1.9).
fig, axes = figure(width_mm=108, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.2, wspace=.16)
def panel(ax, x, y, lo, hi, ymax):
    ax.axhspan(lo, hi, color=YELLOW_FILL, lw=0, zorder=0)
    ax.plot(x, y, color=BLUE, lw=1.4)
    mask = (y >= lo) & (y < hi)
    edges = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))
    for s, e in zip(edges[::2], edges[1::2]):
        l, r = x[s], x[e-1]
        ax.plot([l, r], [0, 0], color=GREEN, lw=3.2, solid_capstyle='butt', clip_on=False, zorder=4)
        ax.plot([l, l], [0, lo], color=MUTED, lw=.85, ls=(0, (3, 2)))
        ax.plot([r, r], [0, hi if y[e-1] > (lo+hi)/2 else lo], color=MUTED, lw=.85, ls=(0, (3, 2)))
    ax.set_xlim(x[0], x[-1]+.02); ax.set_ylim(0, ymax)
xa = np.linspace(0, 2, 8001)
axa = axes[0]; panel(axa, xa, xa**2, 1, 2, 4.2)
axa.set_xticks([0, 1, np.sqrt(2), 2]); axa.set_xticklabels(['0', '1', r'$\sqrt{2}$', '2']); axa.set_yticks([0, 1, 2, 4]); axa.set_yticklabels(['0', '1', '2', '4'])
axa.text(.02, 2.25, r'$B=[1,2)$', color=INK, ha='left', va='bottom', fontsize=7.5)
axa.text(1.6, 3.3, r'$f(x)=x^2$', color=BLUE, ha='right', va='center')
axb = axes[1]; xb = np.linspace(0, 2*np.pi, 8001); panel(axb, xb, 1+np.sin(3*xb), 1.5, 1.9, 2.4)
axb.set_xticks([0, 2, 4, 6]); axb.set_xticklabels(['0', '2', '4', '6']); axb.set_yticks([0, 1, 1.5, 1.9]); axb.set_yticklabels(['0', '1', '1.5', '1.9'])
axb.text(3.3, 2.22, r'$g(x)=1+\sin 3x$', color=BLUE, ha='center', va='center')
fig.text(.285, .018, '(a)', ha='center', va='bottom', color=INK); fig.text(.76, .018, '(b)', ha='center', va='bottom', color=INK)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'preimage of value bands under x^2 and 1+sin(3x)'})
