from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# f(u) = u^{-3/4}, U ~ Unif(0,1): I = 4, infinite variance.  Five independent runs (seeds 3105..3109), N <= 10^5.
# (a) running means (green) and I = 4 (blue).  (b) contribution of the largest single term, max_{i<=N} f(U_i)/N (green),
#     against the reference N^{-1/4} (purple dashed).
N = 10**5; n = np.arange(1, N+1)
runs = [np.random.default_rng(s).random(N)**-0.75 for s in range(3105, 3110)]
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
for f in runs:
    a.semilogx(n, np.cumsum(f)/n, color=GREEN, lw=.7)
    b.loglog(n, np.maximum.accumulate(f)/n, color=GREEN, lw=.7)
a.axhline(4, color=BLUE, lw=1.2); lab(a, 1.15, 4.25, '$I=4$', BLUE)
a.set_xlim(1, N); a.set_ylim(0, 8); logticks(a, [0, 1, 3, 5], 'x'); axlab(a, '$N$')
b.loglog(n, n**-0.25, color=PURPLE, lw=1.0, ls=DASH); lab(b, 6, 3, '$N^{-1/4}$', PURPLE)
b.set_xlim(1, N); b.set_ylim(1e-2, 1e2); logticks(b, [0, 1, 3, 5], 'x'); logticks(b, [-2, 0, 2], 'y'); axlab(b, '$N$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'final_means': [float(f.mean()) for f in runs],
     'final_max_over_N': [float(f.max()/N) for f in runs]})
