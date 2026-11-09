from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.085, right=.985, top=.96, bottom=.25, wspace=.2)
a, b = axes
x = np.linspace(-1, 1, 500)
a.axhspan(.36, .49, color=YELLOW_FILL, lw=0, zorder=0)
a.fill_between(x, 0, 0)
for lo, hi in ((-.7, -.6), (.6, .7)):
    a.bar((lo+hi)/2, .05, width=hi-lo, bottom=0, color=BLUE_FILL, edgecolor=BLUE, lw=.85, zorder=3)
    a.plot([lo, lo], [.05, lo*lo], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
    a.plot([hi, hi], [.05, hi*hi], color=MUTED, lw=.85, ls=(0, (2, 1.5)))
a.plot(x, x**2, color=BLUE, lw=1.4, zorder=4)
a.set_xlim(-1.08, 1.08); a.set_ylim(0, 1.08); a.set_xlabel('$x$', labelpad=1)
a.set_xticks([-1, -.65, 0, .65, 1]); a.set_xticklabels(['-1', '-0.65', '0', '0.65', '1'])
a.set_yticks([0, .36, .49, 1]); a.set_yticklabels(['0', '0.36', '0.49', '1'])
a.text(.08, .415, '$B$', color=INK, va='center'); a.text(0, .82, '$y=x^2$', color=INK, ha='center')
y = np.linspace(.0005, 1, 1600); q = 1/(2*np.sqrt(y))
yy = np.linspace(.36, .49, 80)
b.fill_between(yy, 0, 1/(2*np.sqrt(yy)), color=YELLOW_FILL, lw=0)
b.plot([.36, .36], [0, 1/(2*.6)], color=YELLOW, lw=.85); b.plot([.49, .49], [0, 1/(2*.7)], color=YELLOW, lw=.85)
b.plot(y, q, color=GREEN, lw=1.4)
b.plot(y, q/2, color=GREEN, lw=1.0, ls=(0, (3, 2)))
b.set_xlim(0, 1.06); b.set_ylim(0, 3.2); b.set_xlabel('$y$', labelpad=1)
b.set_xticks([0, .36, .49, 1]); b.set_xticklabels(['0', '0.36', '0.49', '1']); b.set_yticks([0, 1, 2, 3])
b.text(.14, 1.75, '$q(y)$', color=INK); b.text(.15, .28, r'$\frac{1}{4\sqrt{y}}$', color=INK)
for ax, s in zip(axes, ('(a)', '(b)')):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'y=x^2; B=[0.36,0.49]; preimages [-0.7,-0.6] and [0.6,0.7]; q=1/(2 sqrt y) clipped at 3.2'})
