"""Conditional densities f(y|x) at x=0.3,0.6,0.9. (a) independent density 4xy: always 2y.
(b) uniform density 2 on 0<=y<=x<=1: Unif(0,x), height 1/x."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
y = np.linspace(0, 1, 300)
cols = (BLUE, YELLOW, PURPLE); xs = (0.3, 0.6, 0.9); lss = ('-', '--', ':'); lws = (2.6, 1.6, 1.3)
for x, c, ls, lw in zip(xs, cols, lss, lws):
    a.plot(y, 2*y, color=c, ls=ls, lw=lw, label=f'$x={x}$')
    b.plot([0, 0, x, x, 1], [0, 1/x, 1/x, 0, 0], color=c, lw=1.4, ls=ls if ls != ':' else '-')
    b.text(x, 1/x + 0.12, f'$x={x}$', ha='right', fontsize=7.5, color=INK)
a.legend(loc='upper left', handlelength=2.2)
for ax in (a, b):
    ax.set_xlim(0, 1.02); ax.set_xlabel('$y$'); ax.set_xticks([0, 0.5, 1])
a.set_ylim(0, 2.3); b.set_ylim(0, 3.9)
a.set_ylabel(r'$f_{Y\mid X}(y\mid x)$')
tag(a, '(a)'); tag(b, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'a': 'f=4xy -> f(y|x)=2y', 'b': 'triangle -> 1/x on (0,x)', 'x': [0.3, 0.6, 0.9]})
