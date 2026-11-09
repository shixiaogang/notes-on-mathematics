from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Complementarity pairs (s1 lam1, s2 lam2) of the running example, log axes.
fig, ax = figure(width_mm=84, height_mm=62)
lo, hi = 1e-7, 8
ax.fill_between([lo, hi], [lo*.05/1.95, hi*.05/1.95], hi, color=GREEN_FILL, lw=0, zorder=0)
ax.loglog([lo, hi], [lo, hi], color=BLUE, lw=1.2, zorder=2)
gam = .05
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
w = np.array([lo, hi]); up = w*(2/gam-1); dn = w/(2/gam-1)
ax.fill_between(w, dn, up, color=GREEN_FILL, lw=0, zorder=0)
ax.fill_between(w, up, hi*1e3, color='white', lw=0, zorder=.5); ax.fill_between(w, 1e-12, dn, color='white', lw=0, zorder=.5)
ax.loglog(w, up, color=MUTED, lw=.85, zorder=2); ax.loglog(w, dn, color=MUTED, lw=.85, zorder=2)
h1 = pd_ipm([1, 2], [1, 2], [1, .5], sigma=.2, eta=.9, tol=1e-6)
h2 = pd_ipm([1, 2], [1, 2], [1, .5], sigma=.2, eta=.9999, tol=1e-6, merit=False)
h3 = pd_ipm([1, 2], [1, 2], [1, .5], sigma=.02, eta=.9999, tol=1e-6, merit=False)
P1 = np.array([r['prod'] for r in h1]); P3 = np.array([r['prod'] for r in h3])
ax.loglog(P3[:, 0], P3[:, 1], color=YELLOW, lw=1.5, marker='o', ms=3, zorder=4)
ax.loglog(P1[:, 0], P1[:, 1], color=GREEN, lw=1.5, marker='o', ms=3, zorder=5)
ax.set_xlabel('$s_1\\lambda_1$', labelpad=1); ax.set_ylabel('$s_2\\lambda_2$', labelpad=1)
xi1 = [float(np.min(r['prod'])/r['mu']) for r in h1]; xi3 = [float(np.min(r['prod'])/r['mu']) for r in h3]
save(fig, OUT, 'figure', {'centrality_sigma.2': xi1, 'centrality_sigma.02': xi3, 'alphas_.02': [r.get('a') for r in h3]})
