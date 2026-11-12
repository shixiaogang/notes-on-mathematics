"""Conditioning N(mu,Sigma), mu=(2,1), Sigma=[[2,1],[1,2]] on X1=4.
(a) ellipses Q=1,4 (blue), conditional mean line m(x1)=1+(x1-2)/2 (yellow), observation x1=4 (red line),
conditional mean m(4)=2 (red dot);
(b) marginal density of X2, N(1,2) (blue), and conditional density N(2,3/2) (yellow)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

mu = np.array([2., 1.]); S = np.array([[2., 1.], [1., 2.]])
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.97, top=.96, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
for c in (1, 2):
    ex, ey = ellipse(mu, S, c); ax.plot(ex, ey, color=BLUE, lw=1.2)
xx = np.linspace(-2, 6, 2); ax.plot(xx, 1+(xx-2)/2, color=YELLOW, lw=1.6)
ax.plot([4, 4], [-3, 5], color=RED, lw=1.1)
dot(ax, 4, 2)
dot(ax, *mu, color=STROKE, ms=3)
lab(ax, 3.85, 2.45, '$(4,2)$', RED, ha='right')
lab(ax, 4.3, 3.7, '$m(x_1)$', YELLOW, ha='left')
ax.set_xlim(-1.5, 6); ax.set_ylim(-3, 5); ax.set_aspect('equal')
ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([-2, 0, 2, 4]); axlab(ax, '$x_1$', '$x_2$')
ax = axes[1]; style(ax)
g = np.linspace(-4, 6, 400)
ax.plot(g, npdf(g, 1, 2), color=BLUE, lw=1.4)
ax.plot(g, npdf(g, 2, 1.5), color=YELLOW, lw=1.8)
lab(ax, -2.6, .2, r'$\mathcal{N}(1,2)$', BLUE, ha='left')
lab(ax, 3.1, .29, r'$\mathcal{N}(2,3/2)$', YELLOW, ha='left')
ax.set_xlim(-4, 6); ax.set_ylim(0, .36); ax.set_xticks([-2, 0, 2, 4]); ax.set_yticks([0, .1, .2, .3])
axlab(ax, '$x_2$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'cond_mean': 2.0, 'cond_var': 1.5, 'P_marg_gt2': float(1-Phi(1/np.sqrt(2))), 'P_cond_gt2': 0.5})
