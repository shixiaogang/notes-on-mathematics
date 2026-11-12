from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Series with rare large terms: X_1 = eps_1; for k >= 2, X_k = k on B_k (P(B_k) = 1/k^2), otherwise eps_k/k,
# with eps_k = +-1 (prob 1/2) independent of B_k. Six paths (seed 4), k <= 10^4.
# Green: partial sums S_n; yellow: cumulative expectation sum_{k<=n} E[X_k] = sum_{2<=k<=n} 1/k (diverges);
# red dots: the steps where a large term k occurred.
rng = np.random.default_rng(4)
N, M = 10**4, 6
k = np.arange(1, N+1)
pB = np.where(k >= 2, 1/k**2, 0.)
B = rng.random((M, N)) < pB
E = rademacher(rng, (M, N))
X = np.where(B, k, E/k)
S = np.cumsum(X, axis=1)
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, left=.12, right=.97, bottom=.2, top=.95)
for s, b in zip(S, B):
    ax.plot(k, s, color=GREEN, lw=.9)
for s, b in zip(S, B):
    for i in np.flatnonzero(b): dot(ax, k[i], s[i], ms=3.6)
EX = np.cumsum(np.where(k >= 2, 1/k, 0.))
ax.plot(k, EX, color=YELLOW, lw=1.6, ls=DASH)
lab(ax, 300, 7.3, r'$\sum_{k\leq n}\mathbb{E}[X_k]$'.replace(r'\mathbb{E}', 'E'), YELLOW)
ax.set_xscale('log'); ax.set_xlim(1, N); logticks(ax, [0, 1, 2, 3, 4], 'x')
ax.axhline(0, color=STROKE, lw=.6)
axlab(ax, '$n$', '$S_n$')
big = [[int(x) for x in k[b]] for b in B]
save(fig, HERE, 'figure', {'seed': 4, 'big_term_indices': big, 'final': [float(x) for x in S[:, -1]],
     'expected_number_of_big_terms': float(pB.sum())})
