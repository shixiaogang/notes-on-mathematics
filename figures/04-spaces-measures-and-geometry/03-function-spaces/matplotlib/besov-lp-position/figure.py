from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# Haar level j=3: concentrated psi_{3,0} and spread sum_k 8^{-1/2} psi_{3,k}. Both have l2 coefficient norm 1.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.095, right=.985, top=.96, bottom=.26, wspace=.1)
A = 2**1.5
def psi(x, k):
    y = 8*x-k
    return A*(((0 <= y) & (y < .5)).astype(float) - ((.5 <= y) & (y < 1)).astype(float))
x = np.linspace(0, 1, 4001, endpoint=False)
c1 = np.zeros(8); c1[0] = 1
c2 = np.ones(8)/np.sqrt(8)
for ax, c in zip(axes, (c1, c2)):
    g = sum(c[k]*psi(x, k) for k in range(8))
    ax.plot(x, g, color=BLUE, lw=1.4, drawstyle='steps-post')
    ax.axhline(0, color=MUTED, lw=.75)
    ax.set_xlim(0, 1); ax.set_ylim(-3.4, 3.4); ax.set_xticks([0, 1/8, .5, 1]); ax.set_xticklabels(['0', '1/8', '1/2', '1']); ax.set_yticks([-2.83, -1, 1, 2.83]); ax.set_yticklabels([r'$-2^{3/2}$', '$-1$', '$1$', r'$2^{3/2}$'])
    ax.set_xlabel('$x$', labelpad=0)
for a, s in zip(axes, '(a) (b)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Haar j=3, c=(1,0,...) and c=8^{-1/2}(1,...,1)'})
