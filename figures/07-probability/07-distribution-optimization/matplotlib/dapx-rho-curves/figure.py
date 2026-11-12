from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target N(0,[[1,rho],[rho,1]]), independent Gaussian candidates.
# (a) marginal variance of each optimum: D(Q||Pi) gives 1-rho^2 (yellow); D(Pi||Q) gives 1 (purple dashed) = target (blue).
# (b) minimum value of either objective, -0.5 ln(1-rho^2) (blue), and the cross value: the D(Q||Pi)-optimum
#     evaluated by D(Pi||Q), equal to the D(Pi||Q)-optimum evaluated by D(Q||Pi): 0.5(2rho^2/(1-rho^2)+ln(1-rho^2)) (red).
r = np.linspace(-.95, .95, 400)
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.29, wspace=.28)
ax = axs[0]
ax.plot(r, np.ones_like(r), color=BLUE, lw=1.4)
ax.plot(r, np.ones_like(r), color=PURPLE, lw=1.2, ls=DASH)
ax.plot(r, 1-r*r, color=YELLOW, lw=1.6)
dot(ax, RHO, 1-RHO**2, RED, ms=4)
lab(ax, .35, .3, '0.36', INK, fontsize=7)
ax.set_xlim(-1, 1); ax.set_ylim(0, 1.15); axlab(ax, r'$\rho$', None)
ax = axs[1]
mn = -0.5*np.log(1-r*r); cr = 0.5*(2*r*r/(1-r*r)+np.log(1-r*r))
ax.plot(r, mn, color=BLUE, lw=1.4); ax.plot(r, cr, color=RED, lw=1.4, ls=DASH)
for v in (-0.5*math.log(1-RHO**2), 0.5*(2*RHO**2/(1-RHO**2)+math.log(1-RHO**2))):
    dot(ax, RHO, v, RED, ms=4)
lab(ax, -.62, .72, '最小值', BLUE, fontsize=7); lab(ax, -.2, 2.2, '交叉评价', RED, fontsize=7)
ax.set_xlim(-1, 1); ax.set_ylim(0, 3); axlab(ax, r'$\rho$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'rho': RHO, 'min': -0.5*math.log(1-RHO**2), 'cross': 0.5*(2*RHO**2/(1-RHO**2)+math.log(1-RHO**2))})
