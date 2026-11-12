"""Bern(0.3), Hamming distortion, nearest-codeword encoders.
(a) Exhaustive search over all codebooks for n=1..4: smallest expected distortion for each
    size M (rate log2(M)/n). Blue: R(D)=h2(0.3)-h2(D).
(b) Random codebooks of rate R=0.5: M=ceil(2^{nR}) codewords i.i.d. Bern(r*) with r* the optimal
    output law at D(0.5); estimated E d_n (seed SEED, 40 codebooks x 250 blocks per n).
    Dashed: D(0.5) solving h2(0.3)-h2(D)=0.5."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

p = P_SRC


def exhaustive(n):
    N = 2**n
    ones = np.array([bin(x).count('1') for x in range(N)])
    px = p**ones*(1-p)**(n-ones)
    dist = np.array([[bin(x ^ c).count('1') for c in range(N)] for x in range(N)], float)
    big = np.full(N, 1e9)
    mind = np.empty((2**N, N)); mind[0] = big
    best = {}
    for mask in range(1, 2**N):
        low = (mask & -mask).bit_length()-1
        mind[mask] = np.minimum(mind[mask & (mask-1)], dist[:, low])
    sizes = np.array([bin(m).count('1') for m in range(2**N)])
    Dm = mind[1:] @ px / n
    for M in range(1, N+1):
        best[M] = float(Dm[sizes[1:] == M].min())
    return best


res = {n: exhaustive(n) for n in (1, 2, 3, 4)}
# random codebooks
R = .5
lo, hi = 0., .3
for _ in range(80):
    mid = (lo+hi)/2
    if h2(p)-h2(mid) > R: lo = mid
    else: hi = mid
DR = (lo+hi)/2
rstar = (p-DR)/(1-2*DR)
rng = np.random.default_rng(SEED)
ns = np.arange(4, 37, 4)
Ed = []
for n in ns:
    M = int(np.ceil(2**(n*R)))
    w = (1 << np.arange(n)).astype(np.uint64)
    vals = []
    for _ in range(40):
        C = (rng.random((M, n)) < rstar).astype(np.uint64) @ w
        X = (rng.random((250, n)) < p).astype(np.uint64) @ w
        for x in X:
            vals.append(int(np.bitwise_count(C ^ x).min())/n)
    Ed.append(float(np.mean(vals)))
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.085, right=.985, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
D = np.linspace(0, .34, 300)
ax.plot(D, rd_binary(D), color=BLUE, lw=1.4, zorder=3)
mk = {1: 'o', 2: 's', 3: '^', 4: 'D'}
cols = {1: YELLOW, 2: PURPLE, 3: GREEN, 4: RED}
for n, b in res.items():
    xs = [b[M] for M in b]; ys = [np.log2(M)/n for M in b]
    ax.plot(xs, ys, mk[n], ms=3.2, color=cols[n], mew=0, zorder=4, label=f'$n={n}$')
ax.legend(loc='upper right', handletextpad=.2, borderaxespad=.1, labelspacing=.25)
ax.set_xlim(0, .32); ax.set_ylim(0, 1.05)
axlab(ax, '$D$', '码率（bit/符号）')
ax = axs[1]
ax.plot(ns, Ed, 'o-', color=GREEN, ms=3.2, lw=1.1)
ax.axhline(DR, color=BLUE, lw=1.1, ls=DASH)
lab(ax, 22, DR-.012, f'$D(0.5)={DR:.4f}$', BLUE, ha='left', va='top')
ax.set_xlim(0, 38); ax.set_ylim(0, .2); ax.set_xticks([0, 8, 16, 24, 32])
axlab(ax, '块长', '平均失真')
tags(fig, axs)
save(fig, HERE, 'figure', {'exhaustive': {n: {M: v for M, v in b.items()} for n, b in res.items()},
                          'D_of_R0.5': DR, 'rstar': rstar, 'random_Ed': dict(zip(ns.tolist(), Ed))})
