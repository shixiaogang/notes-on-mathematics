from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
from matplotlib.colors import LinearSegmentedColormap
# Grid of n=80 points on [0,1]. Source: 0.5 N(0.25,0.07^2)+0.5 N(0.65,0.08^2) discretized; target N(0.5,0.12^2).
# Cost (x-y)^2. Entropic plans for eps = 2e-2, 5e-3, 5e-4 (log-domain Sinkhorn, 3000 rounds);
# displayed row-normalized, i.e. the conditional law of y given x under pi_eps.
# Red line: monotone (quantile) map of the discretized marginals = unregularized optimum on the line.
n = 80
z = (np.arange(n)+.5)/n
def nd(x, m, s): return np.exp(-(x-m)**2/(2*s*s))
a = .5*nd(z, .25, .07)+.5*nd(z, .65, .08); a /= a.sum()
b = nd(z, .5, .12); b /= b.sum()
C = (z[:, None]-z[None, :])**2
u = np.linspace(.0005, .9995, 2000)
qa = quantile(z, a, u); qb = quantile(z, b, u)
cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, left=.08, right=.97, top=.97, bottom=.27, wspace=.36)
facts = {}
for ax, eps in zip(axs, (2e-2, 5e-3, 5e-4)):
    f, g, _ = sinkhorn_log(a, b, C, eps, 3000)
    P = plan(a, b, C, eps, f, g)
    R = P/P.sum(1, keepdims=True)
    ax.imshow(R.T, origin='lower', extent=(0, 1, 0, 1), cmap=cmap, vmin=0, vmax=R.max(), interpolation='nearest')
    ax.plot(qa, qb, color=RED, lw=.85, ls=DOT)
    ax.set_xticks([0, .5, 1], ['0', '0.5', '1']); ax.set_yticks([0, .5, 1], ['0', '0.5', '1'])
    ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$y$', labelpad=1)
    facts[str(eps)] = {'cost': float((C*P).sum()), 'row_res': float(np.abs(P.sum(1)-a).sum())}
facts['unregularized_cost'] = float(np.mean((qa-qb)**2))
tags(fig, axs)
save(fig, HERE, 'figure', facts)
