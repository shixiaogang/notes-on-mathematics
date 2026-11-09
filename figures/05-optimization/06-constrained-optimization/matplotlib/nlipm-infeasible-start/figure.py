from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Infeasible start of the primal-dual method on the running example.
h = pd_ipm([2, 1], [1, 3], [1, 1/3], sigma=.2, eta=.9, tol=1e-6)
X = np.array([r['x'] for r in h]); T = [r['t'] for r in h]
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
region(a); a.plot(X[:, 0], X[:, 1], color=GREEN, lw=1.5, marker='o', ms=3, zorder=5); a.plot(*XSTAR, 'o', color=RED, ms=5, zorder=6)
a.text(2.07, .78, '$x^{(0)}$', fontsize=7.5); a.set_xlim(-.3, 2.6); a.set_ylim(-.2, 3.4); tag(a, '$x_1$', '(a)'); a.set_ylabel('$x_2$', labelpad=1)
floor = 1e-12
b.semilogy(T, [max(np.abs(r['rp']).max(), floor) for r in h], color=RED, lw=1.5, ls='--', marker='o', ms=2.8)
b.semilogy(T, [max(np.abs(r['rd']).max(), floor) for r in h], color=RED, lw=1.5, marker='o', ms=2.8)
b.semilogy(T, [r['mu'] for r in h], color=GREEN, lw=1.5, marker='o', ms=2.8)
b.set_xlim(0, T[-1]); b.set_ylim(1e-9, 20); tag(b, '$t$', '(b)')
save(fig, OUT, 'figure', {'alpha': [r.get('a') for r in h], 'x': X.tolist(), 'rp': [r['rp'].tolist() for r in h], 'mu': [r['mu'] for r in h]})
