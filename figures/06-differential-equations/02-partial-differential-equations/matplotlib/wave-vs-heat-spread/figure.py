from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: same tent, heat vs wave in space-time, and log view of the tails at t=1.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
xs = np.linspace(-6, 6, 401); ts = np.linspace(.004, 2, 200); X, TT = np.meshgrid(xs, ts)
ax = axs[0]; style(ax); field(ax, wave_tent(X, TT), [-6, 6, 0, 2], vmax=1.)
ax.plot([1, 3], [0, 2], color=LINE, lw=1.1); ax.plot([-1, -3], [0, 2], color=LINE, lw=1.1)
ax.set_xticks([-5, 0, 5]); ax.set_yticks([0, 1, 2]); ax.set_ylabel('$t$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax); field(ax, heat_tent(X, TT), [-6, 6, 0, 2], vmax=1.)
ax.set_xticks([-5, 0, 5]); ax.set_yticks([0, 1, 2]); sub(ax, 'b', '$x$')
ax = axs[2]; style(ax); x = np.linspace(0, 8, 801); h = heat_tent(x, 1.)
ax.semilogy(x, h, color=PURPLE, lw=1.4)
w = wave_tent(x, 1.); m = w > 0
ax.semilogy(x[m], w[m], color=BLUE, lw=1.5)
ax.axvline(2, color=LINE, lw=1.1)
ax.set_xlim(0, 8); ax.set_ylim(1e-8, 2); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([1e-8, 1e-4, 1]); ax.set_ylabel('$u(x,1)$'); sub(ax, 'c', '$x$')
print('heat tail x=8', h[-1], 'wave at 2:', wave_tent(np.array([2.]), 1.))
save(fig, HERE(__file__), 'figure', {'formula': 'c=1; heat kernel convolved with tent; tails at t=1'})
