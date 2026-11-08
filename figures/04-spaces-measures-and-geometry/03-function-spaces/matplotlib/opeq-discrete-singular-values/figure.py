from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Singular values of A_n=(1/n)*lower-triangular ones (computed by numpy SVD) versus sigma_k(V)=1/((k-1/2)pi).
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.97, bottom=.25, wspace=.3)
A = lambda n: np.tril(np.ones((n, n)))/n
ax = axes[0]
k = np.arange(1, 61)
ax.loglog(k, 1/((k-.5)*np.pi), color=INK, lw=.85, ls=(0, (3, 2)))
for n, c, mk in ((5, GREEN, 'o'), (20, YELLOW, 's'), (40, BLUE, '^')):
    s = np.linalg.svd(A(n), compute_uv=False)
    ax.loglog(np.arange(1, n+1), s, ls='none', marker=mk, ms=2.6, color=c, mew=0)
    ax.text(n*1.08, s[-1]*.98, f'$n={n}$', va='center', ha='left', fontsize=7.5)
ax.text(2.1, .035, '$\\sigma_k(V)$', ha='left', va='top', fontsize=7.5)
ax.set_xlim(.8, 150); ax.set_ylim(.008, 1); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['1', '10', '100']); ax.set_yticks([1, .1, .01]); ax.set_yticklabels(['1', '0.1', '0.01']); ax.minorticks_off(); ax.set_xlabel('$k$', labelpad=0)
ax = axes[1]
ns = np.array([2, 4, 8, 16, 32, 64, 128, 256])
cond = [np.linalg.cond(A(int(n))) for n in ns]
xx = np.array([2, 256.])
ax.loglog(xx, 4*xx/np.pi, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.loglog(ns, cond, color=BLUE, lw=1.4, marker='o', ms=3)
ax.text(40, 22, '$4n/\\pi$', fontsize=7.5, color=INK)
ax.text(8, 85, '$\\mathrm{cond}(A_n)$', fontsize=7.5, color=INK, ha='center')
ax.set_xticks([2, 16, 128]); ax.set_xticklabels(['2', '16', '128']); ax.set_yticks([1, 10, 100]); ax.set_yticklabels(['1', '10', '100']); ax.minorticks_off(); ax.set_xlabel('$n$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A_n=(1/n) tril(ones); numpy SVD; sigma_k(V)=1/((k-1/2)pi); cond ~ 4n/pi'})
