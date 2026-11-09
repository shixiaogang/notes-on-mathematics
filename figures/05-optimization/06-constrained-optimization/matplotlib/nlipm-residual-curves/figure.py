from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Residual histories of the primal-dual method on the running example.
h = pd_ipm([1, 2], [1, 2], [1, .5], sigma=.2, eta=.9, tol=1e-6)
T = [r['t'] for r in h]; floor = 1e-12
rd = [max(np.abs(r['rd']).max(), floor) for r in h]; rp = [max(np.abs(r['rp']).max(), floor) for r in h]; mu = [r['mu'] for r in h]
fig, ax = figure(width_mm=88, height_mm=50)
ax.semilogy(T, rd, color=RED, lw=1.5, marker='o', ms=2.8); ax.semilogy(T, rp, color=RED, lw=1.5, ls='--', marker='o', ms=2.8); ax.semilogy(T, mu, color=GREEN, lw=1.5, marker='o', ms=2.8)
ax.set_xlim(0, T[-1]); ax.set_ylim(1e-9, 4); ax.set_xlabel('$t$', labelpad=1)
ax.text(3.3, 3e-1 * .1, '$\\mu^{(t)}$', fontsize=7.5); ax.text(1.05, 1.0, '$\\|r_{\\rm d}\\|_\\infty$', fontsize=7.5); ax.text(.1, 3e-5, '$\\|r_{\\rm p}\\|_\\infty$', fontsize=7.5)
save(fig, OUT, 'figure', {'rp': rp, 'rd': rd, 'mu': mu})
