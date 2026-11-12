from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Approximate chain X' = (1-h) X + sqrt(2h) eps on target N(0,1), integrand f(x) = x^2, I = 1, started in stationarity.
# Stationary law N(0, v), v = 2/(2-h): bias b(h) = h/(2-h).  Long-run variance of x^2 under AR(1) with rho = 1-h:
# sigma_LR^2(h) = 2 v^2 (1+rho^2)/(1-rho^2).  One step costs one unit, so budget B gives B steps.
# MSE(h, B) = b(h)^2 + sigma_LR^2(h)/B (asymptotic in B).  (b) compares the optimised MSE with an exact sampler
# (iid N(0,1), Var(x^2)=2, cost 1 per sample).
def parts(h):
    v = 2/(2-h); r = 1-h
    return h/(2-h), 2*v*v*(1+r*r)/(1-r*r)
hs = np.exp(np.linspace(np.log(2e-3), np.log(1.2), 600))
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.11, right=.98, bottom=.3, top=.96, wspace=.38)
b, lr = parts(hs)
facts = {}
for B, c in [(1e3, YELLOW), (1e4, GREEN), (1e5, BLUE)]:
    m = b*b+lr/B; k = m.argmin()
    a1.plot(hs, m, color=c, lw=1.4); dot(a1, hs[k], m[k])
    facts['B=%g' % B] = {'h_opt': hs[k], 'mse_opt': m[k]}
a1.plot(hs, b*b, color=STROKE, lw=.85, ls=DASH)
a1.set_xscale('log'); a1.set_yscale('log'); a1.set_xlim(2e-3, 1.2); a1.set_ylim(1e-4, 10)
logticks(a1, [-2, -1, 0], 'x'); logticks(a1, [-4, -2, 0])
lab(a1, 2.6e-3, 2.2, r'$B=10^{3}$', YELLOW); lab(a1, 2.6e-3, .22, r'$B=10^{4}$', GREEN); lab(a1, 2.6e-3, .022, r'$B=10^{5}$', BLUE)
lab(a1, .25, 2.4e-3, r'$b(h)^{2}$', STROKE)
axlab(a1, r'$h$', '均方误差')
Bs = np.logspace(3, 7, 60)
opt = []
hh = np.exp(np.linspace(np.log(1e-4), np.log(1.2), 6000)); bb, ll = parts(hh)
for B in Bs:
    opt.append(math.sqrt((bb*bb+ll/B).min()))
a2.plot(Bs, np.sqrt(2/Bs), color=BLUE, lw=1.4); a2.plot(Bs, opt, color=GREEN, lw=1.4)
a2.plot(Bs, 2.8*Bs**(-1/3), color=PURPLE, lw=.85, ls=DASH)
a2.axhline(.01, color=RED, lw=.9, ls=DOT)
a2.set_xscale('log'); a2.set_yscale('log'); a2.set_xlim(1e3, 1e7); a2.set_ylim(2e-4, .5)
logticks(a2, [3, 5, 7], 'x'); logticks(a2, [-3, -2, -1])
lab(a2, 1.5e5, .0011, '精确采样', BLUE); lab(a2, 1.2e4, .026, '近似链', GREEN)
lab(a2, 1.5e6, .034, r'$B^{-1/3}$', PURPLE); lab(a2, 1.2e3, .0068, r'$\varepsilon$', RED)
axlab(a2, r'$B$', '均方根误差')
tags(fig, axs)
facts['exact_B_for_rmse_0.01'] = 2/1e-4
for B in np.logspace(4, 8, 2001):
    if (bb*bb+ll/B).min() <= 1e-4:
        facts['approx_B_for_rmse_0.01'] = B; break
save(fig, HERE, 'figure', facts)
print(facts)
