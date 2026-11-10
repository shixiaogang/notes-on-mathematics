from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: a standing wave is the sum of two travelling waves; L=1, c=1, mode n=1.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
x = np.linspace(0, 1, 401)
ax = axs[0]; style(ax)
ax.plot(x, np.sin(np.pi*x), color=RED, lw=1.5)
for t, col in zip([.15, .3, .5, .7, .85, 1.0], ['#4F6580', '#7188A3', '#C3CEDA', '#7188A3', '#4F6580', '#4F6580']):
    ax.plot(x, np.cos(np.pi*t)*np.sin(np.pi*x), color=col, lw=1.2)
ax.set_xlim(0, 1); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, .5, 1]); ax.set_ylabel('$u$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax); t = .25
xx = np.linspace(-.2, 1.2, 501)
ax.plot(xx, .5*np.sin(np.pi*(xx-t)), color=PURPLE, lw=1.1, ls=(0, (3, 2)))
ax.plot(xx, .5*np.sin(np.pi*(xx+t)), color=YELLOW, lw=1.5, ls=(0, (3, 2)))
ax.plot(x, np.cos(np.pi*t)*np.sin(np.pi*x), color=BLUE, lw=1.5)
ax.axvline(0, color=LINE, lw=1.3); ax.axvline(1, color=LINE, lw=1.3)
ax.set_xlim(-.2, 1.2); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, .5, 1]); sub(ax, 'b', '$x$')
ax = axs[2]; style(ax)
xs = np.linspace(0, 1, 301); ts = np.linspace(0, 2, 601); X, TT = np.meshgrid(xs, ts)
field(ax, np.cos(np.pi*TT)*np.sin(np.pi*X), [0, 1, 0, 2], signed=True, vmax=1.)
ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2]); ax.set_ylabel('$t$'); sub(ax, 'c', '$x$')
save(fig, HERE(__file__), 'figure', {'formula': 'cos(pi t) sin(pi x) = (sin pi(x-t)+sin pi(x+t))/2'})
