from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# d=3, p=2, p*=6: f_n(r)=n^{1/2} phi(n r), phi(r)=exp(1-1/(1-r^2)). Norm ratios to n=1: L2 n^-1, grad-L2 1, L6 1, L4 n^-1/4.
phi = lambda r: np.where(np.abs(r) < 1, np.exp(1-1/np.maximum(1-r**2, 1e-12)), 0.)
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06, right=.98, top=.97, bottom=.27, wspace=.2)
ax = axes[0]; r = np.linspace(0, 1.15, 1600)
for n, c, p in zip((1, 2, 4, 8), (BLUE, GREEN, YELLOW, RED), ((.62, .78), (.42, 1.1), (.24, 1.62), (.14, 2.45))):
    ax.plot(r, n**.5*phi(n*r), color=c, lw=1.4); ax.text(p[0], p[1], f'$n={n}$', ha='left', va='center')
ax.set_xlim(0, 1.15); ax.set_ylim(0, 3.1); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2, 3]); ax.set_xlabel('$|x-x_0|$', labelpad=0)
ax = axes[1]; n = np.array([1, 2, 4, 8, 16, 32.])
# the two constant curves coincide; drawn with distinct dash patterns
ax.plot(n, n**0, color=GREEN, lw=1.4)
ax.plot(n, n**-.25, color=YELLOW, lw=1.4, marker='o', ms=2.6); ax.plot(n, n**-1., color=BLUE, lw=1.4, marker='o', ms=2.6)
ax.set_xscale('log', base=2); ax.set_yscale('log', base=2)
ax.text(30, 1.12, r"$\Vert\nabla f_n\Vert_2,\ \Vert f_n\Vert_6$", ha='right', va='bottom')
ax.text(30, .33, r'$\Vert f_n\Vert_4$', ha='right', va='top'); ax.text(8.5, .075, r'$\Vert f_n\Vert_2$', ha='right', va='center')
ax.set_xlim(1, 32); ax.set_ylim(1/40, 2); ax.set_xticks([1, 4, 16]); ax.set_xticklabels(['1', '4', '16']); ax.minorticks_off()
ax.set_yticks([1, 1/4, 1/16]); ax.set_yticklabels(['1', '1/4', '1/16']); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f_n=n^{1/2} phi(n r), d=3,p=2; ratios n^-1,1,1,n^-1/4'})
