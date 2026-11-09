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

# 沿搜索方向的一维函数 phi，phi'(a)=-1-1.5a+a^3：起步处曲率为负。s^T y=a(phi'(a)-phi'(0))。
dp = lambda a: -1-1.5*a+a**3
p = lambda a: -a-.75*a*a+a**4/4
c1, c2 = .1, .5
aa = np.linspace(0, 2.0, 2000)
fig, (ax, bx) = figure(width_mm=112, height_mm=54, ncols=2)
ok_arm = p(aa) <= p(0)+c1*aa*dp(0)
ok_cur = dp(aa) >= c2*dp(0)
both = ok_arm & ok_cur
neg = dp(aa) < dp(0)
ax.plot(aa, p(aa), color=BLUE, lw=1.4)
ax.plot(aa, p(0)+c1*aa*dp(0), color=STROKE, lw=.85, ls=(0, (4, 2)))
ax.fill_between(aa, -2.7, -2.5, where=both, color=GREEN)
ax.set_xlim(0, 2); ax.set_ylim(-2.7, .4); ax.set_xlabel('$\\alpha$', labelpad=1); ax.set_ylabel('$\\phi(\\alpha)$', labelpad=1)
ax.text(1.97, -.1, 'Armijo线', color=MUTED, ha='right', fontsize=7.5)
bx.axhline(0, color=STROKE, lw=.6)
bx.plot(aa, dp(aa), color=BLUE, lw=1.4)
bx.axhline(dp(0), color=STROKE, lw=.85, ls=(0, (1.2, 1.4)))
bx.axhline(c2*dp(0), color=STROKE, lw=.85, ls=(0, (4, 2)))
y0 = -2.2
bx.fill_between(aa, y0, y0+.14, where=neg, color=RED)
bx.fill_between(aa, y0, y0+.14, where=both, color=GREEN)
bx.text(1.99, dp(0)-.32, "$\\phi'(0)$", color=INK, ha='right')
bx.text(.04, c2*dp(0)+.1, "$c_2\\phi'(0)$", color=INK, ha='left')
bx.text(.62, y0+.25, '曲率为负', color=INK, ha='center')
bx.text(1.72, y0+.25, 'Wolfe', color=INK, ha='center')
bx.set_xlim(0, 2); bx.set_ylim(-2.3, 3.2); bx.set_xlabel('$\\alpha$', labelpad=1); bx.set_ylabel("$\\phi'(\\alpha)$", labelpad=1)
panel(fig, .09, .985, .985, .25, .3); tags(fig, [ax, bx])
ia = aa[both]
save(fig, HERE, 'figure', {'dphi': '-1-1.5a+a^3', 'c1': c1, 'c2': c2, 'wolfe_interval': [float(ia.min()), float(ia.max())], 'neg_interval_end': float(aa[neg].max())})
