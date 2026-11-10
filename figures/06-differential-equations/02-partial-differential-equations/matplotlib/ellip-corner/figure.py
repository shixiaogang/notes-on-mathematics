from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# corner singularity on the L-shaped domain.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [.82, 1]})
panel(fig, left=.03, wspace=.22, bottom=.24, right=.985)
ax = axes[0]
g = np.linspace(-1, 1, 801); P, Q = np.meshgrid(g, g)
R = np.hypot(P, Q); T = np.mod(np.arctan2(Q, P), 2*np.pi)
U = R**(2/3)*np.sin(2*T/3); U[(P > 0) & (Q < 0)] = np.nan
ax.contour(P, Q, U, [.15, .35, .55, .75, .95, 1.15], colors=BLUE, linewidths=.95)
ax.plot([0, 1, 1, -1, -1, 0, 0], [0, 0, 1, 1, -1, -1, 0], color=STROKE, lw=1.6)
ax.plot([0, 1], [0, 0], color=RED, lw=1.8); ax.plot([0, 0], [0, -1], color=RED, lw=1.8); dot(ax, 0, 0, RED, 4.6)
t = np.linspace(0, 1.5*np.pi, 100); ax.plot(.2*np.cos(t), .2*np.sin(t), color=MUTED, lw=.8); lab(ax, -.2, .2, r'$\omega$', MUTED, ha='right', va='bottom')
ax.set_xlim(-1.08, 1.08); ax.set_ylim(-1.08, 1.08); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax = axes[1]
r = np.logspace(-3, 0, 200)
ax.loglog(r, (2/3)*r**(-1/3), color=BLUE, lw=1.4); ax.loglog(r, 2*r, color=YELLOW, lw=1.5)
lab(ax, .02, 4.6, r'$\omega=\frac{3\pi}{2}$', BLUE); lab(ax, .08, .06, r'$\omega=\frac{\pi}{2}$', YELLOW, ha='left')
ax.set_xlim(1e-3, 1); ax.set_ylim(1e-3, 20); ax.minorticks_off(); ax.set_xticks([1e-3, 1e-2, 1e-1, 1]); ax.set_xticklabels([r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$', '1']); ax.set_yticks([1e-2, 1, 10]); ax.set_yticklabels(['0.01', '1', '10']); hat01(ax, '$r$', r'$\Vert\nabla u\Vert_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u': 'r^(2/3) sin(2 theta/3) on L-shape', 'grad': '(2/3) r^(-1/3)', 'convex': 'r^2 sin(2 theta), grad=2r'})
