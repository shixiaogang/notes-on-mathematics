from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X ~ N(0,1), S = +-1 independent, Y = S X: CDF of X+Y = 1/2 1{z>=0} + 1/2 Phi(z/2) vs N(0,2).
fig, ax = figure(width_mm=96, height_mm=46)
panel(fig, left=.09, right=.97, bottom=.22, top=.95)
zl = np.linspace(-5, 0, 200); zr = np.linspace(0, 5, 200)
ax.plot(zl, .5*Phi(zl/2), color=BLUE, lw=1.4); ax.plot(zr, .5+.5*Phi(zr/2), color=BLUE, lw=1.4)
z = np.linspace(-5, 5, 400); ax.plot(z, Phi(z/np.sqrt(2)), color=YELLOW, lw=1.5, ls=DASH)
ax.plot([0, 0], [.25, .75], color=STROKE, lw=.7, ls=DOT)
ax.plot([0], [.25], 'o', ms=4, mfc='white', mec=BLUE, mew=.9, zorder=6); dot(ax, 0, .75, RED)
lab(ax, .25, .45, '跳跃1/2', RED, ha='left'); lab(ax, -4.6, .25, '$\\mathcal{N}(0,2)$', YELLOW)
ax.set_xlim(-5, 5); ax.set_ylim(0, 1.02); ax.set_yticks([0, .25, .5, .75, 1]); axlab(ax, '$z$')
save(fig, HERE, 'figure', {'atom': .5})
