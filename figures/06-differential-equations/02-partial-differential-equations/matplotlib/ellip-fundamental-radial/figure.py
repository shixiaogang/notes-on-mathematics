from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
r = np.linspace(.03, 3, 800)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.085, wspace=.3, bottom=.27)
ax = axes[0]
ax.axhline(0, color=STROKE, lw=.6)
ax.plot(r, -r/2, color=YELLOW, lw=1.5); ax.plot(r, -np.log(r)/(2*np.pi), color=BLUE, lw=1.4); ax.plot(r, 1/(4*np.pi*r), color=PURPLE, lw=1.4)
lab(ax, 2.1, -.82, '$d=1$', YELLOW, ha='right'); lab(ax, .42, .4, '$d=2$', BLUE, ha='left'); lab(ax, .3, .92, '$d=3$', PURPLE)
ax.set_xlim(0, 3); ax.set_ylim(-1.2, 1.3); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([-1, 0, 1]); hat01(ax, '$r$', r'$\varphi(r)$')
ax = axes[1]
ax.loglog(r, .5+0*r, color=YELLOW, lw=1.5); ax.loglog(r, 1/(2*np.pi*r), color=BLUE, lw=1.4); ax.loglog(r, 1/(4*np.pi*r**2), color=PURPLE, lw=1.4)
lab(ax, 2.5, .6, '$d=1$', YELLOW, ha='right'); lab(ax, .09, .62, '$d=2$', BLUE, ha='right', va='bottom'); lab(ax, .2, 3.1, '$d=3$', PURPLE, ha='left')
ax.set_xlim(.03, 3); ax.set_ylim(.008, 80); ax.minorticks_off(); ax.set_xticks([.1, 1]); ax.set_xticklabels(['0.1', '1']); ax.set_yticks([.01, 1, 10]); ax.set_yticklabels(['0.01', '1', '10']); hat01(ax, '$r$', r"$-\varphi'(r)$")
tags(fig, axes)
save(fig, HERE, 'figure', {'phi': '-r/2; -log(r)/(2pi); 1/(4 pi r)'})
