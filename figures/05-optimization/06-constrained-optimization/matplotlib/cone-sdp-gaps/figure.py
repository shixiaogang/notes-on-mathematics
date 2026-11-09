from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# (a) min x1 s.t. [[x1,1],[1,x2]]>=0: value 0 not attained. (b) 3x3 example with p*=0, d*=-1.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .25, .22)
a, b = axes
x = np.linspace(.2, 3.6, 400)
a.fill_between(x, 1/x, 5.2, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
a.plot(x, 1/x, color=BLUE, lw=1.2, zorder=2)
for k in (1, 2, 3, 4):
    dot(a, (1/k, k), GREEN, ms=4)
a.axvline(0, color=PURPLE, lw=1.3, zorder=3)
setup(a, (-.2, 3.6), (0, 5.2), [0, 1, 2, 3], [0, 2, 4], equal=False)
b.axhline(0, color=INK, lw=.9)
b.plot([0], [0], 'o', color=GREEN, ms=5.5, mew=0, zorder=5); b.plot([-1], [0], 'o', color=PURPLE, ms=5.5, mew=0, zorder=5)
b.plot([-1, 0], [0, 0], color=RED, lw=3, solid_capstyle='butt', zorder=4)
b.set_xlim(-1.6, .6); b.set_ylim(-.6, .6); b.set_yticks([]); b.spines['left'].set_visible(False); b.spines['bottom'].set_visible(False)
b.set_xticks([])
b.text(0, .12, '$p^*=0$', color=GREEN, ha='center', fontsize=8); b.text(-1, .12, '$d^*=-1$', color=PURPLE, ha='center', fontsize=8)
b.text(-.5, -.17, '间隙', color=RED, ha='center', fontsize=7.5)
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'a': 'x1*x2>=1,x1>0; inf x1=0 not attained', 'b': 'p*=0,d*=-1'})
