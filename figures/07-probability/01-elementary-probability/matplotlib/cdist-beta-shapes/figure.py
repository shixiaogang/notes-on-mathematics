"""(a) Beta(a,b) shapes; (b) fixed mean 0.2 with a+b=2.5,10,50."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
x = np.linspace(.002, .998, 1500)
for (a, b), c, ls in (((.5, .5), PURPLE, '-.'), ((1, 1), YELLOW, '--'), ((2, 2), BLUE, '-'), ((2, 5), GREEN, '-'), ((5, 2), RED, '-')):
    ax.plot(x, beta_pdf(x, a, b), color=c, lw=1.4, ls=ls)
lab(ax, .09, .13, '(0.5,0.5)', PURPLE); lab(ax, .43, 1.58, '(2,2)', BLUE)
lab(ax, .08, 2.55, '(2,5)', GREEN); lab(ax, .78, 2.55, '(5,2)', RED)
ax.set_xlim(0, 1); ax.set_ylim(0, 3.2); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2, 3])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f_X(x)$', labelpad=1)
ax = axes[1]; style(ax)
for (a, b), c, ls in (((.5, 2), PURPLE, '-.'), ((2, 8), BLUE, '-'), ((10, 40), GREEN, '-')):
    ax.plot(x, beta_pdf(x, a, b), color=c, lw=1.4, ls=ls)
ax.plot([.2, .2], [0, 7.5], color=RED, lw=.85, ls=DASH)
lab(ax, .5, 1.2, '$a+b=2.5$', PURPLE); lab(ax, .36, 2.6, '$a+b=10$', BLUE); lab(ax, .27, 6.0, '$a+b=50$', GREEN)
ax.set_xlim(0, 1); ax.set_ylim(0, 7.5); ax.set_xticks([0, .2, .5, 1]); ax.set_yticks([0, 2, 4, 6])
ax.set_xlabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'var_mean0.2': {k: .16/(k+1) for k in (2.5, 10, 50)}})
