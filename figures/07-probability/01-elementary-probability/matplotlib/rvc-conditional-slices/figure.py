"""Triangle model: (a) strip x<=X<=x+h with x=0.6, h=0.05, conditional-mean line m(x)=x/2 (red);
(b) conditional densities Unif(0,x) for x=0.4 and 0.8 (heights 2.5, 1.25) with means x/2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

fig, (a, b) = figure(width_mm=104, height_mm=48, ncols=2)
a.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE, lw=1.1)
x0, h = 0.6, 0.05
a.fill([x0, x0+h, x0+h, x0], [0, 0, x0+h, x0], color=BLUE_FILL, lw=0)
a.plot([x0, x0+h, x0+h, x0, x0], [0, 0, x0+h, x0, 0], color=BLUE, lw=0.8)
t = np.linspace(0, 1, 50); a.plot(t, t/2, color=RED, lw=1.4)
a.text(0.70, 0.27, '$m(x)=x/2$', ha='left', fontsize=7.5, color=INK)
a.annotate('$x\\leq X\\leq x+h$', xy=(x0+h/2, 0.3), xytext=(0.12, 0.62), fontsize=7.5,
           arrowprops=dict(arrowstyle='->', color=STROKE, lw=0.7))
a.set_aspect('equal'); a.set_xlim(-0.03, 1.05); a.set_ylim(-0.03, 1.05); a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$y$', rotation=0)
for xv, c in ((0.4, BLUE), (0.8, YELLOW)):
    b.plot([0, 0, xv, xv, 1], [0, 1/xv, 1/xv, 0, 0], color=c, lw=1.5)
    b.scatter([xv/2], [0], s=20, color=RED, zorder=4, clip_on=False)
    b.text(xv + 0.02, 1/xv + 0.05, f'$x={xv}$', fontsize=7.5)
b.set_xlim(0, 1.02); b.set_ylim(0, 3.0); b.set_xticks([0, 0.2, 0.4, 0.8, 1]); b.set_xlabel('$y$', labelpad=1)
b.set_ylabel(r'$f_{Y\mid X}(y\mid x)$')
tag(a, '(a)', y=-0.26); tag(b, '(b)', y=-0.26)
save(fig, Path(__file__).resolve().parent, 'figure', {'x0': x0, 'h': h, 'cond': 'Unif(0,x)', 'mean': 'x/2'})
