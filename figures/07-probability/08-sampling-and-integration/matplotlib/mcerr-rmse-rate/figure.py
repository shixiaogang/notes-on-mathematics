from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# (a) f(u)=e^u, U ~ Unif(0,1): simulated root-mean-square error of the sample mean (green dots, 1000 replications
#     per N, seed 3102) against sigma/sqrt(N) (blue), sigma^2 = (e^2-1)/2-(e-1)^2.
# (b) f(u)=u^{-3/4}: I = 4 but E f^2 = inf.  Median absolute error (green dots, 1000 replications, seed 3103)
#     against reference slopes N^{-1/2} and N^{-1/4} (purple).
Ns = np.array([10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000])
R = 1000
def errs(f, I, seed):
    rng = np.random.default_rng(seed); out = []
    for N in Ns:
        m = np.empty(R)
        for j in range(0, R, 100):
            m[j:j+100] = f(rng.random((100, N))).mean(1)
        out.append(m - I)
    return out
ea = errs(np.exp, I_EXP, 3102)
eb = errs(lambda u: u**-0.75, 4.0, 3103)
rmse = np.array([np.sqrt(np.mean(e**2)) for e in ea])
med_b = np.array([np.median(np.abs(e)) for e in eb])
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.98, bottom=.28, top=.95, wspace=.3)
x = np.logspace(1, 5, 50)
a.loglog(x, np.sqrt(S2_EXP/x), color=BLUE, lw=1.3)
a.loglog(Ns, rmse, 'o', ms=3.2, color=GREEN, mew=0)
lab(a, 400, .045, r'$\sigma_f/\sqrt{N}$', BLUE)
a.set_xlim(7, 1.4e5); logticks(a, [1, 3, 5], 'x'); logticks(a, [-3, -2, -1], 'y'); a.set_ylim(8e-4, .3)
axlab(a, '$N$')
b.loglog(Ns, med_b, 'o', ms=3.2, color=GREEN, mew=0)
c4 = med_b[2]*Ns[2]**.25
b.loglog(x, c4*x**-.25, color=PURPLE, lw=.9, ls=DASH)
c2 = med_b[2]*Ns[2]**.5
b.loglog(x, c2*x**-.5, color=PURPLE, lw=.9, ls=DOT)
lab(b, 1.5e3, c4*1.5e3**-.25*1.35, r'$N^{-1/4}$', PURPLE)
lab(b, 1.2e2, c2*1.2e2**-.5*.42, r'$N^{-1/2}$', PURPLE)
b.set_xlim(7, 1.4e5); logticks(b, [1, 3, 5], 'x'); logticks(b, [-1, 0], 'y'); b.set_ylim(.025, 3)
axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'Ns': Ns.tolist(), 'rmse_exp': rmse.tolist(), 'theory': np.sqrt(S2_EXP/Ns).tolist(),
     'median_abs_heavy': med_b.tolist()})
