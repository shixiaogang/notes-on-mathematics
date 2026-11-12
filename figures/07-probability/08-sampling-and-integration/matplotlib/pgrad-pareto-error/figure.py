from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# Same Pareto example.  Median of |mean of n derivative samples - truth| over R = 2000 seeded repetitions,
# n = 10 ... 10^4.  theta = 1 (finite variance, green circles) vs theta = 2 (infinite variance, yellow squares).
# Reference slopes (purple dashed, anchored 1.5x above the last point): n^{-1/2} and n^{-1/3}; the latter is the stable-law rate for tail index 3/2.
rng = np.random.default_rng(SEED+1)
ns = np.array([10, 30, 100, 300, 1000, 3000, 10000]); R = 2000
fig, ax = figure(width_mm=80, height_mm=52)
panel(fig, left=.15, right=.97, bottom=.2, top=.96)
facts = {}
for th, c, mk in [(1.0, GREEN, 'o'), (2.0, YELLOW, 's')]:
    truth = 3/(3-th)**2; med = []
    for n in ns:
        X = (1-rng.random((R, n)))**(-1/3)
        est = (X**th*np.log(X)).mean(axis=1)
        med.append(float(np.median(np.abs(est-truth))))
    ax.plot(ns, med, mk, color=c, ms=3.6, mew=0)
    ax.plot(ns, med, color=c, lw=.9)
    facts[f'median_err_theta{th}'] = med
c1 = facts['median_err_theta1.0'][-1]*1.5*100; c2 = facts['median_err_theta2.0'][-1]*1.5*10**(4/3)
ax.plot(ns, c1*ns**-.5, color=PURPLE, lw=.85, ls=DASH)
ax.plot(ns, c2*ns**(-1/3), color=PURPLE, lw=.85, ls=DASH)
ax.set_xscale('log'); ax.set_yscale('log')
lab(ax, 25, c1*30**-.5*1.15, r'$n^{-1/2}$', PURPLE); lab(ax, 25, c2*30**(-1/3)*1.18, r'$n^{-1/3}$', PURPLE)
lab(ax, 1500, facts['median_err_theta1.0'][-2]*.5, r'$\theta=1$', GREEN); lab(ax, 1500, facts['median_err_theta2.0'][-2]*.55, r'$\theta=2$', YELLOW)
axlab(ax, r'$n$')
save(fig, HERE, 'figure', facts)
