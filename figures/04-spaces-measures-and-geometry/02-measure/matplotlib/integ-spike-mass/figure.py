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

# f_n=n 1_(0,1/n): rectangles for n=1,2,4,8, and the numeric sequence f_n(0.3).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.2, wspace=.16)
a, b = axes
for n, c, fc in ((1, BLUE, 'none'), (2, GREEN, 'none'), (4, YELLOW, 'none'), (8, RED, 'none')):
    a.add_patch(Rectangle((0, 0), 1/n, n, fc=fc, ec=c, lw=1.2))
    a.text(max(1/n+.015, .315 if n == 4 else 0), n-.05, f'$n={n}$', ha='left', va='top', color=INK, fontsize=7.5)
a.axvline(.3, color=MUTED, lw=.85, dashes=(3, 2))
a.set_xlim(0, 1.08); a.set_ylim(0, 8.7); a.set_xticks([0, .3, 1]); a.set_yticks([0, 2, 4, 6, 8])
N = np.arange(1, 13); v = np.where(.3 < 1/N, N, 0)
b.vlines(N, 0, v, color=BLUE, lw=1.2); b.plot(N, v, 'o', ms=3.4, color=BLUE, mew=0)
b.plot(N, 0*N+1, color=RED, lw=1.2, dashes=(4, 2))
b.text(12.5, 1.13, '$\\int f_n$', ha='right', color=INK); b.text(3.25, 3.0, '$f_n(0.3)$', ha='left', va='center', color=INK)
b.set_xlim(.4, 13.4); b.set_ylim(0, 3.5); b.set_xticks([1, 4, 8, 12]); b.set_yticks([0, 1, 2, 3]); b.text(13.35, .14, '$n$', ha='right', va='center', color=INK)
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f_n=n 1_(0,1/n), n=1,2,4,8; f_n(0.3)=1,2,3,0,0,...; integral 1'})
