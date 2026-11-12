"""Gaussian components that are not jointly Gaussian: Z ~ N(0,1), S = +-1 with prob 1/2, independent.
(a) 400 points of (Z, SZ) (seed 3) on the two diagonals;
(b) distribution of Z+SZ: atom of mass 1/2 at 0 (red bar) and continuous part with density 0.5*N(0,4)
(blue), histogram of the nonzero simulated values scaled by their share (green)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

rng = np.random.default_rng(3)
Z = rng.standard_normal(4000); Sg = rng.choice([-1., 1.], 4000)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, top=.96, bottom=.28, wspace=.32)
ax = axes[0]; style(ax)
ax.plot(Z[:400], (Sg*Z)[:400], '.', ms=2.2, color=GREEN)
ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.3, 3.3); ax.set_aspect('equal')
ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$z$', '$sz$')
ax = axes[1]; style(ax)
T = Z+Sg*Z; nz = T[T != 0]
ax.hist(nz, bins=np.arange(-7, 7.01, .7), weights=np.full(nz.size, 1/T.size/.7), color=GREEN_FILL, edgecolor=GREEN, lw=.7)
g = np.linspace(-7, 7, 400); ax.plot(g, .5*npdf(g, 0, 4), color=BLUE, lw=1.4)
ax.plot([0, 0], [0, .5], color=RED, lw=2.4, solid_capstyle='butt'); dot(ax, 0, .5, ms=4)
lab(ax, .35, .47, r'$\mathrm{P}=1/2$', RED, ha='left')
ax.set_xlim(-7, 7); ax.set_ylim(0, .55); ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_yticks([0, .25, .5])
axlab(ax, '$z+sz$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'seed': 3, 'n': 4000, 'share_zero': float(np.mean(T == 0))})
