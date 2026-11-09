from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# H_min 中 q=4x(1-x) 与读数在 1/3,2/3,1 的折线插值 f+；(a) 函数与余项 q-f+；(b) 导数，f+' 是 q' 在每段的平均。
x = np.linspace(0, 1, 601); q = 4*x*(1-x)
n = np.array([0, 1/3, 2/3, 1]); y = 4*n*(1-n); fp = np.interp(x, n, y)
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.08, right=.985, top=.97, bottom=.245, wspace=.2)
a, b = axes
a.plot(x, q, color=BLUE, lw=1.4); a.plot(x, fp, color=GREEN, lw=1.4); a.plot(x, q-fp, color=RED, lw=1.4)
a.plot(n, y, 'o', color=GREEN, ms=3.6, zorder=3)
a.axhline(0, color=GRID, lw=.85, zorder=0)
a.text(.5, 1.03, '$q$', color=INK, ha='center'); a.text(.5, .76, '$f^+$', color=INK, ha='center', va='center'); a.text(.5, .205, '$q-f^+$', color=INK, ha='center', va='center')
a.set_xlim(0, 1); a.set_ylim(-.14, 1.16); a.set_xticks(n); a.set_xticklabels(['0', '1/3', '2/3', '1']); a.set_yticks([0, 8/9]); a.set_yticklabels(['0', '8/9']); a.set_xlabel('$x$', labelpad=1)
s = [8/3, 0, -8/3]
for i in range(3):
    b.plot([n[i], n[i+1]], [s[i], s[i]], color=GREEN, lw=1.5)
b.plot(x, 4-8*x, color=BLUE, lw=1.4)
for p in n[1:-1]: b.axvline(p, color=MUTED, lw=.85, ls=(0, (2, 1.5)))
b.axhline(0, color=GRID, lw=.85, zorder=0)
b.text(.135, 3.45, "$q'$", color=INK, va='center'); b.text(.03, 2.05, "$(f^+)'$", color=INK, va='center')
b.set_xlim(0, 1); b.set_ylim(-4.4, 4.4); b.set_xticks(n); b.set_xticklabels(['0', '1/3', '2/3', '1']); b.set_yticks([-8/3, 0, 8/3]); b.set_yticklabels(['-8/3', '0', '8/3']); b.set_xlabel('$x$', labelpad=1)
fig.canvas.draw()
for ax, t in zip(axes, '(a) (b)'.split()):
    r = ax.get_position(); fig.text((r.x0+r.x1)/2, .015, t, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'q=4x(1-x); f+ piecewise linear interpolant at 0,1/3,2/3,1; slopes 8/3,0,-8/3'})
