from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# 点组 -1,-.5,0,.5,1 上：高斯核 sigma=.5 与仿射核 1+xz 的 Gram 矩阵及特征值（由 numpy 计算）。
cmap = LinearSegmentedColormap.from_list('b', ['#FFFFFF', BLUE_FILL, BLUE])
pts = np.array([-1, -.5, 0, .5, 1.]); s = .5
G = np.exp(-(pts[:, None]-pts[None])**2/(2*s*s)); A = 1+np.outer(pts, pts)
eg = np.linalg.eigvalsh(G)[::-1]; ea = np.clip(np.linalg.eigvalsh(A)[::-1], 0, None)
fig, axes = figure(width_mm=112, height_mm=54, ncols=3, width_ratios=[1, 1, .9])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.02, right=.985, top=.97, bottom=.2, wspace=.14)
for ax, M in zip(axes[:2], (G, A)):
    ax.set_xlim(-.02, 5.02); ax.set_ylim(5.02, -.02); ax.set_aspect('equal'); ax.axis('off')
    for i in range(5):
        for j in range(5):
            ax.add_patch(Rectangle((j, i), 1, 1, fc=cmap(M[i, j]/2), ec='white', lw=.7))
            ax.text(j+.5, i+.5, f'{M[i,j]:.2f}', ha='center', va='center', fontsize=7, color=INK)
c = axes[2]
k = np.arange(1, 6)
c.plot(k, eg, 'o-', color=BLUE, ms=3.5, lw=1.2)
c.plot(k, ea, 's-', color=GREEN, ms=3.5, lw=1.2)
c.set_xticks(k); c.set_yticks([0, 2, 4]); c.set_xlim(.6, 5.4); c.set_ylim(-.25, 5.5); c.set_xlabel('$k$', labelpad=0)
c.text(1.35, 4.9, '仿射', color=GREEN, va='center', fontsize=7.5); c.text(2.45, 2.2, '高斯', color=BLUE, va='center', fontsize=7.5)
c.set_ylabel(r'$\lambda_k$', labelpad=1, rotation=0, va='center')
q = c.get_position(); c.set_position([q.x0+.05, q.y0+.05, q.width-.05, q.height-.05])
fig.canvas.draw()
for ax, s_ in zip(axes, '(a) (b) (c)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s_, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'Gaussian exp(-(x-z)^2/(2*.25)), affine 1+xz, x in -1,-.5,0,.5,1', 'eig_gauss': eg.round(3).tolist(), 'eig_affine': ea.round(3).tolist()})
