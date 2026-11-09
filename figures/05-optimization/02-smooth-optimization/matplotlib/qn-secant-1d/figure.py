from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# 一维目标 f(x)=x^4/4+x^2/2，g(x)=x^3+x。两点 0.5、1 的割线斜率是区间上的平均曲率。
g = lambda x: x**3+x
a, b = .5, 1.
sl = (g(b)-g(a))/(b-a)
fig, ax = figure(width_mm=84, height_mm=56)
xx = np.linspace(-.05, 1.2, 300)
ax.axhline(0, color=STROKE, lw=.85)
ax.plot(xx, g(xx), color=BLUE, lw=1.4)
ax.plot(xx, g(a)+sl*(xx-a), color=GREEN, lw=1.4)
t = np.linspace(.3, .75, 2)
ax.plot(t, g(a)+(3*a*a+1)*(t-a), color=YELLOW, lw=1.2, ls=(0, (4, 2)))
t = np.linspace(.8, 1.15, 2)
ax.plot(t, g(b)+(3*b*b+1)*(t-b), color=YELLOW, lw=1.2, ls=(0, (4, 2)))
ax.plot([a, b], [g(a), g(b)], 'o', ms=3.4, color=GREEN, mew=0, zorder=5)
xs = a-g(a)/sl
ax.plot([xs], [0], 'o', ms=3.4, color=GREEN, mew=0, zorder=5)
ax.plot([0], [0], 'o', ms=3.4, color=RED, mew=0, zorder=5)
ax.text(1.03, 2.72, "$g(x)$", color=INK, ha='right')
ax.text(.59, 1.42, '割线', color=INK, ha='right')
ax.text(1.1, 2.1, '切线', color=MUTED, ha='left', fontsize=7.5)
ax.text(.74, .86, '切线', color=MUTED, ha='left', fontsize=7.5)
ax.text(a+.01, g(a)-.3, '$x^{(1)}$', color=INK)
ax.text(b+.02, g(b)-.28, '$x^{(0)}$', color=INK)
ax.text(xs, -.38, '$x^{(2)}$', color=INK, ha='center')
ax.text(0, -.38, '$x^*$', color=INK, ha='center')
ax.set_xlim(-.08, 1.22); ax.set_ylim(-.6, 3.0)
ax.set_xlabel('$x$', labelpad=1); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2, 3])
save(fig, HERE, 'figure', {'f': 'x^4/4+x^2/2', 'secant_slope': sl, 'x2': xs, 'tangent_slopes': [3*a*a+1, 3*b*b+1]})
