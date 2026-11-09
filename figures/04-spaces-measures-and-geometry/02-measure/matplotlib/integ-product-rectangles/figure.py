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

# (a) A x B, A=[.4,1.4]U[2,2.8], B=[.5,1.5]. (b) cells of side .5 and .25 inside the quarter disc r=2.
fig, axes = figure(width_mm=100, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.19, wspace=.16)
a, b = axes
A = [(.4, 1.4), (2.0, 2.8)]; B = (.5, 1.5)
for l, r in A:
    a.add_patch(Rectangle((l, B[0]), r-l, B[1]-B[0], fc=BLUE_FILL, ec=BLUE, lw=.95))
    a.plot([l, r], [0, 0], color=GREEN, lw=3, solid_capstyle='butt', clip_on=False)
a.plot([0, 0], B, color=GREEN, lw=3, solid_capstyle='butt', clip_on=False)
a.text(.9, 1.02, '$A\\times B$', ha='center', va='center', color=INK)
a.text(.9, .14, '$A$', ha='center', color=INK); a.text(2.4, .14, '$A$', ha='center', color=INK); a.text(.14, 1, '$B$', ha='left', va='center', color=INK)
a.set_xlim(0, 3.1); a.set_ylim(0, 2.1); a.set_xticks([0, 1, 2, 3]); a.set_yticks([0, 1, 2])
inside = lambda x, y, s: (x+s)**2+(y+s)**2 <= 4
big = set()
for i in range(4):
    for j in range(4):
        if inside(i*.5, j*.5, .5):
            big.add((i, j)); b.add_patch(Rectangle((i*.5, j*.5), .5, .5, fc=BLUE_FILL, ec=BLUE, lw=.75))
for i in range(8):
    for j in range(8):
        if (i//2, j//2) not in big and inside(i*.25, j*.25, .25):
            b.add_patch(Rectangle((i*.25, j*.25), .25, .25, fc=GREEN_FILL, ec=GREEN, lw=.65))
t = np.linspace(0, np.pi/2, 200); b.plot(2*np.cos(t), 2*np.sin(t), color=INK, lw=1.3)
b.set_xlim(0, 2.2); b.set_ylim(0, 2.2); b.set_xticks([0, 1, 2]); b.set_yticks([0, 1, 2]); b.set_aspect('equal')
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A=[.4,1.4]U[2,2.8], B=[.5,1.5]; quarter disc r=2 with closed cells inside on .5 and .25 grids'})
