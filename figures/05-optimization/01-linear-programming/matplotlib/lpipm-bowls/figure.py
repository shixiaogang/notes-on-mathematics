from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Level sets of the barrier objective on the running triangle for three values of mu.
X, Y, x1, x2, x3 = tri_grid(700)
inside = (x1 > 1e-4) & (x2 > 1e-4) & (x3 > 1e-4)
ys = np.concatenate([-np.logspace(3, -2, 120), np.linspace(0, 1 - 1e-4, 200)]); P, M = central_run(C_RUN, ys)
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
cases = [(2., '(a) $\\mu=2$'), (.5, '(b) $\\mu=0.5$'), (.1, '(c) $\\mu=0.1$')]
facts = {}
for ax, (mu, lab) in zip(axs, cases):
    draw_tri(ax, labels=False)
    B = np.where(inside, x1 + 2 * x2 + 3 * x3 - mu * (np.log(np.where(inside, x1, 1)) + np.log(np.where(inside, x2, 1)) + np.log(np.where(inside, x3, 1))), np.nan)
    k = np.nanargmin(B); bmin = B.flat[k]
    ax.contour(X, Y, B, levels=bmin + mu * np.array([.15, .5, 1.2, 2.5, 4.5, 7.5]), colors=BLUE, linewidths=.8, zorder=2)
    i = np.argmin(np.abs(M - mu)); p = tri(P[i])
    ax.plot(*tri(P).T, color=GREEN, lw=1.1, zorder=3)
    ax.plot(*p, 'o', color=GREEN, ms=4.4, zorder=5)
    ax.plot(*V3['e1'], 'o', color=RED, ms=4.4, zorder=6, clip_on=False)
    ax.text(0, -.12, lab, ha='center', va='top', fontsize=8)
    facts[str(mu)] = P[i].tolist()
save(fig, OUT, 'figure', {'problem': 'min x1+2x2+3x3, sum x=1', 'central_points': facts})
