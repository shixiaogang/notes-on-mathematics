from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：三个像函数的极点与收敛半平面：运行例、共振例、增长指数。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .075, .985, .97, .26, .3)
data = (([0, -1, -2], [0, 0, 0], 0, ['', '', '']), ([0, 0], [1, -1], 0, ['$\\times 2$', '$\\times 2$']), ([1], [0], 1, ['']))
for ax, (re, im, c, labs) in zip(axes, data):
    ax.axvspan(c, 2.6, color=BLUE_FILL, lw=0, zorder=0)
    ax.axvline(c, color=STROKE, lw=1.2, zorder=2)
    ax.axhline(0, color=MUTED, lw=.6, zorder=1)
    ax.plot(re, im, 'x', ms=5.5, mew=1.5, color=RED, zorder=5)
    for x, y, s in zip(re, im, labs):
        if s:
            ax.text(x-.15, y, s, ha='right', va='center', color=RED, fontsize=7.5)
    ax.set_xlim(-2.8, 2.6); ax.set_ylim(-2, 2); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); label(ax, '$\\mathrm{Re}\\,z$', '$\\mathrm{Im}\\,z$')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'poles 0,-1,-2', 'b': 'double poles +-i', 'c': 'pole 1'})
