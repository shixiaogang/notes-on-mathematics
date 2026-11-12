from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# (a) U,V ~ Unif(0,1): U-V under independence, V=1-U, V=U. (b) jointly Gaussian, rho = 0.8, 0, -0.8: X-Y ~ N(0, 2-2rho).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.25)
ax = axes[0]; z = np.linspace(-1.3, 1.3, 600)
ax.plot(z, np.clip(1-np.abs(z), 0, None), color=BLUE, lw=1.4)
ax.plot([-1.3, -1, -1, 1, 1, 1.3], [0, 0, .5, .5, 0, 0], color=YELLOW, lw=1.5)
ax.plot([0, 0], [0, 1.25], color=RED, lw=1.6); dot(ax, 0, 1.25, RED)
lab(ax, .06, 1.2, '原子', RED, ha='left'); lab(ax, .55, .53, '$V=1-U$', YELLOW, ha='left'); lab(ax, -.95, .78, '独立', BLUE, ha='left')
ax.set_xlim(-1.3, 1.3); ax.set_ylim(0, 1.35); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, .5, 1]); axlab(ax, '$z$')
ax = axes[1]; z = np.linspace(-5, 5, 600)
for rho, c in ((.8, '#4E6784'), (0, '#7188A3'), (-.8, '#A9B9CC')):
    v = 2-2*rho; ax.plot(z, phi(z, 0, np.sqrt(v)), color=c, lw=1.4)
lab(ax, .55, .6, '$\\rho=0.8$', '#4E6784', ha='left'); lab(ax, 1.35, .22, '$\\rho=0$', '#7188A3', ha='left'); lab(ax, 2.6, .1, '$\\rho=-0.8$', '#7F93AB', ha='left')
ax.set_xlim(-5, 5); ax.set_ylim(0, .68); ax.set_xticks([-4, 0, 4]); ax.set_yticks([0, .3, .6]); axlab(ax, '$z$')
tags(fig, axes)
save(fig, HERE, 'figure', {'variances uniform': [1/6, 1/3, 0], 'gauss': [.4, 2, 3.6]})
