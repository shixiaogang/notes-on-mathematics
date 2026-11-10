from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Heat kernel at several times and the scaling collapse.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
xx = np.linspace(-1.6, 1.6, 900); ts = (.01, .04, .16); cc = shades(3)
ax = axes[0]
for t, c in zip(ts, cc): ax.plot(xx, gauss(xx, t), color=c, lw=1.4)
lab(ax, .16, 2.55, '$t=0.01$', cc[0], ha='left'); lab(ax, .3, 1.15, '$0.04$', cc[1], ha='left'); lab(ax, .75, .5, '$0.16$', cc[2], ha='left')
ax.set_xlim(-1.6, 1.6); ax.set_ylim(0, 3.05); ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2, 3]); axlab(ax, yl='$G(x,t)$')
ax = axes[1]; z = np.linspace(-5, 5, 500)
for i, (t, c) in enumerate(zip(ts, cc)):
    ax.plot(z, np.sqrt(t)*gauss(z*np.sqrt(t), t), color=c, lw=1.6-.25*i, ls=[(0, ()), DASH, DOT][i])
ax.set_xlim(-5, 5); ax.set_ylim(0, .32); ax.set_xticks([-4, 0, 4]); ax.set_yticks([0, .28]); ax.set_yticklabels(['0', '0.28']); axlab(ax, r'$x/\sqrt{t}$', r'$\sqrt{t}\,G$')
tags(fig, axes)
save(fig, HERE, 'figure', {'peak': [float(gauss(0., t)) for t in ts], 'std': [float(np.sqrt(2*t)) for t in ts]})
