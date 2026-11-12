from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# I = E[e^U], U ~ Unif(0,1).  Work-normalised variance = (variance of one estimate unit) x (number of e^u evaluations
# in that unit); the control functions are counted as free.  All moments by the midpoint rule on 2*10^6 nodes.
M = 2_000_000; u = (np.arange(M)+.5)/M
def var(x): return np.mean(x*x)-np.mean(x)**2
def cov(x, y): return np.mean(x*y)-np.mean(x)*np.mean(y)
def cv(y, h): return var(y)-cov(y, h)**2/var(h)          # optimal fixed coefficient
f = np.exp(u); g = (np.exp(u)+np.exp(1-u))/2
w = {}
w['直接平均'] = var(f)
w['对偶变量'] = 2*var(g)
w['控制变量 U'] = cv(f, u)
w['对偶 + 控制 U'] = 2*var(g)   # the paired control (U+1-U)/2 = 1/2 is constant, so it removes nothing
w['对偶 + 控制 (U-0.5)²'] = 2*cv(g, (u-.5)**2)
K = 4
w['分层 4 层'] = np.mean([var(np.exp(k/K+u/K)) for k in range(K)])
w['分层 + 对偶'] = 2*np.mean([var((np.exp(k/K+u/K)+np.exp(k/K+(1-u)/K))/2) for k in range(K)])
cov_g_u = cov(g, u)
def sci(v):
    e = int(math.floor(math.log10(v))); m = v/10**e
    return ('%.2g' % v) if e >= -2 else r'$%.1f\times10^{%d}$' % (m, e)
names = list(w)[::-1]; vals = [w[n] for n in names]
fig, ax = figure(width_mm=100, height_mm=56)
panel(fig, left=.37, right=.95, bottom=.18, top=.97)
ax.barh(range(len(names)), vals, color=GREEN_FILL, edgecolor=GREEN, lw=.8, height=.6)
ax.barh([len(names)-1], [vals[-1]], color=BLUE_FILL, edgecolor=BLUE, lw=.8, height=.6)
ax.set_xscale('log'); ax.set_xlim(1e-7, 1); logticks(ax, [-6, -4, -2, 0], 'x')
ax.set_yticks(range(len(names))); ax.set_yticklabels(names)
for i, v in enumerate(vals): lab(ax, v*1.3, i-.17, sci(v), INK)
axlab(ax, '每次求值的方差')
facts = {k: float(v) for k, v in w.items()}; facts['cov_pair_U'] = float(cov_g_u)
save(fig, HERE, 'figure', facts); print(facts)
