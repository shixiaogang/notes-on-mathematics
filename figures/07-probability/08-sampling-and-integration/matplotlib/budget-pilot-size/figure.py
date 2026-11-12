from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# I = P(X > 4), X ~ Exp(1).  Importance sampling with q = Exp(lam), cost 1.5 per sample (as in chapter 7.32).
# Pilot: n0 draws from q0 = Exp(1/2) (cost 1.5 each); contributions c_i = 1{Y_i>4} p(Y_i)/q0(Y_i);
# fitted lam_hat = sum c_i / sum c_i Y_i (contribution-weighted mean matched to 1/lam); no hit -> keep lam = 1/2.
# Main run: fresh n1 = (C - 1.5 n0)/1.5 draws from Exp(lam_hat).  Given the pilot, Var = (m2(lam_hat) - I^2)/n1 exactly,
# m2(lam) = e^{-4(2-lam)}/(lam(2-lam)); averaged over 2000-20000 simulated pilots (seed 7).  Relative RMSE = sqrt(E Var)/I.
I = math.exp(-4)
def m2(l): return np.exp(-4*(2-l))/(l*(2-l))
rng = np.random.default_rng(7); R = 20000
def rel_rmse(n0, C):
    # only pilot draws above 4 contribute; their number K ~ Bin(n0, e^{-2}) and Y - 4 ~ Exp(1/2) given Y > 4
    n1 = (C-1.5*n0)/1.5
    if n1 < 1: return np.nan
    R = int(min(20000, max(2000, 4e7/max(1, n0*math.exp(-2)))))
    K = rng.binomial(n0, math.exp(-2), size=R); tot = K.sum()
    Y = 4+rng.exponential(2.0, size=tot); c = 2*np.exp(-Y/2)
    idx = np.repeat(np.arange(R), K)
    sc = np.bincount(idx, weights=c, minlength=R); scy = np.bincount(idx, weights=c*Y, minlength=R)
    lam = np.where(K > 0, sc/np.where(K > 0, scy, 1), 0.5)
    return math.sqrt(np.mean(m2(lam)-I*I)/n1)/I
ls = (10-math.sqrt(68))/8; vstar = m2(ls)-I*I
fig, ax = figure(width_mm=96, height_mm=54)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
facts = {'lam_star': ls, 'v_star': vstar, 'lam_fit_limit': 0.2, 'v_at_0.2': m2(.2)-I*I}
for C, col in [(1500, YELLOW), (15000, GREEN), (150000, BLUE)]:
    n0s = np.unique(np.round(np.logspace(np.log10(5), np.log10(.7*C/1.5), 28)).astype(int))
    y = np.array([rel_rmse(int(n), C) for n in n0s])
    ax.plot(n0s, y, 'o-', color=col, lw=1.3, ms=2.4)
    ax.axhline(math.sqrt(vstar*1.5/C)/I, color=col, lw=.85, ls=DOT)
    k = np.nanargmin(y); dot(ax, n0s[k], y[k])
    facts['C=%d' % C] = {'n0_best': int(n0s[k]), 'rel_rmse_best': float(y[k]), 'oracle': math.sqrt(vstar*1.5/C)/I,
                         'plain': math.sqrt(I*(1-I)/C)/I, 'curve': {int(a): float(b) for a, b in zip(n0s, y)}}
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(4, 1e5); ax.set_ylim(5e-3, .3)
logticks(ax, [1, 2, 3, 4, 5], 'x'); logticks(ax, [-2, -1])
lab(ax, 1.0e3, .14, r'$C=1500$', YELLOW); lab(ax, 9e3, .045, r'$C=15000$', GREEN); lab(ax, 1.2e3, .0093, r'$C=150000$', BLUE)
axlab(ax, '试运行样本数', '相对均方根误差')
save(fig, HERE, 'figure', facts)
for k, v in facts.items():
    print(k, v if not isinstance(v, dict) else {a: b for a, b in v.items() if a != 'curve'})
