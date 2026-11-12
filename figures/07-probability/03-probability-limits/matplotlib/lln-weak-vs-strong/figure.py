from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Weak versus strong law: 40 frequency paths of a fair coin (seed 21), n <= 2000, band 1/2 +- 0.05 (blue fill).
# Red dot: last time n <= 2000 at which a path is outside the band. Grey vertical line at n = 400.
rng = np.random.default_rng(21)
N, M, eps = 2000, 40, .05
n = np.arange(1, N+1)
F = np.cumsum(rng.random((M, N)) < .5, axis=1)/n
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, left=.11, right=.97, bottom=.2, top=.95)
ax.axhspan(.5-eps, .5+eps, color=BLUE_FILL, lw=0)
for f in F: ax.plot(n, f, color=GREEN, lw=.6)
last = []
for f in F:
    out = np.flatnonzero(np.abs(f-.5) >= eps)
    if len(out): last.append(int(n[out[-1]])); dot(ax, n[out[-1]], f[out[-1]], ms=3.2)
ax.axvline(400, color=STROKE, lw=.8, ls=DASH)
ax.set_xlim(1, N); ax.set_ylim(.2, .8); ax.set_xticks([1, 400, 1000, 2000]); ax.set_yticks([.3, .45, .5, .55, .7])
axlab(ax, '$n$')
out400 = int(np.sum(np.abs(F[:, 399]-.5) >= eps))
save(fig, HERE, 'figure', {'seed': 21, 'outside_at_400': out400, 'last_exit_times': sorted(last), 'max_last_exit': max(last)})
