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

# Cantor function approximations c_n, computed from the retained-interval recursion.
fig, axes = figure(width_mm=108, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.17, wspace=.2)
def keep(n):
    I = [(0., 1.)]
    for _ in range(n):
        I = [v for l, r in I for v in ((l, l+(r-l)/3), (r-(r-l)/3, r))]
    return I
def nodes(n):
    xs = [0.]; ys = [0.]; v = 0.
    for l, r in keep(n):
        if l > xs[-1]:
            xs.append(l); ys.append(v)
        v += 2.**(-n); xs.append(r); ys.append(v)
    return np.array(xs), np.array(ys)
a, b = axes
a.plot(*nodes(1), color=YELLOW, lw=1.2, dashes=(4, 2), label='$c_1$')
a.plot(*nodes(2), color=GREEN, lw=1.2, label='$c_2$')
a.plot(*nodes(6), color=BLUE, lw=1.4, label='$c_6$')
a.legend(loc='upper left', handlelength=2.2, borderaxespad=.1, labelspacing=.25)
b.plot(*nodes(2), color=GREEN, lw=1.2)
for i, (l, r) in enumerate(keep(2)):
    b.plot([l, r], [0, 0], color=RED, lw=3, solid_capstyle='butt', clip_on=False)
    b.plot([0, 0], [i/4+.006, (i+1)/4-.006], color=RED, lw=3, solid_capstyle='butt', clip_on=False)
    for p, v in ((l, i/4), (r, (i+1)/4)):
        b.plot([p, p], [0, v], color=MUTED, lw=.65, dashes=(2.5, 2))
b.set_xticks([0, 1/9, 2/9, 1/3, 2/3, 7/9, 8/9, 1]); b.set_xticklabels(['0', '', '', '1/3', '2/3', '', '', '1'])
b.set_yticks([0, .25, .5, .75, 1]); b.set_yticklabels(['0', '1/4', '1/2', '3/4', '1'])
a.set_xticks([0, 1/3, 2/3, 1]); a.set_xticklabels(['0', '1/3', '2/3', '1']); a.set_yticks([0, .5, 1]); a.set_yticklabels(['0', '1/2', '1'])
for ax in axes:
    ax.set_xlim(0, 1.03); ax.set_ylim(0, 1.05)
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'c_n piecewise linear: rises 2^-n linearly on each of the 2^n retained intervals of step n'})
