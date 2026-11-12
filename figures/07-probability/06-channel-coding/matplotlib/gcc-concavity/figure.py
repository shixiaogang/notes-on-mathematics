from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Concavity of c(p) = 0.5 log2(1 + p) (sigma^2 = 1). A code that spends power 1 on half of the positions and 5 on
# the other half has average power 3; the per-position bounds average to (c(1) + c(5))/2 = 0.896 (green dot on the
# chord), below c(3) = 1 (red dot). Blue: c(p); yellow: chord between (1, c(1)) and (5, c(5)).
p = np.linspace(0, 7, 500)
fig, ax = figure(width_mm=80, height_mm=48)
panel(fig, left=.13, right=.97, top=.95, bottom=.2)
ax.plot(p, cap(p), color=BLUE, lw=1.4)
a, b = 1.0, 5.0; ca, cb_ = float(cap(a)), float(cap(b)); mid = (ca+cb_)/2
ax.plot([a, b], [ca, cb_], color=YELLOW, lw=1.5)
dot(ax, a, ca, color=YELLOW); dot(ax, b, cb_, color=YELLOW)
dot(ax, 3, mid, color=GREEN); dot(ax, 3, 1.0)
ax.plot([3, 3], [0, 1.0], color=STROKE, lw=.8, ls=DOT)
ax.set_xlim(0, 7); ax.set_ylim(0, 1.6); ax.set_xticks([0, 1, 3, 5, 7]); ax.set_yticks([0, .5, 1, 1.5])
ax.set_xlabel(r'$p$', labelpad=1); ax.set_ylabel('bit/次', labelpad=2)
lab(ax, 2.85, 1.04, r'$c(3)=1$', RED, va='bottom', ha='right')
lab(ax, 3.15, mid-.1, '%.3f' % mid, GREEN, va='top')
lab(ax, 5.7, 1.2, r'$c(p)$', BLUE)
save(fig, HERE, 'figure', {'c(1)': ca, 'c(5)': cb_, 'chord mid': mid, 'c(3)': 1.0})
