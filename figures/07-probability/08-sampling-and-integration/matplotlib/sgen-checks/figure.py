from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: what histograms, moments and autocorrelations can and cannot show.
# (a) 5000 draws of Unif(-sqrt3, sqrt3) (mean 0, variance 1) against the N(0,1) density; seed 14.
# (b) first 1000 states of random-walk Metropolis (step 0.3, start -2, seed 9) on the mixture
#     0.3 N(-2, 0.5^2) + 0.7 N(2, 1), against the mixture density.
# (c) sample autocorrelation of X_1 along systematic-scan Gibbs for N(0, [[1, rho],[rho, 1]]), rho = 0.8, 0.99,
#     and of independent draws; 20000 sweeps, seed 15; dashed: rho^{2k}.
fig, (A, B, C) = figure(width_mm=112, height_mm=48, ncols=3)
for ax in (A, B, C): style(ax)
rng = np.random.default_rng(14)
u = math.sqrt(3)*(2*rng.random(5000)-1)
x = np.linspace(-4, 4, 400)
A.hist(u, bins=np.linspace(-4, 4, 33), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
A.plot(x, npdf(x), color=BLUE, lw=1.4)
A.set_xlim(-4, 4); A.set_ylim(0, .5); A.set_yticks([0, .2, .4]); A.set_ylabel('密度'); sub(A, 'a', '$x$')
logp = lambda x: math.log(mix_pdf(np.array([x]))[0]+1e-300)
ch, _ = rwmh(logp, -2.0, .3, 3000, np.random.default_rng(9))
x = np.linspace(-4.5, 6, 400)
B.hist(ch[:1000], bins=np.linspace(-4.5, 6, 36), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
B.plot(x, mix_pdf(x), color=BLUE, lw=1.4)
B.set_xlim(-4.5, 6); B.set_ylim(0, .9); B.set_yticks([0, .4, .8]); sub(B, 'b', '$x$')
rng = np.random.default_rng(15); n = 20000; K = 40
facts = {'unif_mean': float(u.mean()), 'unif_var': float(u.var()), 'chain_first1000_max': float(ch[:1000].max())}
for rho, col in ((.8, YELLOW), (.99, PURPLE)):
    s = math.sqrt(1-rho**2); x1, x2 = 0., 0.; X1 = np.empty(n)
    for t in range(n):
        x1 = rho*x2+s*rng.standard_normal(); x2 = rho*x1+s*rng.standard_normal(); X1[t] = x1
    C.plot(range(K+1), acf(X1, K), color=col, lw=1.2)
    C.plot(range(K+1), rho**(2*np.arange(K+1)), color=col, lw=.8, ls='--')
C.plot(range(K+1), acf(rng.standard_normal(n), K), color=GREEN, lw=1.2)
C.axhline(0, color=LINE, lw=.6)
C.set_xlim(0, K); C.set_ylim(-.1, 1.02); C.set_yticks([0, .5, 1]); sub(C, 'c', '滞后 $k$'.split(' ')[1])
save(fig, HERE(__file__), 'figure', facts)
print(facts)
