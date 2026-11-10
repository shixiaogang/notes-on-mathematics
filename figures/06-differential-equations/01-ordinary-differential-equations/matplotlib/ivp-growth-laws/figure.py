from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：对比指数增长与饱和增长的方向场；同一规律、不同初值给出不同解曲线。
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, .075, .985, .97, .24, .26)
t = np.linspace(0, 5, 500)
inits = [.1, .3, .6]
laws = [(lambda s, x: x, lambda x0: x0*np.exp(t)), (lambda s, x: x*(1 - x), lambda x0: x0*np.exp(t)/(1 - x0 + x0*np.exp(t)))]
for ax, (f, sol) in zip(axes, laws):
    ax.set_xlim(0, 5); ax.set_ylim(0, 1.5); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, .5, 1, 1.5])
    ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
    slope_field(ax, f, nt=15, nx=9)
    for x0, c in zip(inits, (BLUE, YELLOW, YELLOW)):
        ax.plot(t, sol(x0), color=c, lw=1.4, zorder=3)
        dot(ax, 0, x0)
axes[1].axhline(1, color=BLUE, lw=1.0, zorder=2)
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'x\'=x, x0 in 0.1,0.3,0.6', 'b': 'x\'=x(1-x), x0 in 0.1,0.3,0.6'})
