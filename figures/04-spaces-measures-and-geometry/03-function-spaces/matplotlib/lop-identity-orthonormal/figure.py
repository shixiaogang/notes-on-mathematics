from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse, Circle

# (a) 斜投影画出 e1,e2,e3 及其在 A(x_n)=(x_n/n) 下的像；(b) 截断误差随保留坐标数 m 变化。
fig, axes = figure(width_mm=112, height_mm=52, ncols=2, width_ratios=[1, 1.15])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.02, right=.985, top=.97, bottom=.25, wspace=.14)
a, b = axes
def P(x, y, z):  # 斜投影：e1 朝左下，e2 朝右，e3 朝上
    return np.array([y - .55*x, z - .42*x])
O = P(0, 0, 0)
a.set_xlim(-.95, 1.5); a.set_ylim(-.62, 1.42); a.set_aspect('equal'); a.axis('off')
for v, lab, pos in ((( 1.28, 0, 0), '', None), ((0, 1.35, 0), '', None), ((0, 0, 1.3), '', None)):
    q = P(*v)
    a.annotate('', xy=q, xytext=O, arrowprops=dict(arrowstyle='-|>', lw=.75, color='#4C4D4F', mutation_scale=7))
E1, E2, E3 = P(1, 0, 0), P(0, 1, 0), P(0, 0, 1)
A1, A2, A3 = E1, P(0, .5, 0), P(0, 0, 1/3)
tri = np.array([E1, E2, E3, E1]); a.plot(tri[:, 0], tri[:, 1], color=BLUE, lw=.9, ls=(0, (3, 2)))
tr2 = np.array([A1, A2, A3, A1]); a.plot(tr2[:, 0], tr2[:, 1], color=GREEN, lw=.9, ls=(0, (3, 2)))
for q, c, t, off, ha in ((E2, BLUE, '$e_2$', (.04, .05), 'left'), (E3, BLUE, '$e_3$', (.07, 0), 'left')):
    a.plot(*q, 'o', ms=3.8, color=c, mew=0, zorder=5); a.text(q[0]+off[0], q[1]+off[1], t, ha=ha, va='bottom')
a.plot(*A1, 'o', ms=3.8, color=BLUE, mew=0, zorder=5); a.text(A1[0]+.02, A1[1]-.09, '$e_1=Ae_1$', ha='center', va='top')
for q, t, off in ((A2, '$Ae_2$', (.0, .08)), (A3, '$Ae_3$', (.06, .03))):
    a.plot(*q, 'o', ms=3.8, color=GREEN, mew=0, zorder=5); a.text(q[0]+off[0], q[1]+off[1], t, ha='left', va='bottom')
m = np.arange(0, 16)
sum_ = np.pi**2/6
tail = np.sqrt([1-sum(1/i**2 for i in range(1, k+1))/sum_ for k in m])
b.plot(m, np.ones_like(m, float), color=YELLOW, lw=1.4, ls=(0, (5, 2)))
b.plot(m, tail, 's-', color=BLUE, lw=1.0, ms=2.6, mew=0)
b.plot(m, 1/(m+1), 'o-', color=GREEN, lw=1.4, ms=3, mew=0)
b.set_xlim(0, 15.6); b.set_ylim(0, 1.2); b.set_xticks([0, 5, 10, 15]); b.set_yticks([0, .5, 1]); b.set_xlabel('$m$', labelpad=0)
b.tick_params(length=2, pad=1.5)
b.text(5.5, 1.04, r'$\|I-P_m\|=1$', ha='left', va='bottom')
b.text(4.2, .47, r'$\|(I-P_m)x\|$, $x\propto(1/n)$', ha='left', va='bottom')
b.text(.5, .025, r'$\|A-A_m\|$', ha='left', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'A(x_n)=(x_n/n); ||I-P_m||=1; ||A-A_m||=1/(m+1); x_n=sqrt(6)/(pi n)'})
