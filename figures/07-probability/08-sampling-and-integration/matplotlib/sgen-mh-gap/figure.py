from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: uniform distribution on [0,1] U [3,4] (p~ = indicator). Metropolis with proposal Unif(x-h, x+h).
# Start x = 0.5, 2000 steps, seed 10. (a) h = 0.5: no proposal can cross the gap (1,3); (b) h = 2.5: crosses.
def run(h, n=2000, seed=10):
    rng = np.random.default_rng(seed); x = .5; out = np.empty(n); acc = 0
    inside = lambda y: (0 <= y <= 1) or (3 <= y <= 4)
    for t in range(n):
        y = x+h*(2*rng.random()-1)
        if inside(y): x = y; acc += 1
        rng.random()  # the accept uniform (ratio is 0 or 1 here)
        out[t] = x
    return out, acc/n
fig, (A, B) = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
res = {}
for ax, h, L in ((A, .5, 'a'), (B, 2.5, 'b')):
    style(ax)
    ch, a = run(h); res[h] = {'acc': a, 'frac_upper': float((ch > 2).mean())}
    for lo in (0, 3): ax.axhspan(lo, lo+1, color=BLUE_FILL, lw=0)
    ax.plot(np.arange(1, 2001), ch, color=GREEN, lw=.45)
    ax.set_xlim(0, 2000); ax.set_xticks([0, 1000, 2000]); ax.set_ylim(-.3, 4.3); ax.set_yticks([0, 1, 3, 4])
    sub(ax, L, '$t$')
A.set_ylabel('$X^{(t)}$')
save(fig, HERE(__file__), 'figure', {str(k): v for k, v in res.items()})
print(res)
