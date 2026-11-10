from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：两段常系数切换的先后顺序影响结果；对单位正方形比较三种矩阵的像。
A1 = np.array([[0., 1], [0, 0]]); A2 = np.array([[0., 0], [1, 0]])
Ms = (expm(A2)@expm(A1), expm(A1)@expm(A2), expm(A1+A2))
print([m.round(4).tolist() for m in Ms])
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .06, .985, .97, .23, .22)
sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]], float)
for ax, M in zip(axes, Ms):
    ax.fill(sq[0], sq[1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=2)
    p = M@sq
    ax.plot(p[0], p[1], color=GREEN if ax is axes[2] and 0 else BLUE, lw=MAIN, zorder=3)
    q = M@np.array([1., 1])
    ax.plot(*q, 'o', ms=3.8, color=RED, mew=0, zorder=5)
    ax.text(q[0]-.1, q[1]+.13, f'({q[0]:.2f}, {q[1]:.2f})', ha='right' if q[0] > 2 else 'center', fontsize=7.5)
    ax.set_aspect('equal'); ax.set_xlim(-.2, 3.4); ax.set_ylim(-.2, 3.6); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2, 3]); label(ax, '$x_1$', '$x_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'A1': A1.tolist(), 'A2': A2.tolist(), 'matrices': [m.tolist() for m in Ms]})
