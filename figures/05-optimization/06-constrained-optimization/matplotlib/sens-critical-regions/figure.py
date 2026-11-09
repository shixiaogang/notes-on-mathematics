from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Active-set regions of the budget problem with c=(2+theta,1) in the (tau,theta) plane.
fig, ax = figure(width_mm=96, height_mm=62)
xl, yl = (0, 5), (-1, 1.6)
ax.fill_between([0, 5], [-1, -1], [1.6, 1.6], facecolor='white', zorder=0)
TH = np.array(yl)
ax.fill_betweenx(TH, TH+1, TH+3, facecolor=GREEN_FILL, edgecolor='none', zorder=0)
ax.plot(TH+1, TH, color=ACTIVE, lw=1.3, zorder=2); ax.plot(TH+3, TH, color=ACTIVE, lw=1.3, zorder=2)
# verify regions numerically
pts = {}
for t, th in [(.8, .8), (2.6, .6), (4.5, .3)]:
    x, lam = budget(t, (2+th, 1)); pts[f'{t},{th}'] = [list(map(float, x)), list(map(float, lam))]
ax.text(.42, 1.05, '$\\{1,3\\}$', fontsize=8, ha='center'); ax.text(3.0, .85, '$\\{1\\}$', fontsize=8, ha='center'); ax.text(4.55, 0.25, '$\\varnothing$', fontsize=8, ha='center')
kw = dict(arrowstyle='-|>', lw=1.1, mutation_scale=7, shrinkA=0, shrinkB=0)
ax.annotate('', xy=(2.2, .1), xytext=(2, 0), arrowprops=dict(color=GREEN, **kw), zorder=6)
ax.annotate('', xy=(.5, 0), xytext=(2, 0), arrowprops=dict(color=RED, **kw), zorder=5)
opt_point(ax, (2, 0)); ax.plot([2.2], [.1], 'o', color=GREEN, ms=3.2, zorder=7); ax.plot([.5], [0], 'o', color=RED, ms=3.2, zorder=7, mfc='white')
ax.text(.52, -.13, r'$(0.5,0)$', fontsize=7.5, va='top', ha='center', color=RED); ax.text(2.27, .13, r'$(2.2,0.1)$', fontsize=7.5, color=GREEN, va='bottom')
clean(ax, xl, yl, xlabel=r'$\tau$', ylabel=r'$\theta$'); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([-1, 0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'samples': pts})
print(pts)
