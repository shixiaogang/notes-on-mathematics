from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: plucked string L=1,c=1: partial sums, snapshots, and space-time field with reflecting characteristics.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
x = np.linspace(0, 1, 801)
ax = axs[0]; style(ax)
a = lambda n: 4*np.sin(n*np.pi/2)/(n*np.pi)**2
for N, col, lw in zip([1, 3, 7], [YELLOW, PURPLE, BLUE], [1.6, 1.2, 1.4]):
    ax.plot(x, sum(a(n)*np.sin(n*np.pi*x) for n in range(1, N+1)), color=col, lw=lw)
ax.plot(x, pluck(x), color=RED, lw=1.0, ls=(0, (3, 2)))
ax.set_xlim(0, 1); ax.set_ylim(0, .56); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .2, .4]); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
ax.plot(x, pluck(x), color=RED, lw=1.5)
for t, col in zip([.15, .3, .5, .7, 1.], ['#9AACC0', '#7188A3', '#C3CEDA', '#7188A3', '#4F6580']):
    ax.plot(x, pluck_wave(x, t), color=col, lw=1.3)
ax.set_xlim(0, 1); ax.set_ylim(-.56, .56); ax.set_xticks([0, .5, 1]); ax.set_yticks([-.5, 0, .5]); sub(ax, 'b', '$x$')
ax = axs[2]; style(ax)
xs = np.linspace(0, 1, 301); ts = np.linspace(0, 2, 601); X, TT = np.meshgrid(xs, ts)
field(ax, pluck_wave(X, TT), [0, 1, 0, 2], signed=True, vmax=.5)
for t0 in np.arange(-.5, 2.5, 1.):
    ax.plot([0, 1], [t0, t0+1], color=LINE, lw=.95); ax.plot([1, 0], [t0, t0+1], color=LINE, lw=.95)
ax.set_xlim(0, 1); ax.set_ylim(0, 2); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2]); ax.set_ylabel('$t$'); sub(ax, 'c', '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'u0=min(x,1-x), a_n=4 sin(n pi/2)/(n pi)^2; odd 2-periodic extension'})
