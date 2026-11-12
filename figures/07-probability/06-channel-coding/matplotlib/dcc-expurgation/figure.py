from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# A random binary code with M = 16 codewords of length n = 14 (rate 2/7), seed 1, over BSC(0.1) with
# maximum-likelihood decoding (ties to the smallest index). Conditional errors lambda_m are exact sums over all
# outputs (2^14). Bars sorted; blue dashed = average error; red line = 2 x average; red bars are removed by expurgation.
rng = np.random.default_rng(1); n, M, p = 14, 16, BSC_P
cw = rng.integers(0, 2, size=(M, n))
Y = ((np.arange(2**n)[:, None] >> np.arange(n)) & 1)
dist = (Y[:, None, :] != cw[None, :, :]).sum(2)              # outputs x codewords
lik = p**dist*(1-p)**(n-dist)
dec = lik.argmax(1)
lam = np.array([lik[dec != m, m].sum() for m in range(M)])
avg = lam.mean(); order = np.argsort(lam)
fig, ax = figure(width_mm=100, height_mm=48)
panel(fig, left=.12, right=.97, top=.95, bottom=.17)
keep = lam[order] <= 2*avg
ax.bar(np.arange(M)[keep], lam[order][keep], width=.75, color=BLUE_FILL, edgecolor=BLUE, lw=.6)
ax.bar(np.arange(M)[~keep], lam[order][~keep], width=.75, color=RED_FILL, edgecolor=RED, lw=.6)
ax.axhline(avg, color=BLUE, lw=1.1, ls=DASH); ax.axhline(2*avg, color=RED, lw=1.1)
lab(ax, 0, avg+.012, r'$P_{\mathrm{e}}=%.3f$' % avg, BLUE); lab(ax, 0, 2*avg+.012, r'$2P_{\mathrm{e}}$', RED)
ax.set_xlim(-1, M); ax.set_xticks([]); ax.set_xlabel('消息（按条件错误概率排序）', labelpad=2); ax.set_ylabel(r'$\lambda_m$', labelpad=1)
dmin = int(min(((cw[i] != cw[j]).sum() for i in range(M) for j in range(i+1, M))))
save(fig, HERE, 'figure', {'n': n, 'M': M, 'seed': 1, 'avg': float(avg), 'max': float(lam.max()),
     'removed': int((~keep).sum()), 'max_kept': float(lam[order][keep].max()), 'min_distance': dmin})
