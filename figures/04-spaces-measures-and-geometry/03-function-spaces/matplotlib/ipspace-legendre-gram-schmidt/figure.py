from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Monomials vs. normalized Legendre e_k = sqrt((2k+1)/2) P_k.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.26, wspace=.2)
x = np.linspace(-1, 1, 801)
cols = [BLUE, GREEN, YELLOW, RED]
ax = axes[0]
for i, c in enumerate(cols): ax.plot(x, x**i, color=c, lw=1.4)
ax.axhline(0, color=MUTED, lw=.85)
ax.text(-.95, 1.08, '$1$'); ax.text(.62, .75, '$x$'); ax.text(-.72, .36, '$x^2$', ha='right'); ax.text(.72, .2, '$x^3$')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.2, 1.3); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
E = [np.full_like(x, 1/np.sqrt(2)), np.sqrt(3/2)*x, np.sqrt(5/8)*(3*x**2-1), np.sqrt(7/8)*(5*x**3-3*x)]
for e, c in zip(E, cols): ax.plot(x, e, color=c, lw=1.4)
ax.axhline(0, color=MUTED, lw=.85)
ax.text(-.32, .78, '$e_0$'); ax.text(-.52, -1.02, '$e_1$'); ax.text(.2, -.98, '$e_2$'); ax.text(.82, -.6, '$e_3$', ha='right')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-2, 2.1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-2, -1, 0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'e0=1/sqrt2, e1=sqrt(3/2)x, e2=sqrt(5/8)(3x^2-1), e3=sqrt(7/8)(5x^3-3x)'})
