from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f=1_[0,1/2) periodic, h=1/8; ||Delta_h f||_2=(2h)^{1/2}; g=sin(2 pi x), ||Delta_h g||_2=sqrt2 sin(pi h).
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.27, wspace=.27)
ax = axes[0]; h = 1/8
ax.fill_between([.5-h, .5], 0, 1, color=RED_FILL, lw=0)
ax.fill_between([1-h, 1], 0, 1, color=RED_FILL, lw=0)
ax.plot([0, .5], [1, 1], color=BLUE, lw=1.4); ax.plot([.5, 1], [0, 0], color=BLUE, lw=1.4)
ax.plot([0, .5-h], [.965, .965], color=GREEN, lw=1.4, ls=(0, (3, 2))); ax.plot([.5-h, 1-h], [.035, .035], color=GREEN, lw=1.4, ls=(0, (3, 2))); ax.plot([1-h, 1], [.965, .965], color=GREEN, lw=1.4, ls=(0, (3, 2)))
ax.text(.13, 1.07, '$f$', color=BLUE, ha='center', va='bottom')
ax.text(.68, .1, r'$f(\cdot+h)$', color=GREEN, ha='center', va='bottom')
ax.annotate('', xy=(.5, .55), xytext=(.5-h, .55), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.85, shrinkA=0, shrinkB=0))
ax.text(.5-h/2, .6, '$h$', ha='center', va='bottom', color=MUTED)
ax.set_xlim(0, 1); ax.set_ylim(-.08, 1.3); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]; hs = np.logspace(np.log10(1/512), np.log10(.5), 200)
ax.loglog(hs, (2*hs)**.5, color=BLUE, lw=1.4); ax.loglog(hs, np.sqrt(2)*np.sin(np.pi*hs), color=GREEN, lw=1.4)
ax.set_xlim(1/512, .5); ax.set_ylim(.005, 2.2)
ax.set_xticks([1/512, 1/128, 1/32, 1/8, 1/2]); ax.set_xticklabels(['$2^{-9}$', '$2^{-7}$', '$2^{-5}$', '$2^{-3}$', '$2^{-1}$']); ax.minorticks_off()
ax.set_yticks([.01, .1, 1]); ax.set_yticklabels(['0.01', '0.1', '1'])
ax.set_xlabel('$h$', labelpad=0)
ax.text(1/95, .23, r"$(2h)^{1/2}$", color=BLUE, ha='center', va='bottom')
ax.text(1/18, .052, r"$\sqrt{2}\,\sin\pi h$", color=GREEN, ha='center', va='top')
for a, s in zip(axes, '(a) (b)'.split()):
    q = a.get_position(); fig.text((q.x0+q.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'step (2h)^(1/2), sine sqrt2*sin(pi h), h=1/8 in panel a'})
