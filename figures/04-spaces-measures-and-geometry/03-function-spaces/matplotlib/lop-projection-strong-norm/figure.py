from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# (a) x_k=2^(-k/2) 的系数，P_4 保留前四项；(b) 截断误差：2^(-n/2)、y_k∝1/k 的尾部、基向量 e_{n+1}。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.96, bottom=.29, wspace=.2)
a, b = axes
k = np.arange(1, 13); c = 2.0**(-k/2); N = 4
kp = k <= N
a.vlines(k[kp], 0, c[kp], color=BLUE, lw=1.2); a.plot(k[kp], c[kp], 'o', ms=3.4, color=BLUE, mew=0)
a.vlines(k[~kp], 0, c[~kp], color=RED, lw=1.2); a.plot(k[~kp], c[~kp], 'o', ms=3.4, color=RED, mew=0)
a.axvline(N+.5, color=MUTED, lw=.85, ymax=.92)
a.text(N+.8, .68, r'$x-P_4x$', ha='left', va='bottom', color=INK)
a.text(N+.2, .68, r'$P_4x$', ha='right', va='bottom', color=INK)
a.set_xlim(.3, 12.7); a.set_ylim(0, .85); a.set_xticks([1, 4, 8, 12]); a.set_yticks([0, .25, .5, .75]); a.set_xlabel('$k$', labelpad=0)
n = np.arange(0, 21)
xe = 2.0**(-n/2)
s2 = np.pi**2/6
ye = np.sqrt([1-sum(1/i**2 for i in range(1, m+1))/s2 for m in n])
b.plot(n, np.ones_like(n, float), color=YELLOW, lw=1.4, ls=(0, (5, 2)))
b.plot(n, xe, 'o-', color=BLUE, lw=1.4, ms=2.8, mew=0)
b.plot(n, ye, color=GREEN, lw=1.4)
b.set_xlim(0, 20.5); b.set_ylim(0, 1.2); b.set_xticks([0, 5, 10, 15, 20]); b.set_yticks([0, .5, 1]); b.set_xlabel('$n$', labelpad=0)
b.text(7.2, 1.03, r'$\|e_{n+1}-P_ne_{n+1}\|=1$', ha='left', va='bottom')
b.text(6.5, .46, r'$y_k\propto 1/k$', ha='left', va='bottom')
b.text(8.5, .1, r'$x_k=2^{-k/2}$', ha='left', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.tick_params(length=2, pad=1.5)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
print('y tail n=20', ye[20])
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x_k=2^(-k/2), ||x-P_nx||=2^(-n/2); y_k=sqrt(6)/(pi k); ||e_{n+1}-P_ne_{n+1}||=1'})
