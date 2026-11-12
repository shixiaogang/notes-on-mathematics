from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Harmonic moving blocks on U ~ Unif(0,1): level k has k blocks [j/k,(j+1)/k), j = 0..k-1,
# term n = k(k-1)/2 + j + 1, X_n = 1{U in block}. Fixed outcome omega with U(omega) = 0.37.
# (a) layout of the blocks for n = 1..21 (levels 1..6) with the vertical line U = 0.37.
# (b) the path n -> X_n(omega) for n <= 120 (red dots where X_n = 1) and P(X_n = 1) = 1/k (blue).
W = .37
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; style(ax)
for n in range(1, 22):
    k, j = block_index(n)
    hit = j/k <= W < (j+1)/k
    ax.plot([j/k, (j+1)/k], [n, n], color=RED if hit else BLUE, lw=2.6 if hit else 1.8, solid_capstyle='butt')
ax.axvline(W, color=RED, lw=.9, ls=DASH)
lab(ax, W + .02, 22.2, r'$U=0.37$', RED, va='bottom')
ax.set_xlim(0, 1); ax.set_ylim(22.5, .3); ax.set_xticks([0, .5, 1]); ax.set_yticks([1, 3, 6, 10, 15, 21])
axlab(ax, '$U$', '$n$')
ax = axes[1]; style(ax)
nn = np.arange(1, 121)
x = np.array([block_value(int(n), W) for n in nn])
ones = nn[x == 1]
ax.vlines(ones, 0, 1, color=RED, lw=.8)
ax.plot(ones, np.ones_like(ones), 'o', color=RED, ms=2.8, mew=0)
pk = np.array([1/block_index(int(n))[0] for n in nn])
ax.step(nn, pk, where='mid', color=BLUE, lw=1.4)
lab(ax, 60, .32, 'ℙ$(X_n=1)=1/k$', BLUE, ha='left')
ax.set_xlim(0, 121); ax.set_ylim(0, 1.08); ax.set_xticks([1, 30, 60, 90, 120])
axlab(ax, '$n$', r'$X_n(\omega)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'U': W, 'indices_with_X_n_equal_1': [int(v) for v in ones]})
