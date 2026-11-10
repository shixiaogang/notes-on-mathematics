from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Constant unit point source at x=0 on the real line.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.28, bottom=.27)
xx = np.linspace(-4, 4, 401)
def U(t):
    # substitution s=r^2 removes the integrable singularity at s=0
    r = (np.arange(4000)+.5)/4000*np.sqrt(t); dr = np.sqrt(t)/4000
    return np.array([(2*r*gauss(x, r**2)).sum()*dr for x in xx])
ax = axes[0]; cc = shades(3)
for t, c in zip((.25, 1, 4), cc): ax.plot(xx, U(t), color=c, lw=1.4)
dot(ax, 0, 0, RED)
lab(ax, .6, .42, '$t=0.25$', cc[0], ha='left'); lab(ax, 2.1, .55, '$t=4$', cc[2], ha='left')
ax.set_xlim(-4, 4); ax.set_ylim(0, 1.25); ax.set_xticks([-4, 0, 4]); ax.set_yticks([0, .5, 1]); axlab(ax, yl='$u$')
ax = axes[1]; T = np.linspace(0, 4, 300)
ax.plot(T, np.sqrt(T/pi), color=BLUE, lw=1.4); ax.plot([0, 4], [.25, .25], color=YELLOW, lw=1.3, ls=DASH)
dot(ax, 1, 1/np.sqrt(pi), GREEN); dot(ax, 4, 2/np.sqrt(pi), GREEN)
lab(ax, 2.3, .29, '区间稳态 1/4', YELLOW, ha='center', va='bottom')
ax.set_xlim(0, 4.2); ax.set_ylim(0, 1.25); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, .5, 1]); axlab(ax, '$t$', '$u(0,t)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u(0,1)': float(U(1)[200]), 'sqrt(1/pi)': float(1/np.sqrt(pi))}); print(U(1)[200], 1/np.sqrt(pi))
