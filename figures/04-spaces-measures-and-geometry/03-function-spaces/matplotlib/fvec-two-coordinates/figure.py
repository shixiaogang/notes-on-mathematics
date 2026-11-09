from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# p(x)=2-x+3x^2 在基 1,x,x^2 与基 1,x-1,(x-1)^2 下的分解。
fig, axes = figure(width_mm=112, height_mm=56, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.975, top=.97, bottom=.2, wspace=.16)
x = np.linspace(0, 2, 300); p = 2-x+3*x**2
a, b = axes
for ax in axes:
    ax.plot(x, p, color=BLUE, lw=1.6)
    ax.axhline(0, color=GRID, lw=.85, zorder=0)
    ax.set_xlim(0, 2.42); ax.set_ylim(-5.6, 13.2); ax.set_xticks([0, 1, 2]); ax.set_yticks([-4, 0, 4, 8, 12])
a.plot(x, 2+0*x, color=GREEN, lw=1.1); a.plot(x, -x, color=YELLOW, lw=1.1); a.plot(x, 3*x**2, color=RED, lw=1.1)
a.text(2.05, 2, '$2$', va='center'); a.text(2.05, -2, '$-x$', va='center'); a.text(1.5, 4.6, '$3x^2$', va='center', ha='left'); a.text(1.3, 8.2, '$p$', va='center', ha='right')
b.plot(x, 4+0*x, color=GREEN, lw=1.1); b.plot(x, 5*(x-1), color=YELLOW, lw=1.1); b.plot(x, 3*(x-1)**2, color=RED, lw=1.1)
b.text(2.05, 4, '$4$', va='center'); b.text(2.05, 5.6, '$5(x-1)$', va='center'); b.text(2.05, 2.75, '$3(x-1)^2$', va='center'); b.text(1.3, 8.2, '$p$', va='center', ha='right')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'p=2-x+3x^2=4+5(x-1)+3(x-1)^2 on [0,2]'})
