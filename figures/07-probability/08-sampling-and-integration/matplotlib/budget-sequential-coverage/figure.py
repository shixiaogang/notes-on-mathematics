from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Target half-width eps at nominal 95% (z = 1.96).  Integrands: f = U^{-1/3} (Pareto(3) on [1, inf): I = 1.5, sigma^2 = 0.75)
# and f = e^U (I = e-1, sigma^2 = 0.2420).  Rules, each with 20000 replications (seed 5):
#  fixed: n = ceil(z^2 sigma^2/eps^2) with the true sigma^2, interval mean +- z s_n/sqrt(n);
#  sequential: stop at the first n >= 10 with z s_n/sqrt(n) <= eps, report mean +- z s_n/sqrt(n);
#  two-stage: independent pilot of 30, then n = max(30, ceil(z^2 s_0^2/eps^2)) fresh draws, mean +- z s_n/sqrt(n).
z = 1.96; reps = 20000; rng = np.random.default_rng(5)
cases = {'pareto': (lambda u: u**(-1/3), 1.5, .75), 'exp': (lambda u: np.exp(u), E-1, (E*E-1)/2-(E-1)**2)}
def fixed(f, I, s2, eps):
    n = math.ceil(z*z*s2/eps**2); hit = 0
    for _ in range(0, reps, 1000):
        x = f(rng.random((1000, n))); m = x.mean(1); s = x.std(1, ddof=1)
        hit += np.sum(np.abs(m-I) <= z*s/math.sqrt(n))
    return hit/reps
def sequential(f, I, s2, eps):
    nmax = int(8*z*z*s2/eps**2)+50; hit = 0; ns = []
    for _ in range(0, reps, 500):
        x = f(rng.random((500, nmax))); k = np.arange(1, nmax+1)
        c1 = np.cumsum(x, 1); c2 = np.cumsum(x*x, 1); m = c1/k
        with np.errstate(invalid='ignore', divide='ignore'):
            v = (c2-k*m*m)/(k-1)
        ok = (k >= 10) & (z*np.sqrt(np.maximum(v, 0))/np.sqrt(k) <= eps)
        ok[:, -1] = True; j = ok.argmax(1)
        mm = m[np.arange(500), j]; hh = z*np.sqrt(np.maximum(v[np.arange(500), j], 0)/(j+1))
        hit += np.sum(np.abs(mm-I) <= hh); ns += list(j+1)
    return hit/reps, float(np.mean(ns))
def twostage(f, I, s2, eps):
    hit = 0
    for r in range(reps):
        s0 = f(rng.random(30)).std(ddof=1); n = max(30, math.ceil(z*z*s0*s0/eps**2))
        x = f(rng.random(n)); hit += abs(x.mean()-I) <= z*x.std(ddof=1)/math.sqrt(n)
    return hit/reps
epss = [.3, .2, .1, .05, .03]
res = {}
for name, (f, I, s2) in cases.items():
    res[name] = {'fixed': [fixed(f, I, s2, e) for e in epss], 'seq': [sequential(f, I, s2, e) for e in epss],
                 'two': [twostage(f, I, s2, e) for e in epss] if name == 'pareto' else None}
fig, ax = figure(width_mm=96, height_mm=54)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
P = res['pareto']
ax.plot(epss, P['fixed'], 'o-', color=BLUE, lw=1.3, ms=2.6, label='固定样本数')
ax.plot(epss, [a for a, b in P['seq']], 'o-', color=RED, lw=1.3, ms=2.6, label='序贯停止')
ax.plot(epss, P['two'], 'o-', color=GREEN, lw=1.3, ms=2.6, label='两阶段')
ax.plot(epss, [a for a, b in res['exp']['seq']], 'o--', color=RED, lw=1.0, ms=2.4, label='序贯停止，指数被积函数')
ax.axhline(.95, color=PURPLE, lw=.85, ls=DASH)
ax.set_xscale('log'); ax.set_xlim(.025, .36); ax.invert_xaxis(); ax.set_ylim(.6, 1.0)
ax.set_xticks(epss); ax.set_xticklabels(['0.3', '0.2', '0.1', '0.05', '0.03']); ax.minorticks_off()
ax.legend(loc='lower right', frameon=False, fontsize=7.5, handlelength=2.2)
lab(ax, .155, .965, '0.95', PURPLE)
axlab(ax, r'$\varepsilon$', '覆盖率')
save(fig, HERE, 'figure', {'eps': epss, 'results': res})
print(res)
