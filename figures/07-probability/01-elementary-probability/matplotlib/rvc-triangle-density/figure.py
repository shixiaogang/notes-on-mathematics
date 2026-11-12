"""Uniform density 2 on the triangle 0<=y<=x<=1: event {X+Y<=1} (prob 1/2) and the two marginals
f_X(x)=2x, f_Y(y)=2(1-y). Analytic curves, no data."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE='#4C4D4F'
fig, (a, b) = figure(width_mm=104, height_mm=50, ncols=2)
# (a)
a.fill([0, 1, 0.5], [0, 0, 0.5], color=BLUE_FILL, lw=0)
a.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE, lw=1.4)
a.plot([0, 1], [1, 0], color=STROKE, lw=0.85, ls='--')
a.text(0.62, 0.12, r'$X+Y\leq 1$', ha='center', fontsize=7.5)
a.text(0.80, 0.52, r'$f=2$', ha='center', color=INK)
a.text(0.16, 0.86, r'$x+y=1$', color=MUTED, fontsize=7.5)
a.set_xlim(-0.03, 1.08); a.set_ylim(-0.03, 1.08); a.set_aspect('equal')
a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$x$'); a.set_ylabel('$y$', rotation=0)
# (b)
t = np.linspace(0, 1, 200)
b.plot(t, 2*t, color=BLUE, lw=1.4)
b.plot(t, 2*(1-t), color=YELLOW, lw=1.6)
b.text(0.97, 2.22, r'$f_X(t)=2t$', ha='right', color=INK)
b.text(0.03, 2.22, r'$f_Y(t)=2(1-t)$', ha='left', color=INK)
b.set_xlim(0, 1); b.set_ylim(0, 2.45); b.set_xticks([0, 0.5, 1]); b.set_yticks([0, 1, 2])
b.set_xlabel('$t$')
for ax, s in ((a, '(a)'), (b, '(b)')):
    ax.text(0.5, -0.36, s, transform=ax.transAxes, ha='center', va='top')
save(fig, Path(__file__).resolve().parent, 'figure', {'density': '2 on 0<=y<=x<=1', 'P(X+Y<=1)': 0.5, 'f_X': '2x', 'f_Y': '2(1-y)'})
