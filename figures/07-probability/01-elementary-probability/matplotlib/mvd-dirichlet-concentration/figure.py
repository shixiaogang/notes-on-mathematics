"""Dirichlet samples with fixed mean m=(0.2,0.3,0.5) and alpha0 = 1, 10, 100 (alpha = alpha0 * m).
500 samples each by Gamma normalization (numpy gamma, seed 51, 52, 53); mean m as red dot.
Var(P1) = 0.16/(alpha0+1): 0.08, 0.0145, 0.00158; sample values in figure.json."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

m = np.array([.2, .3, .5])
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panel(fig, left=.01, right=.99, top=.98, bottom=.14, wspace=.06)
facts = {}
for ax, a0, seed in zip(axes, (1, 10, 100), (51, 52, 53)):
    rng = np.random.default_rng(seed); G = rng.gamma(a0*m, 1., (500, 3)); P = G/G.sum(1, keepdims=True)
    x, y = tri_xy(P)
    ax.plot(x, y, '.', ms=1.6, color=GREEN, zorder=4)
    tri_frame(ax, labels=('$e_1$', '$e_2$', '$e_3$'))
    mx, my = tri_xy(m); dot(ax, float(mx), float(my), ms=3.8, z=8)
    facts[f'alpha0={a0}'] = {'seed': seed, 'sample_var_P1': float(P[:, 0].var()), 'theory_var_P1': .16/(a0+1)}
tags(fig, axes)
save(fig, HERE(__file__), 'figure', facts)
