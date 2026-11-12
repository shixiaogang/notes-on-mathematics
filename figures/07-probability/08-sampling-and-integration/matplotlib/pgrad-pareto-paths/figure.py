from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X has density 3 x^{-4} on [1, inf) (generated as (1-U)^{-1/3}); J(theta) = E[X^theta] = 3/(3-theta), theta < 3.
# Direct-derivative samples G = X^theta ln X, E[G] = 3/(3-theta)^2.  E[G^2] < inf iff theta < 3/2.
# Running averages of G for 5 seeded paths, n = 1..20000: (a) theta = 1 (truth 0.75), (b) theta = 2 (truth 3).
rng = np.random.default_rng(SEED)
N = 20000; n = np.arange(1, N+1)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.3, top=.95, wspace=.26)
facts = {}
for ax, th, yl in [(axs[0], 1.0, (0, 1.5)), (axs[1], 2.0, (0, 6))]:
    truth = 3/(3-th)**2
    for k in range(5):
        X = (1-rng.random(N))**(-1/3); G = X**th*np.log(X)
        m = np.cumsum(G)/n
        ax.plot(n, m, color=GREEN, lw=.8)
        facts[f'theta{th}_path{k}_final'] = float(m[-1])
    ax.axhline(truth, color=BLUE, lw=1.3)
    ax.set_xscale('log'); ax.set_xlim(10, N); ax.set_ylim(*yl)
    axlab(ax, r'$n$')
    facts[f'truth_{th}'] = truth
axs[0].set_yticks([0, .75, 1.5]); axs[0].set_yticklabels(['0', '0.75', '1.5']); axs[1].set_yticks([0, 3, 6])
tags(fig, axs)
save(fig, HERE, 'figure', facts)
