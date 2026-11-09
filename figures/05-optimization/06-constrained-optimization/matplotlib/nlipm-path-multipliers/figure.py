from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Multiplier estimates and gap along the central path of the running example.
data = central_path(np.logspace(1, -4, 200))
mu = np.array([m for m, _ in data]); X = np.array([c for _, c in data])
sl = np.array([-g(c) for c in X]); lam = mu[:, None]/sl
gap = np.array([f(c)-FSTAR for c in X])
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
a.loglog(mu, lam[:, 0], color=PURPLE, lw=1.5); a.loglog(mu, lam[:, 1], color=PURPLE, lw=1.5, ls='--')
a.axhline(1, color=MUTED, lw=.85); a.text(2e-4, 1.5, '$\\lambda_1(\\mu)$', fontsize=7.5); a.text(.3, 1.5e-3, '$\\lambda_2(\\mu)$', fontsize=7.5)
a.invert_xaxis(); tag(a, '$\\mu$', '(a)')
b.loglog(mu, 2*mu, color=PURPLE, lw=1.5); b.loglog(mu, gap, color=BLUE, lw=1.5)
b.text(1.2e-2, 1.4e-1, '$m\\mu=2\\mu$', fontsize=7.5); b.text(3, 2e-3, '$f(x(\\mu))-f^*$', fontsize=7.5)
b.invert_xaxis(); tag(b, '$\\mu$', '(b)')
save(fig, OUT, 'figure', {'ratio_gap_over_mu_at_1e-4': float(gap[-1]/mu[-1])})
