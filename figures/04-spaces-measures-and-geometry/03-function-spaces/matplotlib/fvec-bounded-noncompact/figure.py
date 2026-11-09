from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

from matplotlib.patches import Circle
# (a) R^2 单位圆盘内两两距离不小于 1/2 的点；(b) 不相交支撑的鼓包；(c) x^n。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3, width_ratios=[.85, 1, 1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.01, right=.985, top=.97, bottom=.235, wspace=.25)
a = axes[0]; a.set_aspect('equal'); a.axis('off')
pts = []
for i in range(-3, 4):
    for j in range(-3, 4):
        q = (.5*(i+j/2), .5*j*np.sqrt(3)/2)
        if q[0]**2+q[1]**2 <= 1+1e-9: pts.append(q)
for q in pts:
    a.add_patch(Circle(q, .25, fc=BLUE_FILL, ec=BLUE, lw=.8))
    a.plot([q[0]], [q[1]], 'o', ms=1.8, color=BLUE, mew=0)
a.add_patch(Circle((0, 0), 1, fc='none', ec=INK, lw=1.2))
a.add_patch(Circle((0, 0), 1.25, fc='none', ec=MUTED, lw=.85, ls=(0, (3, 2))))
a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3)
b = axes[1]
x = np.linspace(0, 1, 6000)
for n in range(1, 7):
    l, r = 1/(n+1), 1/n; c, w = (l+r)/2, (r-l)/2
    y = np.maximum(0, 1-np.abs(x-c)/w)
    b.plot(x, y, color=BLUE, lw=1.2)
b.set_xlim(0, 1.03); b.set_ylim(0, 1.2); b.set_xticks([0, 1/3, 1/2, 1]); b.set_xticklabels(['0', '1/3', '1/2', '1']); b.set_yticks([0, 1])
b.text(.76, 1.04, r'$\varphi_1$', ha='center', va='bottom'); b.text(.42, 1.04, r'$\varphi_2$', ha='center', va='bottom')
c = axes[2]
x = np.linspace(0, 1, 1000)
for n in (1, 2, 4, 8, 16, 32):
    c.plot(x, x**n, color=BLUE, lw=1.2)
c.plot([0, 1], [0, 0], color=RED, lw=1.6, solid_capstyle='butt', clip_on=False, zorder=3)
c.plot([1], [1], 'o', ms=4, color=RED, mew=0, zorder=4, clip_on=False)
c.plot([1], [0], 'o', ms=4, mfc='white', mec=RED, mew=1, zorder=4, clip_on=False)
c.set_xlim(0, 1.03); c.set_ylim(0, 1.2); c.set_xticks([0, .5, 1]); c.set_xticklabels(['0', '1/2', '1']); c.set_yticks([0, 1])
for ax, s in zip(axes, '(a) (b) (c)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .035, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hex points spacing 1/2 in unit disc; tents on [1/(n+1),1/n]; x^n, n=1,2,4,8,16,32'})
