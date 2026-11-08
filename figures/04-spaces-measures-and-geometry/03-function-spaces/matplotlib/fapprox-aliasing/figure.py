from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# M=4 samples at j/4: cos(2 pi x) and cos(10 pi x) coincide. Triangle wave coefficients 1/(pi^2 k^2) (odd k), 1/4 at k=0; residue class k=1 mod 4 folds to hat f_4(1)=1/8.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.97, bottom=.27, wspace=.27)
ax = axes[0]
x = np.linspace(0, 1, 3001); xs = np.arange(0, 5)/4
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(x, np.cos(2*np.pi*x), color=BLUE, lw=1.4); ax.plot(x, np.cos(10*np.pi*x), color=GREEN, lw=1.1)
ax.plot(xs, np.cos(2*np.pi*xs), 'o', ms=4.2, mfc='white', mec=INK, mew=.85)
ax.text(.76, -.62, r'$\cos 2\pi x$', ha='left'); ax.text(.33, 1.1, r'$\cos 10\pi x$', ha='left')
ax.set_xlim(0, 1.02); ax.set_ylim(-1.3, 1.42); ax.set_xticks(xs); ax.set_xticklabels(['0', '1/4', '1/2', '3/4', '1']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ks = [k for k in range(-11, 12) if k % 2]
for k in ks:
    c = RED if (k-1) % 4 == 0 else BLUE
    ax.plot([k, k], [1e-4, 1/(np.pi*k)**2*np.pi**0], color=c, lw=1.2)
    ax.plot([k], [1/(np.pi*k)**2], 'o', ms=3, color=c, mew=0)
ax.plot([0, 0], [1e-4, .25], color=BLUE, lw=1.2); ax.plot([0], [.25], 'o', ms=3, color=BLUE, mew=0)
ax.set_yscale('log'); ax.set_xlim(-12, 12); ax.set_ylim(3e-4, .6); ax.set_xticks([-11, -7, -3, 1, 5, 9]); ax.set_xlabel('$k$', labelpad=0); ax.set_ylabel(r'$\vert\hat f(k)\vert$', labelpad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hat f_M(k) = sum_m hat f(k+mM); M=4,k=1; triangle wave coefficients'})
