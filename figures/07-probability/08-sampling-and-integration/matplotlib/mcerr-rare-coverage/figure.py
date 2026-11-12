from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Rare large contribution: f(u) = 1 + 1000*1{u > 0.999}, U ~ Unif(0,1), I = 2, Var f = 999.
# (a) running means of five runs (seeds 3110..3114), N <= 30000, and I = 2 (blue).
# (b) coverage of the interval  hat I_N +- 1.96 S_N/sqrt(N):  rare f computed exactly from the binomial count
#     of hits (yellow); f(u) = e^u by simulation, 20000 replications per N (seed 3115, blue); 0.95 dashed.
p = 1e-3; N = 30000; n = np.arange(1, N+1)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
for s in range(3110, 3115):
    u = np.random.default_rng(s).random(N); f = 1 + 1000*(u > 1-p)
    a.semilogx(n, np.cumsum(f)/n, color=GREEN, lw=.8)
a.axhline(2, color=BLUE, lw=1.2); lab(a, 1.3, 2.25, '$I=2$', BLUE)
a.set_xlim(1, N); a.set_ylim(0, 7); logticks(a, [0, 2, 4], 'x'); axlab(a, '$N$')
def cov_rare(N):
    tot = 0.0
    for k in range(N+1):
        lp = math.lgamma(N+1)-math.lgamma(k+1)-math.lgamma(N-k+1)+k*math.log(p)+(N-k)*math.log(1-p)
        if lp < -40: continue
        m = 1 + 1000*k/N
        S = 0.0 if k in (0, N) else math.sqrt((k*(1001-m)**2+(N-k)*(1-m)**2)/(N-1))
        if abs(m-2) <= 1.96*S/math.sqrt(N): tot += math.exp(lp)
    return tot
Ns = np.unique(np.round(np.logspace(1, 4.5, 40)).astype(int))
cr = [cov_rare(int(k)) for k in Ns]
rng = np.random.default_rng(3115); Ne = np.array([5, 10, 20, 50, 100, 300, 1000, 3000]); ce = []
for k in Ne:
    hit = 0
    for j in range(0, 20000, 1000):
        f = np.exp(rng.random((1000, k))); m = f.mean(1); S = f.std(1, ddof=1)
        hit += int(np.sum(np.abs(m-I_EXP) <= 1.96*S/np.sqrt(k)))
    ce.append(hit/20000)
b.semilogx(Ns, cr, color=YELLOW, lw=1.4); b.semilogx(Ne, ce, 'o-', color=BLUE, lw=1.0, ms=2.8, mew=0)
b.axhline(.95, color=STROKE, lw=.7, ls=DASH)
lab(b, 12, .78, '$f(u)=\\mathrm{e}^{u}$', BLUE); lab(b, 400, .2, '稀有大贡献', YELLOW)
b.set_xlim(4, 3.2e4); b.set_ylim(0, 1.02); logticks(b, [1, 2, 3, 4], 'x'); b.set_yticks([0, .5, .95]); b.set_yticklabels(['0', '0.5', '0.95'])
axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'cov_rare': dict(zip(map(int, Ns), cr)), 'cov_exp': dict(zip(map(int, Ne), ce)),
     'cov_rare_500': cov_rare(500), 'cov_rare_10000': cov_rare(10000)})
