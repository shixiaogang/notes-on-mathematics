from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# 贯穿例子在 span{e1,e2} 上的坐标：T(a,b)=(a,b/3)。单位圆的像是半轴为 1 与 1/3 的椭圆。
# 虚线圆半径 sqrt(10)/3 为核的 L2 范数（Frobenius 范数）。
fig, axes = figure(width_mm=104, height_mm=52, ncols=2, sharex=True, sharey=True)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.03, right=.97, top=.97, bottom=.11, wspace=.12)
L = 1.42
ang = np.pi/6; fpt = np.array([np.cos(ang), np.sin(ang)])
for ax in axes:
    ax.set_xlim(-L, L); ax.set_ylim(-L, L); ax.set_aspect('equal'); ax.axis('off')
    ax.annotate('', xy=(L, 0), xytext=(-L, 0), arrowprops=dict(arrowstyle='-|>', lw=.75, color='#4C4D4F', mutation_scale=7))
    ax.annotate('', xy=(0, L), xytext=(0, -L), arrowprops=dict(arrowstyle='-|>', lw=.75, color='#4C4D4F', mutation_scale=7))
a, b = axes
b.add_patch(Circle((0, 0), np.sqrt(10)/3, fc='none', ec=MUTED, lw=.85, ls=(0, (3, 2))))
a.add_patch(Circle((0, 0), 1, fc=BLUE_FILL, ec=BLUE, lw=1.3))
b.add_patch(Ellipse((0, 0), 2, 2/3, fc=GREEN_FILL, ec=GREEN, lw=1.3))
for ax, p, c, lab, off in ((a, (1, 0), BLUE, '$e_1$', (1.02, .08)), (a, (0, 1), BLUE, '$e_2$', (.08, 1.04)), (a, fpt, RED, r'$f/\|f\|$', (fpt[0]+.04, fpt[1]+.1)),
                          (b, (1, 0), GREEN, '$e_1$', (1.1, .05)), (b, (0, 1/3), GREEN, r'$\frac{1}{3}e_2$', (.08, .4)), (b, (fpt[0], fpt[1]/3), RED, r'$Tf/\|f\|$', (.4, .36))):
    ax.plot(*p, 'o', ms=3.8, color=c, mew=0, zorder=5)
    ax.plot([0, p[0]], [0, p[1]], color=c, lw=1.0)
    ax.text(*off, lab, ha='left', va='bottom')
b.text(-1.38, -1.4, r'$\|k\|_{L^2}=\sqrt{10}/3$', ha='left', va='bottom', color=MUTED, fontsize=7.5)
b.annotate('', xy=(-.72, -.77), xytext=(-.85, -1.2), arrowprops=dict(arrowstyle='-', lw=.6, color=MUTED))
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'T(a,b)=(a,b/3); f=(sqrt3/2,1/2); ||k||_2=sqrt(10)/3'})
