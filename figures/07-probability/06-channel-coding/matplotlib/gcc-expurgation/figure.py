from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# One random Gaussian codebook (seed 5): M = 32 codewords of length n = 12, entries iid N(0, P'), P' = 2.4, budget P = 3,
# noise sigma^2 = 1, nearest-codeword decoding. lambda_m = conditional error of message m, estimated with 20000 noise
# draws per message (seed 6); a codeword with |x|^2 > nP is counted as lambda_m = 1 (it may not be sent).
# Bars sorted increasingly; red bars: the worst half removed by expurgation. Purple dashed: average lambda;
# red dashed: twice the average. Kept messages all have lambda_m <= 2 x average.
rng = np.random.default_rng(5); n, M, Pp, P = 12, 32, 2.4, 3.0
cb = rng.normal(0, math.sqrt(Pp), (M, n))
viol = (cb**2).sum(1) > n*P
rng2 = np.random.default_rng(6); T = 20000
lam = np.zeros(M)
d2 = None
for m in range(M):
    y = cb[m] + rng2.normal(size=(T, n))
    dist = (y**2).sum(1)[:, None] - 2*y @ cb.T + (cb**2).sum(1)[None, :]
    lam[m] = (np.argmin(dist, 1) != m).mean()
lam[viol] = 1.0
o = np.argsort(lam, kind='stable'); ls = lam[o]
avg = lam.mean()
fig, ax = figure(width_mm=96, height_mm=48)
panel(fig, left=.11, right=.97, top=.95, bottom=.2)
k = np.arange(M)
keep = k < M//2
ax.bar(k[keep], ls[keep], width=.72, color=BLUE_FILL, edgecolor=BLUE, lw=.6)
ax.bar(k[~keep], ls[~keep], width=.72, color=RED_FILL, edgecolor=RED, lw=.6)
ax.axhline(avg, color=PURPLE, lw=1.0, ls=DASH)
ax.axhline(2*avg, color=RED, lw=1.0, ls=DASH)
ax.set_yscale('symlog', linthresh=.01, linscale=.6)
ax.set_ylim(0, 1.3); ax.set_xlim(-1, M)
ax.set_yticks([0, .01, .1, 1]); ax.set_yticklabels(['0', '0.01', '0.1', '1'])
ax.set_xticks([]); ax.set_xlabel('消息（按条件错误概率排序）', labelpad=3)
ax.set_ylabel(r'$\lambda_m$', labelpad=1)
lab(ax, .2, avg*1.15, '平均 %.3f' % avg, PURPLE)
lab(ax, .2, 2*avg*1.15, '2倍平均', RED)
save(fig, HERE, 'figure', {'n': n, 'M': M, 'violating codewords': int(viol.sum()), 'average lambda': float(avg),
                            'max kept lambda': float(ls[M//2-1]), 'energies/n': [float(v) for v in (cb**2).sum(1)/n]})
