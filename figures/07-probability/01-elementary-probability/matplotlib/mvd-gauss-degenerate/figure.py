"""Degenerate Gaussian. X ~ N(mu,Sigma), mu=(2,1), Sigma=[[2,1],[1,2]]; S=X1+X2 ~ N(3,6);
Y=(S,2S) has covariance 6[[1,2],[2,4]] of rank 1 and lies on the line y2=2y1.
(a) 300 points of Y (seed 5) on the line, mean (3,6) marked;
(b) histogram of the line coordinate S (green) and the N(3,6) density (blue)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

rng = np.random.default_rng(5)
mu = np.array([2., 1.]); S = np.array([[2., 1.], [1., 2.]]); L = np.linalg.cholesky(S)
X = mu + rng.standard_normal((300, 2)) @ L.T
s = X.sum(1); Y = np.c_[s, 2*s]
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.32)
ax = axes[0]; style(ax)
xx = np.linspace(-6, 11, 2); ax.plot(xx, 2*xx, color=BLUE, lw=1.0)
ax.plot(Y[:, 0], Y[:, 1], '.', ms=2.4, color=GREEN, zorder=4)
dot(ax, 3, 6)
lab(ax, -4, 16, '$y_2=2y_1$', BLUE, ha='left'); lab(ax, 3.6, 4.2, '$(3,6)$', RED, ha='left')
ax.set_xlim(-5, 12); ax.set_ylim(-10, 22); ax.set_xticks([0, 5, 10]); ax.set_yticks([-10, 0, 10, 20])
axlab(ax, '$y_1$', '$y_2$')
ax = axes[1]; style(ax)
ax.hist(s, bins=np.arange(-6, 12.1, 1.2), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.7)
g = np.linspace(-6, 12, 400); ax.plot(g, npdf(g, 3, 6), color=BLUE, lw=1.4)
ax.set_xlim(-6, 12); ax.set_ylim(0, .2); ax.set_xticks([-3, 0, 3, 6, 9]); ax.set_yticks([0, .1])
axlab(ax, '$s$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'seed': 5, 'n': 300, 'rank': int(np.linalg.matrix_rank(6*np.array([[1, 2], [2, 4]]))), 'mean_s': float(s.mean()), 'var_s': float(s.var())})
