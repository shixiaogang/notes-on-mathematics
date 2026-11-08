from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Circle
# x_n = (cos(n)/n, sin(n)/n), limit x = (0,0), d(x_n,x) = 1/n, epsilon = 1/5, N = 6.
N = 30
n = np.arange(1, N+1)
xs, ys = np.cos(n)/n, np.sin(n)/n
eps = .2
fig, axes = figure(width_mm=108, height_mm=52, ncols=2, width_ratios=[1, 1.15])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.02, right=.985, top=.98, bottom=.235, wspace=.2)
a = axes[0]; a.set_aspect('equal'); a.axis('off')
a.add_patch(Circle((0, 0), eps, fc=BLUE_FILL, ec=BLUE, lw=.9, ls=(0, (3, 2))))
out = n <= 5
a.plot(xs[out], ys[out], 'o', ms=3.4, color=GREEN, mew=0, zorder=3)
a.plot(xs[~out], ys[~out], 'o', ms=2.6, color=BLUE, mew=0, zorder=3)
a.plot([0], [0], 'x', ms=4.5, mew=1.1, color=INK, zorder=4)
off = {1: (.09, .05), 2: (-.03, .08), 3: (-.08, .06), 4: (-.09, -.07), 5: (.07, -.05)}
for k in range(1, 6):
    a.text(xs[k-1]+off[k][0], ys[k-1]+off[k][1], f'$x_{k}$', ha='center', va='center')
a.plot([0, .29], [0, .03], color=MUTED, lw=.7, zorder=3)
a.text(.31, .035, '$x$', ha='left', va='center')
a.set_xlim(-.55, .72); a.set_ylim(-.42, .98)
b = axes[1]
b.axhline(eps, color=BLUE, lw=.85, ls=(0, (3, 2)))
b.axvline(6, color=MUTED, lw=.85, ls=(0, (2, 2)))
m = n <= 18
b.plot(n[m & (n <= 5)], 1/n[m & (n <= 5)], 'o', ms=3.4, color=GREEN, mew=0)
b.plot(n[m & (n > 5)], 1/n[m & (n > 5)], 'o', ms=2.8, color=BLUE, mew=0)
b.set_xlim(0, 19); b.set_ylim(0, 1.08)
b.set_xticks([1, 6, 12, 18]); b.set_yticks([0, .2, .5, 1]); b.set_yticklabels(['0', r'$\varepsilon$', '0.5', '1'])
b.set_xlabel('$n$', labelpad=1); b.set_ylabel('$d(x_n,x)$', labelpad=2)
fig.canvas.draw()
for ax_, lab in zip(axes, ('(a)', '(b)')):
    pos = ax_.get_position()
    fig.text((pos.x0+pos.x1)/2, .045, lab, ha='center', va='center')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x_n=(cos n/n, sin n/n), limit (0,0), d=1/n, eps=1/5, N=6'})
