from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: the factor multiplying mode n under wave and heat evolution on (0,1), c=1, unit diffusivity.
fig, axs = figure(width_mm=112, height_mm=42, ncols=2)
ax = axs[0]; style(ax); t = np.linspace(0, 2, 1001)
ax.axhline(0, color=GRID, lw=.85)
for n, col, lw in zip([1, 2, 3], [BLUE, YELLOW, PURPLE], [1.5, 1.6, 1.1]):
    ax.plot(t, np.cos(n*np.pi*t), color=col, lw=lw)
ax.set_xlim(0, 2); ax.set_ylim(-1.1, 1.1); ax.set_xticks([0, 1, 2]); ax.set_ylabel('模式因子'); sub(ax, 'a', '$t$')
ax = axs[1]; style(ax); t = np.linspace(0, .3, 601)
ax.axhline(0, color=GRID, lw=.85)
for n, col, lw in zip([1, 2, 3], [BLUE, YELLOW, PURPLE], [1.5, 1.6, 1.1]):
    ax.plot(t, np.exp(-(n*np.pi)**2*t), color=col, lw=lw)
ax.set_xlim(0, .3); ax.set_ylim(-.05, 1.1); ax.set_xticks([0, .1, .2, .3]); sub(ax, 'b', '$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'cos(n pi t); exp(-n^2 pi^2 t); n=1,2,3'})
