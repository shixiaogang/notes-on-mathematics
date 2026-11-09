from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Path-following iterates on the triangle: sigma=0.3 and an aggressive sigma=0.1.
ys = np.concatenate([-np.logspace(4, -2, 300), np.linspace(0, 1 - 1e-5, 400)]); P, _ = central_run(C_RUN, ys)
h3 = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=.3, eta=.9, tol=1e-3)
h1 = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=.1, eta=.9, tol=1e-3)
fig, ax = figure(width_mm=96, height_mm=62)
draw_tri(ax, labels=False)
ax.set_xlim(-.3, 1.2); ax.set_ylim(-.12, .85)
ax.text(1.05, -.03, '$\\mathbf{e}_1$', ha='left', va='top', fontsize=8)
ax.plot(*tri(P).T, color=BLUE, lw=1.0, zorder=2)
path(ax, tri(np.array([r['x'] for r in h1])), color=YELLOW, lw=1.5, ms=3.2, zorder=4)
path(ax, tri(np.array([r['x'] for r in h3])), color=GREEN, lw=1.5, ms=3.4, zorder=5)
ax.plot(*V3['e1'], 'o', color=RED, ms=5.2, zorder=8, clip_on=False)
for r, off in zip(h3[:3], [(-.06, .1), (-.02, .14), (-.02, .13)]):
    q = tri(r['x']); ax.text(q[0] + off[0], q[1] + off[1], f"$t={r['t']}$", fontsize=7.5, ha='center')
save(fig, OUT, 'figure', {'rounds_sigma_0.3': len(h3) - 1, 'rounds_sigma_0.1': len(h1) - 1, 'iterates_0.3': [r['x'].tolist() for r in h3]})
