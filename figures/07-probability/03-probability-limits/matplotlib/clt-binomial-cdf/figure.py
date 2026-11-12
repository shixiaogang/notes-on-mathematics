from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# S ~ Bin(20, 0.3): exact distribution function (staircase), normal approximation
# Phi((x-6)/sqrt(4.2)) and the continuity-corrected Phi((x+0.5-6)/sqrt(4.2)); threshold k = 8.
n, p = 20, .3; m = n*p; sd = math.sqrt(n*p*(1-p))
pm = binpmf(n, p); F = np.cumsum(pm)
fig, ax = figure(width_mm=96, height_mm=54)
for k in range(0, 15):
    ax.plot([k, k+1], [F[k], F[k]], color=GREEN, lw=1.4, solid_capstyle='butt')
    ax.plot([k], [F[k]], 'o', ms=2.4, color=GREEN, mew=0)
x = np.linspace(-.5, 15, 800)
ax.plot(x, Phi((x-m)/sd), color=BLUE, lw=1.4)
ax.plot(x, Phi((x+.5-m)/sd), color=YELLOW, lw=1.6, ls=DASH)
ax.axvline(8, color=RED, lw=.9, ymax=.92)
dot(ax, 8, F[8], GREEN, ms=4); dot(ax, 8, float(Phi((8-m)/sd)), BLUE, ms=4); dot(ax, 8, float(Phi((8.5-m)/sd)), YELLOW, ms=4)
lab(ax, 8.35, .79, r'$\Phi\left(\frac{8-6}{\sqrt{4.2}}\right)$', BLUE, ha='left')
lab(ax, 2.2, .62, r'$\Phi\left(\frac{x+0.5-6}{\sqrt{4.2}}\right)$', YELLOW, ha='right')
ax.set_xlim(-.5, 15); ax.set_ylim(0, 1.06); ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
axlab(ax, '$x$', None)
save(fig, HERE, 'figure', {'F(8)': float(F[8]), 'normal': float(Phi((8-m)/sd)), 'corrected': float(Phi((8.5-m)/sd))})
