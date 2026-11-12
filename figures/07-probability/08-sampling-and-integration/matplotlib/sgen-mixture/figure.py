from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
from statistics import NormalDist
# Target: mixture 0.3 N(-2, 0.5^2) + 0.7 N(2, 1).
# (a) correct two-step generation, independent U_0 (label) and U_1 (inside the component); n = 4000, seed 3.
# (b) wrong reuse: the same U picks the label and is fed to the component quantile.
#     The output has density f_1 on x <= -2 + 0.5 Phi^{-1}(0.3) and f_2 on x > 2 + Phi^{-1}(0.3).
N = NormalDist(); Phiinv = np.vectorize(N.inv_cdf)
rng = np.random.default_rng(3); n = 4000
U0, U1 = rng.random(n), rng.random(n)
K = (U0 > .3).astype(int)
m = np.array(M_MIX); s = np.array(S_MIX)
Xok = m[K]+s[K]*Phiinv(U1)
Xbad = m[K]+s[K]*Phiinv(U0)
c1 = -2+.5*N.inv_cdf(.3); c2 = 2+N.inv_cdf(.3)
x = np.linspace(-4.5, 6, 600)
bad = np.where(x <= c1, .3*0+npdf(x, -2, .5), 0)+np.where(x > c2, npdf(x, 2, 1), 0)
fig, (A, B) = figure(width_mm=112, height_mm=50, ncols=2)
bins = np.linspace(-4.5, 6, 43)
for ax, X in ((A, Xok), (B, Xbad)):
    style(ax)
    ax.hist(X, bins=bins, density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
    ax.plot(x, mix_pdf(x), color=BLUE, lw=1.4)
    ax.set_xlim(-4.5, 6); ax.set_ylim(0, .75); ax.set_yticks([0, .2, .4, .6])
A.plot(x, .3*npdf(x, -2, .5), color=YELLOW, lw=1.1, ls='--')
A.plot(x, .7*npdf(x, 2, 1), color=YELLOW, lw=1.1, ls='--')
B.plot(x, bad, color=RED, lw=1.1)
A.set_ylabel('密度'); sub(A, 'a', '$x$'); sub(B, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'n': n, 'seed': 3, 'c1': c1, 'c2': c2})
print(c1, c2)
