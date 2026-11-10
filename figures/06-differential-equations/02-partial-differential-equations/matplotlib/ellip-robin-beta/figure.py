from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -u''=1, Robin both ends, u=x(1-x)/2+1/(2 beta).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.085, wspace=.3, bottom=.27)
ax = axes[0]
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
for b, c in ((1, YELLOW), (2, PURPLE)):
    ax.plot(X, X*(1-X)/2+1/(2*b), color=c, lw=1.4)
    lab(ax, .5, .125+1/(2*b)+.03, r'$\beta=%g$' % b, c, ha='center')
lab(ax, .5, .125+.03, r'$\beta=\infty$', BLUE, ha='center'); dot(ax, 0, 0, RED, 4); dot(ax, 1, 0, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.02, .85); ax.set_xticks([0, 1]); ax.set_yticks([0, .5]); hat01(ax, yl='$u$')
ax = axes[1]
bs = np.logspace(-2, 3, 300)
c = 1/(2*bs); nrm = np.sqrt(1/120+c/6+c**2)
ax.axvspan(.01, .03, color=RED_FILL, lw=0)
ax.loglog(bs, nrm, color=BLUE, lw=1.4); ax.loglog(bs, 1/(2*bs), color=PURPLE, lw=1.1, ls=DASH)
lab(ax, .4, 6, r'$\frac{1}{2\beta}$', PURPLE)
ax.axhline(np.sqrt(1/120), color=STROKE, lw=.85, ls=DOT)
ax.set_xlim(.01, 1000); ax.set_ylim(.005, 80); ax.minorticks_off(); ax.set_xticks([.01, 1, 100]); ax.set_xticklabels(['0.01', '1', '100']); ax.set_yticks([.01, .1, 1, 10]); ax.set_yticklabels(['0.01', '0.1', '1', '10']); hat01(ax, r'$\beta$', r'$\Vert u\Vert_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'u': 'x(1-x)/2+1/(2beta)', 'norm^2': '1/120+c/6+c^2, c=1/(2beta)', 'dirichlet_norm': float(np.sqrt(1/120))})
