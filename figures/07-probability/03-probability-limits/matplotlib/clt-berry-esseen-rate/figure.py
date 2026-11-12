from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Exact Kolmogorov distance sup_x |P(Z_n <= x) - Phi(x)| of the standardized sum against n,
# for Bern(1/2) (blue), Bern(1/10) (yellow) and Exp(1) (green), log-log axes.
# Purple dashed lines: Berry-Esseen bounds C rho/(sigma^3 sqrt n) with C = 0.4748,
# rho/sigma^3 = 1, (p^2+q^2)/sqrt(pq) = 2.733 and 12/e - 2 = 2.415 respectively.
ns = np.unique(np.round(np.logspace(0, 3, 25)).astype(int))
def exp_err(n):
    z = np.linspace(-6, 10, 4001)
    return float(np.max(np.abs(erlang_cdf(n, n+z*math.sqrt(n))-Phi(z))))
cases = [('Bern(1/2)', BLUE, lambda n: bin_sup_error(n, .5), 1.0),
         ('Bern(1/10)', YELLOW, lambda n: bin_sup_error(n, .1), (0.01+0.81)/0.3),
         ('Exp(1)', GREEN, exp_err, 12/math.e-2)]
fig, ax = figure(width_mm=100, height_mm=58)
facts = {}
for name, c, err, ratio in cases:
    e = np.array([err(int(n)) for n in ns])
    ax.plot(ns, e, 'o-', color=c, lw=1.3, ms=2.4, mew=0)
    ax.plot(ns, BE_C*ratio/np.sqrt(ns), color=PURPLE, lw=1.0, ls=DASH)
    facts[name] = {'ratio': ratio, 'err_n100': float(err(100)), 'bound_n100': BE_C*ratio/10,
                   'err_n1000': float(e[-1]), 'bound_n1000': BE_C*ratio/math.sqrt(1000)}
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(1, 4000); ax.set_ylim(3e-3, 2)
logticks(ax, [0, 1, 2, 3], 'x'); logticks(ax, [-2, -1, 0], 'y')
lab(ax, 1.15, 1.45, r'$C\rho/(\sigma^3\sqrt{n})$', PURPLE, ha='left')
lab(ax, 1150, .026, 'Bern(1/10)', YELLOW, ha='left', va='center'); lab(ax, 1150, .0042, 'Exp(1)', GREEN, ha='left', va='center')
lab(ax, 1150, .0115, 'Bern(1/2)', BLUE, ha='left', va='center')
axlab(ax, '$n$', '最大误差')
save(fig, HERE, 'figure', facts)
