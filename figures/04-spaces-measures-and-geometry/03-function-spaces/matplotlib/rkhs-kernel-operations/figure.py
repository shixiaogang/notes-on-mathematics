from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# x=0.4，t in [-1,1]：仿射核截面 1+0.4t，高斯核截面 exp(-(t-.4)^2/(2*.3^2))，二者之和与逐点乘积。
t = np.linspace(-1, 1, 501); x = .4
a_ = 1+x*t; g = np.exp(-(t-x)**2/(2*.3**2))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.97, bottom=.265, wspace=.1)
a, b = axes
a.plot(t, a_, color=BLUE, lw=1.4); a.plot(t, g, color=GREEN, lw=1.4)
a.text(-.95, .78, r'$1+0.4t$', color=INK, va='bottom'); a.text(.78, .55, r'$G_{0.4}$', color=INK, va='center', ha='left')
b.plot(t, a_+g, color=YELLOW, lw=1.4); b.plot(t, a_*g, color=RED, lw=1.4)
b.text(-.05, 1.72, '和核', color=INK, ha='right'); b.text(-.08, .25, '乘积核', color=INK, ha='right')
for ax in axes:
    ax.axvline(x, color=MUTED, lw=.85, ls=(0, (2, 1.5))); ax.set_xlim(-1, 1); ax.set_ylim(0, 2.5); ax.set_xticks([-1, 0, .4, 1]); ax.set_xticklabels(['-1', '0', '0.4', '1']); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$t$', labelpad=1)
fig.canvas.draw()
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'K1=1+xt, K2=exp(-(t-x)^2/(2*0.09)), x=0.4'})
