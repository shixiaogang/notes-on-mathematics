from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Stationary Gaussian AR(1), f(x) = x: autocovariance gamma_k = rho^k.
# (a) gamma_k for rho = 0.9 (blue) and rho = -0.5 (yellow), k = 0..15.
# (b) exact N Var(hat I_N) = gamma_0 + 2 sum_{k<N} (1-k/N) gamma_k for rho = 0.9 (blue), 0 (grey), -0.5 (yellow);
#     purple dashed: long-run variances (1+rho)/(1-rho) = 19, 1, 1/3.
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
k = np.arange(16)
a.bar(k-.18, .9**k, width=.36, color=BLUE_FILL, edgecolor=BLUE, lw=.6)
a.bar(k+.18, (-.5)**k, width=.36, color=YELLOW_FILL, edgecolor=YELLOW, lw=.6)
a.axhline(0, color=STROKE, lw=.7)
lab(a, 9, .55, r'$\rho=0.9$', BLUE); lab(a, 3, -.62, r'$\rho=-0.5$', YELLOW)
a.set_xlim(-.7, 15.7); a.set_ylim(-.75, 1.1); a.set_xticks([0, 5, 10, 15]); a.set_yticks([-.5, 0, .5, 1]); axlab(a, '$k$')
def nvar(rho, N):
    kk = np.arange(1, N); return 1 + 2*np.sum((1-kk/N)*rho**kk)
Ns = np.unique(np.round(np.logspace(0, 3.5, 80)).astype(int))
for rho, c in [(.9, BLUE), (0, STROKE), (-.5, YELLOW)]:
    b.loglog(Ns, [nvar(rho, n) for n in Ns], color=c, lw=1.3)
    b.axhline((1+rho)/(1-rho), color=PURPLE, lw=.8, ls=DASH)
b.set_xlim(1, 3e3); b.set_ylim(.2, 40); logticks(b, [0, 1, 2, 3], 'x'); b.minorticks_off(); b.set_yticks([1/3, 1, 19]); b.set_yticklabels(['$1/3$', '$1$', '$19$']); axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'nvar_4_09': nvar(.9, 4), 'nvar_4_m05': nvar(-.5, 4), 'nvar_100_09': nvar(.9, 100), 'nvar_1000_09': nvar(.9, 1000)})
