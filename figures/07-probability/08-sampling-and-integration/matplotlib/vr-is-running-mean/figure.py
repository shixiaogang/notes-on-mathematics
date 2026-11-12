from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Running importance-sampling estimates of I = P(X>4), X ~ Exp(1), divided by I, n = 1..2e5.
# (a) proposal Exp(1/4): finite variance.  (b) proposal Exp(2.5): unbiased but E_q[(f w)^2] = infinity,
# weight w(x) = 0.4 e^{1.5x} >= 161 on x>4.  Three paths each, seeds 11, 12, 13.
I = math.exp(-4); N = 200000; n = np.arange(1, N+1)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.22)
info = {}
for ax, lam in zip(axs, (0.25, 2.5)):
    for k, s in enumerate((11, 12, 13)):
        rng = np.random.default_rng(s)
        x = rng.exponential(1/lam, N)
        y = np.where(x > 4, np.exp(-x)/(lam*np.exp(-lam*x)), 0.0)
        run = np.cumsum(y)/n/I
        ax.plot(n, run, color=GREEN, lw=.9)
        info[f'lam{lam}_seed{s}_final'] = float(run[-1]); info[f'lam{lam}_seed{s}_hits'] = int((x > 4).sum())
    ax.axhline(1, color=BLUE, lw=1.2)
    ax.set_xscale('log'); ax.set_xlim(10, N); ax.set_ylim(0, 3); ax.set_yticks([0, 1, 2, 3])
    logticks(ax, [1, 3, 5], 'x'); axlab(ax, '$n$')
axs[0].set_ylabel(r'$\hat{I}_n/I$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', info)
