from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Neighbourhoods of the central path in the plane of products, n=2 example.
A2, b2, c2 = np.array([[1., 1.]]), np.array([1.]), np.array([1., 2.])
x0, y0, s0 = np.array([.55, .45]), np.array([-1.]), np.array([2., 3.])
sh = short_step(A2, b2, c2, x0, y0, s0, eps=1e-6)
lg = long_step(A2, b2, c2, x0, y0, s0, sigma=.1, gamma=.1, eps=1e-6)
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
th, ga = .4, .1
L = 1.5
# one-sided neighbourhood: min w >= ga*(w1+w2)/2 -> w2/w1 between ga/(2-ga) and (2-ga)/ga
r1 = ga / (2 - ga)
a.fill([0, L, L, L * r1], [0, L * r1, L, L], facecolor=YELLOW_FILL, edgecolor=YELLOW, lw=.9, zorder=1)
# two-norm neighbourhood: |w1-w2|/sqrt2 <= th*(w1+w2)/2 -> w2/w1 = (1-q)/(1+q), q=th/sqrt2
q = th / np.sqrt(2)
r2 = (1 - q) / (1 + q)
a.fill([0, L, L, L * r2], [0, L * r2, L, L], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=2)
a.plot([0, L], [0, L], color=GREEN, lw=1.5, zorder=3)
a.annotate('$\\mathcal{N}_{2}(0.4)$', xy=(1.13, 1.0), xytext=(1.0, .42), fontsize=7.5, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6), zorder=5)
a.annotate('$\\mathcal{N}_{-\\infty}(0.1)$', xy=(.32, 1.15), xytext=(.03, 1.35), fontsize=7.5, zorder=5)
a.set_xlim(0, L); a.set_ylim(0, L); a.set_aspect('equal')
xlab(a, '$x_1s_1$', '(a) 邻域'); a.set_ylabel('$x_2s_2$', labelpad=1)
ws = np.array([r['x'] * r['s'] for r in sh]); wl = np.array([r['x'] * r['s'] for r in lg])
b.loglog([1e-7, 3], [1e-7, 3], color=GREEN, lw=1, zorder=1)
b.loglog(ws[:, 0], ws[:, 1], color=GREEN, lw=1.1, marker='o', ms=2.2, zorder=3)
b.loglog(wl[:, 0], wl[:, 1], color=YELLOW, lw=1.5, marker='o', ms=3, zorder=4)
b.set_xlim(2e-7, 3); b.set_ylim(2e-7, 3); b.set_aspect('equal')
xlab(b, '$x_1s_1$', '(b) 迭代点'); b.set_ylabel('$x_2s_2$', labelpad=1)
save(fig, OUT, 'figure', {'short_rounds': len(sh) - 1, 'long_rounds': len(lg) - 1, 'long_rel_dev': [float(np.linalg.norm(r['x'] * r['s'] - r['mu']) / r['mu']) for r in lg]})
