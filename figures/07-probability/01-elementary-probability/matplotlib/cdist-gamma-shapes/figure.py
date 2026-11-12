"""(a) Gamma(alpha,1) densities for alpha=0.5,1,2,5; (b) chi-square densities nu=1,2,4,8."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
x = np.linspace(.001, 10, 2000)
for a, c, ls in ((.5, PURPLE, '-.'), (1, YELLOW, '--'), (2, BLUE, '-'), (5, GREEN, '-')):
    ax.plot(x, gamma_pdf(x, a, 1), color=c, lw=1.4, ls=ls)
lab(ax, .5, .88, r'$\alpha=0.5$', PURPLE); lab(ax, .9, .5, r'$\alpha=1$', YELLOW); lab(ax, 1.3, .39, r'$\alpha=2$', BLUE); lab(ax, 4.6, .21, r'$\alpha=5$', GREEN)
ax.set_xlim(0, 10); ax.set_ylim(0, 1.05); ax.set_xticks([0, 2, 4, 6, 8, 10]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$f_X(x)$', labelpad=1)
ax = axes[1]; style(ax)
x = np.linspace(.001, 16, 2000)
for nu, c, ls in ((1, PURPLE, '-.'), (2, YELLOW, '--'), (4, BLUE, '-'), (8, GREEN, '-')):
    ax.plot(x, gamma_pdf(x, nu/2, .5), color=c, lw=1.4, ls=ls)
lab(ax, .9, .42, r'$\nu=1$', PURPLE); lab(ax, 2.2, .28, r'$\nu=2$', YELLOW); lab(ax, 3.4, .2, r'$\nu=4$', BLUE); lab(ax, 8.4, .11, r'$\nu=8$', GREEN)
ax.set_xlim(0, 16); ax.set_ylim(0, .55); ax.set_xticks([0, 4, 8, 12, 16]); ax.set_yticks([0, .25, .5])
ax.set_xlabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'rate_panel_a': 1, 'chi2': 'Gamma(nu/2, 1/2)'})
