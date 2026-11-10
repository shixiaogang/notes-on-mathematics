from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Characteristic pictures of Burgers Riemann problems; the interface x=0 is where the flux is read.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.06, wspace=.16, bottom=.27)
ax = axes[0]
for x0 in np.arange(-1, 0.01, .2):
    t = -x0/(1-.5) if x0 < 0 else 0; ax.plot([x0, x0+t], [0, t], color=STROKE, lw=.8)
for x0 in np.arange(.2, 1.01, .2):
    t = x0/.5; ax.plot([x0, x0], [0, min(t, 1)], color=STROKE, lw=.8)
ax.plot([0, .5], [0, 1], color=STROKE, lw=2)
ax.set_xlim(-1, 1); ax.set_ylim(0, 1); lab(ax, -.72, .82, '$u=1$', BLUE, ha='center', bbox=dict(fc='white', ec='none', pad=1)); lab(ax, .8, .82, '$u=0$', BLUE, ha='center', bbox=dict(fc='white', ec='none', pad=1)); lab(ax, .62, .46, '$s=1/2$', INK, ha='center', bbox=dict(fc='white', ec='none', pad=1))
ax = axes[1]
ax.fill([0, -1, 1], [0, 1, 1], color=BLUE_FILL, lw=0)
for s in np.linspace(-1, 1, 9): ax.plot([0, s], [0, 1], color=STROKE, lw=.8)
for x0 in (-.8, -.5, -.2): ax.plot([x0, x0-(1+x0) if 0 else -1], [0, (-1-x0)/(-1)], color=STROKE, lw=.8)
for x0 in (.2, .5, .8): ax.plot([x0, 1], [0, 1-x0], color=STROKE, lw=.8)
ax.set_xlim(-1, 1); ax.set_ylim(0, 1); lab(ax, -.72, .15, '$u=-1$', BLUE, ha='center', bbox=dict(fc='white', ec='none', pad=1)); lab(ax, .72, .15, '$u=1$', BLUE, ha='center', bbox=dict(fc='white', ec='none', pad=1))
for ax in axes:
    ax.axvline(0, color=PURPLE, lw=1.2, ls=DASH); ax.set_xticks([0]); ax.set_xticklabels(['$0$']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1)
axes[0].set_ylabel('$t$', labelpad=1); tags(fig, axes)
save(fig, HERE, 'figure', {'shock_speed': .5, 'god_flux': [godunov(1, 0), godunov(-1, 1)]})
