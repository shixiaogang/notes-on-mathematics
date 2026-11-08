from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f_b=sum_j b_j 2^{-js} cos(2 pi 2^j x), s=1/2; ||Delta_h f_b||_2^2=sum_j b_j^2 2^{-2js} 2 sin^2(pi 2^j h).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.27, wspace=.2)
J = np.arange(1, 61); s = .5
b1, b2 = np.ones_like(J, float), 1/J
ax = axes[0]; jj = np.arange(1, 13)
ax.vlines(jj-.14, 0, b1[:12], color=BLUE, lw=1.2); ax.plot(jj-.14, b1[:12], 'o', ms=3.2, mew=0, color=BLUE)
ax.vlines(jj+.14, 0, b2[:12], color=GREEN, lw=1.2); ax.plot(jj+.14, b2[:12], 'o', ms=3.2, mew=0, color=GREEN)
ax.set_xlim(.3, 12.7); ax.set_ylim(0, 1.4); ax.set_xticks([1, 4, 8, 12]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$j$', labelpad=0)
ax.text(3.5, 1.1, '$b_j=1$', color=BLUE, ha='center', va='bottom'); ax.text(9, 1.1, '$b_j=1/j$', color=GREEN, ha='center', va='bottom')
ax = axes[1]; n = 1600
lh = np.linspace(-12, -2, n); hs = 2.0**lh
def R(b):
    return np.array([np.sqrt(np.sum(b**2*2.0**(-2*J*s)*2*np.sin(np.pi*2.0**J*h)**2))/h**s for h in hs])
ax.plot(-lh, R(b1), color=BLUE, lw=1.4); ax.plot(-lh, R(b2), color=GREEN, lw=1.4)
ax.set_xlim(2, 12); ax.set_ylim(0, 4.6); ax.set_xticks([2, 4, 8, 12]); ax.set_xticklabels(['$2^{-2}$', '$2^{-4}$', '$2^{-8}$', '$2^{-12}$']); ax.set_yticks([0, 1, 2, 3, 4])
ax.set_xlabel('$h$', labelpad=0)
for a, t in zip(axes, '(a) (b)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, t, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'ratio h^{-1/2}||Delta_h f_b||_2, s=1/2, j<=60, b_j=1 and 1/j'})
