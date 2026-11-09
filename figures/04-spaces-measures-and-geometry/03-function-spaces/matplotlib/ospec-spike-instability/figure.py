from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# (a) unit spikes u_n = sqrt(n) 1_{|x-1/2|<1/(2n)}; (b) truncated solutions f_n=g_n/(x-1/2), g_n=1_{|x-1/2|>1/n}.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.97, bottom=.23, wspace=.24)
ax = axes[0]
for n, c in ((2, YELLOW), (8, GREEN), (32, BLUE)):
    h = 1/(2*n); xs = [0, .5-h, .5-h, .5+h, .5+h, 1]; ys = [0, 0, n**.5, n**.5, 0, 0]
    ax.plot(xs, ys, color=c, lw=1.4)
    ax.text(.5+h+.015, n**.5-.1, f'$u_{{{n}}}$', ha='left', va='top')
ax.set_xlim(0, 1); ax.set_ylim(0, 6.3); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 2, 4, 6]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85)
for n, c in ((20, BLUE), (4, GREEN)):
    for lo, hi in ((0, .5-1/n), (.5+1/n, 1)):
        x = np.linspace(lo, hi, 400); ax.plot(x, 1/(x-.5), color=c, lw=(1.2 if n == 20 else 3.0), zorder=(3 if n == 20 else 2))
ax.text(.13, -6, '$f_4$', ha='center'); ax.text(.41, -16.5, '$f_{20}$', ha='right')
ax.set_xlim(0, 1); ax.set_ylim(-22, 22); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([-20, 0, 20]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
for n in (4, 10, 20, 100, 1000): print(n, (2/n)**.5, (2*n-4)**.5)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'u_n=sqrt(n)*indicator(|x-1/2|<1/(2n)); f_n=indicator(|x-1/2|>1/n)/(x-1/2)'})
