from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Primal-dual iterates against barrier Newton iterates on the running example.
pd = np.array([r['x'] for r in pd_ipm([1, 2], [1, 2], [1, .5], sigma=.2, eta=.9, tol=1e-6)])
bm = barrier_method([1, 2], 1., .2, tol=1e-6, inner=1e-6)['path']
pth = np.array([c for _, c in central_path(np.logspace(1, -5, 300))])
fig, ax = figure(width_mm=88, height_mm=60)
u = np.linspace(.3, 1.6, 200); ax.fill_between(u, u**2, 2.3, color=BLUE_FILL, lw=0, zorder=0); ax.plot(u, u**2, color=EDGE, lw=1.7, zorder=2)
ax.plot(pth[:, 0], pth[:, 1], color=BLUE, lw=1.1, zorder=3)
ax.plot(bm[:, 0], bm[:, 1], color=YELLOW, lw=1.5, marker='o', ms=2.8, zorder=4)
ax.plot(pd[:, 0], pd[:, 1], color=GREEN, lw=1.5, marker='o', ms=3.2, zorder=5)
ax.plot(*XSTAR, 'o', color=RED, ms=5, zorder=7)
ax.text(1.03, 2.05, '$x^{(0)}$', fontsize=7.5)
ax.set_xlim(.4, 1.5); ax.set_ylim(.6, 2.2); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'pd_points': len(pd), 'barrier_points': len(bm)})
