from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Probability that the mean of N values e^{U_i} misses I = e-1 by at least eps = 0.01.
# Chebyshev bound min(1, sigma^2/(N eps^2)) (purple), normal approximation 2(1-Phi(eps sqrt(N)/sigma)) (blue),
# simulated frequency over 2000 replications per N (green dots, seed 3104). Red dots: N where each curve hits 0.05.
eps = 0.01; s = math.sqrt(S2_EXP)
Phi = np.vectorize(lambda z: 0.5*(1+math.erf(z/math.sqrt(2))))
x = np.logspace(2, 5, 300)
cheb = np.minimum(1, S2_EXP/(x*eps**2)); norm = 2*(1-Phi(eps*np.sqrt(x)/s))
Ns = np.array([300, 1000, 3000, 6000, 10000, 20000, 40000, 80000])
rng = np.random.default_rng(3104); R = 2000; freq = []
for N in Ns:
    hit = 0
    for j in range(0, R, 50):
        hit += int(np.sum(np.abs(np.exp(rng.random((50, N))).mean(1) - I_EXP) >= eps))
    freq.append(hit/R)
fig, ax = figure(width_mm=96, height_mm=50)
panel(fig, left=.11, right=.97, bottom=.2, top=.95)
ax.semilogx(x, cheb, color=PURPLE, lw=1.2); ax.semilogx(x, norm, color=BLUE, lw=1.3)
ax.plot(Ns, freq, 'o', ms=3.2, color=GREEN, mew=0)
ax.axhline(.05, color=STROKE, lw=.7, ls=DASH)
n_norm = (1.959964*s/eps)**2; n_cheb = S2_EXP/(0.05*eps**2)
dot(ax, n_norm, .05); dot(ax, n_cheb, .05)
lab(ax, n_norm*1.08, .09, '%d' % math.ceil(n_norm), RED); lab(ax, n_cheb*1.08, .09, '%d' % math.ceil(n_cheb), RED)
lab(ax, 1.3e4, .62, 'Chebyshev界', PURPLE); lab(ax, 1.9e3, .45, '正态近似', BLUE)
ax.set_xlim(100, 1e5); ax.set_ylim(0, 1.02); logticks(ax, [2, 3, 4, 5], 'x'); ax.set_yticks([.05, .5, 1]); ax.set_yticklabels(['0.05', '0.5', '1'])
axlab(ax, '$N$')
save(fig, HERE, 'figure', {'Ns': Ns.tolist(), 'freq': freq, 'n_norm': n_norm, 'n_cheb': n_cheb,
     'cheb_at_Ns': np.minimum(1, S2_EXP/(Ns*eps**2)).tolist(), 'norm_at_Ns': (2*(1-Phi(eps*np.sqrt(Ns)/s))).tolist()})
