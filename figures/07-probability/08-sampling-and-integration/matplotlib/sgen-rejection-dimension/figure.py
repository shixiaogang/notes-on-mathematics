from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: rejection sampling of N(0, I_d) from q = N(0, sigma^2 I_d); the best envelope is M = sigma^d (touching at 0),
# acceptance rate sigma^{-d}.
# (a) d = 1, sigma = 1.5: target density and M q.  (b) acceptance sigma^{-d} for sigma = 1.05, 1.1, 1.5 (log scale);
#     checked by simulation at sigma = 1.1, d = 1, 5, 10, 20 with 200000 candidates each, seed 8.
s = 1.5; x = np.linspace(-5, 5, 500)
fig, (A, B) = figure(width_mm=112, height_mm=50, ncols=2)
style(A); style(B)
A.plot(x, npdf(x), color=BLUE, lw=1.4)
A.plot(x, s*npdf(x, 0, s), color=PURPLE, lw=1.1)
A.text(1.6, .33, r'$Mq$', fontsize=7.5, color=INK)
A.text(-.5, .2, r'$\pi$', fontsize=7.5, color=INK)
A.set_xlim(-5, 5); A.set_ylim(0, .45); A.set_yticks([0, .2, .4]); sub(A, 'a', '$x$')
d = np.arange(1, 101)
for sig, col in ((1.05, GREEN), (1.1, YELLOW), (1.5, PURPLE)):
    B.semilogy(d, sig**(-d.astype(float)), color=col, lw=1.3)
    B.text(d[-1]+2, sig**(-100.)*(1.4 if sig < 1.5 else 8), f'$\\sigma={sig}$', fontsize=7.5, color=INK, va='center')
rng = np.random.default_rng(8); sims = {}
for dd in (1, 5, 10, 20):
    n = 200000
    Xc = 1.1*rng.standard_normal((n, dd))
    logr = -0.5*(Xc**2).sum(1)*(1-1/1.1**2)
    sims[dd] = float((np.log(rng.random(n)) <= logr).mean())
    B.plot([dd], [sims[dd]], 'o', ms=3.2, color=RED, zorder=5)
B.set_xlim(0, 125); B.set_ylim(1e-20, 2); B.set_xticks([0, 25, 50, 75, 100])
B.set_yticks([1, 1e-5, 1e-10, 1e-15])
B.set_ylabel('接受率'); sub(B, 'b', '$d$')
save(fig, HERE(__file__), 'figure', {'sim_sigma_1.1': sims})
print(sims, {k: 1.1**-k for k in sims})
