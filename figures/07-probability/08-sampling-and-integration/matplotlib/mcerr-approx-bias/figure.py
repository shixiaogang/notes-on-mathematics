from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Target I = E[X] = 1, X ~ Exp(1).  Approximate generator min(-ln(1-U), T), T = 2, mean 1-e^{-2}, bias -e^{-2},
# variance 2(1-(1+T)e^{-T}) - (1-e^{-T})^2.
# (a) running means of five runs of the clipped generator (seeds 3116..3120): green; I (blue); 1-e^{-2} (yellow dashed).
# (b) exact RMSE curves: exact generator 1/sqrt(N) (blue); clipped sqrt(b^2 + v/N) (yellow); |b| (red dashed).
T = 2.0; b0 = -math.exp(-T); m2 = 2*(1-(1+T)*math.exp(-T)); v = m2 - (1+b0)**2
N = 10**5; n = np.arange(1, N+1)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
for s in range(3116, 3121):
    x = np.minimum(-np.log1p(-np.random.default_rng(s).random(N)), T)
    a.semilogx(n, np.cumsum(x)/n, color=GREEN, lw=.7)
a.axhline(1, color=BLUE, lw=1.2); a.axhline(1+b0, color=YELLOW, lw=1.3, ls=DASH)
lab(a, 2e3, 1.04, '$I=1$', BLUE); lab(a, 2e3, .76, r'$1-\mathrm{e}^{-2}$', YELLOW)
a.set_xlim(1, N); a.set_ylim(.4, 1.4); logticks(a, [0, 1, 3, 5], 'x'); axlab(a, '$N$')
x = np.logspace(0, 5, 200)
b.loglog(x, 1/np.sqrt(x), color=BLUE, lw=1.3); b.loglog(x, np.sqrt(b0**2 + v/x), color=YELLOW, lw=1.4)
b.axhline(-b0, color=RED, lw=.9, ls=DASH)
nstar = v/b0**2; dot(b, nstar, math.sqrt(2)*(-b0))
lab(b, 3e3, .02, r'$1/\sqrt{N}$', BLUE); lab(b, 1.5, .075, r'$|b|=\mathrm{e}^{-2}$', RED)
b.set_xlim(1, N); b.set_ylim(2e-3, 1.5); logticks(b, [0, 1, 3, 5], 'x'); logticks(b, [-2, -1, 0], 'y'); axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'bias': b0, 'var_clip': v, 'N_star': nstar})
