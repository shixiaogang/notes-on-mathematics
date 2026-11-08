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

# f=sin x on [0,2pi] and its parts f^+=max(f,0), f^-=max(-f,0).
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.23, wspace=.16)
x = np.linspace(0, 2*np.pi, 800); y = np.sin(x)
a, b = axes
a.fill_between(x, 0, y, where=y >= 0, fc=BLUE_FILL, lw=0); a.fill_between(x, 0, y, where=y <= 0, fc=RED_FILL, lw=0)
a.plot(x, y, color=INK, lw=1.4); a.axhline(0, color=MUTED, lw=.75)
b.fill_between(x, 0, np.maximum(y, 0), fc=BLUE_FILL, lw=0); b.fill_between(x, 0, np.maximum(-y, 0), fc=RED_FILL, lw=0)
b.plot(x, np.maximum(y, 0), color=BLUE, lw=1.4); b.plot(x, np.maximum(-y, 0), color=RED, lw=1.4)
a.text(1.57, .55, '$f>0$', ha='center', color=INK); a.text(4.71, -.6, '$f<0$', ha='center', color=INK)
b.text(1.57, .42, '$f^{+}$', ha='center', color=INK); b.text(4.71, .42, '$f^{-}$', ha='center', color=INK)
for ax in axes:
    ax.set_xlim(0, 2*np.pi+.1); ax.set_xticks([0, np.pi, 2*np.pi]); ax.set_xticklabels(['0', '$\\pi$', '$2\\pi$'])
a.set_ylim(-1.15, 1.15); a.set_yticks([-1, 0, 1]); b.set_ylim(0, 1.15); b.set_yticks([0, 1])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=sin x; f^+=max(sin x,0); f^-=max(-sin x,0)'})
