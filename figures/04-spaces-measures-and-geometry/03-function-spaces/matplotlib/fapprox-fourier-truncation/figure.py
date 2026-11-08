from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Period-1 Fourier truncation. Sawtooth f(x)=x: hat f(0)=1/2, hat f(k)=i/(2 pi k). Triangle |x-1/2|: hat f(k)=1/(pi^2 k^2) for odd k.
# Squared L2 error = tail of |hat f|^2 ; triangle uniform error = tail of |hat f| (attained at x=1/2).
K_MAX = 4000000
k = np.arange(1, K_MAX+1, dtype=float); sq = 1/k**2
odd = k[0::2]
tailsaw = np.cumsum(sq[::-1])[::-1]
def saw_l2(K): return np.sqrt(tailsaw[K]/(2*np.pi**2))
t4 = np.cumsum(odd[::-1]**-4.)[::-1]; t2 = np.cumsum(odd[::-1]**-2.)[::-1]
def tri_l2(K): return np.sqrt(2/np.pi**4*t4[(K+1)//2])
def tri_sup(K): return 2/np.pi**2*t2[(K+1)//2]
Ks = np.array([1, 3, 7, 15, 31, 63, 127])
for K in (10, 40): print('saw', K, saw_l2(K), 'tri', tri_l2(K), tri_sup(K))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.97, bottom=.27, wspace=.27)
ax = axes[0]
x = np.linspace(0, 1, 6001)[1:-1]
K = 10
s = .5 - sum(np.sin(2*np.pi*j*x)/(np.pi*j) for j in range(1, K+1))
ax.plot([0, 1], [0, 1], color=BLUE, lw=1.4); ax.plot(x, s, color=GREEN, lw=1.2)
ax.text(.76, .94, '$f$', ha='left'); ax.text(.09, .32, r'$P_{10}f$', ha='left')
ax.set_xlim(0, 1); ax.set_ylim(-.14, 1.14); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.loglog(Ks, [saw_l2(K) for K in Ks], color=BLUE, lw=1.4, marker='o', ms=2.8, mew=0)
ax.loglog(Ks, [tri_sup(K) for K in Ks], color=RED, lw=1.4, marker='^', ms=3, mew=0)
ax.loglog(Ks, [tri_l2(K) for K in Ks], color=GREEN, lw=1.4, marker='s', ms=2.6, mew=0)
ax.text(5, .17, r'$L^2$', color=INK); ax.text(8.5, .17, '锯齿', color=INK); ax.text(11, .016, r'$L^\infty$', color=INK); ax.text(21, .016, '三角波', color=INK); ax.text(1.3, 4e-4, r'$L^2$', color=INK); ax.text(2.3, 4e-4, '三角波', color=INK)
ax.set_xlim(.9, 150); ax.set_ylim(1e-5, .6); ax.set_xlabel('$K$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'L2 error^2 = sum_{|k|>K}|hat f(k)|^2; triangle sup error = sum_{|k|>K}|hat f(k)|'})
