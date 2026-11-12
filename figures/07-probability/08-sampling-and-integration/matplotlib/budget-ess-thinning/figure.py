from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Stationary Gaussian AR(1) chain on N(0,1) with coefficient rho.
# (a) ESS per iteration gamma_0/sigma_LR^2: f(x)=x gives (1-rho)/(1+rho); f(x)=x^2 gives (1-rho^2)/(1+rho^2)
#     (Cov(X_0^2, X_k^2) = 2 rho^{2k}).
# (b) rho = 0.9, keep every k-th state: the kept chain is AR(1) with rho^k, so per effective sample one needs
#     (1+rho^k)/(1-rho^k) kept states, i.e. k(1+rho^k)/(1-rho^k) iterations.
r = np.linspace(0, .99, 400)
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.1, right=.98, bottom=.3, top=.96, wspace=.36)
a1.plot(r, (1-r)/(1+r), color=BLUE, lw=1.4); a1.plot(r, (1-r*r)/(1+r*r), color=YELLOW, lw=1.6)
dot(a1, .9, .1/1.9); dot(a1, .9, .19/1.81)
a1.set_xlim(0, 1); a1.set_ylim(0, 1.02)
lab(a1, .08, .42, r'$f(x)=x$', BLUE); lab(a1, .5, .75, r'$f(x)=x^{2}$', YELLOW)
axlab(a1, r'$\rho$', '每步有效样本数')
k = np.arange(1, 31); rk = .9**k
a2.plot(k, k*(1+rk)/(1-rk), 'o-', color=GREEN, lw=1.3, ms=2.4)
a2.plot(k, (1+rk)/(1-rk), 'o-', color=PURPLE, lw=1.3, ms=2.4)
a2.axhline(19, color=STROKE, lw=.85, ls=DASH)
a2.set_yscale('log'); a2.set_xlim(0, 31); a2.set_ylim(.8, 60); logticks(a2, [0, 1])
lab(a2, 14, 30, '迭代步数', GREEN); lab(a2, 14, 1.9, '保存的状态数', PURPLE)
axlab(a2, '抽稀间隔', '每个有效样本')
tags(fig, axs)
save(fig, HERE, 'figure', {'ess_frac_x_0.9': .1/1.9, 'ess_frac_x2_0.9': .19/1.81,
     'iters_per_eff': {int(i): float(v) for i, v in zip(k, k*(1+rk)/(1-rk)) if i in (1, 2, 5, 10, 20)},
     'kept_per_eff': {int(i): float(v) for i, v in zip(k, (1+rk)/(1-rk)) if i in (1, 2, 5, 10, 20)}})
