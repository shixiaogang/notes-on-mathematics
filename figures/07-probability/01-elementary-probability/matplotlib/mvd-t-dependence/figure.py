"""Bivariate t with nu=5, mu=0, Sigma=I: zero covariance but dependent components.
(a) 1500 points (seed 31) of X = sqrt(5/U) Z; circles Q=1,4 of the density.
(b) E[X2^2 | X1=x1] = (5+x1^2)/4 (blue); binned estimates from 400000 points (seed 32, bins of width 0.5,
green); unconditional E[X2^2]=5/3 (purple dashed)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

nu = 5
def sample(seed, m):
    r = np.random.default_rng(seed); Z = r.standard_normal((m, 2)); U = r.chisquare(nu, m)
    return Z*np.sqrt(nu/U)[:, None]
X = sample(31, 1500)
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.97, top=.96, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
ax.plot(X[:, 0], X[:, 1], '.', ms=1.6, color=GREEN)
t = np.linspace(0, 2*pi, 300)
for c in (1, 2):
    ax.plot(c*np.cos(t), c*np.sin(t), color=BLUE, lw=1.2, zorder=5)
ax.set_xlim(-7, 7); ax.set_ylim(-7, 7); ax.set_aspect('equal')
ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_yticks([-6, -3, 0, 3, 6]); axlab(ax, '$x_1$', '$x_2$')
ax = axes[1]; style(ax)
Y = sample(32, 400000); edges = np.arange(-4, 4.01, .5); mids = (edges[1:]+edges[:-1])/2
est = [float(np.mean(Y[(Y[:, 0] >= a) & (Y[:, 0] < b), 1]**2)) for a, b in zip(edges[:-1], edges[1:])]
g = np.linspace(-4, 4, 300); ax.plot(g, (nu+g**2)/(nu-1), color=BLUE, lw=1.4)
ax.plot(mids, est, 'o', ms=3.0, color=GREEN, zorder=5)
ax.axhline(nu/(nu-2), color=PURPLE, lw=1.0, ls=DASH)
lab(ax, 2.0, 1.25, '$5/3$', PURPLE, ha='left')
ax.set_xlim(-4, 4); ax.set_ylim(0, 6); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, 2, 4, 6])
axlab(ax, '$x_1$', r'$\mathbb{E}[X_2^{2}\mid X_1=x_1]$' if False else r'$\mathrm{E}[X_2^{2}\mid X_1=x_1]$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'nu': nu, 'seeds': [31, 32], 'bins_mid': mids.tolist(), 'binned': est})
