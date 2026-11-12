from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/01-elementary-probability/matplotlib/rvd-common'))
from rvd_common import *
# Target: R = distance to the centre of a point placed uniformly in the unit disk, F(r)=r^2.
# Bars: exact P(r<R<=r+h)/h = 2r+h on cells of width h (probability per unit length); line: density 2r.
r = np.linspace(0, 1, 200)
fig, axs = figure(width_mm=104, height_mm=46, ncols=2)
for ax, h, letter in [(axs[0], .25, 'a'), (axs[1], .05, 'b')]:
    style(ax)
    left = np.arange(0, 1, h)
    height = ((left+h)**2-left**2)/h
    ax.bar(left, height, width=h, align='edge', color=BLUE_FILL, edgecolor=BLUE, linewidth=.7)
    ax.plot(r, 2*r, color=BLUE, lw=1.4)
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 2.15); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2])
    ax.text(.04, 1.95, f'$h={h}$', fontsize=7.5)
    if letter == 'a':
        ax.set_ylabel('概率 / 长度')
    sub(ax, letter, '$r$')
save(fig, HERE(__file__), 'figure', {'formula': 'bar height = ((r+h)^2-r^2)/h = 2r+h', 'h': [.25, .05]})
