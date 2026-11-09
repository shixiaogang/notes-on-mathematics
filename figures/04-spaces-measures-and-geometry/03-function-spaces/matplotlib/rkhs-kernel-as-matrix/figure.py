from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# 最小值核 K(t,x)=min(t,x)：三点网格上是 3x3 矩阵，网格加密后成为二元函数，第 x 行就是核截面 K_x。
cmap = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE])
fig, axes = figure(width_mm=112, height_mm=52, ncols=3, width_ratios=[1, 1, 1.15])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.97, bottom=.26, wspace=.42)
a, b, c = axes
pts = [1/3, 2/3, 1]; lab = ['1/3', '2/3', '1']
K3 = np.array([[min(p, q) for q in pts] for p in pts])
names = [['1/3', '1/3', '1/3'], ['1/3', '2/3', '2/3'], ['1/3', '2/3', '1']]
a.set_xlim(-.05, 3.05); a.set_ylim(3.05, -.05); a.set_aspect('equal'); 
for i in range(3):
    for j in range(3):
        a.add_patch(Rectangle((j, i), 1, 1, fc=cmap(K3[i, j]), ec='white', lw=.8))
        a.text(j+.5, i+.5, names[i][j], ha='center', va='center', fontsize=7.5, color=INK)
a.add_patch(Rectangle((0, 1), 3, 1, fc='none', ec=GREEN, lw=1.4))
a.set_xticks([.5, 1.5, 2.5]); a.set_xticklabels(lab); a.set_yticks([.5, 1.5, 2.5]); a.set_yticklabels(lab)
a.tick_params(length=0, pad=2); a.spines[['left', 'bottom']].set_visible(False)
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$x$', labelpad=7, rotation=0, va='center')
t = np.linspace(0, 1, 301); M = np.minimum.outer(t, t)
b.imshow(M, extent=(0, 1, 1, 0), cmap=cmap, vmin=0, vmax=1, interpolation='bilinear', aspect='equal')
b.axhline(2/3, color=GREEN, lw=1.4)
b.set_xticks([0, 1/3, 2/3, 1]); b.set_xticklabels(['0', '1/3', '2/3', '1']); b.set_yticks([0, 1/3, 2/3, 1]); b.set_yticklabels(['0', '1/3', '2/3', '1'])
b.tick_params(length=2, pad=2); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=5, rotation=0, va='center')
c.plot(t, np.minimum(t, 2/3), color=GREEN, lw=1.5)
c.plot(pts, [1/3, 2/3, 2/3], 'o', color=GREEN, ms=3.6, zorder=3)
c.set_xlim(0, 1.04); c.set_ylim(0, .86); c.set_xticks([0, 1/3, 2/3, 1]); c.set_xticklabels(['0', '1/3', '2/3', '1']); c.set_yticks([0, 1/3, 2/3]); c.set_yticklabels(['0', '1/3', '2/3'])
c.plot([2/3, 2/3], [0, 2/3], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
c.text(.33, .55, '$K_{2/3}(t)$', color=INK, ha='center')
c.set_xlabel('$t$', labelpad=1)
fig.canvas.draw()
for ax, s in zip(axes, '(a) (b) (c)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'K(t,x)=min(t,x); (a) grid 1/3,2/3,1; (b) continuous; (c) row x=2/3'})
