from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# AR(1) chain X^(t) = rho X^(t-1) + sqrt(1-rho^2) eps, rho = 0.9, target N(0,1), f(x) = x, I = 0.
# Total budget B = 2000 iterations split into m chains of T = B/m steps, each started at x0 = 10, first b steps discarded.
# Exact moments: E X^(t) = rho^t x0, Cov(X^(s), X^(t)) = rho^|t-s| (1 - rho^(2 min(s,t))).
rho, x0, B = 0.9, 10.0, 2000
def mse(m, b):
    T = B//m; L = T-b
    if L < 1: return np.inf, np.inf, np.inf
    t = np.arange(b+1, T+1)
    bias = x0*np.sum(rho**t)/L
    S, Tt = np.meshgrid(t, t)
    C = rho**np.abs(S-Tt)*(1-rho**(2*np.minimum(S, Tt)))
    var = C.sum()/L**2/m
    return bias**2+var, bias, var
ms = np.array([1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100])
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
facts = {}
for b, c, ls in [(0, YELLOW, '-'), (30, GREEN, '-')]:
    y = [mse(m, b)[0] for m in ms]
    ax.plot(ms, y, 'o-', color=c, lw=1.4, ms=2.6)
    facts['b=%d' % b] = {int(m): mse(m, b) for m in ms}
best = []
for m in ms:
    vals = [(mse(m, b)[0], b) for b in range(0, B//m)]
    best.append(min(vals))
ax.plot(ms, [v for v, b in best], 'o-', color=BLUE, lw=1.4, ms=2.6)
facts['best'] = {int(m): {'mse': v, 'b': b} for m, (v, b) in zip(ms, best)}
ax.axhline(19/B, color=PURPLE, lw=.85, ls=DASH)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(.8, 130); ax.set_ylim(5e-3, 2)
ax.set_xticks([1, 2, 5, 10, 20, 50, 100]); ax.set_xticklabels(['1', '2', '5', '10', '20', '50', '100']); ax.minorticks_off()
logticks(ax, [-2, -1, 0])
lab(ax, 1.1, .2, r'$b=0$', YELLOW); lab(ax, 3.5, .0062, r'$b=30$', GREEN); lab(ax, 1.1, .0062, '最优', BLUE)
lab(ax, 40, 19/B*1.25, r'$\sigma^{2}_{\mathrm{LR}}/B$', PURPLE)
axlab(ax, '链数', '均方误差')
save(fig, HERE, 'figure', {k: (v if k != 'b=0' and k != 'b=30' else {m: [float(x) for x in t] for m, t in v.items()}) for k, v in facts.items()})
for k in ['b=0', 'b=30']:
    print(k, {m: tuple(round(float(x), 5) for x in facts[k][m]) for m in [1, 4, 10, 20, 50]})
print({m: (round(float(d['mse']), 5), d['b']) for m, d in facts['best'].items()})
