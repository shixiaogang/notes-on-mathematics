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

# (a) rationals p/q, q<=14 at height 1; points frac(k*sqrt2) at height 0 stand for irrationals.
# (b) indicator of the Cantor set, drawn through the 8 retained intervals of step 3.
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.23, wspace=.16)
a, b = axes
from fractions import Fraction
q = sorted({Fraction(p, d) for d in range(1, 15) for p in range(d+1)} | {Fraction(k, 64) for k in range(65)})
irr = np.mod(np.arange(1, 91)*np.sqrt(2), 1)
a.axvspan(.42, .58, fc=YELLOW_FILL, lw=0)
a.plot([float(v) for v in q], [1]*len(q), 'o', ms=1.9, color=BLUE, mew=0)
a.plot(irr, 0*irr, 'o', ms=1.9, color=RED, mew=0)
a.set_xlim(-.02, 1.02); a.set_ylim(-.14, 1.2); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '1/2', '1']); a.set_yticks([0, 1])
def keep(n):
    I = [(0., 1.)]
    for _ in range(n):
        I = [v for l, r in I for v in ((l, l+(r-l)/3), (r-(r-l)/3, r))]
    return I
b.plot([0, 1], [0, 0], color=RED, lw=1.0)
for l, r in keep(3):
    b.plot([l, r], [1, 1], color=BLUE, lw=1.8, solid_capstyle='butt')
    b.plot([l, r], [0, 0], color='white', lw=2.0, solid_capstyle='butt')
b.set_xlim(-.02, 1.02); b.set_ylim(-.14, 1.2); b.set_xticks([0, 1/3, 2/3, 1]); b.set_xticklabels(['0', '1/3', '2/3', '1']); b.set_yticks([0, 1])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'rationals p/q with q<=14; irrational markers frac(k sqrt 2), k=1..90; Cantor step-3 intervals'})
