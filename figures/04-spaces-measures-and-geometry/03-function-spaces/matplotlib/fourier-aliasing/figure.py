from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# g=cos(6 pi x) 与 cos(2 pi x) 在 x=n/4 取值相同；系数 m=+-3 按模 4 折到 k=3,1。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.07, right=.985, top=.96, bottom=.27, wspace=.2)
ax = axes[0]
x = np.linspace(0, 1, 800)
ax.plot(x, np.cos(6*np.pi*x), color=BLUE, lw=1.4)
ax.plot(x, np.cos(2*np.pi*x), color=PURPLE, lw=1.3)
n = np.arange(4); ax.plot(n/4, np.cos(np.pi*n/2), 'o', ms=4.2, color=INK, mew=0)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-1.2, 1.2); ax.set_xticks([0, .25, .5, .75, 1]); ax.set_xticklabels(['$0$', r'$\frac{1}{4}$', r'$\frac{1}{2}$', r'$\frac{3}{4}$', '$1$']); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.fill_between([-.45, 3.45], 0, .78, color=YELLOW_FILL, lw=0)
ax.axhline(0, color=MUTED, lw=.85)
ax.vlines([-3, 3], 0, .5, color=GREEN, lw=1.2); ax.plot([-3, 3], [.5, .5], 'o', ms=3.6, color=GREEN, mew=0)
ax.vlines([1], 0, .5, color=PURPLE, lw=1.2); ax.plot([1], [.5], 'o', ms=3.6, color=PURPLE, mew=0)
ax.annotate('', xy=(1, .6), xytext=(-3, .6), arrowprops=dict(arrowstyle='->', lw=.85, color=INK, connectionstyle='arc3,rad=-.22', shrinkA=2, shrinkB=2))
ax.text(-1, .76, '$+4$', ha='center', va='bottom')
ax.set_xlim(-5.4, 5.4); ax.set_ylim(0, 1.05); ax.set_xticks([-3, -1, 0, 1, 3]); ax.set_yticks([0, .5]); ax.set_yticklabels(['$0$', r'$\frac{1}{2}$']); ax.set_xlabel('$m$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'cos(6 pi n/4)=cos(2 pi n/4); g^(+-3)=1/2, N=4, m=-3 maps to k=1'})
