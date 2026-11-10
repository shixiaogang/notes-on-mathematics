from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：dx/dt=-x/t+1 的解 x=c/t+t/2 在系数连续的区间 (0,inf) 上存在，t->0+ 时一般无界。
fig, ax = figure(width_mm=84, height_mm=52)
panel(fig, .095, .975, .96, .15)
t = np.linspace(.02, 4, 800)
for c in (-1, -.5, .5, 1):
    x = c/t+t/2
    x = np.where(np.abs(x) > 8, np.nan, x)
    ax.plot(t, x, color=BLUE, lw=MAIN)
    ax.plot([1], [c+.5], 'o', ms=3.8, color=RED, mew=0, zorder=5)
ax.plot(t, t/2, color=YELLOW, lw=1.7)
ax.plot([1], [.5], 'o', ms=3.8, color=RED, mew=0, zorder=5)
ax.axvline(0, color=STROKE, lw=1.6)
ax.set_xlim(-.02, 4); ax.set_ylim(-6, 6.5); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([-5, 0, 5]); label(ax, '$t$', '$x$')
save(fig, HERE, 'figure', {'formula': 'x=c/t+t/2', 'c': [-1, -.5, 0, .5, 1], 'initial time': 1})
