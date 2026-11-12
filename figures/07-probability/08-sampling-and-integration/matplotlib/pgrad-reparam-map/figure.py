from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X = mu + sigma*eps with the four teaching normals eps = (0.3, -1.1, 0.8, -0.4), base (mu, sigma) = (1, 0.5).
# (a) mu: 1 -> 1.3: every sample moves by 0.3 (dX/dmu = 1).  (b) sigma: 0.5 -> 0.8: sample i moves by 0.3*eps_i
# (dX/dsigma = eps).  Curves: N(mu, sigma^2) before (blue) and after (yellow); dots below: samples before (blue)
# and after (yellow), arrows show the displacement of the same eps.
eps = np.array(EPS4); mu, sg = 1.0, 0.5
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.04, right=.98, bottom=.27, top=.97, wspace=.12)
x = np.linspace(-1.2, 3.0, 400)
for ax, (m2, s2) in zip(axs, [(1.3, .5), (1.0, .8)]):
    ax.plot(x, npdf(x, mu, sg), color=BLUE, lw=1.4)
    ax.plot(x, npdf(x, m2, s2), color=YELLOW, lw=1.5)
    X0 = mu+sg*eps; X1 = m2+s2*eps
    for a0, a1 in zip(X0, X1):
        ax.annotate('', xy=(a1, -.32), xytext=(a0, -.14), arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=.7, mutation_scale=6, shrinkA=2.5, shrinkB=2.5))
        dot(ax, a0, -.14, BLUE, ms=3.6); dot(ax, a1, -.32, YELLOW, ms=3.6)
    ax.axhline(0, color=STROKE, lw=.6)
    ax.set_xlim(-1.2, 3.0); ax.set_ylim(-.42, .85); ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.set_xticks([-1, 0, 1, 2, 3]); axlab(ax, r'$x$')
tags(fig, axs)
save(fig, HERE, 'figure', {'X_base': (mu+sg*eps).tolist(), 'X_shift': (1.3+.5*eps).tolist(), 'X_scale': (1.0+.8*eps).tolist()})
