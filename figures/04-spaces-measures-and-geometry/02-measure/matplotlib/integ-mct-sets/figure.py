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

# f=1 on (0,1], f_n=x^(1/n) increases to f; c=0.8, E_n={f_n>=c}=[0.8^n,1].
fig, ax = figure(width_mm=92, height_mm=58)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.97, top=.97, bottom=.1)
x = np.linspace(1e-4, 1, 1500); ns = (1, 2, 4, 8)
for n in ns:
    ax.plot(x, x**(1/n), color=GREEN, lw=1.2)
ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
ax.plot([0, 1], [.8, .8], color=RED, lw=1.1, dashes=(4, 2))
ax.text(1.015, 1.0, '$f$', va='center', color=INK); ax.text(1.015, .8, '$cf$', va='center', color=INK)
ax.text(.46, .38, '$f_1$', color=INK); ax.text(.015, .46, '$f_8$', color=INK, ha='left')
ax.axhline(0, color=MUTED, lw=.75)
for i, n in enumerate(ns):
    y = -.13-.13*i
    ax.plot([.8**n, 1], [y, y], color=RED, lw=2.4, solid_capstyle='butt')
    ax.text(1.015, y, f'$E_{n}$', va='center', color=INK)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_bounds(0, 1.08)
ax.set_xlim(0, 1.09); ax.set_ylim(-.62, 1.1); ax.set_yticks([0, .8, 1]); ax.set_yticklabels(['0', '$c$', '1'])
ax.set_xticks([])
ax.plot([0, 1], [-.62, -.62], color=MUTED, lw=.75, clip_on=False)
for v, s in ((0, '0'), (1, '1')):
    ax.text(v, -.72, s, ha='center', va='top', fontsize=7.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=1, f_n=x^(1/n), c=0.8, E_n=[0.8^n,1]; 0.8^n=0.8,0.64,0.4096,0.1678 for n=1,2,4,8'})
