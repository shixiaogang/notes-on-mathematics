from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Tent initial bump under zero Dirichlet and zero Neumann ends (series, kappa=1).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
panel(fig, left=.095, wspace=.12, bottom=.27)
ts = [.01, .05, .2]; cc = shades(3)
for ax, u in zip(axes, (uD, uN)):
    ax.plot(X, tent(X), color=RED, lw=1.5)
    for t, c in zip(ts, cc): ax.plot(X, u(X, t), color=c, lw=1.4)
    ax.set_xlim(0, 1); ax.set_ylim(0, .55); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax)
axes[0].set_ylabel('$u$', labelpad=1)
axes[1].plot(X, .25+0*X, color=YELLOW, lw=1.2, ls=DASH)
lab(axes[0], .5, .515, '$t=0$', RED, ha='center'); lab(axes[0], .5, .265, '$t=0.05$', cc[1], ha='center', va='bottom', fontsize=7.5, bbox=dict(fc='white', ec='none', pad=.4))
lab(axes[0], .5, .08, '$t=0.2$', cc[2], ha='center'); lab(axes[0], .67, .37, '$t=0.01$', cc[0], ha='left')
lab(axes[1], 1.0, .285, '平均值 1/4', YELLOW, ha='right', va='bottom')
tags(fig, axes)
save(fig, HERE, 'figure', {'D center t=.1': float(uD(.5, .1)[0]), 'N center t=.1': float(uN(.5, .1)[0])})
