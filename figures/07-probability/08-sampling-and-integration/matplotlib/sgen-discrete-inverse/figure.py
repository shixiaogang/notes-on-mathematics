from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: inverse-quantile sampling of p = (0.2, 0.5, 0.3) on {1, 2, 3} via cumulative intervals.
# u = 0.37 lies in (0.2, 0.7] -> 2; u = 0.85 lies in (0.7, 1) -> 3.
# (b) relative frequencies of n = 1000 samples, numpy seed 11.
p = np.array([.2, .5, .3]); c = np.cumsum(p)
fig, (A, B) = figure(width_mm=108, height_mm=54, ncols=2)
style(A); style(B)
xs = [1, 2, 3]
A.plot([0.3, 1], [0, 0], color=BLUE, lw=1.4)
for k in range(3):
    right = xs[k+1] if k < 2 else 3.7
    A.plot([xs[k], right], [c[k], c[k]], color=BLUE, lw=1.4)
    A.plot([xs[k]], [c[k]], 'o', ms=3.2, color=BLUE)
    A.plot([xs[k]], [c[k]-p[k]], 'o', ms=3.2, mfc='white', mec=BLUE, mew=.9)
    A.plot([0.3, 0.3], [c[k]-p[k], c[k]], color=[BLUE, YELLOW, PURPLE][k], lw=4, solid_capstyle='butt')
for u, x in ((.37, 2), (.85, 3)):
    A.plot([0.3, x], [u, u], color=GREEN, lw=1.0, ls='--')
    A.plot([x, x], [u, 0], color=GREEN, lw=1.0, ls='--')
    A.plot([0.3], [u], 'o', ms=3.6, color=RED, zorder=6)
    A.text(0.42, u+0.03, f'$u={u}$', fontsize=7.5, color=INK)
A.set_xlim(0.2, 3.7); A.set_ylim(-0.02, 1.05)
A.set_xticks([1, 2, 3]); A.set_yticks([0, .2, .7, 1])
A.set_ylabel('$F(x)$'); sub(A, 'a', '$x$')
rng = np.random.default_rng(11)
U = rng.random(1000)
X = 1+np.searchsorted(c, U, side='left')
freq = np.array([(X == k).mean() for k in xs])
B.bar(xs, freq, width=.5, color=GREEN_FILL, edgecolor=GREEN, lw=.8)
B.plot(xs, p, '_', ms=18, mew=1.6, color=BLUE)
B.set_xticks(xs); B.set_ylim(0, .6); B.set_yticks([0, .2, .4, .6])
B.set_ylabel('频率'); sub(B, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'freq': freq.tolist(), 'n': 1000, 'seed': 11})
print(freq)
