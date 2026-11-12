from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Omega=[0,1] with length. X(w)=w, Y(w)=1-w are both Unif(0,1) but |X-Y|=|1-2w|.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; w = np.linspace(0, 1, 200)
ax.plot(w, w, color=BLUE, lw=1.4); ax.plot(w, 1-w, color=YELLOW, lw=1.6)
w0 = .15; ax.plot([w0, w0], [w0, 1-w0], color=RED, lw=1.4)
dot(ax, w0, w0, BLUE, ms=3.4); dot(ax, w0, 1-w0, YELLOW, ms=3.4)
lab(ax, .92, .8, r'$X$', BLUE, ha='center'); lab(ax, .92, .2, r'$Y$', YELLOW, ha='center', va='top')
lab(ax, w0+.03, .5, r'$|1-2\omega|$', RED, va='center')
ax.set_xlim(0, 1); ax.set_ylim(0, 1.02); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$\omega$')
ax = axes[1]; om = (np.arange(2000)+.5)/2000; bins = np.linspace(0, 1, 11)
hx, _ = np.histogram(om, bins, density=True); hy, _ = np.histogram(1-om, bins, density=True)
assert np.allclose(hx, hy)
ax.bar(bins[:-1], hx, width=.1, align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.7)
ax.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
ax.set_xlim(-.05, 1.05); ax.set_ylim(0, 1.3); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'P_|X-Y|>1/2': 0.5, 'hist_equal': True})
