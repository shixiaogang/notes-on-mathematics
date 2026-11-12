"""(a) 500 samples of (X, X^2), X ~ Unif(-1,1); (b) 500 samples of the product law P_X x P_Y (X, X'^2 with X' independent).
Red dashed rectangle: event {|x| <= 1/2, y > 1/4}; joint probability 0, product probability 1/2 * 1/2 = 1/4. Seed 719."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 500
x = rng.uniform(-1, 1, n); xp = rng.uniform(-1, 1, n)
fig, axs = figure(width_mm=104, height_mm=50, ncols=2)
for ax, (u, v), lab in zip(axs, [(x, x**2), (x, xp**2)], ['(a)', '(b)']):
    ax.scatter(u, v, s=1.6, color=GREEN, linewidths=0)
    ax.plot([-.5, .5, .5, -.5, -.5], [.25, .25, 1.02, 1.02, .25], color=RED, lw=1.0, ls='--')
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-.03, 1.05)
    ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, .25, .5, 1])
    ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=1)
    ax.set_box_aspect(.8)
    gfmt(ax)
    tag(ax, lab, y=-.28)
inside_joint = float(np.mean((np.abs(x) <= .5) & (x**2 > .25)))
inside_prod = float(np.mean((np.abs(x) <= .5) & (xp**2 > .25)))
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'empirical_joint': inside_joint, 'empirical_product': inside_prod, 'exact_joint': 0, 'exact_product': 0.25})
