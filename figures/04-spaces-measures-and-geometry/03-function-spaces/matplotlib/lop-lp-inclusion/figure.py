from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# (a) 有限测度与计数测度上 p-范数随 p 的单调方向；(b) (0,∞) 上两个函数：尖峰与长尾。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.96, bottom=.29, wspace=.2)
a, b = axes
p = np.linspace(1, 12, 300)
a.plot(p, (p+1)**(-1/p), color=BLUE, lw=1.4)
a.plot(p, (1+2.0**(-p)+3.0**(-p))**(1/p), color=GREEN, lw=1.4)
a.set_xlim(1, 12.3); a.set_ylim(.4, 2.0); a.set_xticks([1, 2, 4, 8, 12]); a.set_yticks([.5, 1, 1.5, 2])
a.set_xlabel('$p$', labelpad=0)
a.text(6.2, .53, r'$\|x\|_{L^p[0,1]}$', color=INK, ha='left', va='bottom')
a.text(3.2, 1.3, r'$\|(1,\frac{1}{2},\frac{1}{3})\|_{\ell^p}$', color=INK, ha='left', va='bottom')
x1 = np.linspace(.0025, 1, 400); x2 = np.linspace(1, 8, 200)
b.plot(x1, x1**-.5, color=BLUE, lw=1.4)
b.plot(x2, 1/x2, color=GREEN, lw=1.4)
b.plot([1, 1], [1, 0], color=MUTED, lw=.85, ls=(0, (3, 2)))
b.set_xlim(0, 8.2); b.set_ylim(0, 8); b.set_xticks([0, 1, 4, 8]); b.set_yticks([0, 2, 4, 6, 8])
b.set_xlabel('$x$', labelpad=0)
b.text(.75, 5.6, r'$g=x^{-1/2}\mathbf{1}_{(0,1)}$', ha='left', va='bottom')
b.text(2.0, 1.25, r'$f=x^{-1}\mathbf{1}_{[1,\infty)}$', ha='left', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.tick_params(length=2, pad=1.5)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '||x||_p=(p+1)^(-1/p); ||(1,1/2,1/3)||_p=(1+2^-p+3^-p)^(1/p); g=x^-1/2 on (0,1); f=1/x on [1,inf)'})
