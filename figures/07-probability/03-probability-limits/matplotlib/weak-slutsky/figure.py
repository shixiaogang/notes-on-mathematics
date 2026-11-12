from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# X~N(0,1), ratio X/(1+X/sqrt n) -> N(0,1) by Slutsky. 2e5 samples, seed 3; histogram restricted to [-4,4]
# (density normalised by the full sample size).
rng = np.random.default_rng(3); X = rng.standard_normal(200000)
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.25, bottom=.27)
bins = np.linspace(-4, 4, 81); facts = {}
for ax, n in zip(axes, (4, 100)):
    R = X/(1+X/np.sqrt(n)); h, _ = np.histogram(R, bins); h = h/(len(R)*(bins[1]-bins[0]))
    ax.bar(bins[:-1], h, width=bins[1]-bins[0], align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.3)
    x = np.linspace(-4, 4, 400); ax.plot(x, npdf(x), color=BLUE, lw=1.4)
    lab(ax, 3.9, .75, r'$n=%d$' % n, INK, ha='right', va='top')
    facts[n] = {'outside_[-4,4]': float(np.mean(np.abs(R) > 4))}
    ax.set_xlim(-4, 4); ax.set_ylim(0, .78); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, .2, .4, .6])
    axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 3, 'n_samples': 200000, **{str(k): v for k, v in facts.items()}})
