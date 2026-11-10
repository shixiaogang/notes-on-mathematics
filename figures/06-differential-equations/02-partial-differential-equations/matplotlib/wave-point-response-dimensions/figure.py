from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: point-impulse response at t=1, c=1, in dimensions 1,2,3 (closed formulas).
fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
r = np.linspace(0, 1.6, 1601)
ax = axs[0]; style(ax); ax.plot(r, np.where(r < 1, .5, 0.), color=BLUE, lw=1.5)
ax.set_ylim(0, .8); ax.set_yticks([0, .5]); sub(ax, 'a', '$|x|$')
ax = axs[1]; style(ax); rr = r[r < .9995]; ax.plot(rr, 1/(2*np.pi*np.sqrt(1-rr**2)), color=BLUE, lw=1.5); ax.plot([1, 1.6], [0, 0], color=BLUE, lw=1.5)
ax.set_ylim(0, 1.2); ax.set_yticks([0, .5, 1]); sub(ax, 'b', '$r$')
ax = axs[2]; style(ax); ax.plot([0, 1.6], [0, 0], color=BLUE, lw=1.5)
ax.annotate('', xy=(1, 1.0), xytext=(1, 0), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.5, mutation_scale=9, shrinkA=0, shrinkB=0))
ax.set_ylim(0, 1.2); ax.set_yticks([]); sub(ax, 'c', '$r$')
for ax in axs:
    ax.axvline(1, color=LINE, lw=1.1, zorder=0); ax.set_xlim(0, 1.6); ax.set_xticks([0, 1])
save(fig, HERE(__file__), 'figure', {'formula': '1D: 1/2 on r<1; 2D: 1/(2 pi sqrt(1-r^2)); 3D: delta(r-1)/(4 pi)'})
