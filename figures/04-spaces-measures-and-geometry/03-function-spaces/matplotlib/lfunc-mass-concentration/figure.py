from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f_n = n 1_(0,1/n)：读数 1 恒为 1，1_(1/4,1) 给 (1-n/4)^+，1-t 给 1-1/(2n)。
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.975, top=.97, bottom=.235, wspace=.18)
a = axes[0]
for n in (2, 4, 8):
    a.plot([0, 1/n, 1/n, 1], [n, n, 0, 0], color=BLUE, lw=1.4, solid_joinstyle='miter')
    a.text(1/n+.02, n-.15, f'$f_{{{n}}}$', ha='left', va='center')
a.set_xlim(0, 1.03); a.set_ylim(0, 9); a.set_xticks([0, 1/8, 1/4, 1/2, 1]); a.set_xticklabels(['0', '1/8', '1/4', '1/2', '1']); a.set_yticks([0, 2, 4, 8])
b = axes[1]
ns = np.arange(1, 17)
b.plot(ns, np.ones_like(ns), '-o', color=BLUE, lw=1.2, ms=3.2, mew=0)
b.plot(ns, 1-1/(2*ns), '-o', color=GREEN, lw=1.2, ms=3.2, mew=0)
b.plot(ns, np.maximum(1-ns/4, 0), '-o', color=YELLOW, lw=1.2, ms=3.2, mew=0)
b.set_xlim(0, 17); b.set_ylim(-.05, 1.3); b.set_xticks([1, 4, 8, 16]); b.set_yticks([0, .5, 1])
b.text(9.5, 1.06, '$g=1$', ha='center', va='bottom')
b.text(11.5, .8, '$g=1-t$', ha='center', va='center')
b.text(9.5, .09, r'$g=\mathbf{1}_{(1/4,1)}$', ha='center', va='bottom')
b.text(1.0, .08, '$n$', transform=b.transAxes, ha='right', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f_n=n 1_(0,1/n); readings 1, 1-1/(2n), (1-n/4)^+'})
