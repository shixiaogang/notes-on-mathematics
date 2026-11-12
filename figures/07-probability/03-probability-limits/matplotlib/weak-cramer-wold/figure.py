from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# X=(Z,SZ), S=+-1 w.p. 1/2 independent of Z. (a) 600 samples, seed 11. (b) law of Z+SZ: atom 1/2 at 0
# plus (1/2) N(0,4) density; compare N(0,2) density.
rng = np.random.default_rng(11); Z = rng.standard_normal(600); S = rng.choice([-1, 1], 600)
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, gridspec_kw={'width_ratios': [1, 1.5]})
panel(fig, left=.07, wspace=.28, bottom=.27)
ax = axes[0]; ax.plot(Z, S*Z, 'o', ms=1.6, color=GREEN, mew=0)
ax.annotate('', xy=(2.2, 2.2), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=1.2, mutation_scale=8))
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.3, 3.3); ax.set_aspect('equal'); ax.set_xticks([-3, 0, 3]); ax.set_yticks([-3, 0, 3])
axlab(ax, r'$x_1$')
ax = axes[1]; x = np.linspace(-6, 6, 1200)
ax.plot(x, .5*npdf(x, 2), color=BLUE, lw=1.4); ax.plot(x, npdf(x, np.sqrt(2)), color=YELLOW, lw=1.6)
ax.plot([0, 0], [0, .5], color=RED, lw=2.0); dot(ax, 0, .5, RED)
lab(ax, .3, .48, r'$1/2$', RED); lab(ax, 2.1, .2, r'$\mathcal{N}(0,2)$', YELLOW)
ax.set_xlim(-6, 6); ax.set_ylim(0, .55); ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_yticks([0, .25, .5])
axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 11, 'n': 600, 'atom_at_0': 0.5, 'cov': 0.0})
