from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f(x)=x^2, g(x)=1-x, f+g=x^2-x+1 的逐分量与逐点相加。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.95, bottom=.235, wspace=.2)
f = lambda t: t**2; g = lambda t: 1-t; h = lambda t: f(t)+g(t)
a = axes[0]
xs = np.array([0, 1/3, 2/3, 1])
for off, fn, col in ((-.035, f, BLUE), (0, g, GREEN), (.035, h, YELLOW)):
    a.vlines(xs+off, 0, fn(xs), color=col, lw=1.2); a.plot(xs+off, fn(xs), 'o', ms=3.4, color=col, mew=0)
a.set_xlim(-.1, 1.1); a.set_ylim(0, 1.2); a.set_xticks(xs); a.set_xticklabels(['0', '1/3', '2/3', '1']); a.set_yticks([0, .5, 1])
b = axes[1]
x = np.linspace(0, 1, 300)
b.plot(x, f(x), color=BLUE, lw=1.4); b.plot(x, g(x), color=GREEN, lw=1.4); b.plot(x, h(x), color=YELLOW, lw=1.4)
x0 = .5
b.vlines(x0, 0, f(x0), color=BLUE, lw=2.4); b.vlines(x0, f(x0), f(x0)+g(x0), color=GREEN, lw=2.4)
b.plot([x0], [h(x0)], 'o', ms=3.6, color=YELLOW, mew=0)
b.text(.9, f(.9)-.13, '$f$', color=INK, ha='left'); b.text(.08, g(.08)-.17, '$g$', color=INK, ha='left'); b.text(.1, h(.1)+.06, '$f+g$', color=INK, ha='left')
b.set_xlim(0, 1.03); b.set_ylim(0, 1.2); b.set_xticks([0, x0, 1]); b.set_xticklabels(['0', '$x$', '1']); b.set_yticks([0, .5, 1])
for ax, s in zip(axes, '(a) (b)'.split()):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=x^2, g=1-x, f+g=x^2-x+1 on [0,1]; samples at 0,1/3,2/3,1'})
