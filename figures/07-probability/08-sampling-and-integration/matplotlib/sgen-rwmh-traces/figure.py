from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: random-walk Metropolis on the mixture 0.3 N(-2, 0.5^2) + 0.7 N(2, 1), proposal y = x + s*N(0,1),
# start x = -2, 3000 steps, seed 9 for each run; step sizes s = 0.3, 2.5, 30.
logp = lambda x: math.log(mix_pdf(np.array([x]))[0]+1e-300)
fig, axs = figure(width_mm=112, height_mm=52, ncols=3, sharey=True)
res = {}
for ax, s, L in zip(axs, (0.3, 2.5, 30.0), 'abc'):
    style(ax)
    ch, a = rwmh(logp, -2.0, s, 3000, np.random.default_rng(9))
    res[s] = {'acc': a, 'frac_right': float((ch > 0).mean())}
    ax.plot(np.arange(1, 3001), ch, color=GREEN, lw=.45)
    for m in M_MIX: ax.axhline(m, color=LINE, lw=.6, ls=':')
    ax.set_ylim(-4, 5.5); ax.set_yticks([-2, 0, 2, 4]); ax.set_xlim(0, 3000); ax.set_xticks([0, 1500, 3000])
    sub(ax, L, '$t$')
axs[0].set_ylabel('$X^{(t)}$')
save(fig, HERE(__file__), 'figure', {str(k): v for k, v in res.items()})
print(res)
