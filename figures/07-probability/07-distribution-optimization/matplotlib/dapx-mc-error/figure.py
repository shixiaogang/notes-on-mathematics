from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Monte Carlo estimate of J(Q)=E_Q[ln q(X) - ln pi~(X)] at Q*=N(0, 3^{-1/2}) for pi~=exp(-x^4/4).
# J* = -0.8943 exactly (closed form). Integrand sd sigma from 10^6 draws.
# (a) histogram of 400 independent estimates with n=100 (green), true value (red).
# (b) root-mean-square error over 400 replications vs n (green) and sigma/sqrt(n) (purple dashed).
rng = np.random.default_rng(SEED)
s = 3**-0.25; Js = float(quartic_J(0, s))
def integrand(x):
    return -x*x/(2*s*s)-math.log(s)-0.5*math.log(2*math.pi)+x**4/4
sigma = float(np.std(integrand(rng.normal(0, s, 1_000_000))))
R = 400; ns = np.array([10, 30, 100, 300, 1000, 3000, 10000])
rmse = []; est100 = None
for n in ns:
    est = integrand(rng.normal(0, s, (R, n))).mean(axis=1)
    rmse.append(float(np.sqrt(np.mean((est-Js)**2))))
    if n == 100: est100 = est
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
ax.hist(est100, bins=24, color=GREEN_FILL, edgecolor=GREEN, linewidth=.6)
ax.axvline(Js, color=RED, lw=1.2)
lab(ax, Js+.03, ax.get_ylim()[1]*.9, r'$J^{*}$', RED)
axlab(ax, r'$\hat{J}_{100}$', None)
ax = axs[1]
ax.loglog(ns, rmse, color=GREEN, lw=1.2, marker='o', ms=2.6)
ax.loglog(ns, sigma/np.sqrt(ns), color=PURPLE, lw=.9, ls=DASH)
lab(ax, 400, .03, r'$\sigma/\sqrt{n}$', PURPLE)
axlab(ax, '$n$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'seed': SEED, 'J_star': Js, 'sigma': sigma, 'rmse': dict(zip(map(int, ns), rmse)),
                           'mean_est100': float(est100.mean()), 'sd_est100': float(est100.std())})
