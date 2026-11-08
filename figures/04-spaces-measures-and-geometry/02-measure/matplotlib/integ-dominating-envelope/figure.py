from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Rectangle

def labels(fig, axes, y=.03):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

# (a) f_n=x^n under g=1. (b) spikes, envelope h=sup f_n, lower bound 1/x-1.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.2, wspace=.16)
a, b = axes
x = np.linspace(0, 1, 500)
for n in (1, 2, 4, 8):
    a.plot(x, x**n, color=GREEN, lw=1.2)
    t = .985 if n == 1 else .9
a.text(.42, .28, '$x$', color=INK); a.text(.72, .13, '$x^8$', color=INK)
a.plot([0, 1], [1, 1], color=BLUE, lw=1.4); a.text(.03, 1.05, '$g=1$', color=INK)
a.set_xlim(0, 1.04); a.set_ylim(0, 1.22); a.set_xticks([0, 1]); a.set_yticks([0, 1])
for n in range(1, 6):
    b.add_patch(Rectangle((0, 0), 1/n, n, fc='none', ec=MUTED, lw=.75))
X = [1.0]; Y = [1.0]
for n in range(1, 40):
    l = 1/(n+1); r = 1/n
    X += [l]; Y += [n]
    X += [l]; Y += [n+1]
b.plot(X, Y, color=BLUE, lw=1.4)
u = np.linspace(.12, 1, 400)
b.plot(u, 1/u-1, color=RED, lw=1.2, dashes=(4, 2))
b.text(.27, 4.1, '$h$', color=INK); b.annotate('$1/x-1$', xy=(.72, .39), xytext=(.68, 1.65), color=INK, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.65, shrinkA=1, shrinkB=1), ha='center')
b.set_xlim(0, 1.04); b.set_ylim(0, 6.2); b.set_xticks([0, 1/5, 1/3, 1/2, 1]); b.set_xticklabels(['0', '1/5', '1/3', '1/2', '1']); b.set_yticks([0, 2, 4, 6])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^n, n=1,2,4,8; n 1_(0,1/n), n<=5; h=n on [1/(n+1),1/n); 1/x-1'})
