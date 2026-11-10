from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
STROKE = '#4C4D4F'
X = np.linspace(0, 1, 1001)
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
FIELD = LinearSegmentedColormap.from_list('field', ['#FFFFFF', BLUE_FILL, BLUE])
def panel(fig, left=.09, right=.985, top=.96, bottom=.26, wspace=.26):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def dot(ax, x, y, color=RED, ms=4.6, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)
def hollow(ax, x, y, color=RED, ms=5, z=6):
    ax.plot([x], [y], 'o', ms=ms, mfc='white', mec=color, mew=1, zorder=z, clip_on=False)
def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)
def hat01(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)
