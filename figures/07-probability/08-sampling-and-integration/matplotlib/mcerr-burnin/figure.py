from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Gaussian AR(1) chain X(t+1) = 0.9 X(t) + sqrt(1-0.81) xi, invariant N(0,1), started at x0 = 10.
# (a) 20 paths (seed 3122, green), marginal mean 0.9^t x0 (blue) with +-2 marginal sd band (light blue).
# (b) exact bias of the average of N recorded steps after discarding b steps:
#     x0 rho^{b+1} (1-rho^N) / (N (1-rho)), b = 0, 20, 50 (green solid/dashed/dotted);
#     stationary standard deviation sqrt(19/N) (purple reference).
rho, x0, T = 0.9, 10.0, 60
paths = ar1(np.random.default_rng(3122), rho, T, x0=x0, reps=20)
t = np.arange(0, T+1); m = x0*rho**t; sd = np.sqrt(1-rho**(2*t))
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
a.fill_between(t, m-2*sd, m+2*sd, color=BLUE_FILL, lw=0)
for p in paths: a.plot(t, np.r_[x0, p], color=GREEN, lw=.55)
a.plot(t, m, color=BLUE, lw=1.3); dot(a, 0, x0)
a.set_xlim(0, T); a.set_ylim(-3.5, 11); a.set_xticks([0, 20, 40, 60]); a.set_yticks([0, 5, 10]); axlab(a, '$t$')
N = np.logspace(0, 5, 200)
for bb, ls, s in [(0, '-', '$b=0$'), (20, DASH, '$b=20$'), (50, DOT, '$b=50$')]:
    bias = x0*rho**(bb+1)*(1-rho**N)/(N*(1-rho)); b.loglog(N, bias, color=GREEN, lw=1.2, ls=ls)
b.loglog(N, np.sqrt(19/N), color=PURPLE, lw=1.0)
lab(b, 1.3, 13, '$b=0$', GREEN); lab(b, 1.3, .2, '$b=20$', GREEN); lab(b, 1.3, .008, '$b=50$', GREEN)
lab(b, 3e3, .13, r'$\sqrt{19/N}$', PURPLE)
b.set_xlim(1, 1e5); b.set_ylim(1e-6, 60); logticks(b, [0, 1, 3, 5], 'x'); logticks(b, [-6, -4, -2, 0], 'y'); axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'bias_N100_b0': x0*rho*(1-rho**100)/(100*(1-rho)), 'bias_N100_b20': x0*rho**21*(1-rho**100)/(100*(1-rho)),
     'bias_N100_b50': x0*rho**51*(1-rho**100)/(100*(1-rho))})
