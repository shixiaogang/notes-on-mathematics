from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Neumann iteration for (I-T/2)u=1+x. u_N=a_N+b_N x, a_N=2(1-2^{-(N+1)}), b_N=(6/5)(1-6^{-(N+1)}). Exact u=2+6x/5.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.26, wspace=.26)
ax = axes[0]
x = np.array([-1, 1.])
a = lambda N: 2*(1-2.**-(N+1)); b = lambda N: 1.2*(1-6.**-(N+1))
for N, c in zip(range(3), (GREEN, GREEN, GREEN)):
    ax.plot(x, a(N)+b(N)*x, color=c, lw=1.0)
    ax.text(1.03, a(N)+b(N), f'$u_{N}$', va='center', fontsize=7.5)
ax.plot(x, 2+1.2*x, color=BLUE, lw=1.4)
ax.text(-.9, 2.35, '$u=2+6x/5$', ha='left')
ax.set_xlim(-1, 1.32); ax.set_ylim(-.3, 3.6); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2, 3]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
N = np.arange(0, 9)
c = 2*2.**-(N+1); l = 1.2*6.**-(N+1)/3**.5; e = (c**2+l**2)**.5; B = 2.**-N*2/3**.5
ax.semilogy(N, B, color=YELLOW, lw=1.0, marker='s', ms=2.8)
ax.semilogy(N, e, color=BLUE, lw=1.4, marker='o', ms=3)
ax.semilogy(N, l, color=GREEN, lw=1.0, marker='^', ms=3)
ax.text(5.4, .22, '余项界', ha='left', va='bottom', fontsize=7.5)
ax.text(3.2, .012, '实际误差', ha='left', va='top', fontsize=7.5)
ax.text(.9, 3e-4, '线性方向', ha='left', va='top', fontsize=7.5)
ax.set_ylim(3e-8, 3); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([1, 1e-2, 1e-4, 1e-6]); ax.set_yticklabels(['1', '$10^{-2}$', '$10^{-4}$', '$10^{-6}$']); ax.minorticks_off(); ax.set_xlabel('$N$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'a_N,b_N as above; error sqrt(c^2+l^2), c=2^{-N}, l=(6/5)6^{-(N+1)}/sqrt3; bound 2^{-N}*2/sqrt3'})
