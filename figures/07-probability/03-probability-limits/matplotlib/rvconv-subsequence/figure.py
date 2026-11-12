from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Harmonic moving blocks X_n = 1{U in block}; subsequence n_k = k(k-1)/2 + 1 (first block of level k), X_{n_k} = 1{U < 1/k}.
# Full path n -> X_n(omega) (red stems where X_n = 1) and the subsequence values (blue dots, filled when 1, hollow when 0).
# (a) U = 0.37: subsequence is 1 for k = 1, 2 and 0 for k >= 3.  (b) U = 0.08: subsequence is 1 for k <= 12 and 0 for k >= 13.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, wspace=.26, bottom=.33)
info = {}
for ax, W in ((axes[0], .37), (axes[1], .08)):
    style(ax)
    nn = np.arange(1, 121)
    x = np.array([block_value(int(n), W) for n in nn])
    ones = nn[x == 1]
    ax.vlines(ones, 0, 1, color=RED, lw=.8)
    ks = np.arange(1, 16); nk = ks*(ks - 1)//2 + 1
    v = (W < 1/ks).astype(float)
    ax.plot(nk[v == 1], v[v == 1], 'o', color=BLUE, ms=3.6, mew=0, zorder=5)
    ax.plot(nk[v == 0], v[v == 0], 'o', mfc='white', mec=BLUE, ms=3.6, mew=.9, zorder=5, clip_on=False)
    ax.set_xlim(0, 121); ax.set_ylim(0, 1.1); ax.set_yticks([0, 1]); ax.set_xticks([1, 30, 60, 90, 120])
    axlab(ax, '$n$', r'$X_n(\omega)$')
    lab(ax, 118, 1.04, r'$U=%.2f$' % W, INK, ha='right', va='bottom')
    info[W] = {'ones': [int(o) for o in ones], 'subsequence_last_one_k': int(ks[v == 1].max())}
tags(fig, axes)
save(fig, HERE, 'figure', info)
