from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# 贯穿例子 k(x,y)=1+xy，[-1,1] 上概率测度 dy/2。四个中点 x_i 处的矩阵元素、输入 f=1+x 与输出。
pts = np.array([-.75, -.25, .25, .75])
K = 1 + np.outer(pts, pts); f = 1 + pts; out = K @ f / 4
cmap = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE])
col = lambda v: cmap(np.clip(v/2.0, 0, 1))
fig, (a0, a1) = figure(width_mm=112, height_mm=46, ncols=2, width_ratios=[2.05, 1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.02, right=.965, top=.99, bottom=.21, wspace=.12)
a0.set_xlim(-1.05, 9.2); a0.set_ylim(4.45, -.75); a0.axis('off')
for i in range(4):
    for j in range(4):
        a0.add_patch(Rectangle((j, i), 1, 1, fc=col(K[i, j]), ec='white', lw=.8))
        a0.text(j+.5, i+.5, f'{K[i,j]:.2f}', ha='center', va='center', fontsize=7.5)
a0.add_patch(Rectangle((0, 0), 4, 1, fc='none', ec=RED, lw=1.1))
for j, p in enumerate(pts):
    a0.text(j+.5, -.28, f'{p:g}', ha='center', va='center', color=MUTED, fontsize=7.5)
a0.text(-.55, -.28, '$x_i\\backslash y_j$', ha='center', va='center', color=MUTED, fontsize=7.5)
for i, p in enumerate(pts):
    a0.text(-.55, i+.5, f'{p:g}', ha='center', va='center', color=MUTED, fontsize=7.5)
for i in range(4):
    a0.add_patch(Rectangle((4.75, i), 1, 1, fc=GREEN_FILL, ec='white', lw=.8))
    a0.text(5.25, i+.5, f'{f[i]:.2f}', ha='center', va='center', fontsize=7.5)
    a0.add_patch(Rectangle((7.3, i), 1.45, 1, fc=YELLOW_FILL, ec='white', lw=.8))
    a0.text(8.02, i+.5, f'{out[i]:.3f}', ha='center', va='center', fontsize=7.5)
a0.add_patch(Rectangle((7.3, 0), 1.45, 1, fc='none', ec=RED, lw=1.1))
a0.text(4.37, 2, r'$\times$', ha='center', va='center')
a0.text(6.5, 2, r'$\times\,\frac{1}{4}=$', ha='center', va='center')
a0.text(5.25, -.28, r'$f_j$', ha='center', va='center', color=MUTED, fontsize=7.5)
a0.text(8.02, -.28, r'$(Tf)_i$', ha='center', va='center', color=MUTED, fontsize=7.5)
xs = np.linspace(-1, 1, 201); kk = 1 + np.outer(xs, xs)
a1.imshow(kk, extent=(-1, 1, 1, -1), cmap=cmap, vmin=0, vmax=2, interpolation='bilinear', aspect='equal')
a1.axhline(-.75, color=RED, lw=1.1)
a1.set_xticks([-1, 0, 1]); a1.set_yticks([-1, 0, 1]); a1.tick_params(length=2, pad=1.5)
a1.set_xlabel('$y$', labelpad=-1); a1.set_ylabel('$x$', labelpad=3, rotation=0)
for ax, s in zip((a0, a1), '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'K_ij=1+x_i x_j at midpoints -3/4,-1/4,1/4,3/4; f=1+x; (Tf)_i=(1/4) sum K_ij f_j; (b) k(x,y)=1+xy'})
