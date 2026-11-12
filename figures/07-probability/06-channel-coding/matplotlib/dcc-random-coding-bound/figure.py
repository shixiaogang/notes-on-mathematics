from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Exact random-coding bound for BSC(0.1), uniform i.i.d. codebook, joint-typicality decoding with tolerance eps:
#   E Pe <= P(matched pair atypical) + (M-1) P(independent pair typical),  M = ceil(2^{nR}).
# Both probabilities are exact binomial sums over the number k of disagreements (with uniform input the
# typicality conditions reduce to |-(1/n) log2 W^n(y|x) - h2(p)| < eps). eps = (C-R)/2 for R < C;
# for R = 0.6 > C, eps = 0.05. The bound is clipped at 1.
p = BSC_P; C = 1-float(h2(p)); a, b = -np.log2(p), -np.log2(1-p)
def bound(n, R, eps):
    k = np.arange(n+1); v = (k*a + (n-k)*b)/n; typ = np.abs(v-float(h2(p))) < eps
    e1 = binpmf(n, p)[~typ].sum()
    lg = np.array([math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1) for i in k]) - n*np.log(2)
    lt = lg[typ]; lej = lt.max() + np.log(np.exp(lt-lt.max()).sum())      # log P(independent pair typical)
    return min(1.0, e1 + float(np.exp(min(50., n*R*np.log(2) + lej))))  # (M-1) <= 2^{nR}
ns = np.arange(20, 2001, 20)
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, top=.95, bottom=.18)
facts = {}
for R, col, ls in ((0.25, BLUE, '-'), (0.40, GREEN, '-'), (0.60, RED, DASH)):
    eps = (C-R)/2 if R < C else .05
    v = np.array([bound(n, R, eps) for n in ns]); ax.plot(ns, v, color=col, lw=1.4, ls=ls)
    facts['R=%.2f' % R] = {'eps': eps, 'n=200': float(v[9]), 'n=1000': float(v[49]), 'n=2000': float(v[-1])}
lab(ax, 520, 1e-7, r'$R=0.25$', BLUE); lab(ax, 1300, 1e-3, r'$R=0.40$', GREEN); lab(ax, 1500, .1, r'$R=0.60$', RED)
ax.set_yscale('log'); logticks(ax, [-12, -9, -6, -3, 0]); ax.set_ylim(1e-13, 3); ax.set_xlim(0, 2000)
ax.set_xlabel(r'$n$', labelpad=1)
save(fig, HERE, 'figure', {'p': p, 'C': C, **facts})
