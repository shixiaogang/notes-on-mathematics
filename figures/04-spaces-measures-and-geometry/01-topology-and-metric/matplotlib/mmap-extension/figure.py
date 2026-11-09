from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# Rationals k/m, m<=13, in [0,1]. x*=1/sqrt 2. Sample approximants from left 3/5,2/3,7/10 and from right 4/5,3/4,5/7.
# (a) f(q)=q^2; (b) f(q)=0 for q<x*, 1 for q>x*.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.97, bottom=.22, wspace=.18)
xs = 1/np.sqrt(2)
from fractions import Fraction as Q
R = sorted({Q(k, m) for m in range(1, 14) for k in range(0, m+1)})
qq = np.array([float(r) for r in R])
L = np.array([3/5, 2/3, 7/10]); U = np.array([4/5, 3/4, 5/7])
a, b = axes
a.plot(qq, qq**2, 'o', ms=1.6, color=MUTED, mew=0, zorder=2)
a.plot(L, L**2, 'o', ms=3.2, color=BLUE, mew=0, zorder=4)
a.plot(U, U**2, 'o', ms=3.2, color=GREEN, mew=0, zorder=4)
a.plot([xs], [.5], 'o', ms=3.6, mfc='white', mec=RED, mew=.9, zorder=3)
step = lambda t: (t > xs)*1.0
b.plot(qq, step(qq), 'o', ms=1.6, color=MUTED, mew=0, zorder=2)
b.plot(L, step(L), 'o', ms=3.2, color=BLUE, mew=0, zorder=4)
b.plot(U, step(U), 'o', ms=3.2, color=GREEN, mew=0, zorder=4)
b.plot([xs], [0], 'o', ms=3.6, mfc='white', mec=RED, mew=.9, zorder=3)
b.plot([xs], [1], 'o', ms=3.6, mfc='white', mec=RED, mew=.9, zorder=3)
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.axvline(xs, color=MUTED, lw=.75, ls=(0, (3, 2)), zorder=1)
    ax.set_xlim(0, 1.0); ax.set_xticks([0, xs, 1]); ax.set_xticklabels(['0', r'$1/\sqrt{2}$', '1'])
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
axes[0].set_ylim(0, 1.05); axes[0].set_yticks([0, .5, 1]); axes[0].set_yticklabels(['0', '1/2', '1'])
axes[1].set_ylim(-.1, 1.15); axes[1].set_yticks([0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'rationals k/m, m<=13; f(q)=q^2 and step at 1/sqrt(2); left sequence 3/5,2/3,7/10 and right sequence 4/5,3/4,5/7'})
