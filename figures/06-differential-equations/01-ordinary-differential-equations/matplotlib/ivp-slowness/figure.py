from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：a=1 时经过时间等于 1/b 下的面积，比较到达零点或无穷所需时间的有限与无限。
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
panel(fig, .095, .985, .96, .27, .42)
a, b, c = axes
x = np.linspace(.5, .985, 300); a.plot(x, 1/(x*(1 - x)), color=BLUE, lw=1.4, zorder=3)
xf = x[x <= .95]; a.fill_between(xf, 0, 1/(xf*(1 - xf)), color=BLUE_FILL, lw=0, zorder=1)
a.axvline(1, color=RED, lw=.95, ls=(0, (4, 2)))
a.set_xlim(.5, 1.03); a.set_ylim(0, 40); a.set_xticks([.5, .75, 1]); a.set_xticklabels(['0.5', '0.75', '1']); a.set_yticks([0, 20, 40])
x = np.linspace(.002, 1.25, 400); b.plot(x, 1/(2*np.sqrt(x)), color=BLUE, lw=1.4, zorder=3)
xf = x[x <= 1]; b.fill_between(xf, 0, 1/(2*np.sqrt(xf)), color=BLUE_FILL, lw=0, zorder=1)
b.axvline(0, color=RED, lw=.95, ls=(0, (4, 2)))
b.set_xlim(-.04, 1.25); b.set_ylim(0, 6); b.set_xticks([0, 1]); b.set_yticks([0, 3, 6])
x = np.linspace(1, 8, 400); c.plot(x, 1/x**2, color=BLUE, lw=1.4, zorder=3)
c.fill_between(x, 0, 1/x**2, color=BLUE_FILL, lw=0, zorder=1)
c.annotate('', xy=(8, .13), xytext=(5.4, .13), arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=.85, mutation_scale=7, shrinkA=0, shrinkB=0))
c.set_xlim(.6, 8.2); c.set_ylim(0, 1.15); c.set_xticks([1, 4, 8]); c.set_yticks([0, .5, 1])
for ax, s in zip(axes, ('$1/[x(1-x)]$', '$1/(2\\sqrt{x})$', '$1/x^2$')):
    ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel(s, labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': '1/(x(1-x)), shaded [0.5,0.95]', 'b': '1/(2 sqrt x), shaded [0,1]', 'c': '1/x^2, shaded [1,8]'})
