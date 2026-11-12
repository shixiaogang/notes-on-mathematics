from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: X = sum_k 2 D_k / 3^k with independent fair digits D_k in {0,1}.
# F_n = distribution function of the uniform spread over the 2^n stage-n intervals (stages 1 and 2),
# F = Cantor function, computed by the self-similar recursion to depth 14.
def cantor(x, depth=14):
    x = np.asarray(x, float); out = np.zeros_like(x); scale = .5
    y = x.copy(); done = np.zeros(x.shape, bool)
    for _ in range(depth):
        left = (y < 1/3) & ~done; mid = (y >= 1/3) & (y <= 2/3) & ~done; right = (y > 2/3) & ~done
        out[mid] += scale; done |= mid
        out[right] += scale
        y = np.where(left, 3*y, np.where(right, 3*y-2, y))
        scale /= 2
    return out
def stage_cdf(x, n):
    ivs = [(0.0, 1.0)]
    for _ in range(n):
        ivs = [iv for a, b in ivs for iv in ((a, a+(b-a)/3), (b-(b-a)/3, b))]
    L = (2/3)**n; F = np.zeros_like(x)
    for a, b in ivs:
        F += np.clip((x-a)/(b-a), 0, 1)*(b-a)/L
    return F
x = np.linspace(0, 1, 3001)
fig, ax = figure(width_mm=88, height_mm=56)
style(ax)
ax.plot(x, stage_cdf(x, 1), color=YELLOW, lw=1.2)
ax.plot(x, stage_cdf(x, 2), color=PURPLE, lw=1.0)
ax.plot(x, cantor(x), color=BLUE, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(0, 1.04)
ax.set_xticks([0, 1/3, 2/3, 1]); ax.set_xticklabels(['0', '1/3', '2/3', '1'])
ax.set_yticks([0, .25, .5, .75, 1])
ax.set_xlabel('$x$'); ax.set_ylabel('$F(x)$')
assert abs(cantor(np.array([.25]))[0]-1/3) < 1e-3
save(fig, HERE(__file__), 'figure', {'F(1/4)': 1/3, 'stages': [1, 2], 'depth': 14})
