from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# T(x)=-ln x on (0,1]; equal-mass cells (k/5,(k+1)/5] of mu=lambda|(0,1) go to intervals; bar height = mass/length; q(y)=exp(-y).
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.96, bottom=.25, wspace=.2)
a, b = axes
x = np.linspace(.012, 1, 500)
a.plot(x, -np.log(x), color=BLUE, lw=1.4)
edges = np.array([.2, .4, .6, .8, 1.0])
for xe in edges[:-1]:
    ye = -np.log(xe)
    a.plot([xe, xe], [0, ye], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
    a.plot([0, xe], [ye, ye], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
a.set_xlim(0, 1.04); a.set_ylim(0, 3.6)
a.set_xticks([0, .2, .4, .6, .8, 1]); a.set_xticklabels(['0', '0.2', '0.4', '0.6', '0.8', '1'])
ys = -np.log(edges[:-1])
a.set_yticks(list(ys)); a.set_yticklabels([f'{v:.2f}' for v in ys])
a.set_xlabel('$x$', labelpad=1); a.text(.1, 3.15, '$y=-\\ln x$', color=INK)
lows = -np.log(edges[1:]); highs = -np.log(edges[:-1])
for lo, hi in zip(lows, highs):
    b.bar((lo+hi)/2, .2/(hi-lo), width=hi-lo, color=GREEN_FILL, edgecolor=GREEN, lw=.85)
t = np.linspace(0, 3.6, 300)
b.plot(t, np.exp(-t), color=GREEN, lw=1.4)
b.set_xlim(0, 3.7); b.set_ylim(0, 1.08); b.set_xlabel('$y$', labelpad=1)
b.set_xticks([0, 1, 2, 3]); b.set_yticks([0, .5, 1]); b.set_yticklabels(['0', '0.5', '1'])
b.text(1.65, .34, '$q(y)=\\mathrm{e}^{-y}$', color=INK)
for ax, s in zip(axes, ('(a)', '(b)')):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'y=-ln x; cells (k/5,(k+1)/5], k=1..4; bar height 0.2/length; q=exp(-y)'})
