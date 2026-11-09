from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Factory LP: simplex vertex route (Dantzig rule) against the central path.
mus = np.logspace(2.5, -3.5, 240)
curve = central_curve(A_FAC, B_FAC, C_FAC, np.ones(5), np.zeros(3), np.ones(5), mus)
P = np.array([c[0][:2] for c in curve])
fig, ax = figure(width_mm=92, height_mm=62)
xlim, ylim = (-.4, 6), (-.4, 4.2)
A, b = with_sign(RES_A, RES_B); V = polygon(A, b); draw_region(ax, V)
contours(ax, PROFIT, [8, 15, 26], xlim, ylim)
route = [(0, 0), (0, 3), (2, 3), (4, 2)]
for a, c in zip(route[:-1], route[1:]):
    ax.annotate('', xy=c, xytext=a, arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=1.8, shrinkA=0, shrinkB=0, mutation_scale=9), zorder=4)
ax.plot(*np.array(route[:-1]).T, 'o', color=YELLOW, ms=3.8, zorder=5)
ax.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.6, zorder=6)
ax.plot(*P[0], 'o', color=GREEN, ms=3.8, zorder=7)
opt_point(ax, (4, 2))
ax.text(.13, 3.25, '单纯形路线', fontsize=7.5, color=INK)
ax.text(P[0, 0] - .1, P[0, 1] - .42, '路径起点', fontsize=7.5, color=INK, ha='center')
ax.text(2.55, 1.5, '中心路径', fontsize=7.5, color=INK, ha='center')
ax.text(4.15, 2.1, '$(4,2)$', fontsize=7.5)
setup(ax, xlim, ylim, range(0, 7), range(0, 5))
save(fig, OUT, 'figure', {'problem': 'factory LP of the simplex chapter', 'mu_range': [float(mus[0]), float(mus[-1])], 'start_of_path': P[0].tolist()})
