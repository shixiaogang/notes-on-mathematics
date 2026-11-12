"""Bern(p): (a) mass table for p=0.2 with its mean as balance point; (b) variance p(1-p)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'cdist-common'))
from cdist_fig import *

p = 0.2
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.34)
ax = axes[0]; style(ax)
bars(ax, [0, 1], [1-p, p], width=.28)
ax.plot([p], [-0.035], marker='^', ms=6, color=RED, mew=0, clip_on=False, zorder=6)
lab(ax, p, 0.06, '均值 0.2', RED, ha='left')
lab(ax, 0, 1-p+.03, '0.8', ha='center'); lab(ax, 1, p+.03, '0.2', ha='center')
ax.set_xlim(-.45, 1.45); ax.set_ylim(0, 1); ax.set_xticks([0, 1]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel(r'$p_X(x)$', labelpad=1)
ax = axes[1]; style(ax)
pp = np.linspace(0, 1, 401)
ax.plot(pp, pp*(1-pp), color=BLUE, lw=1.4)
dot(ax, p, p*(1-p)); lab(ax, p+.04, p*(1-p)-.03, '0.16', RED)
ax.plot([.5, .5], [0, .25], color=LINE, lw=.85, ls=DASH)
dot(ax, .5, .25, color=BLUE); lab(ax, .53, .252, '1/4', BLUE)
ax.set_xlim(0, 1); ax.set_ylim(0, .29); ax.set_xticks([0, .2, .5, 1]); ax.set_yticks([0, .1, .2])
ax.set_xlabel('$p$', labelpad=1); ax.set_ylabel(r'$p(1-p)$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'p': p, 'mean': p, 'variance': p*(1-p), 'max_variance': .25})
