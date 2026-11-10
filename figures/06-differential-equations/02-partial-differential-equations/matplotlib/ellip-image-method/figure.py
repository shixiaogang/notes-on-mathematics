from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# half-plane Green function by image; Poisson kernel.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1.15, 1]})
panel(fig, left=.03, wspace=.14, bottom=.27, right=.985)
ax = axes[0]
g1 = np.linspace(-2.6, 2.6, 701); g2 = np.linspace(.0005, 2.6, 601); P, Q = np.meshgrid(g1, g2)
Gv = -(np.log(np.hypot(P, Q-1))-np.log(np.hypot(P, Q+1)))/(2*np.pi)
ax.contour(P, Q, Gv, [.02, .05, .1, .2, .35, .55], colors=BLUE, linewidths=.95)
ax.plot([-2.6, 2.6], [0, 0], color=STROKE, lw=1.8)
dot(ax, 0, 1, RED); hollow(ax, 0, -1, PURPLE)
ax.plot([0, 0], [-1, 1], color=PURPLE, lw=.85, ls=DASH)
lab(ax, .17, 1.12, r'$\mathbf{y}$', RED); lab(ax, .14, -1.0, r'$\mathbf{y}^{*}$', PURPLE, va='center')
lab(ax, 2.55, .1, r'$G=0$', STROKE, ha='right')
ax.set_xlim(-2.6, 2.6); ax.set_ylim(-1.4, 2.6); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax = axes[1]
s = np.linspace(-3, 3, 800)
for x2, c in ((.25, BLUE), (.5, YELLOW), (1, PURPLE)):
    ax.plot(s, x2/(np.pi*(s**2+x2**2)), color=c, lw=1.4)
    lab(ax, x2*.75+.12, 1/(np.pi*x2)*.8, '$x_2=%g$' % x2, c, ha='left')
ax.set_xlim(-3, 3); ax.set_ylim(0, 1.45); ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, 1]); hat01(ax, r'$x_1-y_1$', r'$P$')
tags(fig, axes)
save(fig, HERE, 'figure', {'source': [0, 1], 'levels': [.02, .05, .1, .2, .35, .55], 'P': 'x2/(pi((x1-y1)^2+x2^2))'})
